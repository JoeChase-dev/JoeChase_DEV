class Func:
    """
    __init__ 方法
    构造函数，接收被装饰的函数 fn
    将函数保存为私有属性 self.__fn
    """

    def __init__(self,fn):
    # fn-->用来保存原始的被装饰的函数
        self.__fn = fn

    """
    _call__ 方法
    这是 Python 的魔术方法
    当一个类实现了 __call__ 方法，这个类的实例就可以像函数一样被调用
    语法：对象名() 实际上就是调用 __call__ 方法
    """
    # 让我们的对象（）就可以直接调用这个call方法

    def __call__(self):
        print("验证")
        # 调用原始被装饰的函数
        self.__fn()

# f = Func(1)
# f()
@Func  # my_test = Func(my_test)   类（）创建对象，my_test成为对象
def my_test():
    print("登录")
my_test()