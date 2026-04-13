"""
教务管理系统需求清单
1.
添加学生信息：录入学生姓名、语文、数学、英语成绩，保存到系统中。
2.
修改学生信息：输入要修改的学生姓名，再录入新的语文、数学、英语成绩，完成信息更新。
3.
删除学生信息：输入要删除的学生姓名，根据姓名删除对应学生信息。
4.
查询学生信息：输入要查询的学生姓名，根据姓名查询并输出该学生信息。
5.
列出所有学生：遍历并输出全部学生信息。
6.
统计班级成绩：
- 统计语文、数学、英语成绩的最高分、最低分、平均分
- 分别找出语文、数学、英语最高分和最低分对应的学员姓名
7.
退出系统：结束程序运行。
"""

print(""" 
        ############ 教务管理系统 ############
        #          1.添加学生信息            #
        #          2.修改学生信息            #    
        #          3.删除学生信息            #     
        #          4.查询学生信息            #    
        #          5.列出所有学生            #    
        #          6.统计班级成绩            # 
        #          7.退出系统                #
        ####################################"""
      )

# 修正1：students字典放在循环外，数据才能持久保存
students = {}

while True:
        choice = int(input("\n请输入您的操作1-7："))
        print("请输入数字！")
        match choice:
            case 1:
                stu_name = input("请输入添加的学生姓名：")
                if stu_name in students:
                    print("学生信息已存在！")
                else:
                    # 修正2：成绩转换为整数类型

                    stu_chinese = int(input("请输入学生语文成绩："))
                    stu_math = int(input("请输入学生数学成绩："))
                    stu_english = int(input("请输入学生英语成绩："))
                    students[stu_name] = {
                        "chinese": stu_chinese,
                        "math": stu_math,
                        "english": stu_english
                    }
                    print("学生信息录入成功")
                continue

            case 2:
                stu_name = input("请输入要修改的学生姓名：")
                if stu_name not in students:
                    print(" 学生信息不存在！")
                else:

                    stu_chinese = int(input("请输入学生新的语文成绩："))
                    stu_math = int(input("请输入学生新的数学成绩："))
                    stu_english = int(input("请输入学生新的英语成绩："))
                    students[stu_name] = {
                        "chinese": stu_chinese,
                        "math": stu_math,
                        "english": stu_english
                    }
                    print(" 学生信息修改成功")
                continue

            case 3:
                stu_name = input("请输入要删除的学生姓名：")
                if stu_name not in students:
                    print("学生信息不存在！")
                else:
                    del students[stu_name]
                    print(" 学生信息删除成功")
                continue

            case 4:
                stu_name = input("请输入要查询的学生姓名：")
                if stu_name not in students:
                    print(" 学生信息不存在！")
                else:
                    info = students[stu_name]
                    print(f"【{stu_name}】语文：{info['chinese']}分，数学：{info['math']}分，英语：{info['english']}分")
                continue

            case 5:
                # 修正6：不需要输入姓名，直接列出所有
                if not students:
                    print("暂无学生信息")
                else:
                    print("\n========== 所有学生信息 ==========")
                    # 修正3：正确遍历字典，使用students[stu]获取详情
                    for stu_name in students:
                        print(f"【{stu_name}】语文：{students[stu_name]['chinese']}分，数学：{students[stu_name]['math']}分，英语：{students[stu_name]['english']}分")
                    print("==================================")
                continue

            case 6:
                if not students:
                    print("暂无学生信息，无法统计")
                    continue

                # 修正4：正确提取各科成绩列表
                chinese_scores = [students[s]["chinese"] for s in students]
                math_scores = [students[s]["math"] for s in students]
                english_scores = [students[s]["english"] for s in students]

                # 统计语文
                max_c, min_c = max(chinese_scores), min(chinese_scores)
                avg_c = sum(chinese_scores) / len(chinese_scores)
                # 找最高分和最低分的学生
                max_c_stu = [s for s in students if students[s]["chinese"] == max_c]
                min_c_stu = [s for s in students if students[s]["chinese"] == min_c]

                print(f"语文成绩统计：")
                print(f"   最高分：{max_c}分（{', '.join(max_c_stu)}）")
                print(f"   最低分：{min_c}分（{', '.join(min_c_stu)}）")
                print(f"   平均分：{avg_c:.1f}分")

                # 统计数学
                max_m, min_m = max(math_scores), min(math_scores)
                avg_m = sum(math_scores) / len(math_scores)
                max_m_stu = [s for s in students if students[s]["math"] == max_m]
                min_m_stu = [s for s in students if students[s]["math"] == min_m]

                print(f" 数学成绩统计：")
                print(f"   最高分：{max_m}分（{', '.join(max_m_stu)}）")
                print(f"   最低分：{min_m}分（{', '.join(min_m_stu)}）")
                print(f"   平均分：{avg_m:.1f}分")

                # 统计英语
                max_e, min_e = max(english_scores), min(english_scores)
                avg_e = sum(english_scores) / len(english_scores)
                max_e_stu = [s for s in students if students[s]["english"] == max_e]
                min_e_stu = [s for s in students if students[s]["english"] == min_e]

                print(f" 英语成绩统计：")
                print(f"   最高分：{max_e}分（{', '.join(max_e_stu)}）")
                print(f"   最低分：{min_e}分（{', '.join(min_e_stu)}）")
                print(f"   平均分：{avg_e:.1f}分")
                continue

            case 7:
                #  修正5：添加退出功能
                print("感谢使用教务管理系统，再见！")
                break

            case _:
                print(" 无效操作，请输入1-7之间的数字！")