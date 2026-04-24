# 05 OOP 进阶·高级 ⭐

> **面试高频区域**：深浅拷贝 & GC / 魔法方法大全 / Mixin / 元类 / SOLID 原则 & 设计模式
>
> **难度**: *** | **预计时长**: 70min

---

## 本节知识地图

```
05 OOP 进阶 · 高级 ★面试高频
├── 5.1 深浅拷贝 (copy vs deepcopy)
├── 5.2 == 与 is 的区别
├── 5.3 垃圾回收机制 (GC)
├── 5.4 魔法方法大全 (__str__/__repr__/__eq__/__hash__/__call__/...)
├── 5.5 __call__ 让对象可调用
├── 5.6 上下文管理器 (__enter__/__exit__)
├── 5.7 Mixin 模式 (多重继承组合)
├── 5.8 元类 Metaclass (类的工厂)
├── 5.9 SOLID 设计原则
└── 5.10 经典设计模式 (工厂/策略/观察者/单例)
```

---

## 5.1 深浅拷贝

### 核心区别

| | **浅拷贝** `copy()` / `.copy()` / `[:]` | **深拷贝** `deepcopy()` |
|--|--|--|
| **复制深度** | 只复制**一层**（外层独立，内层共享）| 递归复制**所有层级**（完全独立） |
| **内存开销** | 小（内层对象共享引用）| 大（所有层级都创建新副本）|
| **性能** | 快 | 慢 |
| **适用场景** | 不修改内层可变对象时 | 需要**完全独立的副本**时 |

### 浅拷贝演示 —— 内层共享的坑

```python
import copy

# === 浅拷贝: 只复制外层，内层对象仍然共享 ===
a = [[1, 2], [3, 4]]
b = a.copy()          # 等价于 copy.copy(a) 或 a[:]

# ✅ 修改外层: b 不受影响
a.append([5])
print('a:', a)   # [[1, 2], [3, 4], [5]]
print('b:', b)   # [[1, 2], [3, 4]]   ← 外层独立 ✓

# ❌ 修改内层: b 会跟着变化!
a[0].append(999)
print('修改内层后:')
print('a:', a)   # [[1, 2, 999], [3, 4], [5]]
print('b:', b)   # [[1, 2, 999], [3, 4]]   ← 内层共享! ✗
```

### 深拷贝演示 —— 完全独立

```python
c = [[1, 2], [3, 4]]
d = copy.deepcopy(c)

c[0].append(888)
c.append([99])

print('c:', c)   # [[1, 2, 888], [3, 4], [99]]
print('d:', d)   # [[1, 2], [3, 4]]    ← 完全不受影响! ✓
```

### 图解对比

```
浅拷贝 copy():
  a → [list_0, list_1]
       ↓        ↓
  b → list_0  list_1      ← 内层是同一对象!

深拷贝 deepcopy():
  c → [list_0, list_1]
       ↓        ↓
  d → new_0   new_1        ← 内层也是独立的新对象!
```

> 📌 **口诀**：**浅拷只抄皮，深拷连骨头一起复制**

---

## 5.2 `==` 与 `is` 的区别 ⚠️ 面试常考

```python
x = [1, 2, 3]
y = [1, 2, 3]
z = x

print(x == y)   # True   — 值相等（内容一样）
print(x is y)   # False  — 不是同一个对象（内存地址不同）
print(x is z)   # True   — z 就是 x 的别名（同一内存地址）
```

| 运算符 | 含义 | 比较什么 |
|--------|------|---------|
| `==` | 值相等 | 对象的**内容/值**是否相同 |
| `is` | 身份相同 | 是否是**同一个对象**（内存地址） |

### 小整数缓存机制（CPython 特性）

```python
a = 256; b = 256
print(a is b)   # True  ← Python 缓存了 -5 ~ 256 的小整数

c = 257; d = 257
print(c is d)   # False ← 超出缓存范围，创建了两个不同对象!

# 字符串也有类似行为（intern 机制）
s1 = "hello"; s2 = "hello"
print(s1 is s2)  # True  ← 相同字符串常量可能被复用
```

> 📌 **面试要点**：永远用 `==` 判断值是否相等，`is` 只用于判断 `None`（即 `if x is None:`）。

