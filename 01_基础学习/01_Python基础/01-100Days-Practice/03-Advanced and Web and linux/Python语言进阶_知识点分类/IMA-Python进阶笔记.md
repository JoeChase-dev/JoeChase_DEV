# 📘 Python 进阶知识点 — IMA 笔记合集

> **导入说明**：将以下内容按 `---` 分隔线拆分为独立笔记，或整篇导入后按章节使用
>
> **来源**: Python-100-Days 进阶模块（原 01-Python语言进阶.ipynb）
>
> **标签**: #Python #进阶 #学习笔记

---

# 📌 00 总索引 — 知识导航

## 全局知识地图

```
┌─────────────────────────────────────────────────────────────┐
│                    Python 进阶知识体系                        │
│                                                             │
│  ┌──────────┐  ┌──────────┐  ┌──────────────────────┐     │
│  │ 01 常用  │  │ 02 函数  │  │ 03 装饰器 ★重难点    │     │
│  │ 模块语法 │  │ 进阶核心 │  │                      │     │
│  └──────────┘  └──────────┘  └──────────────────────┘     │
│                                                             │
│  ┌──────────┐  ┌──────────────────────┐                    │
│  │04 OOP    │  │05 OOP 高级 ★面试高频  │                    │
│  │基础       │  │                      │                    │
│  └──────────┘  └──────────────────────┘                    │
│                                                             │
│  ┌──────────┐  ┌──────────┐  ┌──────────────────────┐     │
│  │06 迭代器  │  │07 算法   │  │08 并发编程 ★实战      │     │
│  │生成器     │  │入门      │  │                      │     │
│  └──────────┘  └──────────┘  └──────────────────────┘     │
└─────────────────────────────────────────────────────────────┘
```

## 复习路线

### 路线 A：首次系统学习（推荐）

```
01 → 02 → 03 → 04 → 05 → 06 → 07 → 08
```

### 路线 B：考前突击（重点突破）

| 优先级 | 章节 | 说明 |
|:------:|------|------|
| **P0 必掌握** | 03 → 06 → 08 | 重难点集中突破 |
| **P1 高频** | 05 → 02 | 面试高频区 |
| **P2 工具** | 01 → 04 → 07 | 日常编码工具箱 |

## 易错踩坑速查表

| 坑 | 正确做法 |
|---|---------|
| `[None]*3 * 3` 嵌套列表问题 | 用 `[[None]*3 for _ in range(3)]` |
| 迭代器只能用一次 | 需要多次用就转 `list()` |
| 装饰器丢失函数元信息 | 加 `@functools.wraps(func)` |
| 默认参数用可变对象 | 避免 `def f(lst=[])` |
| `==` 和 `is` 混淆 | `==` 比较值，`is` 比较身份(内存地址) |
| 闭包绑定延迟变量 | 用默认参数捕获 `lambda x=x: ...` |
| GIL 导致多线程不并行 | CPU密集型用多进程 |
| Condition 的 wait() | **必须用 while 不用 if**，防止虚假唤醒 |

---

# 📌 01 常用模块 & 语法糖

> ⭐ 难度: ★ | 🕐 预计时长: 30min

## 知识点脑图

```
01 常用模块 & 语法糖
├── 推导式 Comprehension (列表/字典/集合)
├── 嵌套列表的坑 ★易错
├── heapq 堆模块 (Top-K问题)
├── itertools 迭代工具库 (排列/组合/笛卡尔积)
└── collections 集合增强 (namedtuple/deque/Counter/defaultdict)
```

---

## 🔑 核心卡片 1：三种推导式

| 类型 | 语法 | 示例 | 返回类型 |
|------|------|------|---------|
| 列表推导式 | `[expr for x in iterable if cond]` | `[x**2 for x in range(10)]` | `list` |
| 字典推导式 | `{k: v for k, v in dict.items()}` | `{x: x**2 for x in range(5)}` | `dict` |
| 集合推导式 | `{expr for x in iterable}` | `{x % 3 for x in range(10)}` | `set` |

💡 **核心价值**: 声明式编程——描述"我要什么"而非"怎么做到"

---

## ⚠️ 踩坑卡片 1：嵌套列表陷阱

```python
# ❌ 错误 — 乘法只复制引用
a = [[None] * 3] * 3
a[0][0] = 100
# 结果: 三行全部变成 [100, None, None] !!!

# ✅ 正确 — 每次循环创建新列表对象
a = [[None] * 3 for _ in range(3)]
a[0][0] = 100
# 结果: 只有第一行改变 ✓
```

🧠 **记忆口诀**: *嵌套列表用推导，乘法复制是坑路*

---

