"""
常见操作系统的文件编码
windows  GBK默认
linux macOS  UTF-8
"""

# 以不同的编码打开文件
# open(filename,encoding="utf-8")
# open(filename,encoding="gbk")
f = open('demo_file.txt', mode='w', encoding='UTF-8')
f.write('hello world')
f.close()
f = open('demo_file.txt', mode='r', encoding='UTF-8')
data = f.readline()
print(data)
f.close()


"""
总结
以不正确的编码打开文件会产生乱码
通过encoding参数能够以制定的编码打开文件
"""