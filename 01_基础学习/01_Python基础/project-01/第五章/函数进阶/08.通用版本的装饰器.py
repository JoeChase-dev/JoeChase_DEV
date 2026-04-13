# 结论： 1 调用login（）就相当于---> func_in()
#     调用被装饰的函数   就相当于     调用装饰器函数的内层函数
# 结论： 2 外层函数的参数func ---> 原始的要添加的 login
# 底层代码查看   ctrl + 鼠标左键点击
# 通用装饰器
def func_out(func):
    def func_in(*args,**kwargs):
        # 如果函数中没有返回值，则返回None
        ret = func(*args,**kwargs)
        return ret
    return func_in


@func_out
def my_test(*args,**kwargs):
    print(args)
    print(kwargs)
    return 100
ret = my_test(10,20,age=18)
print(ret)


