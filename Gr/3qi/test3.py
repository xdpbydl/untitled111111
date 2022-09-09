import pandas as pd

gv_Save_Path = r'E:\TEMP\6TEST\GRRPA\DuiChongKuai\20220830_1\\'

#
songhuodan = f'{gv_Save_Path}export_soghuodan_all.xlsx'
file = r'E:\TEMP\6TEST\GRRPA\1\test.xlsx'
df = pd.read_excel(songhuodan)


# for k, i in df.iterrows():
#     print(i)
#     print(i.PO编号)
#     input('--'*88)
# self.po_list = po_data_all['PO 编号'].drop_duplicates().values.tolist()
df1 = pd.read_excel(file)
# df.rename(columns={'category': 'category-size'})
print(df.columns[1])
df.rename(columns={'0': 'PO 编号'}, inplace=True)


print(df.columns[1])
print(df)
# po_list = df1.loc[:, [0]].drop_duplicates().values.tolist()
# print(po_list)