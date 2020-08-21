import pandas as pd

songhuodan = r'E:\TEMP\02GR\export_soghuodan.xlsx'
save_file = r'E:\TEMP\02GR\11.xlsx'
df = pd.read_excel(songhuodan, index=False)
# df = pd.read_excel(songhuodan, index_col=0)   # 忽略第一列
#  删除无效列
df = df.loc[:, ~df.columns.str.contains('Unnamed')]


print(df['选择'])
df['选择']=df.工号箱头分箱.str[:9]
print(df['选择'])

