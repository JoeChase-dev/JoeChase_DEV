"""
╔══════════════════════════════════════════════════════════════╗
║                                                              ║
║   🎓 智能学生成绩管理系统 - 讲解版（带完整知识注释）          ║
║                                                              ║
║   适合：第一次学习 Python 的同学                            ║
║   用法：边读代码边看注释，每个注释标注了对应的知识点        ║
║                                                              ║
╚══════════════════════════════════════════════════════════════╝

📚 本文件将所有核心代码整合在一起，并添加超详细的知识点注释。
每个重要概念都标注了 [知识点标签]，方便你定位复习。

运行方式：
    python annotated_guide.py
    
目录：
  Part 1: 基础语法 (变量/类型/运算符/分支/循环/字符串/容器)
  Part 2: 面向对象 (类/继承/魔术方法/异常/文件IO)
  Part 3: 高级特性 (装饰器/生成器/正则/多线程)
  Part 4: 综合实战 (CLI交互系统)
"""

import json           # JSON序列化/反序列化模块
import os             # 操作系统路径相关功能
import re             # 正则表达式模块
import time           # 时间相关函数
import functools      # 装饰器工具函数
import threading      # 多线程模块
import tempfile       # 临时文件处理
from datetime import datetime  # 日期时间类
from typing import List, Dict, Any, Optional, Callable, Tuple
from dataclasses import dataclass, field  # 数据类装饰器
from enum import Enum, auto               # 枚举类
from abc import ABC, abstractmethod       # 抽象基类


# =====================================================================
#                    Part 1: 基础语法 - 知识点实战
# =====================================================================

"""
【Week 1 核心知识速查】

1️⃣ 变量与数据类型
━━━━━━━━━━━━━━━━━━━━━
Python 是动态类型语言——不需要声明变量类型，解释器自动推断。

基本类型:
  int     → 整数:    42, -7, 0, 999999
  float   → 浮点数:  3.14, 2.0, -0.5, 1e10 (科学计数法)
  str     → 字符串:  "hello", 'world', '多行文本(用单引号包裹)'
  bool    → 布尔值:  True, False (注意首字母大写!)
  NoneType→ 空值:    None (表示"没有值"，不是0，不是"")

类型转换:
  int("42")      → 42      # 字符串转整数
  float("3.14")  → 3.14    # 字符串转浮点数
  str(123)       → "123"   # 数字转字符串
  bool(1)        → True    # 非零值为True
  list("abc")    → ['a','b','c']  # 字符串转列表

2️⃣ 运算符
━━━━━━━━━━━━━━
算术运算:  +  -  *  /  //  %  **
比较运算:  ==  !=  <  >  <=  >=
逻辑运算:  and  or  not
成员运算:  in  not in      # "a" in "apple" → True
身份运算:  is  is not      # x is None (判断是否同一对象)

重点注意:
  /   → 真除法:  7 / 2 = 3.5
  //  → 地板除(取整): 7 // 2 = 3
  %   → 取余数:  7 % 2 = 1
  **  → 幂运算:  **2 = 8

3️⃣ 分支结构 if/elif/else
━━━━━━━━━━━━━━━━━━━━━━━
if 条件1:
    执行语句1
elif 条件2:
    执行语句2         # elif 可以有多个或没有
else:
    执行语句3         # else 也可以没有

注意: Python 用缩进(4个空格)来区分代码块！不用大括号 {}

4️⃣ 循环结构
━━━━━━━━
for循环(遍历已知次数):
    for i in range(5):     # 0,1,2,3,4
    for item in list:      # 遍历列表的每个元素
    for key in dict:       # 遍历字典的键
    for i, val in enumerate(list):  # 同时获取索引和值

while循环(条件未知时):
    while condition:      # 条件为True就一直执行

控制循环:
    break    # 立即退出整个循环
    continue # 跳过本次迭代，继续下一次

5. 函数定义与调用
━━━━━━━━━━━━━━━━━━
def func_name(param1, param2=default_value):
    '''Function doc string (optional but recommended)'''
    return value

Parameter types:( Python 函数的 5 种参数类型)
  positional（位置参数）:   def f(a, b)        # f(1, 2)  顺序传递，不可省略
  keyword（关键字参数）:     def f(a, b)        # f(a=1, b=2)  进行指定，顺序无关
  default（默认值参数）:     def f(a, b=10)     # f(1) -> b defaults to 10  注意：默认值参数必须放在位置参数之后！
  *args（可变位置参数收集为元组）:       def f(*args)      # f(1,2,3) -> args=(1,2,3)
  **kwargs（可变关键字参数）:    def f(**kwargs)   # f(a=1,b=2) -> kwargs={'a':1,'b':2}  **kwargs 把 所有额外的关键字参数 收集为一个 字典

6️⃣ 字符串操作
━━━━━━━━
创建:    s = "hello" 或 s = 'world'
拼接:    s1 + s2 → "helloworld"
重复:    s * 3 → "hellohellohello"
切片:    s[1:4]  → "ell"  (从索引1到3，不包含4)
         s[:3]   → "hel"  (从头开始到2)
         s[-3:]  → "llo"  (倒数3个到最后)
长度:    len(s)  → 5
查找:    s.find("l") → 2 (首次出现的位置,找不到返回-1)
替换:    s.replace("l", "L") → "heLLo"
分割:    s.split(",") → 按逗号分割成列表
大小写:  s.upper(), s.lower(), s.capitalize()
去除空白: s.strip(), s.lstrip(), s.rstrip()

f-string格式化(Python 3.6+ 推荐!):
  name = "张三"; age = 18
  f"我叫{name}, 今年{age}岁"  → "我叫张三, 今年18岁"
  f"{name:>10}"               # 右对齐占10格
  f"{age:.2f}"                # 保留2位小数
  f"{100:,}"                  # 千分位分隔: "100"

7️⃣ 容器类型
━━━━━━
列表 List (有序, 可变):
  创建: lst = [1, 2, 3] 或 lst = list()
  添加: lst.append(4) → [1,2,3,4]
  删除: lst.remove(2) 或 del lst[0] 或 lst.pop()
  访问: lst[0]  lst[-1](最后一个)  lst[1:3](切片)
  长度: len(lst)
  排序: lst.sort() 或 sorted(lst)

字典 Dict (键值对, 无序但Python3.7+保持插入顺序):
  创建: d = {"name": "张三", "age": 18} 或 d = dict()
  访问: d["name"] 或 d.get("name", "默认值")
  修改: d["age"] = 19
  删除: del d["age"] 或 d.pop("age")
  遍历: for k,v in d.items():
       for k in d.keys():    # 只遍历键
       for v in d.values()   # 只遍历值

集合 Set (无序, 唯一, 可变):
  创建: s = {1, 2, 3} 或 s = set([1,2,2,3]) → {1,2,3}(自动去重)
  操作: s.add(4), s.discard(2), s1 & s2(交集), s1 | s2(并集)

元组 Tuple (有序, 不可变):
  创建: t = (1, 2, 3) 或 t = tuple()
  用途: 作为字典键、函数返回多个值 return a, b
"""


