import openpyxl
import pandas as pd

file_path = 'D:\\ZCXX\\3.1 DGYC\\1. 文档\整理文档\\1、监管月报一批(8份)\\'
save_path = 'E:\\TEMP\\6TEST\\'
model_path = 'E:\\TEMP\\6TEST\\model\\'
daily_name = '202006-监管报表.xlsx'

excel_dict = {
    0: {'model_file': 'GF0103-191-存贷款明细报表-2020年12月月报（第一批次）.xlsx', 'source_file': daily_name, 'save_file': '',
        'data': {'s_row': 6, 's_col': 3, 's_sheel': 'GF0103', 'r_header': 4, 'r_row_len': 32, 'r_col': 'C:E',
                 'r_sheel': '存贷明细'}},
    1: {'model_file': 'GF0100-181-资产负债项目统计表-2020年12月月报（第一批次）.xlsx', 'source_file': daily_name, 'save_file': '',
        'data': {'s_row': 5, 's_col': 3, 's_sheel': 'GF0100', 'r_header': 3, 'r_row_len': 130, 'r_col': 'C:E',
                 'r_sheel': 'G01'}},
    2: {'model_file': 'GF0102-201-贷款质量五级分类情况简表-2020年12月月报（第一批次）.xlsx', 'source_file': daily_name, 'save_file': '',
        'data': {'s_row': 6, 's_col': 3, 's_sheel': 'GF0102', 'r_header': 4, 'r_row_len': 11, 'r_col': 'C',
                 'r_sheel': '小五级'}},
    3: {'model_file': 'GF0109-161-存贷款月日均情况表-2020年12月月报（第一批次）.xlsx', 'source_file': daily_name, 'save_file': '',
        'data': {'s_row': 6, 's_col': 3, 's_sheel': 'GF0109', 'r_header': 4, 'r_row_len': 11, 'r_col': 'C:E',
                 'r_sheel': '日均'}},
    4: {'model_file': 'SF6301-201-大中小微型企业贷款情况表-2020年12月月报（第一批次）.xlsx', 'source_file': daily_name, 'save_file': '',
        'data': {'s_row': 6, 's_col': 3, 's_sheel': 'SF6301', 'r_header': 4, 'r_row_len': 37, 'r_col': 'C:I',
                 'r_sheel': 'S6301'}},
    5: {'model_file': 'GF0101-161-表外业务情况表-2020年12月月报（第一批次）.xlsx', 'source_file': daily_name, 'save_file': '',
        'data': {'s_row': 6, 's_col': 4, 's_sheel': 'GF0101', 'r_header': 3, 'r_row_len': 39, 'r_col': 'D:E',
                 'r_sheel': '附注'}},
}


def r_s_excel(source_file, s_col, s_row, s_sheel, model_file, r_header, r_row_len, r_col, r_sheel, save_file):
    print(source_file)
    df = pd.read_excel(source_file, header=r_header, keep_default_na=False, sheet_name=r_sheel, usecols=r_col)
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
    source_file = f"{file_path}{v['source_file']}"
    model_file = f"{model_path}{v['model_file']}"
    save_file = f"{save_path}{v['source_file']}"
    data = v['data']
    r_s_excel(source_file, data['s_row'], data['s_col'], data['s_sheel'], model_file, data['r_header'],
              data['r_row_len'], data['r_col'], data['r_sheel'], save_file)
