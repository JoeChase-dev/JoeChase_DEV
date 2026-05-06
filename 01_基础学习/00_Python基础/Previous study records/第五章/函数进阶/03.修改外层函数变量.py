# 闭包
# 1 在函数嵌套（函数里面定义函数）的情况下，
# 2 内层函数引用了外层函数的变量，
# 3 并且外层函数的返回值是内层函数的情况。
def func_out(data):
    # 函数里面定义函数
    num1 = 100
    print("num1的值为：",num1)

    def func_in():
        # 这个num1是内层函数的局部变量
        # 就近原则
        nonlocal num1  # 修改外层函数的num1变量，不把他变成全局变量global
        num1 = 1000
        # 内层函数引用了外层函数的变量
        print("num1在内层的值为：",num1)
    # 外层函数的返回值是内层函数地址
    func_in()# 执行内层函数，num1的值被修改为1000
    print("num1在内层修改后的值为：",num1) # 输出外层函数的num1值，1000
    return func_in
func = func_out(10)#  先执行   =右边
func()