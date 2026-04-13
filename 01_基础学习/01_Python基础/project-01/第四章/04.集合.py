# # 集合  无序，不可重复，可修改的数据容器
# # 基本操作
# s1.add("t")                 添加元素到集合
# s1.remove("t")              移除指定元素（没有就报错）
# e = s1.pop()                随机删除元素并返回
# s1.clear()                  清空集合
# s1.difference(s2)           求差集
# s1.union(s2)                求并集
# s1.intersection(s2)         求交集
# set <= other                是否set中每个元素都在other中
# set < other                 set是否是other真子集
# s in set
# 定义
s1 = {1,3,54,2,4,6,5,3,7}
print(s1)
print(type(s1))
print()
s2 = set()
print(type(s2))
print()
s3 = {}
print(type(s3))
# 注意：空集合的定义不可以使用{}，{}表示空字典；由于集合无序，因此不支持下标索引访问
s1 = {1,2,3,4,5,6,7,8,9}
s1.add(10)
print(s1)
print()
#删除
s1.remove(1)
print(s1)
print()

e = s1.pop()
print(e)
print(s1)
print()

s1.clear()
print(s1)
print()
#集合操作
s2 = {"A","B","C"}
s3 = {"C","D","E"}
print(s2)
print(s3)
print(s2.difference(s3))
print(s3.difference(s2))
print(s2.union(s3))
print(s2.intersection(s3))
# 案例
# 1 同时修法语和艺术的学生
# 2 找出同修四门课的学生
# 3 找出修了足球但没修篮球的学生
# 4 统计每个人选修的数量
# 足球
football_set = {"a","b","c","d","e","f"}
# 篮球
basketball_set ={"a","b","c","d"}
# 法语
french_set ={"a","d","e",}
# 艺术
art_set = {"a","d","e","f"}
# 方法一
fa_set = french_set.intersection(art_set)
print(f"同时修法语和艺术的学生有：{fa_set}")
# 方法二
fa_set = french_set & art_set
print(f"同时修法语和艺术的学生有：{fa_set}")
print()
# 找出同修四门课的学生
all_set = football_set & basketball_set & french_set & art_set
print(f"找出同修四门课的学生有：{all_set}")
print()
# 找出修了足球但没修篮球的学生
# 方法一
fb_set = football_set.difference(basketball_set)
print(f"修了足球但没修篮球的学生{fb_set}")
# 方法二
fb_set = football_set - basketball_set
print(f"修了足球但没修篮球的学生{fb_set}")
# 方法三 {要往集合中添加的数据 for s in set1 if 条件}
fb_set = {i for i in football_set if i not in basketball_set}
print(f"修了足球但没修篮球的学生{fb_set}")
print()
# 4 统计每个人选修的数量
all_set = football_set|basketball_set|french_set|art_set
print(f"名单为{all_set}")
all_list = [*football_set,*basketball_set,*french_set,*art_set]
for i in all_set:    # 获取名单，从而在list 中遍历
    print(f"{i}选了{all_list.count(i)}门课")
