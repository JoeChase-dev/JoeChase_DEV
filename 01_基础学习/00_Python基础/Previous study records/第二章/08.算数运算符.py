#+   -   *（乘法）   /（除法，结果为小数）  //（整除）   %（取余）   **（幂指数）
print("10 + 4 =",10 + 4)
print("10 - 4 =",10 - 4)
print("10 * 4 =",10 * 4)
print("10 / 4 =",10 / 4)
print("10 // 4 =",10 // 4)
print("10 % 4 =",10 % 4)
print("10 ** 4 = " ,10 ** 4)

#运算符的优先级 -->    ** --> * // / % --> + —
print("0.1 + 10 / 4**2 =",0.1 + 10 / 4**2)

# 案例一
#0.099999999999998 精度损失：浮点数运算时，因二进制（不能表示所有小数）会损失精度
x= float(input("请输入x的值："))
y = float(input("请输入y的值："))
print("x+y=",x+y)
print("x-y=",x-y)

#案例二  计算输入的三个整数的平均值
x = int(input("请输入x的值："))
y = int(input("请输入y的值："))
z = int(input("请输入z的值："))
print("x y z 的平均值为：",(x+y+z)/3)
#案例三 输入梯形的上下底高，计算梯形的面积
up = float(input("请输入上底的值："))
low = float(input("请输入下底的值："))
high = float(input("请输入高的值："))
print("梯形的面积为：",(up+low)*high/2)
#案例四 输入圆的半径，然后计算圆的周长和面积
pai = 3.14
r = float(input("请输入半径r的值："))
print ("圆的周长为：",2*pai*r)
print ("圆的面积为：",pai*r**2)
#案例五 生体质量指数BMI的计算（BMI=体重（kg）/身高（m）**2）
high = float(input("请输入体重（kg）："))
weight = float(input("请输入身高（m）："))
print("您的身体质量指标BMI为：",high/weight**2)



# 常见运算
# abs(x)  绝对值
# int(x)  强制转换成整数
# float(x)  强制转换成浮点数
# complex(re,im)  强制转换成复数
# c.conjugate     获取复数的共轭
# divmod(x,y)     返回商和余数的元组
# pow(x,y)        x的y次方
# x**y             x的y次方