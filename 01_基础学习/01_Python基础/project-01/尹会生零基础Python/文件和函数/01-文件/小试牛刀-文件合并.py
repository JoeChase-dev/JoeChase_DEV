"""
合并文件需求分析
合并文件 = 读取原始文件 + 追加写入新的文件
关键任务：
1.以可读取的模式打开原始文件
2.以写入的模式创建并打开要合并的文件
3.正确关闭文件
"""
# 合并多个文件
files_name = ["demo_file.txt","demo_file02"]
files_data = []
for f_name in files_name:
    with open(f_name,mode='r') as f:
        files_data.append(f.read())
with open("demo3", mode='w') as f:
    for data in files_data:
        f.write(data)