## 🔑 核心卡片 2：heapq 堆模块

| 函数 | 说明 | 时间复杂度 |
|------|------|-----------|
| `heapq.nlargest(n, iter)` | 取最大的 n 个元素 | O(n log k) |
| `heapq.nsmallest(n, iter)` | 取最小的 n 个元素 | O(n log k) |
| `heapq.heappush(heap, item)` | 入堆 | O(log n) |
| `heapq.heappop(heap)` | 弹出最小值 | O(log n) |
| `heapq.heapify(list)` | 原地转为堆 | O(n) |

```python
import heapq
data = [{'name': 'AAPL', 'price': 543.22}, ...]
# key 参数指定排序依据
heapq.nlargest(2, data, key=lambda x: x['price'])
```

---

## 🔑 核心卡片 3：itertools 四大函数

| 函数 | 功能 | 示例输入 | 输出示例 |
|------|------|---------|---------|
| `permutations(iter, r)` | 全排列（有序） | `'ABC', 2` | AB AC BA BC CA CB (6个) |
| `combinations(iter, r)` | 组合（无序） | `'ABC', 2` | AB AC BC (3个) |
| `product(*iters)` | 笛卡尔积 | `'AB', '12'` | A1 A2 B1 B2 (4个) |
| `cycle(iter)` | 无限循环 | `'ABC'` | A B C A B C ... |

💡 **返回迭代器**(惰性计算)，不占额外内存！

---

## 🔑 核心卡片 4：collections 五大工具

| 类名 | 功能 | 使用场景 |
|------|------|---------|
| `namedtuple` | 命名元组（带字段名的不可变对象） | 替代简单类 |
| `deque` | 双端队列（头尾操作都是 O(1)） | 队列/BFS/滑动窗口 |
| `Counter` | 计数器（统计频率） | 词频/Top-K 问题 |
| `OrderedDict` | 有序字典 | Python 3.7+ dict 已内置 |
| `defaultdict` | 带默认值的字典 | 分组统计/图邻接表 |

### deque vs list 性能对比

| 操作 | list | deque |
|------|:----:|:-----:|
| 尾部 append/pop | O(1) ✅ | O(1) ✅ |
| 头部 insert/popleft | **O(n)** ❌ | **O(1)** ✅ |
| 随机访问 arr[i] | O(1) ✅ | O(n) ❌ |

> 📌 **选型结论**: 频繁头部操作用 deque，尾部+随机访问用 list

---

## ✅ 自测题

1. `[[]]*3` 和 `[[] for _ in range(3)]` 的区别？
2. `permutations` 和 `combinations` 的核心区别？
3. 为什么 deque 在头部操作比 list 快？
4. `Counter.most_common(3)` 返回什么格式？

---

# 📌 02 函数进阶核心

> ⭐ 难度: ★★ | 🕐 预计时长: 45min

## 知识点脑图

```
02 函数进阶核心
├── 函数是一等公民 (赋值/传参/返回值)
├── 高阶函数 map & filter + 替代品(推导式)
├── 参数体系 (位置/*args/关键字/**kwargs)
├── lambda 匿名函数
├── 闭包 Closure ★
├── LEGB 变量查找规则
└── global 与 nonlocal 关键字
```

---

## 🔑 核心卡片 1：一等公民三大特权

```python
# 特权1: 赋值给变量
say_hi = greet

# 特权2: 作为参数传入其他函数
call_twice(func, value)

# 特权3: 作为返回值
def make_multiplier(factor):
    def multiplier(x):
        return x * factor
    return multiplier  # ← 返回函数本身!
double = make_multiplier(2)
double(7)  # 14
```

💡 这就是**闭包的基础**——内部函数记住外层变量

---

## 🔑 核心卡片 2：参数体系五件套

```python
def demo(a, b, *args, key=None, **kwargs):
    """
    a, b     → 位置参数（必填按顺序传）
    *args    → 可变位置参数（收集为元组）
    key      → 关键字参数（有默认值可选）
    **kwargs → 可变关键字参数（收集为字典）
    """
```

### 参数顺序铁律

```
位置参数 → *args → 命名关键字参数 → **kwargs
  必填      收集多余位置   仅关键字      收集多余关键字
```

⚠️ **顺序错了会 SyntaxError!**

---

## 🔑 核心卡片 3：闭包(Closure)

> **闭包 = 内部函数 + 引用的外部变量**
>
> 外部函数执行完毕后，内部函数仍能"记住"外部变量

```python
def make_counter(start=0):
    count = start  # ← 被闭包捕获的外部变量
    def increment(step=1):
        nonlocal count  # ← 声明使用外部变量
        count += step
        return count
    return increment

counter_a = make_counter(0)
print(counter_a())  # 1
print(counter_a())  # 2  ← count 被"记住"了!
```

