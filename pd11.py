# encoding: utf-8
import pandas as pd
import numpy as np

# dates = pd.date_range('20170101', periods=7)
# print(dates)
# print("--" * 16)
# df = pd.DataFrame(np.random.rand(7, 4), index=dates, columns=list('ABCD'))
# print(df)

# df2 = pd.DataFrame({'A': 1.,
#                     'B': pd.Timestamp('20170102'),
#                     'C': pd.Series(1, index=list(range(4)), dtype='float32'),
#                     'D': np.array([3] * 4, dtype='int32'),
#                     'E': pd.Categorical(["test", "train", "test", "train"]),
#                     'F': 'foo'})

# print(df2)

dates = pd.date_range('20170101', periods=7)
df = pd.DataFrame(np.random.randn(7, 4), index=dates, columns=list('ABCD'))

# 查看框架的顶部和底部的数据行
# print(df.head())
# print("--------------" * 10)
# print(df.tail(3))

# 显示索引，列和底层numpy数据
# print("index is :" )
# print(df.index)
# print("columns is :" )
# print(df.columns)
# print("values is :" )
# print(df.values)

# 调换数据
# print(df.T)

# 通过轴排序
# print(df.sort_index(axis=1, ascending=False))

# 按值排序
# print(df.sort_values(by='B'))

# 选择一列，产生一个系列
# print(df['A'])


# 选择通过[]操作符，选择切片行
print(df[0:3])

print("========= 指定选择日期 ========")

print(df['20170102':'20170103'])
