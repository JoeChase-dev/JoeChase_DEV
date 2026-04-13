# 模式匹配 match...case
# 用一个模板去匹配数据的结构和内容，匹配成功则执行响应操作
# 应用场景：固定值分支判断
# 案例
# 简易计算器的实现
# num1 = float(input("请输入第一个数："))
# num2 = float(input("请输入第二个数："))
# oper = input("请输入运算符（+ - * /）：")
# match oper:
#     case "+":
#         print(f"{num1} + {num2} = {num1 + num2}")
#     case "-":
#         print(f"{num1} - {num2} = {num1 - num2}")
#     case "*":
#         print(f"{num1} * {num2} = {num1 * num2}")
#     case "/" if num2 != 0:
#         print(f"{num1} / {num2} = {num1 / num2}")
#     case _:
#         print("操作错误！")

oper = input("请输入你的操作：")
match oper:
    case "w" | "W" | "上":
        print("角色向上移动")
    case "s" | "S" | "下":
        print("角色向下移动")
    case "a" | "A" | "左":
        print("角色向左移动")
    case "d" | "D" | "右":
        print("角色向右移动")
    case " " | "上":
        print("角色跳跃")
    case "j" | "J" | "攻击":
        print("角色发动攻击")
    case "esc" | "ESC" | "退出":
        print("角色退出游戏")
    case _:
        print("输入操作无效！")
