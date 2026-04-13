#案例1：定义一个函数：传入底和高计算三角形面积函数
def triangle_area(base, height):
    """
    计算三角形面积
    :param base: 底
    :param height: 高
    :return: 三角形面积
    """
    area = base * height / 2
    return round( area,1)
print(f"三角形面积为：{triangle_area(10,5)}")
# 案例二：定义一个函数，计算传入的字符串中元音字母个数（aeiou AEIOU）
def count_w  (s):
    """
    计算字符串中元音字母个数
    :param s: 字符串
    :return: 元音字母个数
    """
    count  =0
    for i in s:
        if i in "aeiouAEIOU":
            count +=1
    return count
print(f"字符串中元音字母个数：{count_w("Hello Python,Hello World")}")

# 案例三：定义一个函数，计算传入班级学员高考列表中成绩的最高分、最低分、平均分（1位小数）并返回
def class_score(score_list):
    """
    计算班级成绩
    :param score_list: 成绩列表
    :return: 最高分、最低分、平均分
    """
    max_score = max(score_list)
    min_score = min(score_list)
    avg_score = round(sum(score_list)/len(score_list),1)
    return max_score,min_score,avg_score
score_list = [89,90,100,80,70,60,50,40,30,20]
max_s ,min_s,avg_s = class_score(score_list)
print(f"班级最高分：{max_s}")
print(f"班级最低分：{min_s}")
print(f"班级平均分：{avg_s}")


# 定义一个函数，根据传入的分数，计算对应的分数等级并返回
def grade(score):
    """
    根据分数计算分数等级
    :param score:
    :return: 分数对应的等级
    """
# 使用range函数效率低，使用if...elif...else结构效率高
    if score < 0 or score > 100:
        return "输入的分数有误"
    elif score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "E"
score = int (input("请输入分数："))
print(f"{ score}对应的分数等级为：{grade(score)}")
# 定义一个函数，用于判断一个字符串是否是回文，返回BOOL值
def is_Palindrome(s):
    """
    判断字符串是否是回文
    :param s:
    :return: bool值
    """
    if s[::1]==s[::-1]:
        return True
    else:
        return False
s_list = input("请输入一个字符串：")
print(f"{s_list}是否是回文：{is_Palindrome(s_list)}")
#定义一个函数，完成时间转换功能，将传入的秒转换为小时、分钟、秒并返回
def time_convert(seconds):
    """
    将秒转换为小时、分钟、秒
    :param seconds:
    :return:hours,minutes,seconds
    """
    minutes = seconds // 60
    hours = minutes // 60
    seconds = seconds % 60
    minutes = minutes % 60
    return hours, minutes, seconds
seconds = int (input("请输入秒数："))
h,m,s = time_convert(seconds)
print(f"{seconds}秒转换为：{h}小时{m}分{s}秒")
# 定义一个函数，根据传入的三角形的三个边的边长，判定三角形的类型（等边三角形、等腰三角形、普通三角形）并返回
def triangle_type(a,b,c):
    """
    根据三角形边长判断三角形类型
    :param a:
    :param b:
    :param c:
    :return: 三角形类型
    """
    if a+b>c and a + c > b and c + b > a:
        if a == b and b == c and c == a:
            return "等边三角形"
        elif a == b or b == c or c ==a :
            return "等腰三角形"
        else :
            return "普通三角形"
    else:
         return "无法构成一个三角形！"
a = int(input("请输入第一个边的边长："))
b = int(input("请输入第二个边的边长："))
c = int(input("请输入第三个边的边长："))
print(f"{a},{b},{c}构成的三角形类型为：{triangle_type(a,b,c)}")