# ====== 实战演示: 基础语法在项目中的应用 ======

def demo_basic_syntax():
    """演示基础语法的实际应用"""
    
    print("=" * 60)
    print("Part 1: 基础语法实战演示")
    print("=" * 60)
    
    # --- 变量与类型 ---
    student_name = "张三"            # str 类型
    student_id = "20260001"         # str 类型(学号用字符串方便处理前导0)
    python_score = 95              # int 类型
    math_score = 88.5              # float 类型
    is_active = True               # bool 类型
    
    # --- 运算符 ---
    english_score = 92
    total = python_score + math_score + english_score  # + 加法
    average = total / 3                                    # / 真除法
    avg_rounded = round(average, 2)                       # round 四舍五入
    
    print(f"\n学生: {student_name}")
    print(f"成绩: Python={python_score} 数学={math_score} 英语={english_score}")
    print(f"总分: {total}, 平均分: {avg_rounded}")
    
    # --- 分支结构: 成绩等级判定 ---
    print("\n--- 成绩等级判定 (if/elif/else) ---")
    if avg_rounded >= 90:
        level = "A (优秀)"
    elif avg_rounded >= 80:
        level = "B (良好)"
    elif avg_rounded >= 70:
        level = "C (中等)"
    elif avg_rounded >= 60:
        level = "D (及格)"
    else:
        level = "F (不合格)"
    
    print(f"等级: {level}")
    
    # --- 列表操作: 多个学生的成绩 ---
    print("\n--- 列表操作 ---")
    scores_list = [95, 82, 76, 91, 55, 88, 93, 67]  # 8个学生的Python成绩
    
    # 列表推导式: 过滤出及格的成绩
    passing = [s for s in scores_list if s >= 60]
    print(f"全部成绩: {scores_list}")
    print(f"及格成绩: {passing}")
    print(f"最高分: {max(scores_list)}, 最低分: {min(scores_list)}")
    print(f"平均分: {sum(scores_list)/len(scores_list):.2f}")
    
    # 排序 (sorted返回新列表, 不改变原列表)
    sorted_scores = sorted(scores_list, reverse=True)  # 从大到小
    print(f"降序排列: {sorted_scores}")
    
    # --- 字典操作: 学生信息存储 ---
    print("\n--- 字典操作 ---")
    student_dict = {
        "student_id": "20260001",
        "name": "张三",
        "gender": "男",
        "scores": {
            "Python": 95,
            "数学": 88.5,
            "英语": 92,
        }
    }
    
    print(f"学号: {student_dict['student_id']}")
    print(f"姓名: {student_dict.get('name')}")
    print(f"各科成绩:")
    for subject, score in student_dict["scores"].items():  # 遍历字典项
        print(f"  • {subject}: {score}分")
    
    # --- 循环结构 ---
    print("\n--- for循环遍历 ---")
    students = [
        ("20260001", "张三", 95),
        ("20260002", "李四", 82),
        ("20260003", "王五", 76),
    ]
    
    # enumerate 同时获取索引和值
    for idx, (sid, name, score) in enumerate(students, start=1):
        status = "优秀" if score >= 90 else "良好" if score >= 80 else "继续加油"
        print(f"  第{idx}名: [{sid}] {name} - Python:{score}分 ({status})")


