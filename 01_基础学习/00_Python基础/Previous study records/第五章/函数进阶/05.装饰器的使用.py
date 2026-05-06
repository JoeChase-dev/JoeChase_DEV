import time
def func_out(func):
    def func_in():
        start = time.time()
        func()
        end = time.time()
        take_time = end - start
        print("函数执行时间：",take_time)
    return func_in
# 被装饰的函数
@func_out   # 装饰器语法糖
            #相当于加工流水线，将函数送进func_out后，产生带需要的新功能的函数time_test，
def time_test():
    for i in range(0,100000):
        print(i)
time_test()