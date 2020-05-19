# encoding: utf-8
# import pandas as pd, numpy as np
# #
# # from pandas import Series, DataFrame
# #
# # # print("dlfdk")
# # # obj = pd.Series([3, 4, 5, -1.2, 1])
# # # # print(obj)
# # # # print(obj.values)
# # # # print(obj.index)
# # #
# # # obj2 = pd.Series([4, 7, -5, 3], index=['d', 'b', 'a', 'c'])
# # # print(obj2, obj2.index)
# # #
# # #
# # # obj2['d'] = 6
# # # # print(obj2[['c', 'a', 'd']])
# # # # print(obj2[['a', 'b']])
# # #
# # # # print(obj2[obj2 > 0])
# # # # print(obj2 * 2)
# # #
# # # print(np.exp(obj2))
# # # print('b' in obj2, "e" in obj2)
# #
import numpy as np, pandas as pd

# arr1 = np.arange(10)
# print(arr1, type(arr1))
# s1 = pd.Series(arr1)
# print(s1, type(s1))
#
#
# dic1 = {'a': 10, 'b': 20, 'c': 30, 'd': 40, 'e': 50}
# s2 = pd.Series(dic1)
# print(s2, type(s2))
#
# arr2 = np.array(np.arange(12)).reshape(4, 3)
# print(arr2, type(arr2))
#
# df1 = pd.DataFrame(arr2)
# print(df1, type(df1))
#
# dic2 = {'a': [1, 2, 3, 4], 'b': [5, 6, 7, 8], 'c': [9, 10, 11, 12], 'd': [13, 14, 15, 16]}
# df2 = pd.DataFrame(dic2)
# print(df2, type(df2))
#
dic3 = {'one': {'a': 1, 'b': 2, 'c': 3, 'd': 4},

        'two': {'a': 5, 'b': 6, 'c': 7, 'd': 8},

        'three': {'a': 9, 'b': 10, 'c': 11, 'd': 12}}
# print(dic3, type(dic3))

# df3 = pd.DataFrame(dic3)
# # print(df3, type(df3))
#
# df4 = df3[['one', 'three']]
#
# print(df4, type(df4))
#
# s3 = df3['one']
# print(s3, type(s3))
#
# s4 = pd.Series(np.array([1, 1, 2, 3, 5, 8]))
# s4.index = ['a', 'b', 'c', 'd', 'e', 'f']
# print(s4, s4.index)
# print('---' * 12)
# print(s4[[1, 3, 5]])
#
# s5 = pd.Series(np.array([10, 15, 20, 30, 55, 80]),
#
#                index=['a', 'b', 'c', 'd', 'e', 'f'])
#
# print(s5)
#
# s6 = pd.Series(np.array([12, 11, 13, 15, 14, 16]),
#
#                index=['a', 'c', 'g', 'b', 'd', 'f'])
#
# print(s6)
#
# print(s5 + s6)
#
# print(s5 / s6)
import os, os.path

student = pd.read_excel('C:\\Users\\\Administrator\\Desktop\\student.xlsx', sheet_name='aaa')

# print(student.index)
# print(student.head(), student.tail())

# df1 = student["联系人1手机"].count()

# print(student.loc[[1, 10], ['iID', '学号', '姓名', '班级名称', '性别', '联系人1手机']])
# print(student.iloc[[1, 2, 3, 5, 10], [0, 1, 2, 3, 8, 10]])
# print(student.at[1, '联系人1手机'])

# print(student.shape)
# print(student.info)
# print(student.isnull())
# print(student.iloc[0].isnull())
# print(student.loc[[1,2], ['姓名','联系人2']])
# print(student.fillna(value=0))
# print(student.sort_values(by=['卡号']))
# print(student.loc[student['iID'].isin(['99', '999', '9'])])
# print(student.query("姓名 == ['毛子谦', '陶小华', '陈兆健']"))
# print(student.groupby('班级名称').count())
#
# new = student.groupby('班级名称').count()
# print(student.groupby(['班级名称', '性别']).count())

# new.to_excel('统计汇总.xlsx', sheet_name='all')

# print(student[student['姓名'].str.contains('国')])

# df = pd.DataFrame({'AAA': [4, 0, 6, 7],
#                    'BBB': [10, 20, 30, 40],
#                    'CCC': [100, 50, -30, -50]})
# df.loc[df.AAA >= 5, ['BBB', 'CCC']] = 555
# df.loc[df.AAA < 5, ['BBB', 'CCC']] = 2000
#
# ##################???
# df_mask = pd.DataFrame({'AAA': [False] * 4,
#                         'BBB': [True] * 4,
#                         'CCC': [True, False] * 2})
#
# df.where(df_mask, -1000)
#
# print(df)
# 利用pandas实现Excel的数据透视表功能
student1 = pd.read_excel('C:\\Users\\\Administrator\\Desktop\\student.xlsx', sheet_name='bbbb')

# print(student1)

# !!对一个分组变量（Sex），一个数值变量（Height）作统计汇总
# aa = pd.pivot_table(student1, values=['Height'], columns=['sex'])


# !!对一个分组变量（Sex），两个数值变量（Height,Weight）作统计汇总
# aa = pd.pivot_table(student1, values=['Height','Weight'], columns=['sex'])

# !!对两个分组变量（Sex，Age)，两个数值变量（Height,Weight）作统计汇总
# aa = pd.pivot_table(student1, values=['Height','Weight'], columns=['sex', 'age'])


# !!很显然这样的结果并不像Excel中预期的那样，该如何变成列联表的形式的？很简单，只需将结果进行非堆叠操作（unstack）即可：
aa = pd.pivot_table(student1, values=['Height', 'Weight'], columns=['sex', 'age']).unstack()
print(aa)
