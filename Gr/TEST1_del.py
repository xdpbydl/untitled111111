
import pandas as pd

file_path = 'E:\\ZCXX\\东莞邮政\\1.需求\给开发-\\'
jieju_file1 = f'{file_path}result2020-12-10----08-51-07(1).xls'

jieju_df = pd.read_html(jieju_file1, keep_default_na=False)


jieju_df = pd.DataFrame(jieju_df[0])
# print(df.iloc[3])
# jieju_df.columns=jieju_df.iloc[0]

print(jieju_df)