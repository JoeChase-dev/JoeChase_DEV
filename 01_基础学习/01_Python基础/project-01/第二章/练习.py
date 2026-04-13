# 案例一
base =20.7
incr =50
print("未来第一个月的播放总量为",base + incr)
print("未来第二个月的播放总量为",base + incr+incr)

# 升级
base,incr = 20.7,50

#实现变量值交换
a = 10
b = 20

temp = a
a = b
b = temp
print(a,b,temp)

#练习  a b c 的值进行交换，分别赋给c a b
a = 100
b = 200
c = 300
temp1 = c
c = a
temp2 = b
b = temp1
a = temp2
print(a,b,c)