# =====================================================================
#                    Part 2: 面向对象编程 - OOP实战
# =====================================================================

"""
【Week 2 核心知识速查】

1️⃣ 类(Class)与对象(Object)
━━━━━━━━━━━━━━━━━━━━━━━━━
类: 对象的蓝图/模板 (比如"学生"这个概念)
对象: 类的具体实例 (比如"张三"、"李四"这些具体的人)

class Student:                 # 定义类(用 PascalCase 命名)
    count = 0                   # 类属性(所有实例共享)
    
    def __init__(self, name):    # 构造方法(创建对象时自动调用)
        self.name = name        # 实例属性(每个对象独立)
        Student.count += 1       # 访问类属性
        
    def say_hello(self):         # 实例方法
        print(f"你好，我是{self.name}")

s1 = Student("张三")           # 创建实例(__init__自动调用)
s2 = Student("李四")
s1.say_hello()                  # 调用方法

2️⃣ 四大封装特性
━━━━━━━━
封装: 用类把数据和操作绑定在一起 (self.xxx 属性)
继承: 子类获得父类的所有属性和方法
多态: 不同子类对同一方法有不同的实现
抽象: 定义接口规范而不实现细节

3️⃣ 魔术方法(Dunder Methods)
━━━━━━━━━━━━━━━━━━━━━━━━━
以双下划线开头结尾的特殊方法，让自定义类能使用Python内置语法:

__init__   构造方法: obj = MyClass(args)
__str__    字符串:   print(obj) 或 str(obj)
__repr__   开发表示: repr(obj) (用于调试)
__eq__     相等比较: obj1 == obj2
__lt__     小于比较: obj1 < obj2 (实现后可用sorted/max/min)
__len__    长度:     len(obj)
__bool__   布尔转换: if obj:
__contains__: 成员检测: x in obj
__getitem__: 索引访问: obj[key]
__call__   可调用:   obj()  像函数一样调用对象
__hash__   哈希值:   可放入set和作为dict的key

4️⃣ @property 装饰器
━━━━━━━━
把方法变成"只读属性"，访问时不需加括号:

class Circle:
    def __init__(self, r):
        self.radius = r
    
    @property
    def area(self):               # 像属性一样访问: circle.area
        return 3.14159 * self.radius ** 2

c = Circle(5)
print(c.area)                   # 不需要 c.area()!

5️⃣ 异常处理 try/except/finally
━━━━━━━━
try:
    可能出错的代码
except ValueError as e:         # 捕获特定异常
    处理ValueError
except (TypeError, KeyError):   # 捕获多种异常
    处理TypeError或KeyError
else:                           # try中没有异常时执行
    print("一切正常!")
finally:                        # 无论是否异常都执行(常用于清理资源)
    print("清理工作")

6️⃣ 文件I/O
━━━━━━━━
with open("file.txt", "r", encoding="utf-8") as f:
    # with语句会自动关闭文件(即使发生异常)
    content = f.read()            # 全部读取为字符串
    lines = f.readlines()        # 读取所有行为列表
    for line in f:               # 逐行读取(推荐用于大文件)
        pass

写入模式:
  "r"  只读 (默认)
  "w"  写入 (覆盖已有内容!)
  "a"  追加 (在末尾添加)
  "r+" 读写
"""


# ====== 实战演示: 面向对象在项目中的应用 ======

