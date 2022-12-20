import pandas as pd

Save_Path = r'E:\TEMP\Desktop\\'
jd_file = f'{Save_Path}导出进度.xlsx'

df_data = pd.read_excel(jd_file)
df_data['箱头指令产出日期'] = pd.to_datetime(df_data['箱头指令产出日期'], format='%Y-%m-%d').dt.strftime('%Y-%m-%d')
# # df_data['箱头指令产出日期'] = pd.to_datetime(df_data['箱头指令产出日期']).dt.strftime('%Y-%m-%d')
# # df_data['箱头指令产出日期'] = df_data['箱头指令产出日期'].apply(lambda x:x.strftime('Y-%m-%d'))
# df_data['箱头指令产出日期'] = df_data['箱头指令产出日期'].strftime('%Y-%m-%d')

df_data.to_excel(f'{Save_Path}导出进度1.xlsx', index=False)

print(f'待处理有{len(df_data)}条数据')