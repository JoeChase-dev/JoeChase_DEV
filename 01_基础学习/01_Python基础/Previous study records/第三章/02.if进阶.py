#if...else 结构
#if 条件：
#    成立，进行操作
#else ：
# 案例  登录B站  账号 18888888888  密码 666888
# ok_account = "18888888888"
# ok_password = "666888"
#
# #接收账户和密码
# account = input("请输入您的B站账户：")
# password = input("请输入您的B站密码：")
#
# #判断账户和密码是否全部正确
# if account==ok_account and password == ok_password:
#     print("登录成功！")
#     print("进入B站首页")
# else :
#     print("登陆失败！")
#     print("账户或密码错误！")


# 案例  闰年判断
year = int(input("请输入判定的年份："))
if year % 100 != 0 and year % 4 ==0 or year % 400 == 0:
    print(f"{year}是闰年")
else :
    print(f"{year}不是闰年")