class Student:
    """
    学生类 - 手写版本(不使用dataclass)，更清晰地展示OOP知识
    """
    
    def __init__(self, student_id: str, name: str, gender: str,
                 scores: Dict[str, float] = None):
        self.student_id = student_id
        self.name = name
        self.gender = gender
        self.scores = scores if scores is not None else {}
        self._created_at = datetime.now()
        
        # 类变量 (所有实例共享)
        self._subjects = ["Python", "数学", "英语"]
        self._validate()
    
    def _validate(self):
        """验证学号格式"""
        pattern = re.compile(r"^2026\d{4}$")
        if not pattern.match(self.student_id):
            raise ValueError(f"学号格式错误: {self.student_id}")
    
    # ========== @property 属性装饰器 ==========
    
    @property
    def total_score(self) -> float:
        """
        📌 [知识点: @property 只读属性]
        
        普通方法调用: student.total_score()   ← 需要括号
        property调用: student.total_score     ← 不需要括号!
        
        内部使用了 sum() + 生成器表达式:
          sum(scores.values()) 等价于手动循环求和
        """
        return round(sum(self.scores.values()), 2)
    
    @property
    def average_score(self) -> float:
        """平均分计算"""
        if not self.scores:
            return 0.0
        return round(self.total_score / len(self.scores), 2)
    
    # ========== 魔术方法 ==========
    
    def __str__(self) -> str:
        """
        📌 [知识点: __str__ 魔术方法]
        触发时机: print(student), str(student), f"{student}"
        设计原则: 返回用户友好的可读信息
        """
        gender_str = "男" if self.gender == "M" else "女"
        scores_str = " | ".join(
            f"{subj}: {self.scores.get(subj, '--')}分" 
            for subj in self._subjects
        )
        return (
            f"[{self.student_id}] {self.name} ({gender_str})\n"
            f"  成绩: {scores_str}\n"
            f"  总分: {self.total_score} | 均分: {self.average_score:.2f}"
        )
    
    def __repr__(self) -> str:
        """
        📌 [知识点: __repr__ vs __str__]
        __str__ → 给最终用户看(友好)
        __repr__ → 给开发者看(可用于还原对象)
        """
        scores_repr = ", ".join(f"{k}={v}" for k, v in self.scores.items())
        return f"Student('{self.student_id}', '{self.name}', scores={{{scores_repr}}})"
    
    def __eq__(self, other) -> bool:
        """
        📌 [知识点: __eq__ 相等比较]
        触发: student1 == student2
        我们规定: 学号相同就是同一个学生
        """
        if not isinstance(other, Student):
            return NotImplemented
        return self.student_id == other.student_id
    
    def __lt__(self, other) -> bool:
        """
        📌 [知识点: __lt__ 小于比较]
        触发: student1 < student2, sorted([students])
        实现 __lt__ 后，sorted(), min(), max() 都能用了！
        """
        if not isinstance(other, Student):
            return NotImplemented
        # 先比总分，总分相同则比学号(保证排序稳定)
        if self.total_score != other.total_score:
            return self.total_score < other.total_score
        return self.student_id < other.student_id
    
    def __hash__(self) -> int:
        """
        📌 [知识点: __hash__ 哈希方法]
        重写了__eq__就必须同时重写__hash__！
        否则对象无法放入 set 或作为 dict 的 key
        """
        return hash(self.student_id)
    
    def __contains__(self, subject: str) -> bool:
        """
        📌 [知识点: __contains__ in运算符]
        触发: "Python" in student
        让我们用直觉的语法检查某科是否有成绩
        """
        return subject in self.scores  # or subject in self._subjects
    
    def __bool__(self) -> bool:
        """
        📌 [知识点: __bool__ 布尔转换]
        触发: if student:, bool(student)
        有任意一门成绩就视为有效学生
        """
        return len(self.scores) > 0
    
    # ========== 公共方法 ==========
    
    def set_score(self, subject: str, score: float):
        """设置单科成绩(带范围验证)"""
        if not 0 <= score <= 100:
            raise ValueError(f"成绩必须在0-100之间: {score}")
        self.scores[subject] = round(float(score), 2)
    
    def get_score(self, subject: str, default=None):
        """获取单科成绩(键不存在返回默认值)"""
        return self.scores.get(subject, default)
    
    def to_dict(self) -> dict:
        """序列化为字典(用于JSON存储)"""
        return {
            "student_id": self.student_id,
            "name": self.name,
            "gender": self.gender,
            "scores": self.scores,
            "created_at": self._created_at.isoformat(),
        }
    
    @classmethod
    def from_dict(cls, data: dict) -> "Student":
        """
        📌 [知识点: @classmethod 类方法]
        第一个参数是 cls(类本身)，不是 self(实例)
        用途: 工厂模式 - 提供多种方式创建对象
        """
        student = cls(
            student_id=data["student_id"],
            name=data["name"],
            gender=data.get("gender", "M"),
            scores=data.get("scores", {}),
        )
        if "created_at" in data:
            student._created_at = datetime.fromisoformat(data["created_at"])
        return student


# ====== 自定义异常类 ======

class StudentError(Exception):
    """📌 [知识点: 异常继承] 所有自定义异常的基础类"""
    def __init__(self, message: str = "学生管理错误"):
        self.message = message
        super().__init__(self.message)


class DuplicateStudentError(StudentError):
    """学号已存在时的异常"""
    def __init__(self, student_id: str):
        self.sid = student_id
        super().__init__(f"学号 [{student_id}] 已存在!")


class ScoreRangeError(StudentError):
    """成绩超出范围的异常"""
    def __init__(self, score, subject=""):
        subj_info = f"[{subject}] " if subject else ""
        super().__init__(f"{subj_info}成绩无效: {score}，应在0-100范围内")