### 闭包 vs 类 对比

| 维度 | 闭包 | 类 |
|------|------|-----|
| 适用场景 | 逻辑简单、状态少 | 逻辑复杂、多方法 |
| 代码量 | 轻 | 较重 |
| 可读性 | 小场景更清晰 | 大场景更有结构 |

---

## 🔑 核心卡片 4：LEGB 变量查找规则

```
┌─────────────────────────────────────┐
│           L - Local（局部）          │ ← 当前函数内部
│  ┌───────────────────────────────┐  │
│  │     E - Enclosing（嵌套）      │  ← 外层函数（闭包）
│  │   ┌─────────────────────────┐ │  │
│  │   │   G - Global（全局）     │ │  │ ← 当前模块级别
│  │   │ ┌─────────────────────┐ │ │  │
│  │   │ │ B - Built-in（内置）│ │ │  │ ← len/print/int...
│  │   │ └─────────────────────┘ │ │  │
│  │   └─────────────────────────┘ │  │
│  └───────────────────────────────┘  │
└─────────────────────────────────────┘
```

---

## 🔑 核心卡片 5：global vs nonlocal

| 关键字 | 作用范围 | 用途 | 目标必须已存在于？ |
|--------|---------|------|:------------------:|
| `global` | 全局作用域 | 在函数内读写全局变量 | 全局作用域 |
| `nonlocal` | 嵌套作用域 | 在内层函数读写外层变量 | 某个外层函数中 |

```python
# global 示例
total = 0
def add_to_total(value):
    global total  # 操作的是全局的 total!
    total += value

# nonlocal 示例
def outer():
    counter = 0
    def inner():
        nonlocal counter  # 操作的是 outer 的 counter!
        counter += 1
        return counter
```

---

## ✅ 自测题

1. 函数一等公民三大特权是什么？
2. `map(filter(...))` 和列表推导式推荐用哪个？
3. 参数的正确顺序？
4. LEGB 分别代表什么？
5. 不加 nonlocal 直接修改闭包变量会发生什么？

---

# 📌 03 装饰器专题 ★重难点

> ⭐ 难度: ★★★ | 🕐 预计时长: 60min

## 知识点脑图

```
03 装饰器专题 ★重难点
├── @语法糖的本质 (= func = decorator(func))
├── 基础装饰器 (wrapper + *args/**kwargs)
├── functools.wraps 保留元信息
├── 带参数的装饰器（三层嵌套）★★★
├── 类装饰器 (__call__)
├── 实战: 单例模式 (普通版)
└── 线程安全单例 (双重检查锁 DCL)
```

---

## 🔑 核心卡片 1：@语法糖的本质

```python
@simple_decorator          # ↑ 完全等价于 ↓
def say_hi():
    print("Hi!")

# 手动写法:
def say_hi():
    print("Hi!")
say_hi = simple_decorator(say_hi)  # 把函数传入→拿到新函数→赋回去
```

📌 **本质**: *函数接收函数，返回新函数*。@ 只是便捷语法糖。

---

## 🔑 核心卡片 2：基础装饰器模板（背下来！）

```python
from functools import wraps
from time import time

def record_time(func):           # ① 接收被装饰函数
    @wraps(func)                 # ③ 保留原函数元信息
    def wrapper(*args, **kwargs): # ② 通用包装函数
        start = time()
        result = func(*args, **kwargs)  # 执行原函数
        print(f'{func.__name__}: {time()-start:.4f}s')
        return result            # ④ 返回原函数结果
    return wrapper               # ⑤ 返回新函数

@record_time
def add(a, b):
    return a + b
```

⚠️ **三要素**: `*args/**kwargs` 透参、保留返回值、`@wraps` 保元信息

---

## 🔑 核心卡片 3：带参数装饰器的三层嵌套

```python
def repeat(times=3):
    """第一层: 接收装饰器参数 times"""
    def decorator(func):
        """第二层: 接收被装饰函数"""
        @wraps(func)
        def wrapper(*args, **kwargs):
            """第三层: 实际执行的包装"""
            for _ in range(times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(times=5)  # 先执行 repeat(5) → 得到 decorator → 再 @decorator
def greet():
    print("Hello!")
```

🧠 **记忆**: *参数层→函数层→wrapper层*，一层包一层

---

## 🔑 核心卡片 4：单例模式（装饰器实现）

