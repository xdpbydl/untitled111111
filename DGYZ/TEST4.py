import pandas as pd
import ast

file = r'D:\ZCXX\3.1 DGYC\2.TEST\排序.xlsx'
df = pd.read_excel(file)
df = df.sort_values('英文名称')
df[['英文排名']] = df[['英文名称']].rank(ascending=False)
print(df)
ast.literal_eval()

df.to_excel()