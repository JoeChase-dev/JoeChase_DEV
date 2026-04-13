# type()查看类型
# 查看字面量或变量的类型

#isinstance(数据，类型) 输出bool值
#用于判定类型是否正确
print(type("Hello"))
print(type(10))
print(type(1.33))
print(type(None))#NoneType
print(type(True))

num=10
print(type(num))

print(isinstance(num,int))
print(isinstance(num,float))