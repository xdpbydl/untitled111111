import pandas as pd
from io import StringIO

file = r'D:\ZCXX\3.0 DGYH\9.temp\c122129911.xlsx'
txt = '''adlkf1  代码1
adlkf3    代码3  
adlkf2         代码2
adlkf5  代码5'''

txt1 = r'D:\ZCXX\3.0 DGYH\9.temp\txt_test.txt'
txt_ss = StringIO(txt)
txt_df = pd.read_csv(txt_ss, sep='\s+', names=['英文代码', '中文代码'], index_col=None, memory_map=True)
file_df = pd.read_excel(file, keep_default_na=False, index_col=None)
file_df = file_df[['英文代码', '中文代码']]
# 重新排序，再比较
txt_df = txt_df.sort_values(by=['英文代码'],ignore_index=True)
file_df = file_df.sort_values(by=['英文代码'],ignore_index=True)

try:
    df3 = txt_df.equals(file_df)
    print('使用 df.equals 检测是否相同:', df3)
except Exception as err:
    print(err)
