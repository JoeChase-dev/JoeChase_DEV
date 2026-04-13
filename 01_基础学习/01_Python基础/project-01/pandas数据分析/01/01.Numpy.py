"""
就地采用，避免隐式拷贝  x*=2  而不是y=x*2
"""

"""
Numpy中两个重要对象
ndarray   解决多维数组问题
ufunc 解决对数组进行处理的函数
"""

"""
ndarray 对象
多维数组的含义。 维数称为 秩（rank），一维数组秩为1 ，
                        在numpy中，每一个线性的数组成为一个轴（axes），用秩来描述轴的数量
"""
# 创建数组
import numpy as np
a= np.array([1,2,3])
b= np.array([[1,2,3],
             [4,5,6],
             [7,8,9]])
b[1,1] = 10
print (a.shape)   # shape属性获得数组大小，dtype获得元素的属性
print (b.shape)
print (a.dtype)
print (b)

# 结构数组
import numpy as np
# dtype 定义结构类型
persontype = np.dtype({'names':['name','age','chinese','math','english'],
                       'formats':['S32','i','i','i','f']})
peoples = np.array([("zhangfei",32,75,100,90),
                    ("guangyu",24,85,96,88.5),
                    ("zhaoyun",28,90,100,100)],
                   dtype=persontype)
ages = peoples[:]['age']
chineses =peoples[:]['chinese']
maths = peoples[:]['math']
englishs = peoples[:]['english']
print(np.mean(ages))
print(np.mean(chineses))
print(np.mean(maths))
print(np.mean(englishs))

"""
nfunc运算
能够对数组中每个元素进行函数操作
"""

"""
连续数组的创建
arange
linspace
arange类似range  初始值、终值、步长创建，不包括终值
linspace 线性等分向量，初始值、终值、元素个数创建，包括终值
"""
x1 = np.arange(1,11,2)
x2 = np.linspace(1,9,5)
print(x1)
print(x2)

"""
算数运算
可以自由创建等差数组，也可以进行加、减、乘、除、求n次方和取余数
"""
x1 = np.arange(1,11,2)
x2 = np.linspace(1,9,5)
print(np.add(x1,x2))
print(np.subtract(x1,x2))
print(np.multiply(x1,x2))
print(np.divide(x1,x2))
print(np.power(x1,x2))
print(np.remainder(x1,x2))  # 或 np.mod(x1,x2) 结果一样

"""
统计函数
最大值，最小值，平均值，是否符合正态分布，方差、标准差为多少等等
"""
# 最大值和最小值 amax(),amin()
a = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(np.amin(a))
print(np.amin(a,0)) # 沿着axis=0轴
print(np.amin(a,1)) # 沿着axis=1轴

print(np.amax(a))
print(np.amax(a,0))
print(np.amax(a,1))
# 最大值与最小值只差 ptp()
print(np.ptp(a))
print(np.ptp(a,0))
print(np.ptp(a,1))
# 数组的百分位值 percentile()
# 表示第p个百分位数 p=0最小值 p=100最大值 p=50平均值 p=75第75百分位数
print(np.percentile(a,50))
print(np.percentile(a,50,0))
print(np.percentile(a,50,1))
# 数组中的中位数 median() 平均数 mean()
# 中位数
print(np.median(a))
print(np.median(a,0))
print(np.median(a,1))
# 平均数
print(np.mean(a))
print(np.mean(a,0))
print(np.mean(a,1))

# 加权平均值
a = np.array([1,2,3,4])
wts = np.array([1,2,3,4])
print(np.average(a))           # (1+2+3+4)/4   权重为1
print(np.average(a,weights=wts))  # (1*1+2*2+3*3+4*4)/(1+2+3+4) 权重为wts

# 标准差 std()，方差 var()
print(np.std(a))    # 方差算数平方根，称为标准差
print(np.var(a))    # 个数值与平均值之差的平方求和的平均值，称为方差  mean((x-mean(x))**2)

"""
Numpy排序
sort函数 sort(a,axis = -1, kind = 'quicksort'(mergesort\heapsort,快速、合并和堆排序),order = 'None')
"""
a =np.array([[4,3,2],[2,4,1]])
print(np.sort(a))
print(np.sort(a,axis=0))
print(np.sort(a,axis=1))
print(np.sort(a,axis=None))


"""
总结：
排序：
    快速排序
    合并排序
    堆排序
定义数组：
    创建数组
    结构数组
运算：
    算数运算
    统计运算
高效使用Numpy
    为什么使用
    本地操作&隐式拷贝
"""