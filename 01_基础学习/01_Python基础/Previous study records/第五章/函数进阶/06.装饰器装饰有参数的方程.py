# 结论： 1 调用login（）就相当于---> func_in()
#     调用被装饰的函数   就相当于     调用装饰器函数的内层函数
# 结论： 2 外层函数的参数func ---> 原始的要添加的 login
def func_out(func):
    def func_in(*args,**kwargs):        # 添加参数a,
        func(*args,**kwargs)            # func(a) ---> 相当于原始的 my_test(a)
    return func_in

@func_out                               # my_test = func_out(my_test)
def my_test(*args,**kwargs):
    print(args)
    print(kwargs)

# 相当于----> func 变为原有 my_test 的 func_in(10)
my_test(10,20,age=18)