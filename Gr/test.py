import pandas as pd
file = r'E:\TEMP\02GR\export_soghuodan.xlsx'
df = pd.read_excel(file)
df.groupby('PO编号')
po_no = df.drop_duplicates('PO编号', 'first')['PO编号']
print(po_no.tolist())

# t = df
# index1 = t[t[['PO编号']].duplicated(keep="last")].index
# index2 = t[t[['PO编号']].duplicated(keep="first")].index
# t1 = t.loc[index1 | index2, :]
# print(t1['PO编号'])
