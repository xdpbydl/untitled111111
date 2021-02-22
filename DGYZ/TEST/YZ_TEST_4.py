import openpyxl
import pandas as pd
from win32com.client import Dispatch

file_path = 'E:\\TEMP\\6TEST\\DGYC4\\源文件\\'
save_path = 'E:\\TEMP\\6TEST\\DGYC4\\'
model_path = 'E:\\TEMP\\6TEST\\DGYC4\\model\\'

"""参数说明'type'为 'copy': r_row_len为总共需要取行数，r_col 为源数据取数的列名字符； 
'type'为 'openpyxl' 可以取公式代表的值。其中 r_row_len为总共需要取【开始行，结束行+1】，r_col【开始列，结束列+1】；
s_row, s_col都为保存的开始行列"""
excel_dict = {
    0: {'model_file': f'{save_path}2020年11月金融统计信息（业务）.xlsx',  # 空白.xlsx    2020年11月金融统计信息（业务）.xlsx
        'source_file': f'{file_path}存贷增减草稿2019.xlsx',
        'save_file': f'{save_path}2020年11月金融统计信息（业务）.xlsx',
        'type': 'pd_data', 'data': {'s_row': 5, 's_col': 4, 's_sheel': '全市存贷增长',
                                    'r_header': 0, 'r_row_len': 42, 'r_col': 'C:F', 'r_sheel': '202011'}},
    1: {'model_file': f'{save_path}2020年11月金融统计信息（业务）.xlsx',  # 空白.xlsx    2020年11月金融统计信息（业务）.xlsx
        'source_file': f'{file_path}存贷增减草稿2019.xlsx',
        'save_file': f'{save_path}2020年11月金融统计信息（业务）.xlsx',
        'type': 'pd_data', 'data': {'s_row': 5, 's_col': 4, 's_sheel': '全市存贷增长',
                                    'r_header': 0, 'r_row_len': 43, 'r_col': 'C:F', 'r_sheel': '202011'}},
}


def source_data(source_file, header, cols, txt_list):
    """部分需要逻辑处理的取数"""
    df = pd.read_excel(source_file, header=header, keep_default_na=False)
    txt_list = txt_list
    df1 = df[df[cols].isin(txt_list)]
    df1 = df1.iloc[:, 2:]  # 只取第3列及后面的数据
    return df1


def add_fixed_cols(df, up_cols, add_col, fill_value):
    """在up_cols列，后面增加固定的一列，add_col,设置默认值为fill_value"""
    df_columns = df.columns.tolist()
    df_columns.insert(df_columns.index(up_cols) + 1, add_col)  # 在 '一级支行' 列后面插入'客户数量'
    # df.insert(up_cols, add_col)  # 在 up_cols 索引列后面插入add_col列
    df = df.reindex(columns=df_columns, fill_value=fill_value)  # fill_value 为默认值
    return df


def flag_no(i):
    """提供统一取数，方便函数调用"""
    source_file = excel_dict[i]['source_file']
    print(source_file)
    data = excel_dict[i]['data']
    if i == 0:
        df = pd.read_excel(excel_dict[i]['source_file'], header=data['r_header'], keep_default_na=False,
                           sheet_name=data['r_sheel'], usecols=data['r_col'], nrows=data['r_row_len'], index_col=None)
        df = df.reindex(columns=['本月各项存', '排名1', '本月个人', '排名2', '本月单位', '排名3', '本月各项贷款', '排名4'], fill_value='')
        print(df)
        model_df = pd.read_excel(excel_dict[i]['model_file'], header=3, keep_default_na=False,
                                 sheet_name=data['s_sheel'], usecols='D:K', nrows=data['r_row_len'], index_col=None)    # usecols='L:R'
        print('------df', df.info())
        print('------model_df', model_df.info())
        model_df = model_df.reindex(columns=['本年各项存', '排名5', '本年个人存款', '排名6', '本年单位存款', '排名7', '本年各项贷款', '排名8'],
                                    fill_value='')
        print(model_df)
        input()
        df0 = df.join(model_df)
        # df0 = df0.astype('float')
        print('-1-----df0', df0.info())
        df0['本年各项存'] = df0['本年各项存'].astype('float64')
        print('-2-----df0', df0.info())

        df0['本年各项存'] = df0['本月各项存'] + df0['本年各项存']
        df0['本年个人存款'] = df0['本月个人'] + df0['本年个人存款']
        df0['本年单位存款'] = df0['本月单位'] + df0['本年单位存款']
        df0['本年各项贷款'] = df0['本月各项存'] + df0['本年各项贷款']
        input()

        return df0
    elif i == 1:
        df1 = pd.read_excel(excel_dict[i]['source_file'], header=3, keep_default_na=False,
                            sheet_name=data['r_sheel'], usecols=data['r_col'], nrows=data['r_row_len'])
        return df1
    elif i == 3:
        df3 = source_data(source_file=source_file, header=data['r_header'], cols='指标代码',
                          txt_list=['AA370137002', 'AA370136025', 'AA370136031'])
        return df3
    else:
        return 0


def just_open(filename):
    """防止读取excel公式为None"""
    xlApp = Dispatch("Excel.Application")
    xlApp.Visible = False
    xlBook = xlApp.Workbooks.Open(filename)
    xlBook.Save()
    xlBook.Close()


def r_s_excel(source_file, s_row, s_col, s_sheel, model_file, r_header, r_row_len, r_col, r_sheel, save_file, type, df):
    """从源文件 复制数据到 模板格式文件，再保存到结果文件"""
    print(f'--处理文件为：{source_file}-----')
    if type == 'openpyxl':
        just_open(source_file)
        source_excel = openpyxl.load_workbook(source_file, data_only=True)
        model_excel = openpyxl.load_workbook(model_file, data_only=False)
        source_sheet = source_excel[r_sheel]
        model_sheet = model_excel[s_sheel]
        dif_col = s_col - r_col[0]
        dif_row = s_row - r_row_len[0]
        for i in range(r_row_len[0], r_row_len[1]):  # 行
            for r in range(r_col[0], r_col[1]):  # 列
                print(source_sheet.cell(row=i, column=r).value)
                model_sheet.cell(row=i + dif_row, column=r + dif_col).value = source_sheet.cell(row=i, column=r).value
    elif type == 'pd_data':
        df = df
        # print(df)
        # input()
        model_excel = openpyxl.load_workbook(model_file, data_only=False)
        sheet = model_excel[s_sheel]
        for i in range(len(df)):  # 行
            for r in range(len(df.columns)):  # 列a
                if df.iloc[i, r] == '':
                    print(f'-----111---------{df.iloc[i, r]}---')
                    continue
                else:
                    print(f'-----222---------{df.iloc[i, r]}---')
                    sheet.cell(row=i + s_row, column=r + s_col, value=df.iloc[i, r])
    model_excel.save(save_file)
    model_excel.close()


for i, v in excel_dict.items():
    if i != 0:
        continue
    print(f'--处理序号为：{i}-----')
    source_file = v['source_file']
    model_file = v['model_file']
    save_file = v['save_file']
    data = v['data']
    r_s_excel(source_file, data['s_row'], data['s_col'], data['s_sheel'], model_file, data['r_header'],
              data['r_row_len'], data['r_col'], data['r_sheel'], save_file, v['type'], df=flag_no(i))
