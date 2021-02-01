import pandas as pd
import openpyxl
from win32com.client import Dispatch


file = 'E:\\TEMP\\6TEST\\model\\GF0100-181-资产负债项目统计表-2020年12月月报（第一批次）.xlsx'
project_statistics = 'E:\\TEMP\\6TEST\\GF0100-181-资产负债项目统计表-2020年12月月报（第一批次）.xlsx'
daily_file = 'D:\\ZCXX\\3.1 DGYC\\1. 文档\整理文档\\1、监管月报一批(8份)\\202006-监管报表.xlsx'
df = pd.read_excel(daily_file, sheet_name='G01', usecols='C:E', header=3)
df = df.loc[0:130]
print(df)