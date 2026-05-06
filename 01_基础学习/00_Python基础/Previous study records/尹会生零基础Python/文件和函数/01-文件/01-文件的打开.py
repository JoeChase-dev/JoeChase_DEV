"""
文件的打开
类unix 系统操作：一切皆文件
文件的基本操作：打开、关闭、读取、写入
"""
 #open()    # 文件打开第一步
            # 第一个参数为打开的文件名称
# 案例
# open(file,mode="r",buffering=-1,encoding=None,errors=None,
# newline=None,closefd=True,opener=None)

help(open)  # 获取open信息

file_handler = open("/tmp/afile")
# 编码 encoding = utf-8
# 没有报错，则文件打开成功
# 避免误操作，默认只读方式打开文件

# 文件路径处理
import os
os.chdir("/tmp")  # change directory缩写
file_handler = open("afile")

# 常见的mode 参数值
"r"  # 默认值，只读方式打开文件
"w"  # 写入方式并覆盖文件
"a"  # 末尾追加方式打开文件
"b"  # 二进制方式打开文件
"+"  # 支持读取与写入