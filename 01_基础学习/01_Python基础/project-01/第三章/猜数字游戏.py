"""
 1 系统随机生成一个随机数  import random
 2 猜数字
 3 提示
4 猜对 系统自动退出，游戏结束"""


import random
random_num = random.randint(1,100)
while True:
#接收输入数字
    num = int(input("请输入一个数："))

    #判断
    if num > random_num:
        print("你猜的数太大了")
    elif num < random_num:
        print("你的的数小了")
    else :
        print("你输对了,666")
        break#跳出循环

print("随机生成的数字是：",random_num)
