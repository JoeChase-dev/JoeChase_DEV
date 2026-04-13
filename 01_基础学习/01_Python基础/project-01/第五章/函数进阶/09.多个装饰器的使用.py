def func_out01(func01):  # 3 func01  ---> my_test 原始
    print("this is func_out01 being showed")
    def func_in01():
        print("this is func_in01 being showed")    # 9
        func01()         #  10 func01()  ---> my_test() 原始
    return func_in01     # 4 my_test = func_out01(my_test)  ---> my_test = func_in01
def func_out02(func02):  # 7 func02  ---> my_test ---->func_in01
    print("this is func_out02 being showed")
    def func_in02():
        print("this is func_in02 being showed")
        func02()         # func02  ---> my_test ---->func_in01
    return func_in02     # 8 my_test = func_out02(my_test)  ---> my_test = func_in02

@func_out02  # 1 装饰器在下一行没找到函数，继续往下找，等待装饰链完成
@func_out01  # 2 找到函数 my_test，进行装饰，my_test = func_out01(my_test)
             # my_test ----> func_in01()
             # 5 func_out02 在01装饰完成后，继续装饰my_test，my_test = func_out02(my_test)  ---> 6 my_test = func_out02(func_in01)
def my_test():
    print("this is my_test being showed")  # 11

my_test()