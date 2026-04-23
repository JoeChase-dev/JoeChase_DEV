# 10. Mixin 混入

> 来源：`01-Python语言进阶.ipynb`

---

## 10.1 什么是 Mixin？

Mixin 是一种通过**组合而非继承**来复用代码的设计模式。

它本身不独立使用，而是"混入"到其他类中，为其**添加/增强特定功能**。

---

## 10.2 实战示例：只允许设置一次的字典

```python
class SetOnceMappingMixin:
    """自定义混入类"""
    __slots__ = ()                    # ① 空元组，阻止该类创建 __dict__（节省内存）
    
    def __setitem__(self, key, value):
        if key in self:
            raise KeyError(str(key) + ' already set')
        return super().__setitem__(key, value)   # ③ 委托给 MRO 链的下一个类


class SetOnceDict(SetOnceMappingMixin, dict):   # 继承 Mixin + dict
    """自定义字典"""
    pass


my_dict = SetOnceDict()
my_dict['username'] = 'jackfrued'        # ✅ 正常
try:
    my_dict['username'] = 'hellokitty'   # ❌ 报错：KeyError: username already set
except KeyError:
    pass

print(my_dict)                          # {'username': 'jackfrued'}
```

### 关键点解析

| 要点 | 说明 |
|:-----|:-----|
| `__slots__ = ()` | 声明此类没有实例属性，纯功能类 |
| `super()` | 不硬编码 `dict.__setitem__`，委托给 MRO 链的下一个类 |
| 只覆写 `__setitem__` | 单一职责，只管"限制重复设置"这一件事 |

---

## 10.3 MRO 与继承顺序

```
MRO（方法解析顺序）：
SetOnceDict → SetOnceMappingMixin → dict → object
```

执行 `my_dict['username'] = 'jack'` 时：

1. Python 找到 `SetOnceMappingMixin.__setitem__`
2. 该方法检查 key 不存在
3. `super()` 委托给 `dict.__setitem__` 完成实际赋值

---

## 10.4 Mixin vs 直接子类化

| 方式 | 问题 |
|:-----|:-----|
| 直接子类化 `dict` | 耦合度高，无法复用于 UserDict、OrderedDict 等 |
| **Mixin** | **可插拔！可混入任何映射类型** |

---

## 10.5 本质总结

> Mixin 的本质：把一个**横切关注点**（如"只允许设置一次"）从业务类中抽离出来，通过 MRO 的 `super()` 链灵活注入到任何需要的类中。

这是 Python **"组合优于继承"**的典型实践。
