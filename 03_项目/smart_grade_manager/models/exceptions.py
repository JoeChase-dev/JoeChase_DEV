"""
自定义异常类模块
==================
知识点：异常处理体系 - 继承Exception创建业务异常
适用场景：当内置异常不够表达业务含义时，自定义异常更清晰

学习要点：
1. 自定义异常只需要继承 Exception（或其子类）
2. 异常链：raise ... from ... 保留原始错误信息
3. __init__ 接收自定义参数，__str__ 返回友好提示
"""


class StudentManagerError(Exception):
    """学生管理系统基础异常类 - 所有自定义异常的父类"""
    
    def __init__(self, message: str = "学生管理操作失败"):
        self.message = message
        super().__init__(self.message)


class StudentNotFoundError(StudentManagerError):
    """找不到学生的异常 - 用于删除/修改时学号不存在的情况"""
    
    def __init__(self, student_id: str = ""):
        self.student_id = student_id
        message = f"❌ 找不到学号为 [{student_id}] 的学生" if student_id else "❌ 找不到该学生"
        super().__init__(message)


class DuplicateStudentError(StudentManagerError):
    """重复添加学生的异常 - 学号已存在"""
    
    def __init__(self, student_id: str, name: str = ""):
        self.student_id = student_id
        detail = f"姓名: {name}" if name else ""
        message = f"⚠️ 学号 [{student_id}] 已存在！{detail} 请使用修改功能更新信息"
        super().__init__(message)


class InvalidScoreError(StudentManagerError):
    """无效成绩的异常 - 分数不在0-100范围内"""
    
    def __init__(self, score, subject: str = ""):
        self.score = score
        self.subject = subject
        if subject:
            message = f"📊 {subject}成绩无效: {score}，分数必须在 0-100 之间"
        else:
            message = f"📊 成绩无效: {score}，分数必须在 0-100 之间"
        super().__init__(message)


class DataValidationError(StudentManagerError):
    """数据验证异常 - 通用的数据格式错误"""
    
    def __init__(self, field: str, value, reason: str = ""):
        self.field = field
        self.value = value
        message = f"🔍 {field} 验证失败: 值为 [{value}]"
        if reason:
            message += f"，原因: {reason}"
        super().__init__(message)


class FileOperationError(StudentManagerError):
    """文件操作异常 - 读写文件时的错误"""
    
    def __init__(self, filepath: str, operation: str = "读写", reason: str = ""):
        self.filepath = filepath
        message = f"📁 文件{operation}失败: {filepath}"
        if reason:
            message += f"\n   原因: {reason}"
        super().__init__(message)
