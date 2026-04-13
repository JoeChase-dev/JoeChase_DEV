#赋值运算符
#  =  +=  -= *= /= //= %= **=
num = 2
num += 2  #num = num + 2

#比较运算符
# ==  ！+   >  <   >=  <=  成立True  不成立False

#逻辑运算符  用于连接多个条件，并返回布尔值
#and  同时成立，True    or  一个成立
# not   取反操作
num = int(input("请输入一个整数："))
print(f"{num}在10到20之间：", 10 <= num <= 20)
print(f"{num}不在在10到20之间：", num <= 20 or  num >= 20)