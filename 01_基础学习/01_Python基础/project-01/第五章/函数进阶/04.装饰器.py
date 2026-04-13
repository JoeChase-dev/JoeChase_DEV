# 装饰器  在不修改原有的代码的前提下 给函数增加新的功能
def func_out(func):
    def func_in():
        print("验证")
        func()
    return func_in
@func_out # login = func_out(login)
        #   先执行 = 右边  func_out(login) -->将login的函数地址 传给func  func_in 添加func（也就是login函数地址中的语句）
        #   后执行 = 左边  login = func_in 将func_in的函数地址 传给login
def login():
    print("登录")
        # 此时login函数的地址指向func_in函数，执行login() --> func_in() --> 输出验证和登录
login()
# 结论： 1 调用login（）就相当于---> func_in()
#     调用被装饰的函数   就相当于     调用装饰器函数的内层函数
# 结论： 2 外层函数的参数func ---> 原始的要添加的 login
