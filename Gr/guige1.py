import pandas as pd

excel_file = r'E:\TEMP\02GR\report11.xls'
# excel_file = r'E:\TEMP\02GR\export_soghuodan.xlsx'
df = pd.read_html(excel_file)
# print(df)
# print(df[0])
df = pd.DataFrame(df[0])
# print(df.iloc[3])
df.columns=df.iloc[0]
# print(df.iloc[0])ee
# print(df.columns)
# print(df.info())
# df = df.asfreq(str)
df = df[df['物料号'].str.contains('R')]
# print(df)
# group = df.groupby('工号')
# print(group)


def guige(x):
    x_1 = x.split(',')[0]

    return x_1
#
df["规格"] = df["规格"].apply(guige)
df["规格"] = df["规格"]+'='+ df["数量"]

# print(df["规格"]+'='+ df["数量"])
df1 = df[['工号', '规格']]
print(df1)
# group = df1.groupby('工号')
# print(group)
#
# for i in group:
#     print(i)