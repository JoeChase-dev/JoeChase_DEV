# if...elif...else 实现多条件判断 elif可写多个
# if 条件1：
#     成立，操作1
# elif 条件2：
#     成立，操作2
# else:
#     操作3


# num = float(input("请输入数字："))
# if num > 0:
#     print(f"{num}是一个正数")
# elif num == 0:
#     print(f"{num}为零")
# else :
#     print(f"{num}为负数")


# 案例
username = input("请输入用户名：")
password = input("请输入密码：")
if username == "admin" and password == "666888":
    print("登录成功1！")
elif username == "root" and password == "574527":
    print("登录成功2！")
elif username == "张三" and password == "123456":
    print("登录成功3！")
else :
    print("登陆失败！")