"""
数字类型  int float complex
文本类型  str
序列类型  list tuple range
映射类型  dict
"""

# 列表
# 数据容器的一类，存储多个数据(可以不同类型)，可重复，有序，可修改（下表/索引）
# 索引正向0开始，反向-1开始
# 列表名称 = [元素 ...]
# 序列类型：容器中的元素按顺序排列、可通过索引访问的容器类型称为序列（可以切片）
# 查看：list[0]   修改：list[0] = "a"  删除 ：del list[0]   索引不能超出范围


# #列表定义 --list
# s = ["a",1,3,5,-1,"hello"]
#
# print(s)
#
# #获取
# print(s[1])
#
# print(s[-5])
#
# #修改
# s[1] = ("b")
# print(s[1])
#
# #删除
# del s[0]
# print(s)


#列表切片
#切片  对操作的数据中截取其中一部分。
#语法 序列数据[开始索引：结束索引：步长]
# 不包含结束索引对应元素，（开始默认0，结束默认列表长度，步长默认1）

#定义列表
# s = ["A","V", "G", "K", "t", "Y"]
#
# #切片操作[开始索引：结束索引：步长]
#
# print(s[0:5:2])
# print(type(s[0:5:2]))  #仍为列表

# 简写
# s[:5:1]
# s[0:5:]
# s[0:5]  以上三种可以
# s[5]    不行


#常见方法（能力/功能）
#列表常见内置方法
# append()    尾部追加元素  s.append(10086)
# insert()    指定索引前插入 s.insert(0,92)
# extend(可迭代对象*)   尾部追加列表元素  s.extend([10086,10010])  abc  -->  a,b,c
# remove()    移除第一个匹配的值   s.remove(75)
# pop()   删除指定索引的元素,会返回(未指定，默认最后一个)   s.pop(2)
# sort()  类型一致，进行排序   s.sort()
# reserve()   反转列表元素  s.reverse()
# del  删除
# copy()   列表的浅拷贝  s.copy()
# clear()   清空列表元素  s.clear()
# len(list)
# list.count()   统计某个元素出现的次数

# list.sort()原地排序
# sort(list)排序后返回新的列表

# #列表定义
# s = [32,53,63,24,14,56,78]
#
# #追加元素
# s.append(12)
# print(s)
#
# #插入元素
# s.insert(3,45)
# print(s)
#
# #移除元素
# s.remove(53)
# print(s)
#
# #删除指定索引并返回
# e= s.pop(4)
# print(s)
# print(e)
#
# #类型一致，排序
# s.sort()
# print(s)
#
# #反转
# s.reverse()
# print(s)



# 案例1
#定义列表，实现10个数的排序，输出其中的最小值、最大值和平均值
# 1.定义列表
# num_list = []
#
# #输入10个数字
#
# for i in range(10):
#     num = int(input("请输入一个数字："))
#     num_list.append(num)
#
# #进行排序
#
# num_list.sort()
# print("排序后的数字列表为：",num_list)
#
# #输出最值，平均值    sum()函数求和，len()函数获取元素数量
# print("最大值：",num_list[-1])
# print("最小值：",num_list[0])
# print("平均值：",sum(num_list)/len(num_list))


#python数据统计中常用语句
# min()  获取最小值
# max()  获取最大值
# sum()  求和
# len()  获取元素个数


# 案例2
# 合并两个列表中的元素，对合并的结果进行去重处理

#定义列表
# num_list1 = [1,24,53,65,78,45,98]
# num_list2 = [2,34,54,66,45,67,23,99,47]

# # 1.合并列表
# # for i in num_list2:
# #     num_list1.append(i)
#
# #简化合并
# # num _list = num_list1+num_list2  (也可以)
#
# #解包：将列表这一类容器揭开成一个个独立元素
# #组包:将多个值合并到一个容器
# num_list = []
# num_list = [*num_list1,*num_list2]
#
# print("合并后的列表为：",num_list1)
#
# #2去重复元素
# new_list = []
# for i in num_list1:
#     # 判断new_list 中是否存在num元素
#     if i not in new_list:  #in/not in   判断是否存在于列表中，存在True 不存在False
#         new_list.append(i)
#
# new_list.sort()
# print("去重复后的列表为：",new_list)

# # 案例3
# # 方法一：
# num_list1 = []
# for i in range(1,21):
#     num_list1.append(i ** 2)
# print(num_list1)
#
# # 方法二：
# 列表推导式 ---> 按照一定规则快速生成一个列表的方法 -->  格式1：[要插入的值 for i in 列表/序列]
# num_list2 = [i**2 for i in range(1,21)]
# print(num_list2)


# 案例四
# 数字列表中提取偶数，并计算其平方，组成一个新的列表
# 列表推导式 --->  语法格式2： [要插入的值 for i in 序列/列表 if 条件]

num_list = [1,3,5,2,34,67,24,63,23]
new_list = [i**2 for i in num_list if i%2==0]

print(new_list)