"""
枚举定义模块
================
知识点：枚举(Enum) - 限制变量只能取特定值，避免魔法字符串
适用场景：性别、成绩等级等有限选项的场景

学习要点：
1. Enum vs IntEnum 的区别
2. 枚举成员的 name 和 value 属性
3. 如何在类中使用枚举类型注解
"""
from enum import Enum, auto


class Gender(Enum):
    """性别枚举"""
    MALE = "M"      # 男性
    FEMALE = "F"    # 女性
    
    @classmethod
    def from_str(cls, value: str) -> "Gender":
        """
        从字符串转换为枚举值
        知识点：类方法(cls) vs 实例方法(self)
        """
        value = value.upper().strip()
        for gender in cls:
            if gender.value == value:
                return gender
        raise ValueError(f"无效的性别值: {value}，请输入 M(男) 或 F(女)")
    
    def __str__(self) -> str:
        """魔术方法：自定义枚举的字符串表示"""
        return "男" if self == Gender.MALE else "女"
    
    def display(self) -> str:
        return str(self)


class GradeLevel(Enum):
    """成绩等级枚举 - 基于百分制的等级划分"""
    A = auto()   # 优秀 (90-100)
    B = auto()   # 良好 (80-89)
    C = auto()   # 中等 (70-79)
    D = auto()   # 及格 (60-69)
    F = auto()   # 不合格 (<60)
    
    @classmethod
    def from_score(cls, score: float) -> "GradeLevel":
        """根据分数返回对应的等级"""
        if score >= 90:
            return cls.A
        elif score >= 80:
            return cls.B
        elif score >= 70:
            return cls.C
        elif score >= 60:
            return cls.D
        else:
            return cls.F
    
    def __str__(self) -> str:
        """返回等级的中文名称"""
        names = {
            GradeLevel.A: "A (优秀)",
            GradeLevel.B: "B (良好)",
            GradeLevel.C: "C (中等)",
            GradeLevel.D: "D (及格)",
            GradeLevel.F: "F (不合格)",
        }
        return names[self]
    
    @property
    def is_passing(self) -> bool:
        """
        属性装饰器@property：让方法可以像属性一样访问
        用法：grade_level.is_passing  # 不需要加括号！
        """
        return self != GradeLevel.F


class Subject(Enum):
    """科目枚举"""
    PYTHON = "Python"
    MATH = "数学"
    ENGLISH = "英语"
    
    def __str__(self) -> str:
        return self.value
