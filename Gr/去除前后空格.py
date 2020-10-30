import pandas as pd

file = r"C:\Users\Administrator\Desktop\GRWL_202010\装箱清单.xls"
file1 = r"C:\Users\Administrator\Desktop\GRWL_202010\装箱清单_11.xls"
# df = pd.read_html(file, header=0, keep_default_na=False, encoding='utf-8')[0]      # html格式excel

def move_nan(file,file1):
    try:
        df = pd.read_excel(file, index=False, keep_default_na=False, engine='openpyxl')
    except:
        df = pd.read_html(file, header=0, keep_default_na=False)[0]  # html格式excel

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
    df.to_excel(file1, index=False, engine='openpyxl')

move_nan(file,file1)
