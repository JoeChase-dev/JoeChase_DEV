"""
定义一个类：
class Coffee(object):
class 定义类的关键字
Coffee 类的名称，一般首字母大写
object 父类，可不写默认继承自object
还可以使用type()函数创建类，动态创建类
"""

"""
类的实例化
mocha = Coffee()
mocha 类Coffee实例化的对象
"""



#类的方法
class Coffee(object):
    water = 0
    milk = 0
    def add_water(self): #self表示当前对象，第一个参数必须使用 self
        self.water = 10
mocha = Coffee()
print(mocha.water)

#self 举例
"""
# 创建两个对象
dog1 = Dog("旺财")    # self = dog1
dog2 = Dog("来福")    # self = dog2

dog1.bark()           # 旺财: 汪汪！
dog2.bark()           # 来福: 汪汪！
"""

"""
总结：
类的实例化可以创建一个该类的对象
对象拥有类的属性和方法
要根据上下文区分类的实例化和函数的调用
"""