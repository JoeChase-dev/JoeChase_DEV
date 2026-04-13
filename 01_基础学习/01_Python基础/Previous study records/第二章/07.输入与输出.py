#输入 input  s = input(提示信息)  （键盘录入数据为字符串类型）
#输出 print  print(数据)
#在字符串中插入变量的方法  使用f-string：f"字符串{变量}字符串"


name = input("请输入你的名字：")
age =input("请输入你的年龄：")
print(f"你的名字为{name}，你的年龄为{age}岁")

# 案例
# ATM机取款，本金10000
#1 定义本金
total = 10000
#2 输入密码
password = input("请输入您的密码：")
print("密码正确")
num = input("请输入取款金额：")
#3 输入取款金额并输出
print(f"您的剩余余额为{total-int(num)}")  #num使用input后为字符型，使用int()实现类型转换
