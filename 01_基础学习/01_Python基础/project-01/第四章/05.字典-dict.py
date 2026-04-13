# # 字典：使用键值（key：value）存储数据，一一对应，快速找到
# # 特点：键值对存储，键不可重复，可修改
# # 注意：字典中的value可以是任意类型数据，而key不能为可变类型（如：list，set，dict）
# # 定义：
# dict1 = {"王林":609,"李牧万":587,"陈平安":700,"杨间":560}
# print(dict1)
# print(type(dict1))
# # key不能为可变类型（如：list，set，dict）
# dict2 = {1:90,1.3:40,"程实":700,(1,3):90}
# print(dict2)
# # 获取  key来获取
# print(dict1["李牧万"])
# dict1["李牧万"] =600
# print(dict1["李牧万"])

# dict_score = {"王林":609,"李牧万":587,"陈平安":700,"杨间":560}
# # 添加  如若存在则为修改
# dict_score["启哥"] = 601
# print(dict_score)
# # 修改
# dict_score["启哥"] =610
# print(dict_score)
# # 删除
# v = dict_score.pop("李牧万")
# print(v)
# print(dict_score)
# del dict_score["王林"]
# print(dict_score)
# # 查询
# print(dict_score["启哥"])
# print(dict_score.keys())
# print(dict_score.values())
# print(dict_score.items())
# # 遍历
# for key in dict_score.keys():
#     print(f"{key}: {dict_score[key]}")
# for k,v in dict_score.items():
#     print(f"{k}: {v}")


