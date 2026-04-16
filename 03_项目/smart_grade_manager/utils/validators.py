"""
输入验证模块 - 正则表达式实战
==============================
正则表达式(Regular Expression)是一种强大的文本模式匹配工具。
Python中通过 re 模块使用。

本文件展示正则在实际项目中的应用：验证各种输入格式

📚 知识点覆盖:
  ✓ re.match() vs re.search() vs re.fullmatch()
  ✓ re.compile() 预编译（性能优化）
  ✓ 捕获组与非捕获组 (?:...)
  ✓ 字符类、量词、锚点、转义
  ✓ 常用验证模式的编写
"""
import re
from typing import Tuple, Optional


# ========== 预编译的正则模式 ==========
# 知识点：re.compile() 将正则表达式编译为Pattern对象
#         编译一次，多次使用，比每次调用re.match()效率更高
#         特别适合在循环或频繁调用的场景

# 学号模式：2026 + 4位数字
STUDENT_ID_PATTERN = re.compile(
    r"^2026\d{4}$"          # ^开头, 2026固定前缀, \d{4}恰好4位数字, $结尾
)

# 姓名模式：中文姓名（2-4个汉字）
NAME_PATTERN = re.compile(
    r"^[\u4e00-\u9fa5]{2,4}$"   # \u4e00-\u9fa5 是Unicode中文范围
)

# 手机号模式：1开头的11位数字
PHONE_PATTERN = re.compile(
    r"^1[3-9]\d{9}$"        # 1开头, 第2位3-9, 共11位
)

# 邮箱模式
EMAIL_PATTERN = re.compile(
    r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
)

# 成绩范围验证（非正则，但放在一起管理）
SCORE_RANGE = (0, 100)


def validate_student_id(student_id: str) -> Tuple[bool, str]:
    r"""
    验证学号格式
    
    学号规则：
      - 以2026开头（入学年份）
      - 后跟4位数字（序号0001-9999）
      - 总长度8位
    
    正则拆解：
      ^       - 匹配字符串开头
      2026    - 固定字符 "2026"
      \d{4}   - 恰好4个数字字符 (等价于 [0-9]{4})
      $       - 匹配字符串结尾
      
    返回:
      (True, "") 表示通过
      (False, "错误信息") 表示未通过
    """
    if not student_id or not isinstance(student_id, str):
        return False, "学号不能为空且必须是字符串"
    
    if STUDENT_ID_PATTERN.fullmatch(student_id):
        return True, ""
    
    # 提供详细的错误提示
    if not student_id.startswith("2026"):
        return False, f"学号应以 '2026' 开头，当前值: '{student_id}'"
    if len(student_id) != 8:
        return False, f"学号应为8位，当前 {len(student_id)} 位: '{student_id}'"
    if not student_id[4:].isdigit():
        return False, f"学号后4位应为纯数字，当前: '{student_id[4:]}'"
    
    return False, f"学号格式无效: '{student_id}'"


def validate_name(name: str) -> Tuple[bool, str]:
    """验证姓名（支持中文名和英文名）"""
    if not name or not isinstance(name, str):
        return False, "姓名不能为空"
    
    name = name.strip()
    
    # 中文名：2-4个汉字
    if NAME_PATTERN.fullmatch(name):
        return True, ""
    
    # 英文名：2-20个字母（允许空格）
    english_pattern = re.compile(r"^[a-zA-Z][a-zA-Z ]{1,19}$")
    if english_pattern.fullmatch(name):
        return True, ""
    
    return False, f"姓名格式无效: '{name}'，请输入2-4个汉字或英文名"


def validate_score(score, subject: str = "") -> Tuple[bool, str]:
    """
    验证成绩是否在有效范围内
    
    参数可以是int、float或可转换为数字的字符串
    
    知识点：try/except 用于类型转换的优雅处理
              比先检查 type() 再转换更 Pythonic
    """
    # 尝试转换为浮点数
    try:
        score_val = float(score)
    except (TypeError, ValueError):
        return False, f"'{score}' 不是有效的数字"
    
    min_score, max_score = SCORE_RANGE
    if min_score <= score_val <= max_score:
        return True, ""
    
    subj_info = f"[{subject}] " if subject else ""
    return False, f"{subj_info}成绩 {score_val} 超出范围 ({min_score}-{max_score})"


