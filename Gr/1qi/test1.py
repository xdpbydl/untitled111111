import pandas as pd

file = r'E:\TEMP\6TEST\GRRPA\duichongkuai\20220726_1\export_soghuodan.xlsx'
df = pd.read_excel(file)
df2 = pd.read_excel(file)

txt = df.iloc[0, [1]].values[0]
print(txt)
print(df.columns[1])

# 把第2列改为指定的列名
df.rename(columns={df.columns[0]: 'A'}, inplace=True)
col_list = df2.columns.tolist()
print(col_list)
print(df2.columns)
df2.columns = df.columns
# print(df1)
print(df2.columns)