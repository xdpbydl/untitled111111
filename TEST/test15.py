import pandas as pd

fiel_1 = r'E:\TEMP\6TEST\GRWL\03\箱头保留信息.csv'
fiel_2 = r'E:\TEMP\6TEST\GRWL\03\工号暂挂.csv'

def csv_to_xlsx(file):
    data = pd.read_csv(file,  engine='python')
    print(data.columns)
    file_xlxs = f"{file.split('.csv')[0]}.xlsx"
    data.drop(data.filter(regex="Unname"), axis=1, inplace=True)
    data.to_excel(file_xlxs, index=False)
    file = file_xlxs
    return file


fiel_1 = csv_to_xlsx(fiel_1)

## 20220303，增加箱头保留信息过滤##
df_bl = pd.read_excel(fiel_1)
print(len(df_bl))
df_bl.drop(df_bl[(df_bl['单据类型'] == '箱头转仓单') & (df_bl['保留人'].astype(str).str.startswith('BA0147'))].index, inplace=True)
print(len(df_bl))
df_bl.to_excel(fiel_1, index=False)
## 20220303，增加箱头保留信息过滤##