```python
def singleton(cls):
    _instances = {}  # 缓存字典: 类 → 唯一实例
    
    @wraps(cls)
    def get_instance(*args, **kwargs):
        if cls not in _instances:
            _instances[cls] = cls(*args, **kwargs)
        return _instances[cls]
    
    return get_instance

@singleton
class Database:
    pass

db1 = Database()
db2 = Database()
print(db1 is db2)  # True! 同一个对象
```

---

## 🔑 核心卡片 5：线程安全单例（双重检查锁 DCL）

```python
import threading

def thread_safe_singleton(cls):
    _instances = {}
    _lock = threading.Lock()

    @wraps(cls)
    def get_instance(*args, **kwargs):
        if cls not in _instances:       # 第一次检查（快速路径）
            with _lock:                  # 加锁
                if cls not in _instances: # 第二次检查（防止竞态）
                    _instances[cls] = cls(*args, **kwargs)
        return _instances[cls]
    
    return get_instance
```

> 📌 **DCL**: 第一层 if 跳过已存在实例；加锁后第二层 if 防止多线程重复创建

---

## ✅ 自测题

1. `@decorator` 的本质是什么？（一行代码等价写法）
2. 基础装饰器模板的三要素是什么？
3. 带参装饰器为什么需要三层函数？
4. 什么是单例模式？如何用装饰器实现？
5. 双重检查锁(DCL)解决什么问题？

---

# 📌 04 OOP 进阶·基础

> ⭐ 难度: ★★ | 🕐 预计时长: 40min

## 知识点脑图

```
04 OOP 进阶·基础
├── 抽象基类 ABC (metaclass=ABCMeta + @abstractmethod)
├── 为什么需要抽象类（接口契约）
├── 枚举类型 Enum (.name / .value)
├── @property 属性装饰器 (getter/setter)
├── __main__ 程序入口保护
├── 类关系 (is-a / has-a / use-a)
└── 综合实战: 工资结算系统(工厂模式)
```

---

## 🔑 核心卡片 1：抽象基类 ABC

```python
from abc import ABCMeta, abstractmethod

class Employee(metaclass=ABCMeta):  # ← 声明抽象类
    def __init__(self, name):
        self.name = name

    @abstractmethod               # ← 子类必须实现!
    def get_salary(self):
        pass

# 子类必须实现所有抽象方法，否则 TypeError!
class Manager(Employee):
    def get_salary(self): return 15000.0  # ✅

class Programmer(Employee):
    def __init__(self, name, working_hour=0):
        self.working_hour = working_hour
        super().__init__(name)
    def get_salary(self): return 200.0 * self.working_hour  # ✅
```

📌 **抽象类 = 接口契约**："你必须实现这些方法，否则别想运行！"

---

## 🔑 核心卡片 2：Enum 枚举

```python
from enum import Enum, unique

@unique  # 禁止重复值
class Suite(Enum):
    SPADE = 0    # 黑桃
    HEART = 1    # 红心
    CLUB = 2     # 梅花
    DIAMOND = 3  # 方块

s = Suite.SPADE
print(s.name)    # 'SPADE'    ← 名字字符串
print(s.value)   # 0          ← 赋的值
print(Suite(0))  # Suite.SPADE ← 通过 value 反查
```

🧠 **口诀**: *.name 是名字字符串 .value 是赋的值*

---

## 🔑 核心卡片 3：@property 方法变属性

```python
class Temperature:
    def __init__(self, celsius=0):
        self._celsius = celsius

    @property                      # getter: 读时调用
    def celsius(self):
        return self._celsius

    @celsius.setter               # setter: 写时调用
    def celsius(self, value):
        if value < -273.15:
            raise ValueError('温度不能低于绝对零度!')
        self._celsius = value

temp = Temperature(25)
print(temp.celsius)    # 25  (不用括号!)
temp.celsius = 30      # 自动验证
```

---

## 🔑 核心卡片 4：if __name__ == '__main__'

```
┌────────────────────────────────────────────────────┐
│ 直接运行此文件 → 开关 ON  → 执行 main()             │
│ python my_module.py                                │
│ 被其他文件导入 → 开关 OFF → 跳过，只提供定义         │
│ import my_module                                   │
│                                                    │
│ ✓ 同一文件既能运行也能导入                           │
│ ✓ 避免导入时触发副作用                               │
└────────────────────────────────────────────────────┘
```

🧠 **口诀**: *"如果我是主角(__main__)，就开始表演(main())"*

---

## 🔑 核心卡片 5：三种类关系

| 关系类型 | 关键词 | 说明 | 示例 |
|---------|--------|------|------|
| **is-a** | 继承 | B 是 A 的特化 | Manager is-a Employee |
| **has-a** | 组合 | B 包含 A 作为组成部分 | Poker has-a Card |
| **use-a** | 依赖 | B 使用 A | Player use-a Poker |

