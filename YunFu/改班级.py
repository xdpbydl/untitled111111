# -*- coding: utf-8 -*-

#  存在数据不正确.后面再看
import pandas as pd

# srcFile = r'E:\TEMP\01YZ\图片\初一级学生'
# dstFile = r'E:\TEMP\01YZ\改后的'
excel_fiel = r'D:\Temp\orher\11.xlsx'
save_fiel = r'D:\Temp\orher\new.xls'

df = pd.read_excel(excel_fiel, index=False, keep_default_na=False)

df = df.sort_values(by=['学号'])
print(df)
df = df.applymap(str)
# duiying key 为表格中的班名,
duiying = {"初二（1班）": "（1班）",
           "初二（2班）": "（2班）",
           "初二（3班）": "（3班）",
           "初二（4班）": "（4班）",
           "初二（5班）": "（5班）",
           "初二（6班）": "（6班）",
           "初二（7班）": "（7班）",
           "初二（8班）": "（8班）",
           "初二（9班）": "（9班）",
           "初二（10班）": "（10班）"}

m = 1

#
def preprocess1(x):

    for k, v in duiying.items():
        if (x['班级'].replace(' ', '') == k):
            print(v, x['班级'])
            x['班级'] = v
            return x
    return x


df = df.apply(preprocess1, axis=1)

df.to_excel(save_fiel, index=False)
