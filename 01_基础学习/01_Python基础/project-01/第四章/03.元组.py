# 元组  不可变的序列，类似列表，但创建后不可修改
# 特点： 可以存储不同类型的元素
#       元素可以重复，有序，不可修改（支持索引访问、切片）
# 存储一次性数据的容器，执行效率高


# 定义为
# 元组名称 = （元素...）
# 定义空元组
# 元组名称 = ()/tuple()

# 常用方法
# count() :统计元素在元组中出现的次数
# index() :查找某个元素在元组中的索引位置

# 元组基本操作  tuple

# 定义
s = (20,14,35,23,50,76,50,23)
print(s)

# 索引访问
print(s[2])
print(s[-1])

# 切片
print(s[1:5:2])
print(s[::-1])

# count
# index
print(s.count(50))
print(s.index(20))

# 注意点：定义单元素的元组，单个元素后加  ，
t = ()
s = (13,)
print(f"类型为{type(s)},{type(t)}")
print(s)


# 组包与解包
# 组包：多个值合并到一个容器内
# 解包：将容器解开成独立元素，分别赋值给多个变量

# 定义元组
t1 = (2,4,6,8)  # t1 = 2,4,6,8   也行

#基础解包       (一对一)
a,b,c,d = t1
print(a,b,c,d)

#扩展解包
e,*f,g = t1
h,*i = t1
*j,k = t1
print(e,f,g)
print(h,i)
print(j,k)
# 说明：元组解包时，*表示收集剩余所有元素，允许处理不确定元素（生成列表）

"""
案例一：两个变量，进行值交换
案例三：三个变量，a,b,c,赋给c,a,b
"""
a,b = 12,56
a,b = b,a
print(a,b)

c,e,f = 1,2,3
c,e,f =e,f,c
print(c)
print(e)
print(f)



"""
1 计算每个学生的总份、各科平均分，然后一并输出出来
2 统计各科成绩的最低分、最高分、平均分，并输出
3 查找成绩优秀（平均分大于90）的学生，并输出
"""
# 1 计算每个学生的总份、各科平均分，然后一并输出出来
students =(
    ("S001","王林",85,92,78),
    ("S002","李沐婉",92,88,95),
    ("S003","十三",78,85,82),
    ("S004","曾牛",88,79,91),
    ("S005","周铁",95,96,89),
)
print("学号 \t\t姓名 \t\t平均分 \t\t")
#方式一
# for i in students:
#     total = i[2] + i[3] +i[4]
#     avg = total / 3
#     print(f"{i[0]} \t\t{i[1]} \t\t{avg:.1f}")
# 方式二--->元组解包  先是students中一个元素（元组）抽出，再进行元组中元组的解包
for num,name,chinese,math,english in students:
    total = chinese + math + english
    avg = total / 3
    print(f"{num} \t\t{name} \t\t{avg:.1f}")

print()
# 2 统计各科成绩的最低分、最高分、平均分，并输出
chinese_scores = [i[2] for i in students]
math_scores = [i[3] for i in students]
english_scores = [i[4] for i in students]
print(f"语文最低分为{min(chinese_scores)}，最高分为{max(chinese_scores)},平均分为{sum(chinese_scores)/len(chinese_scores)}")
print(f"数学最低分为{min(math_scores)}，最高分为{max(math_scores)},平均分为{sum(math_scores)/len(math_scores)}")
print(f"英语最低分为{min(english_scores)}，最高分为{max(english_scores)},平均分为{sum(english_scores)/len(english_scores)}")
print()

# 3 查找成绩优秀（平均分大于90）的学生，并输出
for num,name,chinese,math,english in students:
    total = chinese + math + english
    avg = total / 3
    if avg > 90:
        print(f"优秀学生有：{num} \t\t{name} \t\t{avg:.1f}")
