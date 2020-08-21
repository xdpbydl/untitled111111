import pandas as pd

#  处理好的数据
file1 = r'E:\TEMP\02GR\11.xlsx'
#  模版
file2 = r'E:\TEMP\02GR\2020-7-11供应商分配第一批.xlsx'
#  新的文件
file3 = r'E:\TEMP\02GR\2020-7-11供应商分配第一批_new.xlsx'
df1 = pd.read_excel(file1, index=False)
df2 = pd.read_excel(file2, index=False)
print(df1)
print(df2)

#
print(len(df2))
# # print(df2.loc[n-1])
df3 = df2.append(df1, ignore_index=True, sort=False)
print(len(df3))
print(df3)
df3.to_excel(file3,index=False, header=False)


