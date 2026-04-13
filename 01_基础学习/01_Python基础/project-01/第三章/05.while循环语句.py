# while 循环语句
# 格式
# while 条件表达式：
#     循环语句1
#     循环语句2
#     ...
# i = 0
# while i < 10:
#     print("人生苦短，我用Python")
#     i += 1
# else :  #可选
#     print("循环正常结果")

# 表达式为bool值
# 空格缩进表示层级
# 终止条件

# 计算1 - 100 之间所有偶数的和
total = 0
i = 1
while i <= 100:
    if i % 2 == 0:#偶数
        total += i
    i += 1
print(f"累加之和为{total}")