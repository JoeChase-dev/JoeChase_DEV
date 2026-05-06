"""
总结：
    1 python爬虫流程
    2 了解XPath定位，JSON对象提取
    3 如何使用lxml库，进行XPath的提取
    4 如何在Python中使用Selenium库来帮助模拟浏览器，获取完整的HTML
"""

"""
爬虫流程：  打开网页 ---> 提取数据 ---> 保存数据
         Requests     XPath/JSON    Pandas
"""

"""
Requests:两种访问方式： Get 和 Post
区别： get 将参数包含在url中
        post 通过request body 来传递参数
"""
# # get 进行访问
# import requests
# r = requests.get("http://www.baidu.com")  # 可以使用 r.text 获取网页内容
# # post 进行表单传递
# r = requests.post("http://httpbin.org/post", data = {"key": "value"}) # data就是传递的表单参数

"""
XPath是XML的路径语言，实际是通过元素和属性进行导航
node        选node节点的所有子节点
/           从根节点选取
//          选取所有当前节点，不考虑他们的位置
.           当前节点
..          父节点
@           属性选择
|           或 两个节点的合计
text()      当前路径下的文本内容
"""
# xpath('node') 选取了 node 节点的所有子节点
# xpath('/div') 从根节点上选取 div 节点
# xpath('//div') 选取所有的 div 节点
# xpath('./div') 选取当前节点下的 div 节点
# xpath('…') 回到上一个节点
# xpath('//@id') 选取所有的 id 属性
# xpath('//book[@id]') 选取所有拥有名为 id 的属性的 book 元素
# xpath('//book[@id=abc]') 选取所有 book 元素，且这些 book 元素拥有 id= "abc"的属性
# xpath('//book/title | //book/price') 选取 book 元素的所有 title 和 price 元素
# """
# xpath 会使用 lxml
# """
# from lxml import etree
# html = etree.HTML(html)
# result = html.xpath('//li')
#
#
#
# """
# json 轻量级的交互方式
# json.dumps()    将python对象转换成json对象
# json.loads()    将json对象转换为python对象
# """
# import json
# jsonData = '{"a":1,"b":2,"c":3}';
# input = json.loads(jsonData)
# print(input)

"""
使用JSON数据自动下载王祖贤的海报"""

# import requests
# import json
# query = "王祖贤"
# '''下载图片'''
# def download(src,id):
#     dir ='./'+ str(id) + '.jpg'
#     try:
#         pic = requests.get(src,timeout=10)
#         fp = open(dir,'wb')
#         fp.write(pic.content)
#         fp.close()
#     except requests.exceptions.ConnectionError:
#         print('图片无法下载')
#
# '''for 循环 请求全部的url'''
# for i in range(0,22471,20):
#     url = 'https://www.douban.com/j/search_photo?q='+query+'&limit=20&start='+str(i)
#     html = requests.get(url).text
#     response = json.loads(html,encoding='utf-8')
# for image in response['images']:
#     print(image['src'])
#     download(image['src'],image['id'])

import requests
import json
import os

query = "王祖贤"

# 创建保存目录
save_dir = './download_images'
if not os.path.exists(save_dir):
    os.makedirs(save_dir)

'''下载图片'''


def download(src, id):
    dir_path = os.path.join(save_dir, str(id) + '.jpg')
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
    }
    try:
        pic = requests.get(src, timeout=10, headers=headers)
        with open(dir_path, 'wb') as fp:
            fp.write(pic.content)
        print(f'下载成功：{id}.jpg')
    except requests.exceptions.ConnectionError:
        print('图片无法下载')
    except Exception as e:
        print(f'下载出错：{e}')


'''for 循环 请求全部的 url'''
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
    'Referer': 'https://www.douban.com/'
}

for i in range(0, 22471, 20):
    url = f'https://www.douban.com/j/search_photo?q={query}&limit=20&start={i}'
    try:
        html = requests.get(url, headers=headers, timeout=10).text
        response = json.loads(html)

        if 'images' in response:
            for image in response['images']:
                print(image['src'])
                download(image['src'], image['id'])

        print(f'第 {i // 20 + 1} 页抓取完成')

    except json.JSONDecodeError:
        print(f'JSON 解析失败，页码：{i // 20 + 1}')
    except Exception as e:
        print(f'请求出错：{e}')

    # 添加延时，避免请求过快
    import time

    time.sleep(1)