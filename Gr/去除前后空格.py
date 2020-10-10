import pandas as pd

file = r"E:\TEMP\02GR\test\装箱0.xls"
file1 = r"E:\TEMP\02GR\test\装箱0_1.xls"
# df = pd.read_html(file, header=0, keep_default_na=False, encoding='utf-8')[0]      # html格式excel
df = pd.read_excel(file, index=False, keep_default_na=False)


# print(type(df))
# print(df)
# print(df.columns)
n = 1

for i in df.columns:
    if "Unnamed" in i:
        i1 = ' '*n
        n += 1
        df.rename(columns={i: i1}, inplace=True)  # 替换列

        i = i1
        # print(i, n)

    df[i] = df[i].astype('str')
    df[i] = df[i].str.strip()  # 去掉前后空格

df.fillna('', inplace=True)  # 替换nan空值
df.to_excel(file1, index=False)


