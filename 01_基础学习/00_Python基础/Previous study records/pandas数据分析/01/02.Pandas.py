"""
pandas核心数据结构
Series 和 DataFrame
"""


"""
Series是个定长的字典序列，在存储中相当于两个ndarray
两个基本属性：index 和 values
"""
import pandas as pd
from pandas import Series,DataFrame
import numpy as np
x1 = Series([1,2,3,4])
x2 = Series(data = [1,2,3,4],index = ['a','b','c','d'])   # 对index进行指定
print(x1)
print(x2)

d = {'a':1,'b':2,'c':3,'d':4}
x3 = Series(d)
print(x3)


"""
DataFrame类型结构数据类似数据库表
包含行索引和列索引 可以将DataFrame看成是由相同索引的Series组成的字典类型
"""
data = {'Chinese':[66,95,93,90,80],'English':[65,85,90,80,90],'Math':[80,80,80,80,80]}
df1 = DataFrame(data)
df2 = DataFrame(data,index=['zhangfei','guanyu','liubei','dianwei','zhaoyun'],columns = ['Chinese','English','Math'])
print(df1)
print(df2)


"""
数据导入和导出
Pandas 允许直接从xlsx，csv等文件中导入数据，也可以输出到xlsx，csv等文件中
"""


"""
数据清洗
简单介绍pandas在数据清洗中的使用方法
"""
data = {'chinese':[66,95,93,90,80],'english':[65,85,90,80,90],'math':[80,80,80,80,80]}
df2 = DataFrame(data,index=['zhangfei','guanyu','liubei','dianwei','zhaoyun'],columns = ['chinese','english','math'])

# 1 删除Dataframe中不必要的列或行     drop()函数
df2 = df2.drop(columns = ['chinese'])    # 删掉语文这列
print(df2)
df2 = df2.drop(index=['zhangfei'])
print(df2)

# 2 重命名列名columns 让列表名更容易识别     rename(columns = new_names,inplace =True)函数
df2.rename(columns={'english':'yingyu'},inplace=True)
print(df2)

# 3 去重复的的值      drop_duplicates()函数
df = df1.drop_duplicates()

"""
4 格式问题
    更改数据格式
    数据间的空格
    大小写转换
    查找空格
"""
# 更改数据格式  astype()函数
df2['math'].astype('str')
df2['math'].astype(np.int64)


# 数据间的空格  strip()函数
# 先将格式转换为str类型，方便对数据进行操作
# 删除左右两边的空格
df2['math']= df2['math'].astype(str).map(str.strip)
# 删除左边空格
df2['math']= df2['math'].astype(str).map(str.lstrip)
# 删除右边空格
df2['math']= df2['math'].astype(str).map(str.rstrip)
# 若含有某个特殊符号，
df2['math'] = df2['math'].astype(str).str.strip('$')


# 大小写转换   upper() lower() title()
# 全部大写
df2.columns = df2.columns.str.upper()
# 全部小写
df2.columns = df2.columns.str.lower()
# 首字母大写
df2.columns = df2.columns.str.title()


# 查找空值  某些字段存在NaN可能，isnull函数进行查找
# df.isnull().any()


"""
使用apply函数进行数据清洗
apply函数是Pandas中自由度非常高的函数，使用频率也非常高
"""
# name列的数值进行大写转换
df = DataFrame({'name':['zhangfei','guanyu','b','c','d'],'yuwen':range(1,6)})
df['name'] = df['name'].apply(str.upper)
# 可以定义函数，在apply中进行使用
def double_df(x):
    return x*2
df1['Chinese'] = df1[('Chinese')].apply(double_df)
# 更复杂函数，例如DataFrame，新增两列，new1是yuwen和英语的成绩之和的m倍，new2 是n倍
def plus(df,n,m):
    df['new1'] = df[u'Chinese'] + df[u'English'] * m
    df['new2'] = df[u'Chinese'] * n
    return  df
df1 =df1.apply(plus,axis=1,args=(2,3,))  # axis=1 表示行，args传递参数

"""
数据统计
pandas和numpy一样，都有常用的统计函数，如果遇到空值NaN，会自动排除
count()             统计个数，空值不计算
describe()          一次性输出多个统计指标
min()               最小值
max()
sum()
mean()              平均值
median()            中位数
var()               方差
std()               标准差
argmin()            最小值的索引位置
argmax()            
idxmin()            统计最小值的索引值
idxmax()

describe()最简便
"""
df1 = DataFrame({'name':['zhangfei','guanyu','a','b'],'data1':range(1,5)})
print(df1.describe())


""""
数据表合并
一个DataFrame相当于一个数据库的数据表
两个DataFrame数据表合并使用的是merge()函数
"""
df_merge1 = DataFrame({'name':['zhangfei','guanyu','liubei'],'chinese':[66,95,93]})
df_merge2 = DataFrame({'name':['zhangfei','guanyu','dianwei'],'math':[80,80,80]})

# 1 基于指定列进行连接
df3 = pd.merge(df_merge1,df_merge2,on='name')
# 2 inner 内连接 merge 合并的默认，就是键的交集
df3 = pd.merge(df_merge1,df_merge2,how='inner')
# 3 left 左连接  第一个为主进行连接，第二个进行补充
df3 = pd.merge(df_merge1,df_merge2,how='left')
# 4 right 右连接
df3 = pd.merge(df_merge1,df_merge2,how='right')
# 5 outer 外连接  相当于求两个的并集
df3 = pd.merge(df_merge1,df_merge2,how='outer')



"""
SQL方式打开Pandas
工具 pandasql
主要函数 sqldf  接收两个参数：一个SQL查询语句，一组环境变量globals 或 locals
"""
import pandas as pd
from pandas import DataFrame
from pandasql import sqldf,load_meat,load_births
df_sql = DataFrame({'name':['zhangfei','guanyu','a','b'],'data1':range(1,5)})
pysqldf = lambda sql: sqldf(sql,globals())
sql = "select * from df1 where name='zhangfei'"
print(pysqldf(sql))
# lambda argument_list: expression



"""
Pandas总结
两个重要的数据结构：Series 和 DataFrame    可以直接从csv和xlsx等文件中导入数据，以及最终输出到excel中

一 数据结构
    Series 和 DataFrame
二 数据导入和输出
三 数据清洗
    -删除DataFrame中不必要的列或行
    -重命名列名columns
    -去重
    -格式问题
四 数据统计
五 数据表合并
六 如何使用SQL方式打开Pandas
"""