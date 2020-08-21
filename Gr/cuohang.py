import pandas as pd

excel = r'E:\TEMP\02GR\export_soghuodan.xlsx'
df = pd.read_excel(excel,index=False )
print(df['选择'])
#
df['选择']=df.工号箱头分箱.str[:9]
print(df['选择'])
# print(df.iloc[66, 23:24])
# # print(df.columns[:22])
# df['工号箱头分箱'] = df['工号箱头分箱'].mask(df['工号箱头分箱']=='s', 's')
#
#
# print(df['工号箱头分箱'])
# print(df.iloc[1,['工号箱头分箱']].fillna("s"))