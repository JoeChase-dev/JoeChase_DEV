# 04 OOP 进阶·基础

> **OOP 基本功**：抽象基类 ABC / Enum / @property / 实例化 / `__main__` / 类关系
>
> **难度**: ** | **预计时长**: 40min

---

## 本节知识地图

```
04 OOP 进阶 · 基础
├── 4.1 抽象基类 ABC (Abstract Base Class)
├── 4.2 为什么需要抽象类
├── 4.3 枚举类型 Enum
├── 4.4 @property 属性装饰器
├── 4.5 __main__ 程序入口保护
├── 4.6 类与类之间的关系 (is-a/has-a/use-a)
└── 4.7 综合实战: 工资结算系统 + 扑克游戏
```

---

## 4.1 抽象基类 ABC (Abstract Base Class)

### 核心概念

> **抽象基类 = 不能实例化的"模板类"，强制子类实现某些方法**

```python
from abc import ABCMeta, abstractmethod

class Employee(metaclass=ABCMeta):
    """
    员工抽象类
    
    metaclass=ABCMeta → 声明这是抽象类，不能直接 Employee("xxx") 实例化
    @abstractmethod     → 标记"抽象方法"，子类必须实现，否则报错
    """

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def get_salary(self):
        """结算月薪（抽象方法 — 子类必须实现）"""
        pass


# 子类1: 部门经理（固定月薪）
class Manager(Employee):
    def get_salary(self):
        return 15000.0


# 子类2: 程序员（按工时计算）
class Programmer(Employee):
    def __init__(self, name, working_hour=0):
        self.working_hour = working_hour
        super().__init__(name)  # 调用父类的 __init__

    def get_salary(self):
        return 200.0 * self.working_hour


# 子类3: 销售员（底薪 + 提成）
class Salesman(Employee):
    def __init__(self, name, sales=0.0):
        self.sales = sales
        super().__init__(name)

    def get_salary(self):
        return 1800.0 + self.sales * 0.05


# 使用
emps = [
    Manager('曹操'),
    Programmer('荀彧', 120),
    Programmer('郭嘉', 85),
    Salesman('典韦', 123000),
]

for emp in emps:
    print(f'{emp.name}: {emp.get_salary():.2f}元')
# 曹操: 15000.00元
# 荀彧: 24000.00元
# 郭嘉: 17000.00元
# 典韦: 7950.00元
```

### 关键语法说明

| 语法 | 含义 |
|------|------|
| `metaclass=ABCMeta` | 元类声明，表示这是一个**抽象类**，不能直接实例化 |
| `@abstractmethod` | 装饰器标记，声明**抽象方法**，子类必须实现 |
| `super().__init__(...)` | 调用父类的构造方法，初始化继承来的属性 |

> ⚠️ 如果子类忘记实现抽象方法：
> ```python
> class BadEmployee(Employee):
> >     pass  # 忘记实现 get_salary()
>
> emp = BadEmployee('test')
> # TypeError: Can't instantiate abstract class BadEmployee 
> # with abstract method get_salary
> ```

---

## 4.2 为什么需要抽象类？

### 场景分析

想象你在设计一个框架：

```
你定义了一个"通用规则/模板" → 但具体实现由各子类自己决定

Employee 是抽象类 → 不能直接 Employee("张三") 创建对象 ✗
所有子类必须实现 get_salary() → 否则报错 ✓
这样保证了代码的规范性和一致性 ✓
```

### 一句话总结

> **抽象类 = 接口契约**。它告诉所有子类："你必须实现这些方法，否则别想运行！"

---

## 4.3 枚举类型 Enum

> **符号常量 > 字面常量 > 枚举 Enum（最佳实践）**

### 对比三种方式

```python
# ❌ 字面常量：含义模糊
if status == 0: ...
if status == 1: ...

# ✅ 符号常量：语义清晰
STATUS_OK = 1
STATUS_ERROR = 0
if status == STATUS_OK: ...

# ⭐⭐⭐ 枚举：带类型约束 + 防重复 + 自带属性
from enum import Enum, unique

@unique  # 禁止枚举值重复
class Suite(Enum):
    """扑克牌花色"""
    SPADE = 0   # 黑桃
    HEART = 1   # 红心
    CLUB = 2    # 梅花
    DIAMOND = 3 # 方块
    
    def __lt__(self, other):
        return self.value < other.value  # 支持比较排序
```

### 枚举成员的属性

```python
s = Suite.SPADE
print(s.name)    # 'SPADE'   ← 成员名称（字符串）
print(s.value)   # 0         ← 成员值（你赋的值）
print(Suite(0))  # Suite.SPADE ← 通过 value 反查枚举
print(Suite['SPADE'])  # Suite.SPADE ← 通过 name 查找
```

> 📌 **记忆口诀**：`.name` 是名字字符串，`.value` 是赋的值。

---

## 4.4 `@property` —— 方法变属性

### 基本用法

```python
class Thing:
    def __init__(self, price, weight):
        self.price = price
        self.weight = weight

    @property
    def value(self):
        """价格重量比（只读属性）"""
        return self.price / self.weight


t = Thing(price=200, weight=20)
print(t.value)      # 10.0 ← 不需要加括号! 像访问普通属性一样

# 如果尝试修改:
# t.value = 5  
# AttributeError: can't set attribute (因为没定义 setter)
```

### 完整版：getter + setter

```python
class Temperature:
    def __init__(self, celsius=0):
        self._celsius = celsius  # 下划线前缀表示"内部属性"

    @property
    def celsius(self):           # getter：读取时自动调用
        return self._celsius

    @celsius.setter               # setter：赋值时自动调用
    def celsius(self, value):
        if value < -273.15:
            raise ValueError('温度不能低于绝对零度!')
        self._celsius = value


temp = Temperature(25)
print(temp.celsius)       # 25 （调用 getter）
temp.celsius = 30          # （调用 setter）
# temp.celsius = -300       # ValueError!
```