---

## 5.3 垃圾回收机制 (GC)

### 引用计数 + 分代回收

```python
import sys
import gc

obj = {'key': 'value'}

# 查看引用计数 (getrefcount 自身会+1)
print(f'refcount: {sys.getrefcount(obj)}')  # 通常为 2 (自身引用 + obj变量)

# 手动触发垃圾回收
collected = gc.collect()
print(f'gc collected: {collected} objects')

# 查看不可达垃圾对象
print(f'garbage: {len(gc.garbage)}')
```

### GC 工作原理简述

```
Python GC 采用两种机制:

1. 引用计数 (Reference Counting) — 主要方式
   - 每个对象记录有多少地方在引用它
   - 引用数归零 → 立即回收
   - 优点: 实时性好; 缺点: 无法处理循环引用

2. 分代回收 (Generational Collection) — 补救方式  
   - 定期扫描，处理循环引用
   - 新对象(第0代) → 存活久(第1代) → 更久(第2代)
   - 越老的对象越少检查（假设"活得久的不会轻易死"）
```

---

## 5.4 魔法方法大全

> 魔法方法（Dunder Method）让自定义类像内置类型一样工作！

### 核心魔法方法速查表

| 方法 | 触发时机 | 示例场景 |
|------|---------|---------|
| `__init__(self)` | 创建实例后初始化 | `obj = MyClass()` |
| `__new__(cls)` | 创建实例之前（控制创建过程）| 单例模式 |
| `__str__(self)` | `str(obj)` / `print(obj)` | 用户友好的显示 |
| `__repr__(self)` | `repr(obj)` / 交互式终端 | 开发者调试用 |
| `__eq__(self, other)` | `obj1 == obj2` | 自定义相等判断 |
| `__lt__(self, other)` | `obj1 < obj2` | 排序比较 |
| `__len__(self)` | `len(obj)` | 自定义长度 |
| `__getitem__(self, key)` | `obj[key]` | 索引访问 |
| `__setitem__(self, key, val)` | `obj[key] = val` | 索引赋值 |
| `__iter__(self)` | `iter(obj)` | 迭代协议 |
| `__next__(self)` | `next(it)` | 迭代器下一项 |
| `__call__(self, *args)` | `obj(*args)` | 对象可调用 |
| `__enter__` / `__exit__` | `with obj as ...` | 上下文管理器 |

### 实战示例：Student 类

```python
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        """给用户看的字符串"""
        return f'Student({self.name}, {self.age}岁)'

    def __repr__(self):
        """给开发者看的字符串（调试用）"""
        return f'<Student name={self.name!r} age={self.age}>'

    def __eq__(self, other):
        """自定义 == 比较"""
        if not isinstance(other, Student):
            return NotImplemented
        return self.name == other.name and self.age == other.age


s1 = Student('Alice', 20)
s2 = Student('Alice', 20)
s3 = Student('Bob', 21)

print(s1)                # Student(Alice, 20岁)     ← __str__
print(repr(s1))         # <Student name='Alice' age=20>  ← __repr__
print(s1 == s2)         # True                      ← __eq__
print(s1 == s3)         # False                     ← __eq__
```

### 记忆口诀

> **`__str__` 给人看，`__repr__` 给机器看；`__eq__` 定相等，`__lt__` 排大小。**

---

## 5.5 `__call__` —— 让对象可以像函数一样调用

```python
class Accumulator:
    """累加器 — 可调用的类"""

    def __init__(self, start=0):
        self.total = start

    def __call__(self, value):
        """让对象能被直接调用: acc(value)"""
        self.total += value
        print(f'累计: {self.total}')
        return self.total


acc = Accumulator(100)  # 初始值为 100
acc(10)   # 累计: 110
acc(20)   # 累计: 130
acc(-30)  # 累计: 100
print(acc.total)  # 100
```

> 📌 **应用场景**：装饰器类（03节已讲）、状态机、回调函数封装等。

---

## 5.6 上下文管理器 (`__enter__` / `__exit__`)

