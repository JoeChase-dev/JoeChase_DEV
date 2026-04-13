"""
文件的读取
read([size])  返回指定size大小的内容，如不指定则返回整个文件
readline() 返回一行数据
readlines([size])  返回指定 size 行数，如不指定size，则返回全部文件
for line in file  迭代文件的每一行  # 常用
"""
f  = open('demo_file.txt', mode='r', encoding='UTF-8')
for data in f:
    print(data)
f.close()



"""
文件的写入
mode = "r" 报错
mode = "w" 或 "w+" 清空文件，写入内容，返回写入字符数量
mode = "a" 或 mode = "a+" 在文件结尾追加
a/w+  实现读取和写入

write() 实现写入
seek()函数控制写入位置
close()  关闭文件,必须存在关闭
"""
f  = open('demo_file.txt', mode='a', encoding='UTF-8')
f.write('\nhello python')
f.close()