---

## ✅ 自测题

1. `metaclass=ABCMeta` 和 `@abstractmethod` 分别做什么？
2. Enum 比字面常量好在哪里？
3. `@property` getter/setter 怎么定义？
4. `if __name__ == '__main__'` 的作用？
5. 工厂模式解决了什么问题？

---

# 📌 05 OOP 进阶·高级 ★面试高频

> ⭐ 难度: ★★★ | 🕐 预计时长: 70min

## 知识点脑图

```
05 OOP 进阶·高级 ★面试高频
├── 深浅拷贝 copy vs deepcopy
├── == 与 is 的区别 ★面试常考
├── 垃圾回收 GC (引用计数+分代回收)
├── 魔法方法大全 (__str__/__repr__/__eq__/...)
├── __call__ 让对象可调用
├── 上下文管理器 (__enter__/__exit__)
├── Mixin 模式 (多重继承组合)
├── 元类 Metaclass (类的工厂)
├── SOLID 设计原则
└── 经典设计模式 (工厂/策略/观察者/单例)
```

---

## 🔑 核心卡片 1：深浅拷贝对比

| | 浅拷贝 `copy()` | 深拷贝 `deepcopy()` |
|--|--|--|
| **复制深度** | 只复制一层（内层共享）| 递归复制所有层级（完全独立）|
| **内存开销** | 小 | 大 |
| **性能** | 快 | 慢 |
| **适用** | 不修改内层可变对象时 | 需要完全独立的副本时 |

```
浅拷贝: a → [list₀, list₁]  →  b 共享内层对象
深拷贝: c → [list₀, list₁]  →  d 内层也是全新副本
```

🧠 **口诀**: *浅拷只抄皮，深拷连骨头一起复制*

---

## 🔑 核心卡片 2：== vs is

```python
x = [1, 2, 3]
y = [1, 2, 3]

print(x == y)   # True   → 值相等（内容一样）
print(x is y)   # False  → 不是同一对象（内存不同）

# ⚠️ 小整数缓存陷阱 (-5 ~ 256)
a = 256; b = 256
print(a is b)   # True  ← 缓存了!
c = 257; d = 257
print(c is d)   # False ← 超出范围!
```

> 📌 **铁律**: 永远用 `==` 判断值相等，`is` 只用于判断 `None`

---

## 🔑 核心卡片 3：魔法方法速查表

| 方法 | 触发时机 | 场景 |
|------|---------|------|
| `__init__(self)` | `obj = Class()` | 初始化属性 |
| `__new__(cls)` | 创建实例之前 | 单例模式 |
| `__str__(self)` | `str(obj)` / `print(obj)` | 用户友好显示 |
| `__repr__(self)` | `repr(obj)` / 终端 | 调试开发用 |
| `__eq__(self, other)` | `obj1 == obj2` | 自定义相等判断 |
| `__lt__(self, other)` | `obj1 < obj2` | 排序比较 |
| `__len__(self)` | `len(obj)` | 自定义长度 |
| `__getitem__(self, k)` | `obj[k]` | 索引访问 |
| `__iter__` / `__next__` | `for/inext()` | 迭代协议 |
| `__call__(self, *args)` | `obj(args)` | 对象可调用 |
| `__enter__` / `__exit__` | `with obj as x:` | 上下文管理器 |

🧠 **记忆口诀**: *__str__ 给人看，__repr__ 给机器看；__eq__ 定相等，__lt__ 排大小*

---

## 🔑 核心卡片 4：Mixin 模式

```python
class JsonMixin:
    """为任意类混入 JSON 序列化能力"""

    def to_dict(self):
        return {k: v for k, v in vars(self).items()
                if not k.startswith('_')}

    def to_json(self, indent=None):
        return json.dumps(self.to_dict(), indent=indent,
                         default=str, ensure_ascii=False)


class Person(JsonMixin):   # 只需继承 Mixin
    def __init__(self, name, age):
        self.name = name
        self.age = age

p = Person('张三', 25)
print(p.to_json(indent=2))  # 直接拥有 to_json 能力!
```

📌 **精髓**: 不改变原有类结构，只是"混入"额外能力。命名以 Mixin 结尾放继承链左侧。

---

## 🔑 核心卡片 5：SOLID 五大原则

| 原则 | 全称 | 一句话理解 |
|------|------|-----------|
| **S** | Single Responsibility | 一个类只做一件事 |
| **O** | Open/Closed | 对扩展开放对修改关闭 |
| **L** | Liskov Substitution | 子类能完美替代父类 |
| **I** | Interface Segregation | 接口要小而精 |
| **D** | Dependency Inversion | 依赖抽象不依赖具体 |

