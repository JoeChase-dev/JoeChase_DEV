# # 注意：函数定义时并不会执行，只有在调用函数时才会执行函数体内的代码。；函数必须先定义，才能调用。
# # 函数的定义
# """def out_line(参数名):
#         函数体
#         return  返回值
# """
# def out_line():
#     print("这是一个函数")
#     print("______________________________________")
# # 函数调用
# out_line()

# 函数的参数和返回值
# 注意
# 函数定义时，多个参数之间用逗号分隔；函数调用时，实参的个数和形参的个数必须一致；
# return 只有返回功能，没有打印功能，输出结合print()函数使用；
# 形参：函数定义时括号内的参数，只能在函数中使用
# 实参：函数调用时括号内的参数，实参的值会传递给形参


# # 函数1  计算圆的面积
# def circle_area(r):
#     area = 3.14 * r ** 2
#     return area
# print(circle_area(10))

# # 函数2  计算矩形的面积
# def rectangle_area(l,w):
#     area = l * w
#     return area
# print(rectangle_area(10,5))
#
# # 函数3 计算圆的面积和周长  --> 返回多个值，返回值用逗号分隔， ----> 返回值为元组类型
# # 注意：round(数值,保留小数位数)
# def circle_area_lenth(r):
#     area = 3.14 * r **2
#     lenth = 2 * 3.14 * r
#     return round(area,1) ,round(lenth,1)
# c = circle_area_lenth(10)
# # 解包
# area,lenth = circle_area_lenth(10)
# print(area,lenth)
# print(type(c))

