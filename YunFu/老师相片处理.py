# -*- coding: utf-8 -*-
'''批量改名'''
import shutil, os
import pandas as pd
import numpy as np

srcFile = r'E:\TEMP\01YZ\0903'
dstFile = r'E:\TEMP\01YZ\改后的'
excel_fiel = r'E:\ZCXX\1.2方辰\3. 云中\2.1实施 过程\第二次所发\导入\老师信息——20200903.xlsx'
excel_save_log = r'E:\ZCXX\1.2方辰\3. 云中\2.1实施 过程\第二次所发\导入\111.xlsx'

df = pd.read_excel(excel_fiel, index=False)
file_list = sorted(os.listdir(srcFile))

# for index, item in enumerate(sh["b2":"b379"]):
#     for cell in item:
#         name = str(cell.value)
# for index1, file_name in enumerate(file_list):

# print(file_name,index1)
# print("---"*20)
# tu_no = np.where(df[u'姓名'].str.contains(file_name), df[u'编号'], r'')
# print(tu_no, file_name)

# print(df.编号, df.姓名)
#
file_name = [file_name for index1, file_name in enumerate(file_list)]
df["头像是否存在"] = ''
# df[df.姓名.isin(file_name)]
m = 1

for i in range(len(df)):
    for x in file_name:
        print(df.iloc[i].姓名, x)
        if df.iloc[i].姓名 in x:
            tu_no = df.iloc[i].编号
            # print(df.iloc[i].姓名, x, tu_no)
            print("---" * 20)

            # print(srcFile + '\\' + x, dstFile + '\\' + str(tu_no) + r'.jpg')
            m += 1

            try:
                os.rename(srcFile + '\\' + x, srcFile + '\\' + str(tu_no) + r'.jpg')
                print(srcFile + '\\' + x, srcFile + '\\' + str(tu_no) + r'.jpg')
                df.loc[i, "头像是否存在"] = 'YES'
                pass
            except Exception as e:
                # print(e)
                df.loc[i, "头像是否存在"] = '存在同名头像'
                print(x, tu_no, '改名 失败\r\n')

    # break
print(m)

df.to_excel(excel_save_log, index=False)
# # print(len(df.姓名))
# bb = set(df.姓名)
# print(len(bb))


# shutil.copyfile(sct,path+file)
# print(sorted(os.listdir(path)))
