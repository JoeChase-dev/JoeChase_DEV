# 案例
# 购物车系统：实现商品信息的添加、修改、删除、查询功能，
# 1：添加：录入名称，价格，数量，保存到购物车内
# 2：修改：输入要修改的商品名称，然后输入价格数量，
# 3：删除：输入名称，删除商品
# 4：查询：将商品信息展示出来，格式为
# 5：退出购物车
# 制作menu
print("欢迎来到购物车系统！")
menu = """
      ###### 购物车系统 ######
      #      1添加购物车     #
      #      2修改购物车     #
      #      3删除购物车     #
      #      4查询购物车     #
      #      5退出购物车     #
      #######################
    """
print(menu)
goods = {}
#输入操作
while True:
    option = int(input("请输入你所选择的操作（1-5）："))
    match option:
        case 1:
            # 1.添加购物车
            goods_name = input("请输入商品名称：")
            goods_price = float(input("请输入商品价格："))
            goods_num = int(input("请输入商品数量："))

            if goods_name in goods:
                print("商品已存在！")
            else :
                goods[goods_name] = {"price": goods_price, "num": goods_num}
                print("商品添加完毕！")
        case 2:
            # 2.修改购物车
            goods_name = input("请输入要修改的商品名称：")
            if goods_name not in goods:
                print("商品不存在！")
                continue

            goods_price = float(input("请输入最新商品价格："))
            goods_num = int(input("请输入商品最新数量："))
            goods[goods_name] = {"price": goods_price, "num": goods_num}
            print("商品修改完毕！")
        case 3:
            # 3.删除购物车
            goods_name = input("请输入要删除的商品名称：")
            if goods_name not in goods:
                print("商品不存在！")
            else :
                del goods[goods_name]
                print("商品已删除！")
        case 4:
            # 4.查询购物车
            for goods_name in goods.keys():
                goods_meg = goods[goods_name]
                print(f"商品名称：{goods_name},商品价格：{goods_meg['price']},商品数量:{goods_meg['num']}")
        case 5:
            # 5退出购物车
            print("Bey~")
            break
        case _:
            print("操作异常！请重新输入")
