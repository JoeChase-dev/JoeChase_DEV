# 16. API 基础概念

> 来源：`01-Python语言进阶.ipynb`

---

## 16.1 API 是什么？

**API = Application Programming Interface（应用程序编程接口）**

### 通俗理解

```
你（程序员）───→ 【API 就是菜单/服务员】───→ 厨房（系统/模块内部）
```

### 本质

API = 一组预先定义好的 **"调用规则"**。

它告诉其他程序：
1. 我能提供什么功能（方法名）
2. 你需要给我什么参数
3. 我会返回什么结果

---

## 16.2 编程中的含义

| 术语 | 全称 | 含义 |
|:-----|:-----|:-----|
| **API** | Application Programming Interface | 应用程序编程接口 |

**API 就是软件模块对外暴露的"使用说明书"。**

---

## 16.3 笔记中的 API 示例（并发编程模块）

```python
threading.Lock()              # ← 这是一个 API（创建锁的方法）
lock.acquire()                # ← 这也是一个 API（获取锁的方法）
pool.submit(fn, *args)        # ← 这也是 API（提交任务的方法）
future.result()               # ← 还是 API（获取结果的方法）
```

这些都是 `threading` 和 `concurrent.futures` 模块暴露给开发者使用的接口。

---

## 16.4 一句话总结

> **API = 别人写好的代码给你调用的"窗口"。你只管调用，不用关心内部怎么实现。**
