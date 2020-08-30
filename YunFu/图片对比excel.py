import pandas as pd
import os

srcFile = r'E:\TEMP\01YZ\车牌对应\s\excel\bak\S_all'
excel_fiel = r'E:\TEMP\01YZ\车牌对应\s\excel\bak\学生信息.xlsx'
excel_save_log = r'E:\TEMP\01YZ\车牌对应\s\excel\bak\学生信息_无相片.xlsx'


df = pd.read_excel(excel_fiel, index=False)

# print(df[df.姓名.duplicated()])
# print(df[df.联系人1手机.duplicated()])
df["是否有相片"] = ''

fns = [os.path.join(root, fn) for root, dirs, files in os.walk(srcFile) for fn in files]
# print(len(fns))
m = 1
for f in fns:
    file_n = f.split('\\')[-1].split('.')[0]
    file_path = '\\'.join(f.split('\\')[:-1])


    for i in range(len(df)):

        if df.loc[i, "学号"].astype('str') == file_n:
            print(df.loc[i, "学号"], file_n)
            # print(df.loc[i, "学号"],df.loc[i, "姓名"], f)
            df.loc[i, "是否有相片"] = "YES"


            m +=1

    # break
print(m)
df.to_excel(excel_save_log, index=False)