---

## ✅ 自测题

1. 浅拷贝和深拷贝的核心区别？
2. `__str__` 和 `__repr__` 分别何时被调用？
3. 什么是元类？它和普通类的关系？
4. SOLID 中 S 和 O 分别代表什么？
5. Mixin 为什么要放在继承链左侧？

---

# 📌 06 迭代器与生成器 ★重难点

> ⭐ 难度: ★★★ | 🕐 预计时长: 50min

## 知识点脑图

```
06 迭代器与生成器 ★重难点
├── 迭代器协议 (__iter__ + __next__)
├── for 循环底层原理
├── 迭代器一次性特性 ⚠️
├── Iterable 与 Iterator 分离设计
├── yield 三种用法 (生成器/无限序列/协程send)
├── 生成器表达式 vs 列表推导式
├── yield from 子生成器委派
└── 鸭子类型 vs ABC vs Protocol
```

---

## 🔑 核心卡片 1：迭代器协议

| 方法 | 所属 | 作用 |
|------|------|------|
| `__iter__(self)` | 可迭代对象 | 返回迭代器（通常 `return self`）|
| `__next__(self)` | 迭代器 | 返回下一项，没有则抛 `StopIteration` |

### for 循环底层做了什么？

```
for item in iterable:
    do_something(item)

# Python 背后:
iterator = iter(iterable)        # ① 调用 __iter__()
while True:
    try:
        item = next(iterator)    # ② 调用 __next__()
        do_something(item)       # ③ 执行循环体
    except StopIteration:        # ④ 结束信号
        break
```

---

## 🔑 核心卡片 2：迭代器一次性特性 ⚠️

```python
cd = Countdown(3)

list1 = list(cd)   # [3, 2, 1]  水流完了
list2 = list(cd)   # []         已空!!!

# 解决: 分离 Iterable 和 Iterator
class RangeIterable:      # 可迭代对象
    def __iter__(self):
        return RangeIterator(...)  # 每次返回新的迭代器!

ri = RangeIterable(1, 4)
list(ri)  # [1, 2, 3]
list(ri)  # [1, 2, 3]  ← 可以重复遍历! ✓
```

📌 **教训**: *需要多次遍历时转 list() 或分离设计*

---

## 🔑 核心卡片 3：yield 三种用法

### 用法一：基本生成器（替代手写迭代器）

```python
def countdown_gen(start):
    while start > 0:
        yield start    # 暂停并返回值
        start -= 1
```

### 用法二：无限序列（惰性计算省内存）

```python
def fibonacci():
    a, b = 0, 1
    while True:
        yield a       # 无限序列但不占内存!
        a, b = b, a + b
```

### 用法三：协程 send()

```python
def accumulator(start=0):
    total = start
    while True:
        value = yield total   # 右边产出，左边接收
        if value is not None:
            total += value

acc = accumulator(100)
next(acc)              # 启动! → 100
acc.send(10)           # → 110
acc.send(20)           # → 130
```

> ⚠️ **send() 前必须先 next() "启动"生成器!**

---

## 🔑 核心卡片 4：鸭子类型 vs ABC vs Protocol

| 特性 | 鸭子类型 | ABC | Protocol |
|------|:-------:|:----:|:--------:|
| 机制 | 运行时隐式检查 | 显式继承 | 类型注解/静态分析 |
| 灵活性 | 最高 | 中等 | 高 |
| IDE 支持 | 弱 | 强 | 最强(Python 3.8+) |
| 适用场景 | 快速脚本 | 库 API 定义 | 大项目类型安全 |

```python
# 鸭子类型: "走起来像鸭子叫起来像鸭子就是鸭子"
# 只要实现了 __iter__ 就能被 for 遍历

# ABC: 必须显式继承并实现抽象方法
class Circle(Drawable): ...

# Protocol: 不需要继承结构上匹配即可
class Person:  # 没继承 HasName 但有 name 属性 → 通过!
    ...
```

---

## ✅ 自测题

1. 迭代器协议的两个必要方法？
2. `for item in iterable:` 背后 Python 做了哪些事？
3. 为什么迭代器只能遍历一次？如何避免？
4. yield 三种用法分别举例。
5. send() 前为什么要先 next()？

---

# 📌 07 数据结构与算法

> ⭐ 难度: ★★ | 🕐 预计时长: 50min

## 知识点脑图

```
07 数据结构与算法
├── Big-O 时间复杂度
├── Python 内置类型复杂度速查 ★面试常考
├── 五大算法思想 (穷举/贪婪/分治/回溯/DP)
├── 排序算法 (冒泡/选择/归并/快速)
├── 查找算法 (顺序/折半)
├── 经典例题 (两数之和/有效括号/LRU)
└── 算法学习建议
```

