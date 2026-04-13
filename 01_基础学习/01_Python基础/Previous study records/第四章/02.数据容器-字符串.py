# 字符串
# 可以存放任意数量的字符
# 特点：不可变性、有序性、可迭代性（可遍历迭代）
# 字符串中每一个字符元素都有其对应下标（索引），就可以获取到对应元素
# 可以切片
s = "Hello_world"
print(s[4])  #正向索引
print(s[-7]) #反向索引
#切片操作
print(s[0:5:2])
print(s[:5:2])
print(s[0:5:])
print(s[:5])
print(s[0::1])
#步长为正数  从前往后；负数  从后往前（要与索引顺序一致）
# print(s[::-1]
# 常用方法
# find()  查找子串，返回第一次出现的索引的位置，找不到返回-1
# join()  将字符串列表中的元素连接成一个新的字符串，指定连接符
# count() 统计子串出现的次数
# upper() 将所有字母转换为大写
# lower() 将所有字母转换为小写
# split() 将字符串按指定分隔符分割为列表
# strip() 去除两边空白字符或指定字符
# replace()   将字符串中的指定子串替换为新的子串
# startswith()    检查字符串是否以指定子串开头，返回布尔
# -------------------------字符串常用方法
# s = " Hello - Python - Hello - world "
# #find 查找指定字符串中第一次出现的索引位置
# index = s.find("-")
# print(index)
# # count 统计子字符在指定字符串中出现的次数
# c = s.count("-")
# print(c)
# # upper转为大写
# su = s.upper()
# print(su)
# #lower 转为小写
# sl = s.lower()
# print(sl)
# # split 将字符串按指定字符串切割 - 列表
# slist = s.split("-")
# print(slist)
# # strip 去除字符串两边的空格
# ss = s.split()
# print(ss)
# # replace 将字符串中的指定字串替换为新的内容
# sr = s.replace("-", "*")
# print(sr)
# # startswith/endswith判断字符串是否以指定字符串开头/结尾，返回布尔值
# print(sr.startswith("*"))
# print(sr.endswith("*")

# ：
# 格式验证：输入邮箱，验证邮箱是否正确(至少一个.和只有一个@)，如果输入正确，输出“邮箱格式正确”，否则输出“邮箱格式错误”

# 输入邮件
mail = input("请输入你的邮箱：")
#判断是否格式正确
if mail.count("@") == 1 and mail.count(".") >= 1:
    print("邮件格式输入正确！")
else :
    print("邮件格式输入错误！")
# 方法二：
if mail.count("@") == 1 and "." in mail:
    print("邮件格式输入正确！")
else:
    print("邮件格式输入错误！")
# 如何判断指定的字符串是否出现在字符串中
# in运算符  返回bool



# 字符串的基本操作
# 成员运算：
# x in s
# x not in s


# 连接运算
# s + t  实现字符串的拼接
# s * t  实现字符串的重复
# 注意：字符串的连接和重复会生成新的字符串对象，原有的字符串对象保持不变

#切片操作
# s[i]       s[i] 访问字符串中索引为i的字符，索引从0开始，负数索引从-1开始
# s[i:j]     s[i:j] 访问字符串中索引从i到j-1的字符，左闭右开区间
# s[i:j:k]   s[i:j:k] 访问字符串中索引从i到j-1的字符，步长为k


# 字串的常用方法
#