# -*- coding: utf-8 -*-
'''批量改名'''
import shutil, os
import pandas as pd
import numpy as np

srcFile = r'E:\TEMP\01YZ\车牌对应\t\all'
dstFile = r'E:\TEMP\01YZ\改后的'
excel_fiel = r'E:\TEMP\01YZ\车牌对应\t\导入老师_20200816.xls'
excel_save_log = r'E:\TEMP\01YZ\车牌对应\t\log.xls'

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

# df[df.姓名.isin(file_name)]
m = 1
for x in file_name:
    for i in range(len(df)):
        if df.iloc[i].姓名 in x:
            tu_no = df.iloc[i].编号
            # print(df.iloc[i].姓名, x, tu_no)
            print("---"*20)

            # print(srcFile + '\\' + x, dstFile + '\\' + str(tu_no) + r'.jpg')
            m += 1
            # break

            try:
                os.rename(srcFile + '\\' + x, srcFile + '\\' + str(tu_no) + r'.jpg')
            except Exception as e:
                # print(e)
                print(x,tu_no, '改名 失败\r\n')
            else:
                print(srcFile + '\\' + x, srcFile + '\\' + str(tu_no) + r'.jpg')
print(m)

# # print(len(df.姓名))
# bb = set(df.姓名)
# print(len(bb))


# shutil.copyfile(sct,path+file)
# print(sorted(os.listdir(path)))
