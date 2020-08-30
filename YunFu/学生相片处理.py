# -*- coding: utf-8 -*-
'''批量改名'''
import shutil, os
import pandas as pd

srcFile = r'E:\TEMP\01YZ\图片\高二级学生相片'
# dstFile = r'E:\TEMP\01YZ\改后的'
excel_fiel = r'E:\TEMP\01YZ\车牌对应\s\excel\云浮中学门禁卡师生基本信息（原高二）.xlsx'
# excel_save_log = r'E:\TEMP\01YZ\车牌对应\t\部分老师没有头像.xlsx'


df = pd.read_excel(excel_fiel, index=False)

print(df[df.姓名.duplicated()])
# print(df[df.联系人1手机.duplicated()])

fns = [os.path.join(root, fn) for root, dirs, files in os.walk(srcFile) for fn in files]
# print(len(fns))
m = 1
for f in fns:
    file_n = f.split('\\')[-1].split('.')[0]
    file_path = '\\'.join(f.split('\\')[:-1])


    for i in range(len(df)):
        if df.loc[i, "姓名"].replace(' ', '') in file_n.replace(' ', ''):
            # print(df.loc[i, "学号"],df.loc[i, "姓名"], f)


            try:
                os.rename(f, file_path + '\\' + str(df.loc[i, "学号"]) + r'.jpg')
                print(f, file_path + '\\' + str(df.loc[i, "学号"]) + r'.jpg')
            except:
                print("--"*15 + "文件rename 失败!", f, file_path + '\\' + str(df.loc[i, "学号"]) + r'.jpg')

            m +=1

    # break
print(m)
# file_list = sorted(os.listdir(srcFile))
# file_name = [file_name for index1, file_name in enumerate(file_list)]
# df["头像是否存在"] = ''
# # df[df.姓名.isin(file_name)]
# m = 1
#
# for i in range(len(df)):
#     for x in file_name:
#         if df.iloc[i].姓名 in x:
#             tu_no = df.iloc[i].编号
#             # print(df.iloc[i].姓名, x, tu_no)
#             print("---" * 20)
#
#             # print(srcFile + '\\' + x, dstFile + '\\' + str(tu_no) + r'.jpg')
#             m += 1
#
#             try:
#                 os.rename(srcFile + '\\' + x, srcFile + '\\' + str(tu_no) + r'.jpg')
#                 print(srcFile + '\\' + x, srcFile + '\\' + str(tu_no) + r'.jpg')
#                 df.loc[i, "头像是否存在"] = 'OK'
#                 pass
#             except Exception as e:
#                 # print(e)
#                 df.loc[i, "头像是否存在"] = '存在同名头像'
#                 print(x, tu_no, '改名 失败\r\n')
#
#     # break
# print(m)
#
# df.to_excel(excel_save_log, index=False)
# # print(len(df.姓名))
# bb = set(df.姓名)
# print(len(bb))


# shutil.copyfile(sct,path+file)
# print(sorted(os.listdir(path)))
