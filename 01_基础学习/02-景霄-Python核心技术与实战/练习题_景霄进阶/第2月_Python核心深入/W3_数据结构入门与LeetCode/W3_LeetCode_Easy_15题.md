# 🏆 第2月 W3：LeetCode Easy 15题实战

> **目标**：完成15道LeetCode Easy题目，建立刷题节奏  
> **刷题策略**：按Tag刷，先Array → String → Linked List → Hash Table  
> **时间分配**：每天2-3题，周末复习错题

---

## 📋 15题清单与进度跟踪

| 序号 | 题号 | 题目 | Tag | 难度 | 第一次 | 第二次 | 笔记 |
|------|------|------|-----|------|--------|--------|------|
| 1 | #1 | 两数之和 | Array + Hash Table | Easy | ⬜ | ⬜ | |
| 2 | #20 | 有效的括号 | String + Stack | Easy | ⬜ | ⬜ | |
| 3 | #21 | 合并两个有序链表 | Linked List | Easy | ⬜ | ⬜ | |
| 4 | #70 | 爬楼梯 | DP | Easy | ⬜ | ⬜ | |
| 5 | #101 | 对称二叉树 | Tree + DFS | Easy | ⬜ | ⬜ | |
| 6 | #104 | 二叉树最大深度 | Tree + DFS/BFS | Easy | ⬜ | ⬜ | |
| 7 | #136 | 只出现一次的数字 | Bit Manipulation | Easy | ⬜ | ⬜ | |
| 8 | #155 | 最小栈 | Stack | Easy | ⬜ | ⬜ | |
| 9 | #160 | 相交链表 | Linked List | Easy | ⬜ | ⬜ | |
| 10 | #167 | 两数之和 II | Two Pointers | Easy | ⬜ | ⬜ | |
| 11 | #169 | 多数元素 | Array | Easy | ⬜ | ⬜ | |
| 12 | #206 | 反转链表 | Linked List | Easy | ⬜ | ⬜ | |
| 13 | #217 | 存在重复元素 | Array + Hash Set | Easy | ⬜ | ⬜ | |
| 14 | #242 | 有效的字母异位词 | String + Hash | Easy | ⬜ | ⬜ | |
| 15 | #704 | 二分查找 | Binary Search | Easy | ⬜ | ⬜ | |

> ⬜ 未做 | 🟦 尝试中 | ✅ 已AC | ❌ 需要复习

---

## 📖 题目详解（按Tag分类）

### 🔷 Tag 1：Array（数组）

#### 🏆 #1 两数之和

**题目描述**：  
给定整数数组 `nums` 和目标值 `target`，找出和为目标值的两个整数的下标。

**示例**：
```
输入：nums = [2,7,11,15], target = 9
输出：[0,1]
```

**解法1：哈希表（推荐）— O(n)**
```python
def two_sum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []
```

**解法2：暴力法 — O(n²)**
```python
def two_sum_brute(nums, target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []
```

**记忆模板**：
```python
# 哈希表模板（适用：两数之和类问题）
seen = {}
for i, num in enumerate(nums):
    if target - num in seen:
        return [seen[target-num], i]
    seen[num] = i
```

---

#### 🏆 #169 多数元素

**题目描述**：  
给定大小为 `n` 的数组，找出其中占多数（出现次数 > ⌊ n/2 ⌋）的元素。

**示例**：
```
输入：[3,2,3]
输出：3
```

**解法1：哈希表 — O(n)**
```python
from collections import Counter

def majority_element(nums):
    count = Counter(nums)
    return max(count.keys(), key=count.get)
    
    # 更简洁：
    # return Counter(nums).most_common(1)[0][0]
```

**解法2：Boyer-Moore 投票算法 — O(n)，O(1)空间**
```python
def majority_element_vote(nums):
    candidate = None
    count = 0
    for num in nums:
        if count == 0:
            candidate = num
        count += 1 if num == candidate else -1
    return candidate
```

---

#### 🏆 #217 存在重复元素

**题目描述**：  
给定整数数组，判断是否存在重复元素。

**示例**：
```
输入：[1,2,3,1]
输出：True
```

**解法1：集合 — O(n)**
```python
def contains_duplicate(nums):
    return len(nums) != len(set(nums))
```

**解法2：排序 — O(n log n)**
```python
def contains_duplicate_sort(nums):
    nums.sort()
    for i in range(1, len(nums)):
        if nums[i] == nums[i-1]:
            return True
    return False
```

---

#### 🏆 #704 二分查找

**题目描述**：  
在升序数组中查找目标值，返回下标或-1。

**示例**：
```
输入：nums = [-1,0,3,5,9,12], target = 9
输出：4
```

**解法：二分查找 — O(log n)**
```python
def search(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# 记忆模板：
# while left <= right:
#     mid = (left + right) // 2
#     if nums[mid] == target: return mid
#     if nums[mid] < target: left = mid + 1
#     else: right = mid - 1
# return -1
```

---

### 🔷 Tag 2：String（字符串）

#### 🏆 #20 有效的括号

**题目描述**：  
判断括号字符串是否有效（正确闭合）。

**示例**：
```
输入："()[]{}"
输出：True
```

**解法：栈 — O(n)**
```python
def is_valid(s):
    stack = []
    mapping = {')': '(', ']': '[', '}': '{'}
    for char in s:
        if char in mapping:
            top = stack.pop() if stack else '#'
            if mapping[char] != top:
                return False
        else:
            stack.append(char)
    return not stack
```