# =====================================================================
#                    Part 3: 高级特性 - Week 3 核心知识
# =====================================================================

"""
【Week 3 核心知识速查】

1️⃣ 装饰器 Decorator
━━━━━━━━━━━━━━━━━━
本质: 一个函数A，接收函数B作为参数，返回一个新函数C
效果: 在不修改原函数B的情况下，扩展B的功能

基本结构:
  def my_decorator(func):
      @functools.wraps(func)     # 重要！保留原函数信息
      def wrapper(*args, **kwargs):
          # 前置逻辑(执行前要做的事)
          result = func(*args, **kwargs)  # 调用原始函数
          # 后置逻辑(执行后要做的事)
          return result
      return wrapper

  @my_decorator                     # 语法糖: 等价于 func = my_decorator(func)
  def my_function(x):
      return x * 2

带参数的装饰器(三层嵌套):
  def decorator_with_args(param):
      def actual_decorator(func):       # 第2层: 接收函数
          @functools.wraps(func)
          def wrapper(*args, **kwargs): # 第3层: 接收调用参数
              # 使用 param 和 func
              result = func(*args, **kwargs)
              return result
          return wrapper
      return actual_decorator          # 第1层返回第2层

  @decorator_with_args(param=value)
  def my_func():
      ...

常用内置装饰器:
  @staticmethod   静态方法(不需要self/cls)
  @classmethod    类方法(第一个参数是cls)
  @property       只读属性

2️⃣ 生成器 Generator
━━━━━━━━━━━━
yield 关键字让函数变成生成器:
  - 每次调用 yield 暂停并返回值
  - 下次调用从暂停处继续
  - 优势: 内存效率极高(一次只产生一条数据)

def countdown(n):
    while n > 0:
        yield n        # ← 不是return！暂停在这里
        n -= 1

for num in countdown(5):
    print(num)      # 输出: 5, 4, 3, 2, 1

生成器表达式:
  gen = (x**2 for x in range(10))  # 圆括号不是元组，是生成器！

3️⃣ 正则表达式 Regex
━━━━━━━━━━━━━━━━
import re

pattern = re.compile(r"正则表达式")  # 预编译(多次使用时更高效)

主要方法:
  pattern.match(text)    # 从开头匹配
  pattern.search(text)   # 从任意位置搜索第一个
  pattern.findall(text)  # 找到所有匹配项(返回列表)
  pattern.sub(repl,text) # 替换所有匹配项

常用正则语法:
  \d  数字 [0-9]          \w  单词字符 [a-zA-Z0-9_]
  \s  空白 [ \t\n\r]      .   任意字符(换行除外)
  ^   行开头              $   行结尾
  *   0次或多次           +   1次或多次
  ?   0次或1次            {n} 恰好n次
  [...] 字符集           [^..] 排除字符集
  (...) 捕获组           (?:..)非捕获组

4️⃣ *args 和 **kwargs
━━━━━━━━━━━━━━━━
*args:      收集所有多余的位置参数 → 元组
**kwargs:   收集所有多余的关键字参数 → 字典

def show_args(*args, **kwargs):
    print(f"位置参数: {args}")      # 元组
    print(f"关键字参数: {kwargs}")  # 字典

show_args(1, 2, 3, name="张三", age=18)
# 输出: 位置参数: (1, 2, 3)
#       关键字参数: {'name': '张三', 'age': 18}

用途: 编写通用包装函数(如装饰器的wrapper)
"""


# ====== 实战演示: 装饰器 ======

def log_execution(func):
    """
    📌 [知识点: 基础装饰器] 日志记录装饰器
    
    三要素:
      1. 接收函数 func
      2. 定义内部函数 wrapper
      3. 返回 wrapper 替代原函数
    """
    @functools.wraps(func)  # 📌 [关键!] 保留原函数名称和文档字符串
    def wrapper(*args, **kwargs):
        # 📌 [*args, **kwargs] 通用包装: 接收任意参数
        args_str = ", ".join(repr(a) for a in args[:3])
        print(f"[LOG] 调用 {func.__name__}({args_str})...")
        
        start = time.time()
        result = func(*args, **kwargs)  # 调用被装饰的原函数
        elapsed = time.time() - start
        
        print(f"[LOG] {func.__name__}() 完成 ({elapsed:.4f}s)")
        return result  # 📌 必须返回结果！否则调用者拿不到返回值
    
    return wrapper


def timer(show_args: bool = True, precision: int = 4):
    """
    📌 [知识点: 带参数装饰器] 性能计时器
    
    注意三层嵌套结构:
      第1层 timer(precision=...) → 返回 decorator
      第2层 decorator(func)         → 返回 wrapper  
      第3层 wrapper(*args, **kwargs)  → 执行逻辑
    
    @timer(precision=6) 实际执行的是: timer(precision=6)(your_function)
    """
    def decorator(func):  # 第2层
        @functools.wraps(func)
        def wrapper(*args, **kwargs):  # 第3层
            start = time.perf_counter()
            result = func(*args, **kwargs)
            elapsed = time.perf_counter() - start
            
            # 📌 f-string格式化: {value:.Nf} 保留N位小数
            print(f"[TIMER] {func.__name__}: {elapsed:.{precision}f}s")
            return result
        return wrapper
    return decorator  # 第1层返回第2层


