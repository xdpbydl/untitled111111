import pandas as pd
import os

poto_file = r'E:\TEMP\01YZ\20201012\POTO_ALL'
excel_web = r'C:\Users\Administrator\Desktop\老师信息_20201009.xlsx'
excel_fie = r'E:\TEMP\01YZ\20201012\20201012_all.xls'


df = pd.read_excel(excel_fie, index=False, keep_default_na=False)
df_web = pd.read_excel(excel_web, index=False, keep_default_na=False)

# print(df[df.姓名.duplicated()])
# print(df[df.联系人1手机.duplicated()])
df["是否有姓名"] = ''
df["是否有手机"] = ''
df["是否有车牌"] = ''
df["本次有相片"] = ''

# print(df)
# print(df["姓名"], df["电话号码"], df["小车车牌号码"])
# print(df_web["姓名"], df_web["手机"], df_web["车牌号码"])


# df.to_excel(excel_save_log, index=False)
# index = df[df.姓名 == '刘红然'].index.tolist()
# print(index)

def shifoucunzai(a, b, c):
    for i in a:
        for m in b:
            if str(i) == str(m) and str(i) != '':
                print(i, m)
                index = df[a == i].index.tolist()
                print(index)
                df.loc[index[0], [c]] = '存在'
            elif str(i) == str(m) and str(i) == '':
                df.loc[index[0], [c]] = '无车牌'

shifoucunzai(df["姓名"], df_web["姓名"], "是否有姓名")
shifoucunzai(df["电话号码"], df_web["手机"], "是否有手机")
shifoucunzai(df["小车车牌号码"], df_web["车牌号码"], "是否有车牌")

if os.path.exists(poto_file):
    # root 所指的是当前正在遍历的这个文件夹的本身的地址
    # dirs 是一个 list，内容是该文件夹中所有的目录的名字(不包括子目录)
    # files 同样是 list, 内容是该文件夹中所有的文件(不包括子目录)
    for root, dirs, files in os.walk(poto_file):
        for file in files:
            src_file = os.path.join(root, file)
            aa = file.replace(".jpg", '')
            for i in  df["姓名"]:
                if aa == i:
                    index = df[df["姓名"] == i].index.tolist()
                    # print(index)
                    df.loc[index[0], ["本次有相片"]] = '存在'



df.to_excel(excel_fie.replace(".xls", "_11.xls"), index=False)