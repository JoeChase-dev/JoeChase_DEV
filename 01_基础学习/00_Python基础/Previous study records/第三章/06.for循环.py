# while  条件控制
# for    循环遍历
# for 元素 in 待处理数据集:
#     循环体代码
# else:
#     循环结束时，执行的代码


# msg = input("请输入需要遍历的字符：")
# for i in msg:
#     print(i)
# else :
#     print("循环结束！")


# 案例
# 1-100奇数之和
# 100-500的3的倍数之和
# range 用法：
# 1 range(end)  从1开始到end前一个数
# 2 range(start,end)
# 3 range(start,end,step)  step(步长)
# total1 = 0
# for i in range(1,101):   # for j in range(i,101,2)
#     if i % 2 == 1:
#         total1 += i
# else :
#     print("循环1结束")
# print(f"奇数和为{total1}")
#
# total2 = 0
# for i in range(100,501):
#     if i % 3 == 0 :
#         total2 += i
# else :
#     print("循环2结束")
# print(f"奇数和为{total2}")

# 嵌套循环
#  先聚焦内层循环
# for 元素 in 数据集1：
#     语句
#     for 元素 in 数据组2
#         语句
# m = int(input("请输入长度："))
# n = int(input("请输入宽度："))
# for j in range(n):
#     for i in range(m):
#         print("*",end="")  #  end="" 以空字符串结束
#     print()  #print自带换行效果，默认end=“\n”

# 案例，打印九九乘法表
for i in range(1,10):
    for j in range(1,i+1):
        print(f"{i} X {j} = {i*j}",end="\t")
    print()