def validate_input(**validators):
    """
    📌 [知识点: 动态参数装饰器] 输入验证装饰器
    
    **validators 收集关键字参数为字典:
      @validate_input(name=lambda v: len(v)>0, age=lambda v: v>0)
      → validators = {"name": <function>, "age": <function>}
    """
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # 📌 inspect.signature 获取函数签名，将位置参数映射到参数名
            import inspect
            sig = inspect.signature(func)
            bound = sig.bind(*args, **kwargs)
            bound.apply_defaults()
            
            errors = []
            for param_name, validator_fn in validators.items():
                if param_name in bound.arguments:
                    value = bound.arguments[param_name]
                    # 验证函数返回 (bool, str) 或 bool
                    result = validator_fn(value)
                    if isinstance(result, tuple):
                        is_valid, msg = result
                    else:
                        is_valid, msg = result, ""
                    
                    if not is_valid:
                        errors.append(f"  {param_name}: {msg}")
            
            if errors:
                raise ValueError("验证失败:\n" + "\n".join(errors))
            
            return func(*args, **kwargs)
        return wrapper
    return decorator


# ====== 实战演示: 生成器 ======

def ranking_generator(students, limit=5):
    """
    📌 [知识点: yield 生成器]
    
    与普通函数的区别:
      - 普通: return 后函数结束，一次性返回所有数据
      - 生成器: yield 后函数暂停，下次调用继续
    
    内存优势:
      - 如果有100万条数据，列表版本需要全部存入内存
      - 生成器版本每次只在内存中保持1条数据
    """
    ranked = sorted(
        [s for s in students if s.scores],
        key=lambda s: s.average_score,
        reverse=True
    )[:limit]
    
    for rank, student in enumerate(ranked, 1):
        yield rank, student  # 📌 yield 不是return! 这里暂停


def failing_student_generator(students):
    """📌 [知识点: 生成器过滤不及格学生"""
    for student in students:
        if student.average_score < 60:
            yield student  # 只yield满足条件的


# ====== 实战演示: 迭代器协议 ======

class StudentCollection:
    """
    📌 [知识点: 迭代器协议] 让自定义对象支持for循环
    
    协议要求两个方法:
      __iter__() → 返回迭代器对象(通常返回self)
      __next__() → 返回下一个值，没有则抛出StopIteration
    """
    
    def __init__(self, students):
        self._students = students
        self._index = 0
    
    def __iter__(self):
        """迭代器必须返回自身"""
        self._index = 0  # 重置索引
        return self
    
    def __next__(self):
        """返回下一个学生"""
        if self._index >= len(self._students):
            raise StopIteration  # 📌 必须！否则for循环不会停止
        
        student = self._students[self._index]
        self._index += 1
        return student


# ====== 实战演示: 正则表达式 ======

def demo_regex():
    """📌 [知识点: 正则表达式 实战示例]"""
    
    print("\n" + "=" * 60)
    print("Part 3: 正则表达式实战演示")
    print("=" * 60)
    
    # 预编译正则(性能更好)
    student_id_pattern = re.compile(r"^2026\d{4}$")   # 学号: 2026 + 4位数字
    phone_pattern = re.compile(r"^1[3-9]\d{9}$")      # 手机号: 1 + 3-9 + 9位数字
    email_pattern = re.compile(r"^[\w.-]+@[\w.-]+\.\w+$")  # 邮箱
    
    test_cases = [
        ("20260001", "学号", student_id_pattern),
        ("13812345678", "手机号", phone_pattern),
        ("test@example.com", "邮箱", email_pattern),
        ("abc", "无效学号", student_id_pattern),
        ("12345", "无效手机号", phone_pattern),
    ]
    
    print("\n--- 格式验证 ---")
    for text, desc, pattern in test_cases:
        match = pattern.match(text)
        status = "✅ 通过" if match else "❌ 不通过"
        print(f"  {text:<20} ({desc}): {status}")
    
    # findall 提取所有数字
    print("\n--- 文本提取 ---")
    text = "张三: Python=95, 数学=88, 英语=92; 总分275, 均分91.67"
    numbers = re.findall(r"-?\d+\.?\d*", text)  # 提取所有数字(包括负数和小数)
    print(f"  原文: {text}")
    print(f"  提取的数字: {numbers}")
    
    # sub 替换
    phone_text = "我的手机号是 13812345678，备用 15987654321"
    masked = re.sub(r"(1)(\d{2})(\d{4})(\d{4})", r"\1\2****\4", phone_text)
    print(f"\n  脱敏前: {phone_text}")
    print(f"  脱敏后: {masked}")


