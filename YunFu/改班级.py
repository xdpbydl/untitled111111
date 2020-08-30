# -*- coding: utf-8 -*-

#  存在数据不正确.后面再看
import pandas as pd

# srcFile = r'E:\TEMP\01YZ\图片\初一级学生'
# dstFile = r'E:\TEMP\01YZ\改后的'
excel_fiel = r'E:\TEMP\01YZ\车牌对应\s\excel\云浮中学初二级学生、老师基础信息录入.xls'
save_fiel = r'E:\TEMP\01YZ\车牌对应\s\excel\new.xls'

df = pd.read_excel(excel_fiel, index=False)
# duiying key 为表格中的班名,
duiying = {"初二(1班)": "初二（1班）",
           "初二(2)班": "初二（2班）",
           "初二(3)班": "初二（3班）",
           "初二(4)班": "初二（4班）",
           "初二(5)班": "初二（5班）",
           "初二(6)班": "初二（6班）",
           "初二(7)班": "初二（7班）",
           "初二(8)班": "初二（8班）",
           "初二(9)班": "初二（9班）",
           "初二10)班": "初二（10班）"}

m = 1


def preprocess(x):
    if (x['班级'].replace(' ', '') == "八年级1班"):
        x['班级'] = "初三（1班）"
        return x
    elif x['班级'].replace(' ', '') == "八年级2班":
        x['班级'] = "初三（2班）"
        return x
    elif x['班级'].replace(' ', '') == "八年级3班":
        x['班级'] = "初三（3班）"
        return x
    elif x['班级'].replace(' ', '') == "八年级4班":
        x['班级'] = "初三（4班）"
        return x
    elif x['班级'].replace(' ', '') == "八年级5班":
        x['班级'] = "初三（5班）"
        return x
    elif x['班级'].replace(' ', '') == "八年级6班":
        x['班级'] = "初三（6班）"
        return x
    elif x['班级'].replace(' ', '') == "八年级7班":
        x['班级'] = "初三（6班）"
        return x
    elif x['班级'].replace(' ', '') == "八年级8班":
        x['班级'] = "初三（6班）"
        return x
    elif x['班级'].replace(' ', '') == "八年级9班":
        x['班级'] = "初三（7班）"
        return x
    elif x['班级'].replace(' ', '') == "八年级10班":
        x['班级'] = "初三（8班）"
        return x
    elif x['班级'].replace(' ', '') == "初二(8班)":
        x['班级'] = "初二（8班）"
        return x
    elif x['班级'].replace(' ', '') == "初二(9班)":
        x['班级'] = "初二（9班）"
        return x
    elif x['班级'].replace(' ', '') == "初二10)班":
        x['班级'] = "初二（10班）"
        return x
    else:
        return x

df = df.apply(preprocess, axis=1)

df.to_excel(save_fiel, index=False)