def validate_phone(phone: str) -> Tuple[bool, str]:
    """
    验证手机号格式
    
    中国手机号规则：
      - 1开头
      - 第二位是3-9（排除早期的10、11、12等号段）
      - 总共11位纯数字
    """
    if not phone:
        return True, ""  # 手机号可选，空值通过
    
    if PHONE_PATTERN.fullmatch(phone.strip()):
        return True, ""
    
    return False, f"手机号格式无效: '{phone}'，应为11位中国手机号"


def validate_email(email: str) -> Tuple[bool, str]:
    """验证邮箱格式"""
    if not email:
        return True, ""  # 邮箱可选
    
    if EMAIL_PATTERN.fullmatch(email.strip()):
        return True, ""
    
    return False, f"邮箱格式无效: '{email}'"


def validate_gender(gender_str: str) -> Tuple[bool, str]:
    """验证性别输入"""
    valid_values = {"M", "F", "男", "女", "male", "female", "m", "f"}
    if gender_str.upper().strip() in {"M", "MALE"}:
        return True, "M"
    elif gender_str.upper().strip() in {"F", "FEMALE"}:
        return True, "F"
    elif gender_str in ("男", "♀"):
        return True, "M"
    elif gender_str in ("女", "♂"):
        return True, "F"
    
    return False, f"性别无效: '{gender_str}'，请输入 M/F 或 男/女"


# ========== 高级正则示例 ==========

class TextExtractor:
    """
    文本提取工具类 - 展示正则的高级用法
    
    知识点：
      - re.findall(): 找到所有匹配项
      - re.sub(): 替换匹配项
      - re.finditer(): 返回迭代器（大数据时更省内存）
      - 捕获组 (): 提取子串
      - 非捕获组 (?:...): 分组但不捕获
      - 命名捕获组 (?P<name>...): 给组起名字
    """
    
    @staticmethod
    def extract_numbers(text: str) -> list:
        """提取文本中的所有数字（包括小数）"""
        pattern = r"-?\d+\.?\d*"     # -? 可选负号, \d+ 整数部分, \.?可选小数点, \d* 小数部分
        return re.findall(pattern, text)
    
    @staticmethod
    def extract_chinese(text: str) -> str:
        """提取文本中所有汉字"""
        pattern = r"[\u4e00-\u9fa5]+"
        return "".join(re.findall(pattern, text))
    
    @staticmethod
    def mask_phone(text: str) -> str:
        """脱敏处理手机号（中间4位用*替代）"""
        # 使用命名捕获组和反向引用
        pattern = r"(1)(\d{2})(\d{4})(\d{4})"
        replacement = r"\1\2****\4"    # \1,\2,\4 引用对应的捕获组
        return re.sub(pattern, replacement, text)
    
    @staticmethod
    def parse_log_line(line: str) -> Optional[dict]:
        """
        解析日志行 - 综合运用多种正则特性
        
        示例日志格式:
            [2026-04-16 12:30:45] [INFO] [main] 用户登录成功 user_id=12345
        
        命名捕获组 (?P<name>...) 让代码更易读！
        """
        log_pattern = re.compile(
            r"\[(?P<timestamp>[^\]]+)\]"   # 时间戳（方括号内非]内容）
            r"\s+\[(?P<level>\w+)\]"        # 日志级别
            r"\s+\[(?P<module>[^\]]+)\]"    # 模块名
            r"\s+(?P<message>.+)"           # 日志消息
        )
        
        match = log_pattern.match(line.strip())
        if match:
            return match.groupdict()   # 返回命名组的字典
        return None


# ========== 实用工具函数 ==========

def sanitize_input(text: str) -> str:
    """清理用户输入：去除首尾空白、合并多余空格"""
    return " ".join(text.split())


def truncate(text: str, max_length: int = 20, suffix: str = "...") -> str:
    """截断过长的文本"""
    if len(text) <= max_length:
        return text
    return text[:max_length - len(suffix)] + suffix
