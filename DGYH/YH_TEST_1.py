import pandas as pd

file = r'D:\ZCXX\3.0 DGYH\9.temp\c122129911.xlsx'
txt = """adlkf1	代码1
adlkf2	代码2
adlkf4	代码4
adlkf3	代码3"""

txt_list = txt.replace('\t', '').split('\n')
file_df = pd.read_excel(file, keep_default_na=False)
file_txt = file_df['英文代码'] + file_df['中文代码']
is_same = True
if len(file_df) == len(txt_list):
    for i in range(0, len(txt_list)):
        if txt_list[i] not in file_txt.values:
            is_same = False
            print(txt_list[i])
            break
else:
    is_same = False

print(is_same)
