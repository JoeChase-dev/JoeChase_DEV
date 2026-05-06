# num = int(input("请输入一个整数："))
# if num % 2 ==0:
#     print(f"{num}是偶数。")
# else:
#    print(f"{num}是奇数。")
#
#
# age = int(input("请输入你的年龄："))
# if age >= 18:
#     print("您已成年！")
# else :
#     print("您未成年！")
#
#
# num1 = (float(input("请输入一个非零数：")))
# if num1 > 0 :
#     print(f"{num1}为整数。")
# else :
#     print(f"{num1}为负数。")
#
#
# score = float(input("请输入你的成绩："))
# if score >= 60:
#     print("你的考试及格了！")
# else :
#     print("你的考试未及格！")



# score = float(input("请输入你的成绩："))
# if score >= 85:
#     print("你的成绩为优秀！")
# elif score >= 60 and score <= 85:
#     print("你的成绩为及格！")
# else :
#     print("你的成绩为不及格！")



# cost = float(input("请输入总金额："))
# if cost >= 500:
#     print("折扣为八折,实付金额为：",cost*0.8)
# elif 500 > cost >= 300 :
#     print("折扣为九折,实付金额为：",cost*0.9)
# elif 100 <= cost < 300 :
#     print("折扣为九五折,实付金额为：", cost *0.95)
# else :
#     print("无折扣！")
"""
案例
三角形类型判断：等腰 等边 普通
"""
# #1 接受三角形边长
# a = int(input("请输入第一个边的边长："))
# b = int(input("请输入第二个边的边长："))
# c = int(input("请输入第三个边的边长："))
#
# # 2判断能否构成三角形
# if a+b>c and a + c > b and c + b > a:
#     if a == b and b == c and c == a:
#         print("可以构成等边三角形。")
#     elif a == b or b == c or c ==a :
#         print("可以构成等腰三角形。")
#     else :
#         print("可以构成普通三角形。")
# else:
#      print(f"{a},{b},{c}无法构成一个三角形！")


# # 练习
# total = float(input("请输入用电度数："))
# if total >=2880 :
#     if total >4800:
#         print("电费单价为：0.7883元/度，电费为：",total*0.7883)
#     else :
#         print("电费单价为：0.5383元/度，电费为：",total*0.5383)
# else :
#     print("电费单价为：0.4883元/度，电费为：",total*0.4883)

# 打印数字金字塔
# num = int(input("请输入数字："))
# for i in range(1,num+1):
#     for j in range(1,i+1):
#         print(j,end="\t")
#     print()

# for j in range(1,9):
#     if j %2 == 0:
#         for i in range(1,9):
#             if i%2==1 :
#                 print("1 ",end="")
#             else:
#                 print("0 ",end="")
#         print()
#     else :
#         for i in range(1,9):
#             if i%2==1 :
#                 print("0 ",end="")
#             else:
#                 print("1 ",end="")
#         print()
#
# for a in range(8):
#     for b in range(8):
#         if (a+b)%2==1:  #行与列的关系
#             print("1 ",end="")
#         else :
#             print("0 ",end="")
#     print()


# B站登录进阶
#break 只能够出现在循环中，跳出循环（while后的else语句不会执行
#continue 只能中断本次循环，进入下一次循环
# account = input("Enter your account details:")
# password = input("Enter your password:")
# while True:
#     if account ==" " or password == " ":
#         print("输入结果不能为空！")
#         continue
#     if account == "周中期" and password =="666888":
#         print("输入成功，登录B站！")
#         break
#     else :
#         print("请重新输入！")

# 五次后，不允许再次操作

# num = 0
# while num <=5:
#     account = input("Enter your account details:")
#     password = input("Enter your password:")
#     if account ==" " or password == " ":
#         print("输入结果不能为空！")
#         continue
#     if account == "周中期" and password =="666888":
#         print("输入成功，登录B站！")
#         break
#     else :
#         num+=1
#         print("请重新输入！")
#     if num ==5:
#         print("登录超五次，30min后重试")


#练习 1-1000之间的5的倍数累加
#练习2 统计字符串“adsgkrhsjasdgfkhrdyeags”有多少个a和k
# total = 0
# for i in range(1,1001):
#     if i%5 ==0 :
#         total +=i
# print(total)
#
# msg = "adsgkrhsjasdgfkhrdyeags"
# num1 = 0
# num2 = 0
# for i in msg:
#     match i :
#         case "a" :
#             num1 +=1
#         case "k" :
#             num2 +=1
# print(f"a的数量为{num1}，k的数量为{num2}")