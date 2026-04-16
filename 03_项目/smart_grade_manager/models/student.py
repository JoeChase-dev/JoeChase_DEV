"""
学生数据模型 - 核心OOP知识点集中体现
=====================================
本文件是整个项目的核心，涵盖以下Week 1-2的Python知识点：

📚 Week 1 知识点：
  ✓ 变量与类型注解 (type hints)
  ✓ 字符串操作 (f-string, 方法)
  ✓ 列表/字典/集合 (scores字典, _subjects列表)
  ✓ 分支结构 (if/elif/else 用于等级判断)
  ✓ 函数定义与方法

📚 Week 2 知识点：
  ✓ 类与对象 (class Student)
  ✓ 继承 (异常类的继承体系)
  ✓ 魔术方法 (__init__, __str__, __repr__, __lt__, __eq__, etc.)
  ✓ 封装 (私有属性_, 属性@property)
  ✓ 异常处理 (raise + 自定义异常)
  ✓ @property 装饰器 (getter/setter)

🎯 设计模式：
  - 数据类模式：用属性存储学生信息
  - 值对象模式：通过魔术方法支持比较和显示
"""
from dataclasses import dataclass, field
from typing import Dict, List, Optional
from datetime import datetime
import re

# 导入同包中的枚举和异常
from .enums import Gender, GradeLevel, Subject
from .exceptions import InvalidScoreError, DataValidationError


