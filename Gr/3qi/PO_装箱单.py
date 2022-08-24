import os
import pandas as pd

srcFile = 'E:\\TEMP\\3Note\\截图\\'
fns = [os.path.join(root, fn) for root, dirs, files in os.walk(srcFile) for fn in files if 'Snipaste_2022' and '49' in fn]
# print(fns)
file_path = 'E:\\TEMP\\6TEST\\GRRPA\\'
file = r'E:\TEMP\6TEST\GRRPA\采购订单行明细.xlsx'
df = pd.read_excel(file)

# # 分类存文件
# aa = df['材质'].unique()
# print(len(df))
# for i in aa:
#     df1 = df[df['材质'] == i]
#     if pd.isnull(i):
#         i = '空'
#         df1 = df[df['材质'].isnull()]
#     df1.to_excel(f'{file_path}采购订单行明细_{i}_riqi.xlsx', index=False)
#     print(i, len(df1))


taizhang = r'E:\TEMP\6TEST\GRRPA\PO_\箱头计划及台帐信息查询.csv'
mingxi = r'E:\TEMP\6TEST\GRRPA\PO_\装箱清单明细_all.xlsx'
tz_df = pd.read_csv(taizhang)
mx_df = pd.read_excel(mingxi)


def xt_chuli(a):
    if a < 10:
        return f'0{str(a)}'
    else:
        return str(a)


# 采用 '工号-箱头-分箱'查找差异
tz_data = tz_df['工号-箱头-分箱']
mx_df["分箱"] = mx_df['分箱'].apply(xt_chuli)
mx_data = mx_df["工号"].map(str) + '-' + mx_df["箱号"].map(str) + '-' + mx_df["分箱"].map(str)

# 采用 'PO号','PO行'查找差异
# tz_df[['外购箱头PO', 'PO行']] = tz_df[['外购箱头PO', 'PO行']].astype('str')
# mx_df[['PO号',	'PO行']] = mx_df[['PO号',	'PO行']].astype('str')
# tz_data = tz_df[['外购箱头PO', 'PO行']].apply('-'.join, axis=1)
# mx_data = mx_df[['PO号',	'PO行']].apply('-'.join, axis=1)
# mx_data = mx_data.drop_duplicates().reset_index(drop=True)

print(tz_data)
print(mx_data)

chayi_data = pd.concat([tz_data, mx_data]).drop_duplicates(keep=False)
tz_data.to_excel(r'E:\TEMP\6TEST\GRRPA\PO_\tz_箱头计划及台帐信息查询.xlsx')
mx_data.to_excel(r'E:\TEMP\6TEST\GRRPA\PO_\mx_装箱清单明细_all.xlsx')
print(len(chayi_data))
