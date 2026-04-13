"""
为什么要及时关闭文件：
写入函数执行完成后，写入部分仍然在内存中
内存是易失存储，突然断电会导致数据丢失
close()可以告知内核文件在内存中更新
"""

"""
close()
write()函数写入后，必须显示close()
read族函数读取后，不必close()但建议关闭，避免文件描述符耗尽
open失败，不必close
"""

# """
# with 语句
# with 语句可以使打开和关闭文件保持一致性，即：
# 使用with 语句打开的文件，离开 with语句块作用域会自动关闭
#
# with open(文件) as 文件描述符
#     文件读写操作
# with 语句块结束，自动关闭文件
# """

# f  = open('./demo_file.txt',mode='r',encoding='UTF-8')
# data = f.read()
# print(data)
# f.close()


with open('demo_file.txt', mode='r', encoding='UTF-8') as f:
    data = f.read()

print(data)  # 离开with语句块，自动关闭文件

"""
使用with 语句可以使文件打开和关闭保持一致性
"""

