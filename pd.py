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

print(student.loc[1:100, ['iID', '姓名']])
