import os
import pandas as pd


srcFile = 'E:\\TEMP\\3Note\\截图\\'
fns = [os.path.join(root, fn) for root, dirs, files in os.walk(srcFile) for fn in files if 'Snipaste_2022' and '49' in fn]
# print(fns)
file_path = 'E:\\TEMP\\6TEST\\GRRPA\\'
file = r'E:\TEMP\6TEST\GRRPA\采购订单行明细.xlsx'
df = pd.read_excel(file)


# 分类存文件
aa = df['材质'].unique()
print(len(df))
for i in aa:
    df1 = df[df['材质'] == i]
    if pd.isnull(i):
        i = '空'
        df1 = df[df['材质'].isnull()]
    df1.to_excel(f'{file_path}采购订单行明细_{i}.xlsx', index=False)
    print(i, len(df1))