```python
class Timer:
    """计时上下文管理器 — 配合 with 使用"""
    
    def __init__(self, label=''):
        self.label = label

    def __enter__(self):
        """进入 with 块时自动调用"""
        import time
        self.start = time.time()
        return self  # 返回值会绑定到 as 变量

    def __exit__(self, exc_type, exc_val, exc_tb):
        """退出 with 块时自动调用（即使发生异常也会执行）"""
        import time
        elapsed = time.time() - self.start
        prefix = f'[{self.label}] ' if self.label else ''
        print(f'{prefix}耗时: {elapsed:.4f}s')
        return False  # 不吞掉异常（True 则抑制异常）


with Timer('排序测试') as t:
    data = [random.randint(1, 1000) for _ in range(10000)]
    data.sort()
# 输出: [排序测试] 耗时: 0.xxs
```

> 📌 **核心价值**：`with` 保证资源一定会被释放（文件关闭、锁释放、连接归还），即使发生异常。

---

## 5.7 Mixin 模式（多继承组合）

> Mixin = 为多个类"混入"通用能力，避免钻石继承问题。

### 命名规范

```python
# Mixin 类命名以 Mixin 结尾
class JsonMixin:           # ✅ 正确
class Serialize:           # ❌ 不够明确

# Mixin 类通常不单独实例化
# 放在继承链的最左侧（Python MRO 从左到右）
```

### 实战：为任意类添加 JSON 序列化能力

```python
import json

class JsonMixin:
    """为任何类添加 to_json 能力的 Mixin"""

    def to_dict(self):
        """将实例属性转为字典（过滤掉私有属性）"""
        return {k: v for k, v in vars(self).items()
                if not k.startswith('_')}

    def to_json(self, indent=None):
        """序列化为 JSON 字符串"""
        return json.dumps(
            self.to_dict(),
            indent=indent,
            default=str,
            ensure_ascii=False
        )


# 使用: 只需继承 JsonMixin
class Person(JsonMixin):
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Book(JsonMixin):
    def __init__(self, title, author):
        self.title = title
        self.author = author


p = Person('张三', 25)
b = Book('Python入门', '作者A')

print(p.to_json(indent=2))
# {
#   "name": "张三",
#   "age": 25
# }

print(b.to_json())
# {"title": "Python入门", "author": "作者A"}
```

> 📌 **Mixin 的精髓**：不改变原有类结构，只是"混入"额外的能力。比多重继承更安全、更清晰。

---

## 5.8 元类 Metaclass

> **元类 = 创建类的类**。普通类创建实例，元类创建类本身。

### 三行理解

```
Metaclass (元类) --创建--> Class (类) --创建--> Instance (实例)
  "类的工厂"              "对象的模具"          "最终产品"
type / SingletonMeta      President             obj = President()
```

### 方式一：用 `type()` 动态创建类

```python
Dog = type('Dog', (), {
    'species': 'Canis familiaris',
    'bark': lambda self: 'Woof!'
})

d = Dog()
print(d.bark())          # Woof!
print(type(Dog))         # <class 'type'> ← Dog 的"类型"是 type
print(type(type))        # <class 'type'> ← type 自己的类型也是 type
```

### 方式二：自定义元类 —— 自动校验子类实现

```python
class ValidateMeta(type):
    """
    元类: 在类创建时自动检查是否缺少必要方法
    """
    REQUIRED_METHODS = ('validate', 'save')

    def __new__(mcs, name, bases, namespace):
        cls = super().__new__(mcs, name, bases, namespace)
        
        # 只对具体子类进行检查（跳过基类 BaseModel）
        if any(isinstance(b, mcs) for b in bases):
            for method in mcs.REQUIRED_METHODS:
                if method not in namespace:
                    raise TypeError(
                        f'{name} must implement {method}() method'
                    )
        return cls


class BaseModel(metaclass=ValidateMeta):
    """抽象基类 — 子类必须实现 validate() 和 save()"""
    pass


# ✅ 正确实现
class User(BaseModel):
    def validate(self): pass
    def save(): pass

u = User()
print('User 创建成功!')

# ❌ 错误演示（取消注释会报错）
# class BadModel(BaseModel):
#     def save(self): pass
#     # 忘记实现 validate → TypeError!
```

