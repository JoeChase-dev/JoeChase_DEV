#if条件判断
# 缩进实现代码的归属
#基本格式
# if 要判断的条件：
#     成立时，执行的操作
# score = int(input("请输入你的高考成绩:"))
# if score >= 680:
#     print("欢迎来到清华！")

# 案例  登录B站  账号 18888888888  密码 666888
ok_account = "18888888888"
ok_password = "666888"

#接收账户和密码
account = input("请输入您的B站账户：")
password = input("请输入您的B站密码：")

#判断账户和密码是否全部正确
if account==ok_account and password == ok_password:
    print("登录成功！")
    print("进入B站首页")
if account != ok_account or password != ok_password:
    print("登陆失败！")
    print("账户或密码错误！")