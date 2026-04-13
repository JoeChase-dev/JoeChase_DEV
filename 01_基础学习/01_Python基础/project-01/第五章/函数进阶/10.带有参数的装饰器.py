# 在原装饰器的基础上，添加参数
# 只需要再套一层外函数，并返回原装饰器
def logging(s):
    def func_out(func):
        def func_in(a):
            if s == "参数":
                print("参数判断成功")
            else :
                print("参数判断失败")
            func(a)
        return func_in
    return func_out

@logging("canshu")  # 传参
# 1 执行logging（10），获取返回值func_out
# 2 @func_out
# 3 执行func_out(my_test)，my_test=func_out(my_test)
def my_test(a):
    print(a)
my_test(10)
