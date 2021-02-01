import openpyxl
import pandas as pd

file_path = 'D:\\ZCXX\\3.1 DGYC\\1. 文档\整理文档\\2、邮储银行各镇街贷款统计表\\来源\\'
save_path = 'E:\\TEMP\\6TEST\\'
model_path = 'E:\\TEMP\\6TEST\\model\\'


excel_dict = {
    0: {'name': 'GF0103-191-存贷款明细报表-2020年12月月报（第一批次）.xlsx', 'daily_name': 'A3701商业银行日报表_汇总表（人民币）_20201130_东莞市分行(44001444).xls',
        'data': {'s_row': 0, 's_col': 0, 's_sheel': '1.A3701(人民币)', 'r_header': 0, 'r_row_len': 82, 'r_col': 'A:EA',
                 'r_sheel': 1}},
}


def r_s_excel(file, s_col, s_row, s_sheel, model_file, r_header, r_row_len, r_col, r_sheel, save_file):
    print(model_file)
    df = pd.read_excel(file, header=r_header, keep_default_na=False, sheet_name=r_sheel, usecols=r_col)
    s_df = df.loc[0:r_row_len - 1]

    oxl_excel = openpyxl.load_workbook(model_file, data_only=False)
    sheet = oxl_excel[s_sheel]
    for i in range(len(s_df)):  # 行
        for r in range(len(s_df.columns)):  # 列
            if s_df.iloc[i, r] == '':
                print(f'-----111---------{s_df.iloc[i, r]}---')
                continue
            else:
                print(f'-----222---------{s_df.iloc[i, r]}---')
                sheet.cell(row=i + s_col, column=r + s_row, value=s_df.iloc[i, r])

    oxl_excel.save(save_file)


for i, v in excel_dict.items():
    # print(i, v['data'])
    daily_file = f"{file_path}{v['daily_name']}"
    model_file = f"{model_path}{v['name']}"
    save_file = f"{save_path}{v['name']}"
    data = v['data']
    r_s_excel(daily_file, data['s_row'], data['s_col'], data['s_sheel'], model_file, data['r_header'],
              data['r_row_len'], data['r_col'], data['r_sheel'], save_file)
