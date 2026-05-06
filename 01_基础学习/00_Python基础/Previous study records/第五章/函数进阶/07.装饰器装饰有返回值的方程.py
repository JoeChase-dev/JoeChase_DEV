# 结论： 1 调用login（）就相当于---> func_in()
#     调用被装饰的函数   就相当于     调用装饰器函数的内层函数
# 结论： 2 外层函数的参数func ---> 原始的要添加的 login
def func_out(func):
    def func_in():
        ret = func()   # ret 接收了被装饰函数  my_test  原始的返回值
        return ret     # func_in() 的返回值 就是 func()  ---->原被修饰函数 my_test 的返回值
    return func_in

@func_out
def my_test():
    return 100    # 这里的返回值将  ----> 给了  func()
a = my_test()     # 接收装饰后的函数 my_test()-----> func_in() 的返回值
print(a)