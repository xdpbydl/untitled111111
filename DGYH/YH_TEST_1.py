import pandas as pd
import time
import datetime
file = r'D:\ZCXX\3.0 DGYH\9.temp\c122129911.xlsx'
txt = """adlkf1	代码1
adlkf2	代码2
adlkf4	代码4
adlkf3	代码3  """

txt_list = txt.replace('\t', '').split('\n')
file_df = pd.read_excel(file, keep_default_na=False)
file_txt = file_df[['英文代码','中文代码']]
if len(file_df) == len(txt_list):
    for i in range(0, len(txt_list)):
        if txt_list[i] not in file_txt.values:
            is_same = False
            print(f'--------{txt_list[i]}---')
            break


else:
    is_same = False
im_txt = ''
if not is_same:
    for index, crows in file_txt.iterrows():
        print(type(crows))
        im_txt += crows['英文代码'] + '\t'+ crows['英文代码'] + '\r\n'


# im_txt = file_txt.str.cat(sep='\n', na_rep=None)
print(is_same)
print(im_txt)
print(type(im_txt))

#TODO: LIST ALAL
# print(file_txt.to_string)

cc = datetime.datetime.now().strftime("%Y%m%d%H%M%S%f")
print(cc)


import os
dirs = 'd:\\112\\11\\222'
# if not os.path.exists(dirs):
if not os.path.isdir(dirs):
    os.makedirs(dirs)