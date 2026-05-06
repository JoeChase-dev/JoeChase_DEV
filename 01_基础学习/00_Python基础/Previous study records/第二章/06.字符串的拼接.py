#字符串拼接  直接使用（+）拼接  只能拼接两个字符串
s1 = "人生苦短""我用Python"
print(s1)

msg1 = "Python"
msg2 = ("我爱你！")

print("南林说："+msg1+","+msg2 )

# 案例：  ----> str(int 数字）---> 将int类型的数字转为字符串
# 输出个人实际信息
name = "周启"
age = 20
pro = "计算机科学与技术"
hobby = "Python,JAVA"
print("大家好,"+"我是"+name+",""今年"+str(age)+","+"我的爱好为"+hobby+",""我的专业为"+pro+".")
#拼接繁琐  破坏字符串完整性  类型转换


#字符串格式化
# 方式一： %s实现字符串拼接
print("大家好,我是 %s,今年 %s 岁,我的爱好为 %s ,我的专业为 %s ." % (name,age,hobby,pro))

#方式二：f"内容{变量名/表达式}内容"(开发主流）
print(f"大家好,我是{name},今年 {age}岁,我的爱好为{hobby},我的专业为 {pro} .")