@dataclass
class Student:
    """
    学生数据模型
    
    使用 @dataclass 装饰器自动生成 __init__ 和 __repr__
    知识点：dataclass 是 Python 3.7+ 引入的语法糖，减少样板代码
    
    属性说明:
        student_id: 学号 (唯一标识)
        name: 姓名
        gender: 性别 (使用Gender枚举)
        scores: 各科成绩字典 {科目名: 分数}
    """
    
    # ====== 实例属性 (每个学生对象独有的数据) ======
    student_id: str                          # 学号 - 字符串类型
    name: str                                # 姓名
    gender: Gender                           # 性别 - 枚举类型(非简单str)
    scores: Dict[str, float] = field(default_factory=dict)  # 成绩字典 - 默认空字典
    _created_at: datetime = field(default_factory=datetime.now, init=False, repr=False)
    
    # ====== 类属性 (所有学生共享的数据) ======
    # 知识点：类变量 vs 实例变量的区别
    #   类变量：属于类本身，所有实例共享（如学生总数统计）
    #   实例变量：属于每个对象，各自独立（如姓名、成绩）
    _subjects = ["Python", "数学", "英语"]     # 支持的科目列表（类级别共享）
    _id_pattern = re.compile(r"^2026\d{4}$") # 学号正则模式（编译一次，全局复用）
    
    def __post_init__(self):
        """
        dataclass 特殊钩子：在__init__之后自动调用
        用途：进行初始化后的验证和额外处理
        
        知识点：这是 dataclass 的"构造后回调"，相当于增强版的 __init__
        """
        self._validate_student_id()
        self._validate_scores()
    
    # ========== 私有方法 - 内部辅助函数 ==========
    def _validate_student_id(self):
        """验证学号格式是否合法"""
        if not self._id_pattern.match(self.student_id):
            raise DataValidationError(
                field="学号",
                value=self.student_id,
                reason="格式应为 2026 + 4位数字，如 20260001"
            )
    
    def _validate_scores(self):
        """验证所有成绩是否在合法范围内"""
        for subject, score in self.scores.items():
            if not isinstance(score, (int, float)):
                raise DataValidationError(field=f"{subject}成绩", value=score, reason="必须是数字")
            if not 0 <= score <= 100:
                raise InvalidScoreError(score=score, subject=subject)
    
    # ========== 属性装饰器 - getter/setter ==========
    @property
    def total_score(self) -> float:
        """
        总分计算属性 (只读)
        
        @property 装饰器的用法：
          - 让方法像属性一样访问: student.total_score (不用加括号!)
          - 只需要 getter 时最简洁
          
        知识点：sum()内置函数 + 生成器表达式
              sum(score for score in self.scores.values()) 
              等价于手动循环求和，但更 Pythonic！
        """
        return round(sum(self.scores.values()), 2)
    
    @property
    def average_score(self) -> float:
        """平均分 (保留2位小数)"""
        if not self.scores:
            return 0.0
        return round(self.total_score / len(self.scores), 2)
    
    @property
    def grade_level(self) -> GradeLevel:
        """根据平均分返回成绩等级"""
        return GradeLevel.from_score(self.average_score)
    
    @property
    def rank_info(self) -> str:
        """排名信息字符串 - 组合多个属性"""
        level = self.grade_level
        passing_status = "✅ 及格" if level.is_passing else "❌ 不及格"
        return f"{level} | {passing_status}"
    
    # ========== 魔术方法 (Dunder Methods) ==========
    # 这些以 __开头结尾的方法让对象能和Python内置语法/函数配合使用
    # 是面向对象编程中最重要的概念之一！
    
    def __str__(self) -> str:
        """
        魔术方法：对象的字符串表示
        触发时机：print(student), str(student), f"{student}"
        
        设计原则：返回用户友好的、可读的信息
        """
        gender_str = str(self.gender)
        scores_str = " | ".join(
            f"{subj}: {self.scores.get(subj, '--')}分" 
            for subj in self._subjects
        )
        return (
            f"[{self.student_id}] {self.name} ({gender_str})\n"
            f"  📊 成绩: {scores_str}\n"
            f"  📈 总分: {self.total_score} | 均分: {self.average_score} | 等级: {self.grade_level}"
        )
    
    def __repr__(self) -> str:
        """
        魔术方法：开发者用的字符串表示
        触发时机：在交互式环境中直接输入对象名，或 repr(student)
        
        与 __str__ 的区别：
          - __str__: 给最终用户看，要友好可读
          - __repr__: 给开发者看，要能还原对象 student == eval(repr(student))
        """
        scores_repr = ", ".join(
            f"{k}={v}" for k, v in self.scores.items()
        )
        return (
            f"Student(student_id='{self.student_id}', "
            f"name='{self.name}', "
            f"gender={self.gender}, "
            f"scores={{{scores_repr}}})"
        )
    
    def __eq__(self, other) -> bool:
        """
        魔术方法：相等比较 (==)
        触发时机：student1 == student2
        
        设计决策：两个学生相等的判定标准是学号相同
        这符合业务逻辑：学号是唯一标识
        """
        if not isinstance(other, Student):
            return NotImplemented  # 返回NotImplemented让Python尝试反向操作
        return self.student_id == other.student_id
    
    def __lt__(self, other) -> bool:
        """
        魔术方法：小于比较 (<)
        触发时刻：student1 < student2, sorted([students])
        
        知识点：实现 __lt__ 后，sorted()、min()、max() 都能用了！
               Python会自动推导出 >, >=, <= (基于 __lt__ 取反)
        """
        if not isinstance(other, Student):
            return NotImplemented
        # 比较规则：按总分排序，总分相同按学号排（保证稳定）
        if self.total_score != other.total_score:
            return self.total_score < other.total_score
        return self.student_id < other.student_id
    
    def __hash__(self) -> int:
        """
        魔术方法：哈希值计算
        触发时机：将对象放入 set 或作为 dict 的键时
        
        重要规则：如果重写了 __eq__，必须同时重写 __hash__！
                  且相等对象必须有相同的哈希值
        """
        return hash(self.student_id)
    
    def __bool__(self) -> bool:
        """
        魔术方法：布尔值转换
        触发时机：if student:, bool(student)
        
        设计：只要有任意一门成绩就视为有效学生
        """
        return len(self.scores) > 0
    
    def __contains__(self, subject: str) -> bool:
        """
        魔术方法：in 运算符
        触发时机："Python" in student
        
        知识点：这让我们能用直观的语法检查某科是否有成绩
        """
        return subject in self.scores
    
    # ========== 公共实例方法 ==========
    
    def set_score(self, subject: str, score: float):
        """
        设置单科成绩（带验证）
        
        参数:
            subject: 科目名称
            score: 分数 (0-100)
            
        异常:
            InvalidScoreError: 当分数不在0-100范围时抛出
        """
        if not 0 <= score <= 100:
            raise InvalidScoreError(score=score, subject=subject)
        self.scores[subject] = round(float(score), 2)
    
    def get_score(self, subject: str, default=None) -> Optional[float]:
        """
        获取单科成绩
        
        知识点：dict.get() 的 default 参数 - 键不存在时返回默认值而非报错
        """
        return self.scores.get(subject, default)
    
    def to_dict(self) -> dict:
        """
        序列化为字典 - 用于JSON存储
        
        知识点：数据转换 - 对象 → 可序列化的字典
        """
        return {
            "student_id": self.student_id,
            "name": self.name,
            "gender": self.gender.value,  # 枚举转为其value值
            "scores": self.scores,
            "created_at": self._created_at.isoformat(),
        }
    
    @classmethod
    def from_dict(cls, data: dict) -> "Student":
        """
        类方法：从字典反序列化为对象
        与 to_dict() 配对使用
        
        知识点：
          - @classmethod: 第一个参数是 cls（类本身），不是 self（实例）
          - 工厂模式：提供多种创建对象的方式
        """
        gender = Gender.from_str(data.get("gender", "M"))
        student = cls(
            student_id=data["student_id"],
            name=data["name"],
            gender=gender,
            scores=data.get("scores", {}),
        )
        if "created_at" in data:
            student._created_at = datetime.fromisoformat(data["created_at"])
        return student
    
    def display_summary(self) -> str:
        """生成简短摘要行 - 用于列表展示"""
        avg = self.average_score
        level = self.grade_level
        return (
            f"{self.student_id:>8} | {self.name:<8} | "
            f"{str(self.gender):>2} | "
            f"均分:{avg:>6.2f} | 总分:{self.total_score:>6.1f} | {level}"
        )
    
    def display_detailed(self) -> str:
        """生成详细信息展示"""
        lines = [
            "=" * 50,
            f"  🎓 学生详细信息",
            "=" * 50,
            f"  学号:   {self.student_id}",
            f"  姓名:   {self.name}",
            f"  性别:   {self.gender}",
            f"  注册时间: {_fmt_datetime(self._created_at)}",
            "-" * 50,
            "  📊 各科成绩:",
        ]
        for subj in self._subjects:
            score = self.scores.get(subj, "--")
            level = GradeLevel.from_score(score) if isinstance(score, (int, float)) else None
            level_str = f" [{level}]" if level else ""
            lines.append(f"    • {subj}: {score}分{level_str}")
        lines += [
            "-" * 50,
            f"  📈 汇总: 总分={self.total_score}, 均分={self.average_score:.2f}",
            f"  🏆 等级: {self.grade_level}",
            "=" * 50,
        ]
        return "\n".join(lines)


# ========== 辅助函数 (模块级，不属于任何类) ==========
def _fmt_datetime(dt: datetime) -> str:
    """格式化日期时间"""
    return dt.strftime("%Y-%m-%d %H:%M:%S")


def create_student_from_input(student_id: str, name: str, 
                               gender_str: str, **scores) -> Student:
    """
    工厂函数：从输入参数快速创建学生对象
    
    知识点：**kwargs 接收任意关键字参数
           **scores 会收集所有传入的关键字参数为字典
           
    用法示例:
        create_student_from_input(
            "2026001", "张三", "M", 
            Python=95, 数学=88, 英语=92
        )
    """
    gender = Gender.from_str(gender_str)
    student = Student(
        student_id=student_id,
        name=name,
        gender=gender,
        scores=scores,
    )
    return student


def batch_create_students(data_list: list) -> List[Student]:
    """
    批量创建学生对象 - 从字典列表
    
    知识点：列表推导式 + 条件过滤的一行实现
    """
    students = []
    for item in data_list:
        try:
            student = Student.from_dict(item) if isinstance(item, dict) else item
            students.append(student)
        except Exception as e:
            print(f"⚠️ 跳过无效数据: {item}, 原因: {e}")
    return students
