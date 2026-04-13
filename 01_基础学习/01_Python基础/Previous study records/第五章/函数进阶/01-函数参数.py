# 函数名存放的是函数所在地址
def func():
    print("func")

print(func)  # 直接打印函数名，输出函数所在地址
# 去到函数所在空间执行对应代码
func()  #加括号调用函数，输出函数内的代码

# func作为形参名，与上文func函数名没有任何关系,只在my_test函数内有效
# func作为形参接收一个函数地址
def my_test(func):
    # 相当于  地址（）  -->调用该地址对应的函数
    func()
# 传递func函数名所在地址
my_test(func)
