# 函数对象与函数调用的用法区别
# 函数对象：函数名本身是一个对象，对象名 = 函数名
# 函数调用：函数名()
"""
高阶函数
高阶函数通常指的是 map、filter、reduce
map、filter、是内置函数，可以直接使用
reduce需要通过fuctools库导入
"""

"""
map(函数，可迭代对象)
-函数：函数对象、lambda表达式
-可迭代对象：列表、元组、range等
-将可迭代对象的每个元素作为函数参数执行

"""
def add(x):
    return x+x
for i in map (add,range(5)):
    print(i)


print(list(map(lambda x:x+x,range(5))))

"""
filter(函数，可迭代对象)
-过滤掉可迭代对象中返回值不为True的元素
-filter函数返回一个可迭代对象
"""

for i in filter(lambda x:x>0,(-1,0,-2,4)):
    print(i)

"""
reduce(函数，可迭代对象)
-对可迭代对象进行累积
"""
from functools import reduce
data = reduce(lambda x,y:x+y,[1,2,3,4,5])
print(data)

"""
偏函数：固定某个参数，形成新的函数
from functools import partial
new_func = partial(旧的函数对象，被固定的参数)
new_func(参数)
"""

int("0f",base = 16)
from functools import partial
int_16 = partial(int,base = 16)
print(int_16("0f"))