import pandas as pd
file = r'E:\TEMP\02GR\export_soghuodan.xlsx'
df = pd.read_excel(file)
df.groupby('PO编号')
po_no = df.drop_duplicates('PO编号', 'first')['PO编号']
# print(po_no.tolist())

# t = df
# index1 = t[t[['PO编号']].duplicated(keep="last")].index
# index2 = t[t[['PO编号']].duplicated(keep="first")].index
# t1 = t.loc[index1 | index2, :]
# print(t1['PO编号'])

fahuo_file1 = r'E:\TEMP\02GR\kefahuo\可发货通知书(代运）2020——导入2.0______1.xlsx'
fahuo_df = pd.read_excel(fahuo_file1, index=False)
hetong_l = fahuo_df.合同号.tolist()
hetong_s = set(hetong_l)

# print(hetong_l)
# print(hetong_s)