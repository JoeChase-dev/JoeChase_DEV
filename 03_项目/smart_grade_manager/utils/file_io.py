"""
文件读写模块 - 数据持久化
==========================
知识点：文件的打开/读写/关闭，JSON序列化与反序列化

📚 知识点覆盖:
  ✓ open() 的各种模式 (r/w/a/r+/w+)
  ✓ with 语句 (上下文管理器) - 自动关闭文件
  ✓ json.dump() / json.load() 序列化
  ✓ os.path 文件路径操作
  ✓ 异常处理在文件操作中的应用
  ✓ 多线程异步保存
"""
import json
import os
from typing import List, Any, Optional
import threading

# 默认数据文件路径（相对于项目根目录）
DEFAULT_DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data")
DEFAULT_DATA_FILE = os.path.join(DEFAULT_DATA_DIR, "students.json")


def ensure_data_dir(filepath: str = DEFAULT_DATA_FILE) -> str:
    """
    确保数据目录存在
    
    知识点：
      - os.path.dirname(): 获取文件所在目录
      - os.makedirs(exist_ok=True): 创建目录（已存在不报错）
      - os.path.abspath(): 获取绝对路径
    """
    dir_path = os.path.dirname(os.path.abspath(filepath))
    if not os.path.exists(dir_path):
        os.makedirs(dir_path, exist_ok=True)
        print(f"📁 自动创建数据目录: {dir_path}")
    return filepath


def save_to_json(data: List[Any], 
                 filepath: str = DEFAULT_DATA_FILE,
                 indent: int = 2,
                 encoding: str = "utf-8") -> bool:
    r"""
    将数据列表保存为JSON文件
    
    参数:
        data: 要保存的数据（通常是字典或对象列表）
        filepath: 目标文件路径
        indent: JSON缩进空格数（美化输出）
        encoding: 文件编码
        
    返回:
        True表示成功，失败抛异常
    
    知识点：
      - with open() as f: 上下文管理器（自动close）
      - json.dump(): 直接写入文件对象
      - ensure_ascii=False: 保留中文（否则\uXXXX转义）
      
    使用示例:
        save_to_json([student1.to_dict(), student2.to_dict()])
    """
    filepath = ensure_data_dir(filepath)
    
    try:
        with open(filepath, "w", encoding=encoding) as f:
            json.dump(data, f, ensure_ascii=False, indent=indent)
        
        file_size = os.path.getsize(filepath)
        print(f"💾 数据已保存到 {filepath} ({file_size} 字节, {len(data)} 条记录)")
        return True
        
    except PermissionError:
        raise PermissionError(f"没有写入权限: {filepath}")
    except OSError as e:
        raise OSError(f"文件写入错误: {e}")


def load_from_json(filepath: str = DEFAULT_DATA_FILE,
                   encoding: str = "utf-8") -> list:
    """
    从JSON文件加载数据
    
    返回:
        数据列表，文件不存在或为空时返回空列表
        
    知识点：
      - os.path.exists(): 检查文件是否存在
      - os.path.getsize(): 检查文件大小（判断是否为空）
      - json.load() vs json.loads():
          * load(): 从文件对象读取
          * loads(): 从字符串读取
    """
    if not os.path.exists(filepath):
        print(f"ℹ️ 数据文件不存在: {filepath}，将创建新文件")
        return []
    
    if os.path.getsize(filepath) == 0:
        print(f"⚠️ 数据文件为空: {filepath}")
        return []
    
    try:
        with open(filepath, "r", encoding=encoding) as f:
            data = json.load(f)
            
        if not isinstance(data, list):
            print(f"⚠️ 数据格式异常：期望list，实际{type(data).__name__}")
            return []
        
        print(f"📂 从 {filepath} 加载了 {len(data)} 条记录")
        return data
        
    except json.JSONDecodeError as e:
        print(f"❌ JSON解析错误: {e}")
        return []
    except Exception as e:
        print(f"❌ 文件读取错误: {e}")
        return []


def append_to_json(item: dict,
                   filepath: str = DEFAULT_DATA_FILE,
                   encoding: str = "utf-8") -> bool:
    """
    向JSON文件追加一条数据
    
    知识点：追加模式的文件操作
         先读取全部 → 添加新项 → 全部写回
         （JSON格式不支持真正意义上的追加写）
    """
    filepath = ensure_data_dir(filepath)
    
    existing_data = load_from_json(filepath, encoding)
    existing_data.append(item)
    
    return save_to_json(existing_data, filepath, encoding=encoding)


class AsyncFileSaver:
    """
    异步文件保存器 - 多线程基础应用
    
    知识点：
      - threading.Thread: 创建新线程
      - daemon=True: 设置为守护线程（主程序退出时自动结束）
      - 队列思想：将保存任务放入队列，后台线程逐个处理
      
    使用场景：保存大文件时不阻塞用户界面操作
    """
    
    def __init__(self, filepath: str = DEFAULT_DATA_FILE):
        self.filepath = filepath
        self._pending_data = None
        self._lock = threading.Lock()
        self._save_thread = None
        
    def save_async(self, data: list):
        """异步保存 - 不阻塞调用者"""
        self._pending_data = data
        
        # 启动后台保存线程
        self._save_thread = threading.Thread(
            target=self._do_save,
            daemon=True,   # 守护线程：主程序退出时自动结束
            name="FileSaver"
        )
        self._save_thread.start()
        print("💾 正在后台保存数据...（不阻塞界面）")
    
    def _do_save(self):
        """实际执行保存的函数（在子线程中运行）"""
        try:
            with self._lock:   # 线程锁：防止并发写入冲突
                save_to_json(self._pending_data, self.filepath)
                print("✅ 后台保存完成！")
        except Exception as e:
            print(f"❌ 后台保存失败: {e}")
    
    def wait_for_completion(self, timeout: float = 5.0):
        """等待保存完成（可选）"""
        if self._save_thread and self._save_thread.is_alive():
            self._save_thread.join(timeout=timeout)


def backup_file(filepath: str = DEFAULT_DATA_FILE) -> Optional[str]:
    """
    创建备份文件
    
    知识点：
      - shutil.copy2: 复制文件（保留元数据）
      - 时间戳命名备份文件
      - datetime.now().strftime() 格式化时间
    """
    import shutil
    from datetime import datetime
    
    if not os.path.exists(filepath):
        return None
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    base, ext = os.path.splitext(filepath)
    backup_path = f"{base}_backup_{timestamp}{ext}"
    
    shutil.copy2(filepath, backup_path)
    size = os.path.getsize(backup_path)
    print(f"📋 备份已创建: {backup_path} ({size} 字节)")
    
    return backup_path


def clear_data_file(filepath: str = DEFAULT_DATA_FILE) -> bool:
    """清空数据文件"""
    filepath = ensure_data_dir(filepath)
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump([], f)
    print(f"🗑️ 数据文件已清空: {filepath}")
    return True