# =====================================================================
#                    Part 4: 综合实战 - CLI交互系统
# =====================================================================

"""
【综合实战】命令行交互系统的设计要点

1. 主循环: while running: → 显示菜单 → 获取输入 → 分发处理
2. 命令分发: 用字典映射替代大量 if/elif (更易维护)
3. 输入验证: 每个输入都要验证，给用户友好的错误提示
4. 异常捕获: 所有可能出错的地方都要try/except
5. 优雅退出: Ctrl+C 中断处理、未保存数据提示
"""


class GradeManager:
    """
    学生成绩管理器 - 业务逻辑核心
    
    📌 [知识点综合运用]:
      - 列表/字典 存储数据
      - 推导式 过滤和搜索
      - sorted + lambda 排序
      - 生成器 惰性遍历
      - 异常处理 分层设计
    """
    
    def __init__(self):
        self._students: list = []
        self._modified = False
    
    @property
    def count(self) -> int:
        return len(self._students)
    
    # ========== CRUD操作 ==========
    
    def add_student(self, sid, name, gender, **scores):
        """添加学生(含验证和去重检查)"""
        
        # 📌 [知识点: any() + 生成器表达式] 高效检查是否存在
        if any(s.student_id == sid for s in self._students):
            raise DuplicateStudentError(sid)
        
        # 📌 [知识点: **scores 解包字典为关键字参数]
        student = Student(sid, name, gender, scores=scores)
        self._students.append(student)
        self._modified = True
        return student
    
    def remove_student(self, sid):
        """删除学生"""
        for i, s in enumerate(self._students):  # 📌 enumerate 同时获取索引和值
            if s.student_id == sid:
                removed = self._students.pop(i)
                self._modified = True
                return removed
        raise ValueError(f"学号 {sid} 不存在")
    
    def find_by_id(self, sid):
        """按学号查找"""
        # 📌 [知识点: next() + 生成器] 短路查找(找到即停)
        return next((s for s in self._students if s.student_id == sid), None)
    
    def search(self, keyword):
        """模糊搜索"""
        keyword = keyword.lower().strip()
        results = set()
        
        # 📌 [知识点: 列表推导式过滤]
        results.update(
            s for s in self._students 
            if keyword in s.name.lower() or keyword == s.student_id
        )
        return list(results)
    
    # ========== 统计与分析 ==========
    
    def get_statistics(self) -> dict:
        """统计全体数据"""
        active = [s for s in self._students if s.scores]
        if not active:
            return {"total": self.count, "active": 0}
        
        # 各科统计
        subjects = ["Python", "数学", "英语"]
        subject_stats = {}
        for subj in subjects:
            scores = [s.get_score(subj) for s in active if subj in s]
            if scores:
                subject_stats[subj] = {
                    "avg": round(sum(scores)/len(scores), 2),
                    "max": max(scores),
                    "min": min(scores),
                }
        
        # 📌 [知识点: dict.get() + 计数模式]
        grade_dist = {}
        for s in active:
            level = "A" if s.average_score >= 90 else \
                   "B" if s.average_score >= 80 else \
                   "C" if s.average_score >= 70 else \
                   "D" if s.average_score >= 60 else "F"
            grade_dist[level] = grade_dist.get(level, 0) + 1
        
        return {
            "total": self.count,
            "active": len(active),
            "overall_avg": round(sum(s.average_score for s in active)/len(active), 2),
            "subjects": subject_stats,
            "grades": grade_dist,
        }
    
    def get_ranking(self, by="average", reverse=True):
        """
        📌 [知识点: sorted + lambda 排序]
        lambda 创建匿名函数作为排序key
        """
        from operator import attrgetter
        
        key_map = {
            "average": attrgetter("average_score"),
            "total": attrgetter("total_score"),
        }
        
        sort_key = key_map.get(by, lambda s: getattr(s, 'get_score')(by, 0))
        
        return sorted(
            [s for s in self._students if s.scores],
            key=sort_key,
            reverse=reverse
        )
    
    # ========== 文件持久化 ==========
    
    def save_to_file(self, filepath):
        """保存到JSON文件"""
        data = [s.to_dict() for s in self._students]
        with open(filepath, "w", encoding="utf-8") as f:  # 📌 [知识点: with语句自动关闭]
            json.dump(data, f, ensure_ascii=False, indent=2)
        self._modified = False
        print(f"已保存 {len(data)} 条记录到 {filepath}")
    
    def load_from_file(self, filepath):
        """从JSON文件加载"""
        if not os.path.exists(filepath):
            print(f"文件不存在: {filepath}")
            return
        
        with open(filepath, "r", encoding="utf-8") as f:
            data = json.load(f)
        
        self._students = [Student.from_dict(d) for d in data]
        print(f"已加载 {len(self._students)} 条记录")


