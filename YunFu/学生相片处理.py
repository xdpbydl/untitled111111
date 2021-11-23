# -*- coding: utf-8 -*-
'''批量改名'''
import shutil, os, traceback
import pandas as pd

srcFile = r'E:\TEMP\6TEST\yz_temp\2高一处理后\change'
dstFile = r'E:\TEMP\6TEST\yz_temp\2高一处理后\改名后'
excel_file = r'E:\TEMP\6TEST\yz_temp\高一级学生信息.xlsx'
dst_excel_file = r'E:\TEMP\6TEST\yz_temp\2高一处理后\高一级学生信息_处理.xlsx'
dst_excel_file_na = r'E:\TEMP\6TEST\yz_temp\2高一处理后\高一级学生信息_处理_na.xlsx'
# excel_save_log = r'E:\TEMP\01YZ\车牌对应\t\部分老师没有头像.xlsx'
# 开始编号
start_no = 5000


# print(df[df.姓名.duplicated()])
# print(df[df.联系人1手机.duplicated()])

# fns = [os.path.join(root, fn) for root, dirs, files in os.walk(srcFile) for fn in files]

def name_isin(df, ph_str):
    if df['姓名'] in ph_str:
        return 1


def change_name(srcFile, dst_path, excel_file, dst_excel_file, start_no):
    ##文件名改编号

    df = pd.read_excel(excel_file, index=False)
    df_save = pd.read_excel(excel_file, index=False)
    # df["学号"] = df["学号"].astype(str)
    df = df.astype({'学号': 'str', '姓名': 'str'})

    # input('--')
    # df = df.applymap(str)
    # df["学号"].fillna('GG', inplace=False)
    df_save["学号"].fillna('GG', inplace=False)

    for root, dirs, files in os.walk(srcFile):
        for fn in files:
            src_pho = os.path.join(root, fn)  # 所有的文件

            for i in range(len(df)):
                if df.loc[i, "学号"].replace(' ', '') in fn.replace(' ', ''):  # 使用学号核对
                    try:
                        # os.rename(src_pho, dstFile + '\\' + str(df.loc[i, "学号"]) + r'.jpg')
                        shutil.copy(src_pho, f'{dst_path}\\{str(start_no + i)}.jpg')
                        print(f'复制成功，源文件：{src_pho}；目标文件：{dst_path}\\{str(start_no + i)}.jpg')
                        df_save.loc[i, "学号"] = str(start_no + i)
                        break
                    except:
                        print(f'''{"--" * 15}文件复制 失败!{src_pho}{dst_path}\\{str(start_no + i)}.jpg''')
                        print(traceback.format_exc())
                elif i + 1 == len(df):
                    print(f'''{"***" * 15}{src_pho}文件不在表格中!''')
                # if i + 1 == len(df):
                #     df_na = df[df["姓名"] in fn.replace(' ', '')]
                #     if len(df_na) != 0:
                #         print(df_na)
    df_save.to_excel(dst_excel_file, index=False)


change_name(srcFile, dstFile, excel_file, dst_excel_file, start_no)
