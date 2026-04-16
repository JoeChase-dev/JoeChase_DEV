"""
格式化输出模块 - 美化终端显示
============================
知识点：字符串格式化的多种方式

📚 知识点覆盖:
  ✓ f-string (格式化字符串字面值) - Python 3.6+ 推荐
  ✓ str.format() 方法
  ✓ % 格式化（旧式，了解即可）
  ✓ str.center(), ljust(), rjust() 文本对齐
  ✓ 字符串的乘法重复操作
"""
from typing import List, Any


def separator(char: str = "=", length: int = 50) -> str:
    """生成分隔线"""
    return char * length


def format_title(title: str, width: int = 50, 
                 char: str = "=") -> str:
    """
    生成带标题的分隔横幅
    
    示例输出：
    ===================
      🎓 学生成绩管理系统
    ===================
    """
    line = char * width
    # center(width) 让文字居中，填充空格到指定宽度
    title_line = f"  {title}  ".center(width)
    return f"{line}\n{title_line}\n{line}"


def format_table(headers: List[str], 
                 rows: List[List[Any]],
                 col_widths: List[int] = None,
                 align: str = "<") -> str:
    """
    生成文本表格
    
    参数:
        headers: 表头列表 ["学号", "姓名", "成绩"]
        rows: 数据行列表，每行是一个列表
        col_widths: 各列宽度（自动计算或手动指定）
        align: 对齐方式 < 左对齐 | > 右对齐 | ^ 居中
        
    知识点：
      - 列表推导式 + zip() 组合多列数据
      - f-string 的格式化语法 {value:>width} 右对齐指定宽度
      - join() 拼接字符串
      
    输出示例：
      ┌────────┬──────────┬─────────┐
      │ 学号   │ 姓名     │ 平均分   │
      ├────────┼──────────┼─────────┤
      │20260001│ 张三     │   91.67 │
      └────────┴──────────┴─────────┘
    """
    if not headers:
        return "(空表)"
    
    # 自动计算列宽（如果没有指定）
    if col_widths is None:
        col_widths = [len(str(h)) for h in headers]
        for row in rows:
            for i, cell in enumerate(row):
                if i < len(col_widths):
                    col_widths[i] = max(col_widths[i], len(str(cell)))
                else:
                    col_widths.append(len(str(cell)))
    
    # 确保列数匹配
    num_cols = len(headers)
    
    def format_row(cells: list, is_header: bool = False) -> str:
        """格式化单行"""
        formatted_cells = []
        for i in range(num_cols):
            cell = cells[i] if i < len(cells) else ""
            cell_str = str(cell)
            w = col_widths[i] if i < len(col_widths) else 10
            
            # 根据align参数选择对齐方式
            if align == "^":
                formatted = f" {cell_str:^{w}} "
            elif align == ">":
                formatted = f" {cell_str:>{w}} "
            else:  # default: left align
                formatted = f" {cell_str:<{w}} "
            
            formatted_cells.append(formatted)
        
        prefix = "│" if not is_header else "│"
        suffix = "│"
        return prefix + "│".join(formatted_cells) + suffix
    
    # 构建表格各部分
    top_line = "┌" + "┬".join("─" * (w + 2) for w in col_widths[:num_cols]) + "┐"
    mid_line = "├" + "┼".join("─" * (w + 2) for w in col_widths[:num_cols]) + "┤"
    bot_line = "└" + "┴".join("─" * (w + 2) for w in col_widths[:num_cols]) + "┘"
    
    lines = [
        top_line,
        format_row(headers, is_header=True),
        mid_line,
    ]
    
    for row in rows:
        lines.append(format_row(row))
    
    lines.append(bot_line)
    return "\n".join(lines)


def format_progress_bar(current: int, total: int, 
                        width: int = 30,
                        filled_char: str = "█",
                        empty_char: str = "░") -> str:
    """
    生成进度条字符串
    
    知识点：
      - 整数除法 // 和取模 %
      - 字符串重复 * 运算符
      
    用法示例：
      [████████░░░░░░░░░░░░░░░░░] 30% (3/10)
    """
    if total <= 0:
        return "[" + filled_char * width + "] 100%"
    
    ratio = min(current / total, 1.0)
    filled = int(width * ratio)
    empty = width - filled
    
    percentage = int(ratio * 100)
    
    bar = filled_char * filled + empty_char * empty
    return f"[{bar}] {percentage}% ({current}/{total})"


def format_number(num, decimal_places: int = 2) -> str:
    """
    数字格式化（添加千分位分隔符）
    
    知识点：f-string的格式说明符
      :,   → 千分位逗号分隔
      .2f  → 保留2位小数
      :,   → 组合使用
    """
    if isinstance(num, (int, float)):
        return f"{num:,.{decimal_places}f}"
    return str(num)


def highlight_text(text: str, color_code: str = "93") -> str:
    """
    终端彩色文本（ANSI转义码）
    
    常用颜色码：
      31 红 | 32 绿 | 33 黄 | 34 蓝 | 35 紫 | 36 青 | 93 亮黄 | 94 亮蓝 | 95 亮品红 | 97 白
    样式码：
      1 粗体 | 4 下划线
    """
    return f"\033[{color_code}m{text}\033[0m"


# 预定义颜色快捷函数
def red(text: str) -> str:       return highlight_text(text, "31")
def green(text: str) -> str:     return highlight_text(text, "32")
def yellow(text: str) -> str:    return highlight_text(text, "33")
def blue(text: str) -> str:      return highlight_text(text, "34")
def bold(text: str) -> str:      return highlight_text(text, "1")


def paginate(items: list, page: int = 1, per_page: int = 10) -> dict:
    """
    分页处理工具
    
    知识点：切片操作 [start:end]
         Python切片越界不会报错！这是非常方便的特性。
         
    返回字典:
    {
        "items": 当前页数据,
        "page": 当前页码,
        "total_pages": 总页数,
        "total_items": 总数量,
        "has_next": 是否有下一页,
        "has_prev": 是否有上一页,
    }
    """
    total = len(items)
    total_pages = max(1, (total + per_page - 1) // per_page)  # 向上取整
    page = max(1, min(page, total_pages))  # 限制页码范围
    
    start = (page - 1) * per_page
    end = start + per_page
    page_items = items[start:end]
    
    return {
        "items": page_items,
        "page": page,
        "total_pages": total_pages,
        "total_items": total,
        "has_next": page < total_pages,
        "has_prev": page > 1,
    }