**记忆模板**：
```python
# 栈模板（适用：括号匹配、表达式求值）
stack = []
for char in s:
    if char in '([{':
        stack.append(char)
    else:
        if not stack: return False
        if not is_match(stack.pop(), char):
            return False
return not stack
```

---

#### 🏆 #242 有效的字母异位词

**题目描述**：  
判断两个字符串是否包含相同字符（顺序可不同）。

**示例**：
```
输入：s = "anagram", t = "nagaram"
输出：True
```

**解法1：排序 — O(n log n)**
```python
def is_anagram(s, t):
    return sorted(s) == sorted(t)
```

**解法2：哈希表 — O(n)**
```python
from collections import Counter

def is_anagram(s, t):
    return Counter(s) == Counter(t)
```

---

### 🔷 Tag 3：Linked List（链表）

#### 🏆 #21 合并两个有序链表

**题目描述**：  
合并两个升序链表为一个新的升序链表。

**示例**：
```
输入：1->2->4, 1->3->4
输出：1->1->2->3->4->4
```

**解法1：迭代 — O(n+m)**
```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def merge_two_lists(l1, l2):
    dummy = ListNode(0)
    curr = dummy
    while l1 and l2:
        if l1.val <= l2.val:
            curr.next = l1
            l1 = l1.next
        else:
            curr.next = l2
            l2 = l2.next
        curr = curr.next
    curr.next = l1 if l1 else l2
    return dummy.next
```

---

#### 🏆 #206 反转链表

**题目描述**：  
反转单链表。

**示例**：
```
输入：1->2->3->4->5->NULL
输出：5->4->3->2->1->NULL
```

**解法1：迭代 — O(n)**
```python
def reverse_list(head):
    prev = None
    curr = head
    while curr:
        next_temp = curr.next
        curr.next = prev
        prev = curr
        curr = next_temp
    return prev
```

**解法2：递归 — O(n)**
```python
def reverse_list_recursive(head):
    if not head or not head.next:
        return head
    new_head = reverse_list_recursive(head.next)
    head.next.next = head
    head.next = None
    return new_head
```

**记忆模板**：
```python
# 反转链表迭代法
prev, curr = None, head
while curr:
    next_temp = curr.next
    curr.next = prev
    prev = curr
    curr = next_temp
return prev
```

---

#### 🏆 #160 相交链表

**题目描述**：  
找到两个单链表相交的起始节点。

**解法：双指针 — O(n)**
```python
def get_intersection_node(headA, headB):
    pA, pB = headA, headB
    while pA != pB:
        pA = pA.next if pA else headB
        pB = pB.next if pB else headA
    return pA
```

---

### 🔷 Tag 4：Tree（二叉树）

#### 🏆 #101 对称二叉树

**题目描述**：  
判断二叉树是否轴对称。

**解法：递归 — O(n)**
```python
def is_symmetric(root):
    def is_mirror(left, right):
        if not left and not right:
            return True
        if not left or not right:
            return False
        return (left.val == right.val and
                is_mirror(left.left, right.right) and
                is_mirror(left.right, right.left))
    
    return is_mirror(root.left, root.right) if root else True
```

---

#### 🏆 #104 二叉树最大深度

**题目描述**：  
给定二叉树，找出其最大深度。

**解法1：递归（DFS）— O(n)**
```python
def max_depth(root):
    if not root:
        return 0
    return 1 + max(max_depth(root.left), max_depth(root.right))
```

**解法2：迭代（BFS）— O(n)**
```python
from collections import deque

def max_depth_bfs(root):
    if not root:
        return 0
    queue = deque([root])
    depth = 0
    while queue:
        for _ in range(len(queue)):
            node = queue.popleft()
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        depth += 1
    return depth
```

---

### 🔷 Tag 5：Dynamic Programming（动态规划）

#### 🏆 #70 爬楼梯

**题目描述**：  
每次爬1或2个台阶，爬n阶有多少种不同的方法？

**解法：动态规划 — O(n)**
```python
def climb_stairs(n):
    if n <= 2:
        return n
    prev2, prev1 = 1, 1
    for _ in range(2, n+1):
        curr = prev1 + prev2
        prev2, prev1 = prev1, curr
    return prev1

# 数学原理：斐波那契数列
# dp[n] = dp[n-1] + dp[n-2]
```

---

## 📊 本周刷题统计

| 日期 | 完成题目 | 正确率 | 用时 | 错题原因 |
|------|---------|--------|------|---------|
| 05-15 | #1, #20 | 100% | 30min | - |
| 05-16 | #21, #70 | 100% | 35min | - |
| 05-17 | #101, #104 | 50% | 45min | 递归边界条件 |
| ... | ... | ... | ... | ... |

---

## 💡 刷题技巧总结

### 通用解题步骤
1. **理解题意** — 用自己的话复述题目
2. **举例子** — 用简单例子验证理解
3. **想暴力** — 先想最笨的方法（确保正确性）
4. **优化** — 找规律、用合适的数据结构
5. **写代码** — 注意边界条件
6. **测试** — 用例子验证

### 常见错误
- ❌ 没考虑空输入（None、空数组）
- ❌ 没考虑边界（数组只有一个元素）
- ❌ 整数溢出（Python不存在，但其他语言要注意）
- ❌ 时间复杂度过高（暴力法超时）

---

*📅 创建日期: 2026年5月6日*  
*🏆 目标：本月累计完成 LeetCode Easy 25-30 题*  
*📌 正确率目标：> 60%*