---

## 🔑 核心卡片 1：Big-O 复杂度排序

```
O(1) < O(log n) < O(n) < O(n log n) < O(n²) < O(2ⁿ) < O(n!)
```

| 大O | 名称 | 典型算法 | 实际感受 |
|:----:|------|---------|---------|
| O(1) | 常数时间 | 哈希表/数组索引 | 瞬间完成 |
| O(log n) | 对数时间 | 二分查找 | 数据×10 多几次操作 |
| O(n) | 线性时间 | 遍历列表 | 数据翻倍时间翻倍 |
| O(n log n) | 对数线性 | 归并/快排(平均) | 高效排序标准 |
| O(n²) | 平方时间 | 冒泡/嵌套循环 | 数据大就很慢 |
| O(2ⁿ) | 指数时间 | 斐波那契递归 | 数据>30不可接受 |

---

## 🔑 核心卡片 2：Python 内置复杂度速查 ★面试必考

### list

| 操作 | 复杂度 |
|------|:-----:|
| `append(x)` | **O(1)** ✅ |
| `pop()` | **O(1)** ✅ |
| `insert(i, x)` / `pop(i)` | **O(n)** ❌ |
| `x in list` | **O(n)** ❌ |
| `list[i]` | **O(1)** ✅ |

### dict / set（远优于 list!）

| 操作 | dict | set |
|------|:----:|:---:|
| 设置/获取/删除 | **O(1)** | **O(1)** |
| `key in dict` / `x in set` | **O(1)** ⭐ | **O(1)** ⭐ |

> 📌 **实用结论**: 成员判断用 set > list；头部操作用 deque > list

---

## 🔑 核心卡片 3：五大算法思想

| 思想 | 核心 | 经典问题 | 一句话理解 |
|------|------|---------|-----------|
| **穷举** | 尝试所有可能 | 百钱百鸡 | 规模小的暴力搜索 |
| **贪婪** | 每步选当前最优 | 找零/Dijkstra | 局部最优→希望全局最优 |
| **分治** | 分→治→合并 | 归并/快排 | 大问题拆成独立子问题 |
| **回溯** | 试探→回退 | 八皇后/N皇后 | 深度搜索+撤销选择 |
| **DP** | 记忆重叠子问题 | 斐波那契/爬楼梯 | 以空间换时间避免重复计算 |

---

## 🔑 核心卡片 4：经典例题速览

### 两数之和 — 哈希表 O(n)

```python
def two_sum_hash(nums, target):
    seen = {}                     # {value: index}
    for i, num in enumerate(nums):
        complement = target - num  # 需要的补数
        if complement in seen:     # 补数出现过?
            return seen[complement], i  # 找到了!
        seen[num] = i             # 记录当前位置
```

### 有效括号 — 栈

```python
def is_valid(s):
    stack = []
    pairs = {')': '(', '}': '{', ']': '['}
    for ch in s:
        if ch in pairs.values():  # 左括号入栈
            stack.append(ch)
        elif ch in pairs.keys():   # 右括号检查栈顶
            if not stack or stack.pop() != pairs[ch]:
                return False
    return not stack  # 栈空则匹配成功
```

### LRU 缓存 — OrderedDict

```python
class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key):
        if key not in self.cache: return -1
        self.cache.move_to_end(key)  # 访问→移到最后(最新)
        return self.cache[key]

    def put(self, key, value):
        if key in self.cache: self.cache.move_to_end(key)
        self.cache[key] = value
        if len > capacity:
            self.cache.popitem(last=False)  # 弹出头部的(最旧)
```

---

## ✅ 自测题

1. `list.append()` 和 `list.insert(0,x)` 复杂度？
2. 五大算法思想及各一个经典例子？
3. 二分查找前提条件？为什么？
4. DP 为什么比递归快？（关键词？）
5. LRU 淘汰策略？

---

# 📌 08 并发编程实战 ★重难点

> ⭐ 难度: ★★★ | 🕐 预计时长: 60min

## 知识点脑图

```
08 并发编程实战 ★重难点
├── GIL 全局解释器锁（Python并发基石）
├── 多线程 threading
│   ├── Lock / RLock 解决竞态条件
│   ├── Condition 生产者-消费者模型
│   ├── Semaphore 限制并发数
│   └── ThreadPoolExecutor 线程池
├── 多进程 multiprocessing（绕过GIL）
│   └── 进程间通信 IPC (Queue)
├── 异步IO async/await + aiohttp
└── 三种并发方式选型指南
```

---