> 📌 **核心作用**：`@property` 让调用者**不需要加括号**，同时可以在读取/赋值时加入验证逻辑。对外看起来像属性，内部却是方法的执行。

---

## 4.5 `__main__` 程序入口保护

### 它是什么？

```python
if __name__ == '__main__':
    main()
```

### 本质：一个智能开关

```
┌────────────────────────────────────────────────────┐
│                                                    │
│   直接运行此文件 → 开关 ON  → 执行 main()          │
│   python my_module.py                              │
│                                                    │
│   被其他文件导入 → 开关 OFF → 跳过，只提供定义      │
│   import my_module                                 │
│                                                    │
│   目的:                                           │
│   ✓ 让同一文件既能运行也能被导入                    │
│   ✓ 避免"导入时就触发副作用"(弹窗/等待输入等)       │
│   ✓ Python 社区的标准惯例 (PEP 推荐)              │
│                                                    │
└────────────────────────────────────────────────────┘
```

### 记忆口诀

> **"如果我是主角(`__main__`)，就开始表演(`main()`)"**

---

## 4.6 类与类之间的关系

| 关系类型 | 关键词 | 说明 | 示例 |
|---------|--------|------|------|
| **is-a** (是一个) | 继承 `class B(A)` | B 是 A 的特化 | 经理 is-a 员工 |
| **has-a** (有一个) | 关联/聚合/合成 | B 包含 A 作为组成部分 | 扑克 has-a 牌 |
| **use-a** (使用一个) | 依赖 | B 的方法中使用了 A | 玩家 use-a 扑克 |

### 代码示例

```python
# is-a: 继承关系
class Employee: ...          # 父类
class Manager(Employee): ... # 子类 is-a 父类

# has-a: 组合关系（扑克游戏示例）
class Card: ...              # 牌
class Poker:                 # 一副扑克
    def __init__(self):
        self.cards = [Card(...) for _ in range(52)]  # Poker has-a Card

class Player:                # 玩家
    def __init__(self, name):
        self.cards = []      # Player has-a Card

# use-a: 依赖关系
def shuffle(poker: Poker):   # 函数 use-a Poker 对象
    random.shuffle(poker.cards)
```

---

## 4.7 综合实战：工资结算系统（工厂模式）

```python
from abc import ABCMeta, abstractmethod

class Employee(metaclass=ABCMeta):
    """员工抽象类"""
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def get_salary(self):
        pass


class Manager(Employee):
    def get_salary(self): return 15000.0

class Programmer(Employee):
    def __init__(self, name, working_hour=0):
        self.working_hour = working_hour
        super().__init__(name)
    def get_salary(self): return 200.0 * self.working_hour

class Salesman(Employee):
    def __init__(self, name, sales=0.0):
        self.sales = sales
        super().__init__(name)
    def get_salary(self): return 1800.0 + self.sales * 0.05


class EmployeeFactory:
    """
    员工工厂 — 工厂模式
    通过工厂实现对象使用者和具体类之间的解耦
    """
    
    @staticmethod
    def create(emp_type, *args, **kwargs):
        """根据类型码创建对应的员工对象"""
        all_emp_types = {
            'M': Manager,
            'P': Programmer,
            'S': Salesman,
        }
        cls = all_emp_types.get(emp_type.upper())
        return cls(*args, **kwargs) if cls else None


def main():
    emps = [
        EmployeeFactory.create('M', '曹操'),
        EmployeeFactory.create('P', '荀彧', 120),
        EmployeeFactory.create('P', '郭嘉', 85),
        EmployeeFactory.create('S', '典韦', 123000),
    ]
    for emp in emps:
        print(f'{emp.name}: {emp.get_salary():.2f}元')

if __name__ == '__main__':
    main()
```

### 工厂模式的价值

```
不使用工厂:          使用工厂:
用户需要知道:         用户只需知道:
- Manager 类名        - 类型码 ('M', 'P', 'S')
- Programmer 类名      
- 各自的构造参数       工厂负责: 
                      - 映射类型码到具体类
容易出错:             - 处理参数传递
写错类名? 参数顺序?    用户完全不需要知道具体类名!
```

### 语法点汇总表

| 语法 | 所在位置 | 含义 |
|------|---------|------|
| `class Thing(object)` | 定义类 | 继承自 object（Python 3 可省略） |
| `def __init__(self, ...)` | 类内部 | 构造方法，初始化对象属性 |
| `self.name = name` | `__init__` 内部 | 绑定实例属性 |
| `@property` | 方法上方 | 装饰器，让方法像属性一样调用 |
| `*input_thing()` | 函数调用处 | 解包操作符，元组→多参数 |
| `lambda x: x.value` | key 参数 | 匿名函数，定义排序/筛选依据 |
| `.sort(key=..., reverse=True)` | 列表方法 | 原地排序 |
| `f'{var}'` | 字符串中 | f-string 格式化 |
| `if __name__ == '__main__':` | 文件底部 | 程序入口保护 |

---

## 快速自测

1. `metaclass=ABCMeta` 和 `@abstractmethod` 分别做什么？
2. 为什么推荐用 Enum 代替字面常量？
3. `@property` 的 getter 和 setter 怎么定义？
4. `if __name__ == '__main__'` 的作用？
5. is-a / has-a / use-a 三种关系的区别？各举一例。
6. 工厂模式解决了什么问题？

---

> 📖 下一节 → [05-OOP进阶高级](05-OOP进阶高级.md)：⭐ **面试高频区** —— 深浅拷贝、魔法方法、元类、设计模式
