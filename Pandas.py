import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#通过传递一个numpy array，日期索引以及列标签来创建一个DataFrame：
dates = pd.date_range('20130101', periods=6)

df = pd.DataFrame(np.random.randn(6,4), index=dates, columns=list('ABCD'))
print(df)

#通过传递一个能够被转换为类似series的dict对象来创建一个DataFrame:
df2 = pd.DataFrame({ 'A' : 1.,
                     'B' : pd.Timestamp('20130102'),
                     'C' : pd.Series(1,index=list(range(4)),dtype='float32'),
                     'D' : np.array([3]*4,dtype='int32'),
                     'E' : pd.Categorical(["test","train","test","train"]),
                     'F' : 'foo' })

print(df2)


#查看frame中头部和尾部的几行：
print(df.head())
print(df.tail(3))

#显示索引、列名以及底层的numpy数据
print(df.index)
print(df.columns)
print(df.values)

#选择某一列数据，它会返回一个Series，等同于df.A：
print(df['A'])

#通过使用:进行切片选取：
print(df[0:3])

#对于DataFrame类型，plot()能很方便地画出所有列及其标签
ts = pd.Series(np.random.randn(1000), index=pd.date_range('1/1/2000', periods=1000))
ts = ts.cumsum()
ts.plot()
plt.show()

df = pd.DataFrame(np.random.randn(1000, 4), index=ts.index, columns=['A', 'B', 'C', 'D'])
df = df.cumsum()
plt.figure()
df.plot()
plt.legend(loc='best')
plt.show()


#写入一个csv文件
df.to_csv('data/foo.csv')

#从一个csv文件读入
pd.read_csv('data/foo.csv')

#写入一个Excel文件
df.to_excel('data/foo.xlsx', sheet_name='Sheet1')

#从一个excel文件读入
pd.read_excel('data/foo.xlsx', 'Sheet1', index_col=None, na_values=['NA'])