## 🔑 核心卡片 1：GIL 及其影响

```
GIL = Global Interpreter Lock = CPython 全局互斥锁
规则: 同一时刻只有一个线程执行 Python 字节码
```

| 任务类型 | 多线程效果 | 原因 |
|---------|----------|------|
| **IO 密集型** (网络/文件/数据库) | ✅ 有效加速 | IO等待时 GIL释放 其他线程可跑 |
| **CPU 密集型** (计算/图像处理) | ❌ 不能并行 | 同一时间只有一线程在执行 |

📌 **结论**: CPU 密集型用**多进程**替代多线程!

---

## 🔑 核心卡片 2：Lock / RLock / Condition / Semaphore

| 工具 | 作用 | 特点 |
|------|------|------|
| `Lock` | 互斥锁 | 不可重入，同一线程 acquire 两次会死锁 |
| `RLock` | 可重入锁 | 同一线程可多次 acquire（需匹配 release）|
| `Condition` | 条件变量 | wait()/notify() 生产者-消费者模型 |
| `Semaphore` | 信号量 | 限制最大并发数（类似停车场车位）|

> ⚠️ **Condition.wait() 必须用 while 不用 if** —— 防止虚假唤醒!

---

## 🔑 核心卡片 3：线程池 ThreadPoolExecutor（推荐方式）

```python
from concurrent.futures import ThreadPoolExecutor
import time

def worker(name, seconds):
    time.sleep(seconds)
    return f'{name} done'

# 方式一: submit 提交单个任务
with ThreadPoolExecutor(max_workers=3) as pool:
    future = pool.submit(worker, 'TaskA', 2)
    print(future.result())  # 阻塞获取结果

# 方式二: map 批量提交（保持顺序）
with ThreadPoolExecutor(max_workers=3) as pool:
    results = pool.map(worker, ['A','B','C'], [2,1,3])
    for r in results:
        print(r)
```

📌 **不要手动创建 Thread 对象**，用线程池自动管理！

---

## 🔑 核心卡片 4：多进程 multiprocessing

```python
from multiprocessing import Process, Queue
import os

def worker(queue, data):
    result = data * 2
    queue.put(result)  # 通过 Queue IPC 通信

if __name__ == '__main__':
    q = Queue()
    p = Process(target=worker, args=(q, 42))
    p.start()
    p.join()
    print(q.get())  # 84
```

> 📌 **每个进程有独立的解释器和内存空间**——真正并行绕过 GIL

---

## 🔑 核心卡片 5：async/await 异步IO

```python
import asyncio
import aiohttp

async def fetch_url(session, url):
    async with session.get(url) as resp:
        return await resp.text()

async def main():
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_url(session, url) for url in urls]
        results = await asyncio.gather(*tasks)  # 并发执行!
        return results

asyncio.run(main())
```

💡 **适用**: 高并发 IO 任务（大量网络请求）。单线程事件循环调度协程切换。

---

## 🔑 核心卡片 6：选型指南（面试必答）

| 场景 | 推荐方案 | 原因 |
|------|---------|------|
| IO 密集少量任务 (<10) | **多线程 threading** | 简单够用 |
| IO 密集大量任务 (>50) | **async/aiohttp** | 最高效（单线程高并发）|
| CPU 密集型任务 | **多进程 multiprocessing** | 绕过 GIL 真正并行 |
| 混合型 | **多进程 + 线程池** | 各取所长 |
| 定时任务/回调 | **asyncio** | 天然支持异步调度 |

---

## ✅ 自测题

1. GIL 是什么？对 CPU 密集型和 IO 密集型的区别影响？
2. Lock 和 RLock 的区别？
3. Condition.wait() 为什么必须用 while？
4. Semaphore 的用途？
5. 三种并发方式的选型原则？

---

## 附录：记忆口诀汇总

| 口诀 | 适用章节 |
|------|---------|
| *嵌套列表用推导，乘法复制是坑路* | 01 嵌套列表 |
| *__str__给人看，__repr__给机器看* | 05 魔法方法 |
| *浅拷只抄皮，深拷连骨头一起复制* | 05 深浅拷贝 |
| *如果我是主角(__main__)就开始表演(main())* | 04 程序入口 |
| *参数层→函数层→wrapper层* | 03 带参装饰器 |
| *while-not-if 并发编程铁律* | 08 Condition |
| *.name是名字.value是赋值* | 04 Enum |
| *迭代器像水流流完就没* | 06 一次性特性 |

---

> 🎉 **祝学习顺利！建议配合 Anki 卡片间隔重复记忆效果更佳！**
>
> **生成日期**: 2026-04-24 | **来源**: Python-100-Days Master
