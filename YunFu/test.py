# -*- coding: utf-8 -*-


import pandas as pd

srcFile = r'E:\TEMP\01YZ\图片\初一级学生'
dstFile = r'E:\TEMP\01YZ\改后的'
excel_fiel = r'E:\TEMP\01YZ\车牌对应\s\excel\云浮中学初一级学生、老师基础信息录入__导入.xls'

df = pd.read_excel(excel_fiel, index=False)
print()