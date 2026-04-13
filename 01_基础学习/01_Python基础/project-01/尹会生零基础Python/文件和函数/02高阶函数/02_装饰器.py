"""
变量的作用域
LEGB规则
Local  本地变量     最优先  1函数内部的变量
Enclosed  闭包变量          2
Global  全局变量            3外部变量
Builtin  内置变量           4import导入库
"""

"""
闭包
函数内的再次定义的内部函数形成闭包
闭包作用域之内，内部函数可以访问外部函数的变量
"""
# 闭包
# 1 在函数嵌套（函数里面定义函数）的情况下，
# 2 内层函数引用了外层函数的变量，
# 3 并且外层函数的返回值是内层函数的情况。
"""
def func_out():
    value =1
    def func_in():
        return value
    return func_in
f = func_out()
print(f())
"""


"""
装饰器语法
@实现函数嵌套定义
"""

#from functools import wraps
import time
def func_out(func):  # func 为被装饰的函数
    #@wraps(func)
    def func_in():
        start = time.time()
        func()
        end = time.time()
        print(f"函数一共执行了{int(end-start)}秒")
    return func_in

@func_out
def work():
    print("开始")
    time.sleep(2)
    print("结束")

work()    # 已经变为内部函数

"""
python自带的装饰器使用functools
常用的有：
@lrucache# 缓存
@wraps # 被装饰的函数保持原对象不变 保留原名
"""