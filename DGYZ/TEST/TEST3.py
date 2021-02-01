import pandas as pd
import openpyxl

file = r'D:\ZCXX\3.1 DGYC\2.TEST\111.xlsx'
save_file = r'D:\ZCXX\3.1 DGYC\2.TEST\000.xlsx'
s_row = 16  # 保存的，列位置
s_col = 10  # 保存的，行位置
r_header = 12  # 读取的，表头位置
r_row = 2  # 读取的，行数
r_col = ['A', 'B', 'C', 'D']  # 读取的，列名


def r_s_excel(file, s_row, s_col, save_file, r_header, r_row, r_col):
    df = pd.read_excel(file, header=r_header, keep_default_na=False)
    s_df = df.loc[0:r_row, r_col]

    oxl_excel = openpyxl.load_workbook(save_file, data_only=False)
    sheet = oxl_excel["Sheet1"]
    for i in range(len(s_df)):  # 行
        for r in range(len(s_df.columns)):  # 列
            sheet.cell(row=i + s_col, column=r + s_row, value=s_df.iloc[i, r])

    oxl_excel.save(save_file)


r_s_excel(file, s_row, s_col, save_file, r_header, r_row, r_col)
