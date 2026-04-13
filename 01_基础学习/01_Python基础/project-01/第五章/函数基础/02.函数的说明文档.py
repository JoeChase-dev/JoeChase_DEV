# 函数1  计算圆的面积
def circle_area(r):
    """
    根据圆的半径，计算圆的面积
    :param r:圆的半径
    :return: 圆的面积
    """
    area = 3.14 * r ** 2
    return area
print(circle_area(10))

# 函数2  计算矩形的面积
def rectangle_area(l,w):
    """
    根据长度和宽度，计算长方形面积
    :param l: 长度
    :param w: 宽度
    :return: 返回矩形面积
    """
    area = l * w
    return area
print(rectangle_area(10,5))

# 函数3 计算圆的面积和周长  --> 返回多个值，返回值用逗号分隔， ----> 返回值为元组类型
# 注意：round(数值,保留小数位数)
def circle_area_lenth(r):
    """
    根据半径，计算圆的面积和周长
    :param r: 圆的半径
    :return: 圆的面积和周长
    """
    area = 3.14 * r **2
    lenth = 2 * 3.14 * r
    return round(area,1) ,round(lenth,1)
al = circle_area_lenth(10)
print(type(al))
# 解包
area,lenth = circle_area_lenth(10)
print(area,lenth)