> 📌 **使用建议**：99% 的场景不需要自定义元类。**类装饰器**或 `__init_subclass__`（Python 3.6+）通常是更好的选择。

---

## 5.9 SOLID 设计原则

### 五大原则速记

| 原则 | 全称 | 一句话理解 |
|------|------|-----------|
| **S** | Single Responsibility | 单一职责 — 一个类只做一件事 |
| **O** | Open/Closed | 开闭原则 — 对扩展开放，对修改关闭 |
| **L** | Liskov Substitution | 里氏替换 — 子类能完美替代父类 |
| **I** | Interface Segregation | 接口隔离 — 接口要小而精 |
| **D** | Dependency Inversion | 依赖倒置 — 依赖抽象，不依赖具体 |

---

## 5.10 经典设计模式

### 工厂模式

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self): pass

class Circle(Shape):
    def __init__(self, r): self.r = r
    def area(self): return 3.14 * self.r ** 2

class Rectangle(Shape):
    def __init__(self, w, h): self.w, self.h = w, h
    def area(self): return self.w * self.h


def create_shape(shape_type, **kwargs):
    """简单工厂 — 根据类型参数创建对应对象"""
    shapes = {'circle': Circle, 'rectangle': Rectangle}
    cls = shapes.get(shape_type.lower())
    if not cls:
        raise ValueError(f'Unknown shape: {shape_type}')
    return cls(**kwargs)


shapes_list = [
    create_shape('circle', r=5),
    create_shape('rectangle', w=3, h=4),
]

for s in shapes_list:
    print(f'{type(s).__name__}: area={s.area()}')
```

### 策略模式

```python
class DiscountStrategy(ABC):
    @abstractmethod
    def calc(self, price): pass

class NoDiscount(DiscountStrategy):
    def calc(self, price): return price

class PercentOff(DiscountStrategy):
    def __init__(self, percent): self.percent = percent
    def calc(self, price): return price * (1 - self.percent / 100)

class ShoppingCart:
    def __init__(self, strategy=None):
        self.items = []
        self.discount = strategy or NoDiscount()

    def add_item(self, item, price):
        self.items.append((item, price))

    def total(self):
        subtotal = sum(p for _, p in self.items)
        return self.discount.calc(subtotal)


cart = ShoppingCart(PercentOff(20))  # 8折
cart.add_item('book', 50)
cart.add_item('pen', 10)
print(f'折后总价: {cart.total()}')  # 48.0
```

### 观察者模式

```python
class Subject:
    """被观察者"""
    def __init__(self):
        self._observers = []

    def attach(self, observer):
        self._observers.append(observer)

    def notify(self, message):
        for obs in self._observers:
            obs.update(message)


class LoggerObserver:
    def update(self, message):
        print(f'[LOG] {message}')


class EmailObserver:
    def update(self, message):
        print(f'[EMAIL] 发送通知: {message}')


server = Subject()
server.attach(LoggerObserver())
server.attach(EmailObserver())
server.notify('服务器启动完成')
# [LOG] 服务器启动完成
# [EMAIL] 发送通知: 服务器启动完成
```

---

## 易错踩坑速查

| 坑 | 正确做法 |
|---|---------|
| `copy()` 不是完全独立的副本 | 修改嵌套的可变对象会影响原对象 |
| `-5~256` 整数有缓存导致 `is` 返回 True | 不要依赖 `is` 比较数值 |
| `__str__` 没有 fallback 到 `__repr__` | 两个都写才完整 |
| 元类过度使用 | 99% 场景用类装饰器就够了 |
| 多重继承的菱形问题 | 用 C3/MRO 解决，优先考虑 Mixin |

---

## 快速自测

1. `copy.copy()` 和 `copy.deepcopy()` 的核心区别？
2. `__str__` 和 `__repr__` 分别什么时候被调用？
3. 什么是元类？它和普通类的关系？
4. SOLID 中 S 和 O 分别代表什么？
5. 为什么 Mixin 要放在继承链的左侧？
6. `__enter__` / `__exit__` 的核心价值是什么？

---

> 📖 下一节 → [06-迭代器与生成器](./06-迭代器与生成器.md)：⭐ **惰性计算思维**
