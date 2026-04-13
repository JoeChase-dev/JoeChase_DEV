"""
1.将多个列表合并为一个列表，并去除重复元素，排好序后输出
2.将1-30中能被3 或 5 整除的元素提出来，并获取这些数字对应的平方，组成一个新的列表
3.将如下列表中的正数提取出来，封装成一个新的列表
"""

# #1
# list1 = [1,2,4,5,6,24,67,35,24]
# list2 = [2,4,6,78,35,34,23,67,80]
# list3 = [2,4,6,8,10]
# #解包，重组
# new_list = [*list1, *list2, *list3]
# end_list =[]
# # 排序
# for i in new_list:
#     if i not in end_list:
#         end_list.append(i)
# end_list.sort()
#
# print(end_list)


# #2
# list1 = []
# for i in range(1,31):
#     if i % 3 ==0 or i % 5 ==0:
#         list1.append(i**2)
# list1.sort()
# print(list1)

# #3
# list1 = [1,3,-5,3,6,-7,13,-45,78,-91]
# list2 = [i for i in list1 if i>0]
# print(list2)

#字符串练习
"""
1.输入一个字符串，判断是否是回文
2.输入十个字符串，反转后全部转换为大写，然后记录在列表中，最后将列表中内容遍历输出"""


# # 输入一个字符串
# s_word = input("请输入一段字符串：")
#
# # 判断是否为回文  字符串的正反向索引实现
# if s_word[::1] == s_word[::-1]:
#     print("是回文")
# else :
#     print("不是回文")


# 输入十个字符串
# s_list = []
# for i in range(1,11):
#     s = input("请输入字符串：")
#     around =s[::-1].upper()
#     s_list.append(around)
#
# print(s_list)
