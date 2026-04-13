"""
数字类型  int float complex
文本类型  str
序列类型  list tuple range
映射类型  dict
"""
"""
映射是可变类型
只有一种数据类型，即：字典
一个元素由 键 和 值 两部分组成
键不能重复，无法哈希的类型，列表，字典不能作为键来使用
1和1.0被认为相同的键
"""
# 1 {1:1,1.0:2}                       花括号定义
# 2 dict(one = 1,two = 2)             类型构造器
# 3 {x:x**2 for x in range(1,11)}     字典推导式


# 访问tom
mail_list = {"tom":"tom@163.com","jerry":"jerry@163.com"}
mail_list["tom"]
mail_list.get("tom")


mail_list.keys()     # 键
mail_list.values()   # 值
mail_list.items()    # 访问所有项

# 遍历   结合解包
for key,value in mail_list.items():
    print(key)
    print(value)

# 修改字典的内容
mail_list["wilson"] = 'wilson@163.com'  # 增加新的键值对
# 若已存在键：‘wilson’，则修改对应的值


"""
# 返回字典的项数
len(dict)
# 判断键是否在字典内
x in dict
# 如果键存在且在字典内，移除该键，返回该键对应的值
dict.pop(key)
# 返回键值对
dict.popitem()  没有参数，移除最后一个
"""


# 字典高级用法  setdefault()
tom_mail = mail_list.setdefault('tom')
# setdefault 好处  如果键重复，返回键的现有值，避免值被覆盖
# tom_mail = mail_list.setdefault('tom2')
# 输出 None 空类型
print(tom_mail)
print(mail_list)

tom_mail = mail_list.setdefault('tom2',"tom2@163.com")

print(tom_mail)
print(mail_list)

# |=   用新字典的键和值  更新  旧的字典，新字典的优先
# mail_list |= new_mail_list

# 数据类型转换  zip()  将两个列表合并为一个字典
# 字典 = dict（zip（列表1，列表2））

"""
列表属于可变序列
元组、字符串属于不可变序列  append() pop() insert()等内置函数无法使用
"""


"""
习题
字典的数据类型用于存储通讯录，包含姓名，可以为空的备注名，一个邮箱，至少两个手机号码，尝试添加和删除联系人
"""


"""
数据处理的思路
1 汇总体现更多价值
2 大部分数据无法直接处理
3 数据需要去除噪声
4 数据需要从非结构化转化为半结构化或者结构化数据
"""

# 统计一种类型数据，如非空行，可以使用集合去除空行重复，再使用计数器统计，最终-1实现
# 集合可以自动去重复，用于避免重复元素最便捷
# 元组不可变，利用元组可以避免误修改

"""
常见数据类型
常量   ：None
逻辑值  :True False
空集   :""、() [] set() range(0)
数字   :int float
序列   :list tuple range
文本序列:str
集合   :set
映射   :dict
"""

"""
str.count(sub[,start[,end])
str --> 对象
count --> 对象的方法
sub -->参数（必选）
[start] --> 参数（可选）
"""


# 迭代时数量计算，引入枚举函数enumerate（），将对象转换为元组，再解包快速提取元素编号
"""
for i in enumerate(movie1.items())
    print(i)
(0,('name','friends'))
"""

"""
for循环实现推导式   列表 字典 元组 集合
推导式格式
  表达式 for 变量 in 序列
  表达式 for 变量 in 序列 if条件
"""


# 嵌套超过3层就应考虑开发需求层面拆分，避免3层以上


"""
遍历中修改列表导致误操作
数据遗漏
list1 = ['a','b','c','d']

for i in range(len(list1)):
    list1.pop(i)

列表在执行pop()之后，长度会减少，因此不能使用固定长度的for 循环遍历
"""


"""
交互式：
    input
非交互式：
    命令行/文件,自动处理
    
    

"""

"""
实现参数处理的两个函数库
argparse--用户友好的命令行选项解析器
getopt--C风格命令行选项解析器

编写命令行参数的一般逻辑
import argparse
parser = argparse.ArgumentParser(description = "这个程序的用途")
parser.add_argument(要添加的参数和参数描述)  可以强制转换参数类型和设置默认值 
args = parser.parse_args()

*args 用于接收参数并进行处理
*执行方式  python3 文件名.py 参数
"""



"""
三种格式化输出方式
1 % 与C++一致
2 format()函数   
3 f-strings   : f"{   } " 可以实现数字计算、字符串相连、函数执行等计算任务
                嵌入的内容可解释执行
    宽度和精度调整 ： f"{对象：宽度.精度类型}"
"""
number = 123.456
print(f"{number:10}")
# '   123.456'

print(f"{number:010}")
# '0000123.456'

print(f"{number:4f}")
# '123.4560000' 指定类型后，默认保存小数点后6位