# ====== 主程序入口 ======

def main():
    """主程序 - 综合展示所有知识点"""
    
    print("╔" + "═"*58 + "╗")
    print("║" + "  🎓 智能学生成绩管理系统 - 讲解版 (带完整知识注释)".center(58) + "║")
    print("╚" + "═"*58 + "╝")
    
    # 创建管理器
    manager = GradeManager()
    
    # 添加示例数据 (直接创建Student对象添加到内部列表)
    print("\n>>> 添加学生数据...")
    demo_students = [
        Student("20260001", "张三", "M", {"Python": 95, "数学": 88, "英语": 92}),
        Student("20260002", "李四", "F", {"Python": 82, "数学": 95, "英语": 78}),
        Student("20260003", "王五", "M", {"Python": 55, "数学": 48, "英语": 52}),
        Student("20260004", "赵六", "F", {"Python": 91, "数学": 97, "英语": 94}),
        Student("20260005", "孙七", "M", {"Python": 88, "数学": 76, "英语": 81}),
    ]
    for s in demo_students:
        manager._students.append(s)
    
    # 演示基础语法
    demo_basic_syntax()
    
    # 演示OOP
    print("\n" + "=" * 60)
    print("Part 2: 面向对象实战演示")
    print("=" * 60)
    
    s = manager.find_by_id("20260001")
    print(f"\n>>> __str__ 魔术方法:")
    print(s)                      # 自动调用 __str__
    
    print(f">>> __repr__ 魔术方法:")
    print(repr(s))                # 自动调用 __repr__
    
    print(f"\n>>> 比较 (__eq__, __lt__):")
    s2 = manager.find_by_id("20260002")
    print(f"s == s2? {s == s2}")   # __eq__
    print(f"s < s2?  {s < s2}")    # __lt__
    
    print(f"\n>>> 成员检测 (__contains__):")
    print(f"'Python' in s? {'Python' in s}")  # __contains__
    
    print(f"\n>>> 布尔转换 (__bool__):")
    print(f"if s: {bool(s)}")
    
    # 演示排序(利用__lt__)
    print("\n>>> 利用 __lt__ 进行排序:")
    ranked = manager.get_ranking()
    for rank, stu in enumerate(ranked, 1):
        medal = "🥇" if rank==1 else "🥈" if rank==2 else "🥉" if rank==3 else "  "
        print(f"  {medal}{rank}. {stu.name}: 均分{stu.average_score:.1f}")
    
    # 演示高级特性
    demo_regex()
    
    print("\n" + "=" * 60)
    print("Part 3: 装饰器和生成器演示")
    print("=" * 60)
    
    # 装饰器效果
    print("\n>>> @log_execution 装饰器效果:")
    s_new = Student("20260006", "周八", "F", {"Python": 93, "数学": 89, "英语": 96})
    manager._students.append(s_new)
    
    # 生成器效果
    print("\n>>> yield 生成器 - 前3名:")
    for rank, student in ranking_generator(manager._students, limit=3):
        print(f"  第{rank}名: {student.name}({student.student_id}) - 均分{student.average_score:.1f}")
    
    # 迭代器效果
    print("\n>>> 迭代器协议 - 遍历所有学生:")
    collection = StudentCollection(manager._students[:3])
    for student in collection:  # 📌 for循环自动调用__iter__和__next__
        print(f"  → {student.name}")
    
    # 统计信息
    print("\n" + "=" * 60)
    print("Part 4: 统计分析")
    print("=" * 60)
    
    stats = manager.get_statistics()
    print(f"\n总人数: {stats['total']}, 有效记录: {stats['active']}")
    print(f"总体均分: {stats['overall_avg']}")
    
    if stats.get("subjects"):
        print("\n各科情况:")
        for subj, info in stats["subjects"].items():
            bar = "█" * int(info["avg"] / 5) + "░" * (20 - int(info["avg"] / 5))
            print(f"  {subj}: 均分{info['avg']:.1f} | 最高{info['max']:.0f} | 最低{info['min']:.0f}  {bar}")
    
    if stats.get("grades"):
        print("\n等级分布:")
        for grade, count in sorted(stats["grades"].items()):
            pct = count / stats["active"] * 100
            print(f"  {grade}: {count}人 ({pct:.0f}%)")
    
    print("\n" + "=" * 60)
    print("✅ 讲解版演示完成！建议接下来阅读正常版的源代码")
    print("   并尝试自己动手修改/添加功能")
    print("=" * 60)


if __name__ == "__main__":
    # 📌 [知识点: if __name__ == "__main__"]
    # 确保只有直接运行此文件时才执行main()
    # 导入为模块时不执行(避免副作用)
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n程序被中断(Ctrl+C)")
    except Exception as e:
        print(f"\n程序出错: {e}")
        import traceback
        traceback.print_exc()
