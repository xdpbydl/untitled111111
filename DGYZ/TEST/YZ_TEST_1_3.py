import pandas as pd


file = r'E:\TEMP\6TEST\111.xls'
df_source = pd.read_excel(file, header=1, keep_default_na=False, sheet_name='个人网银1', usecols='B, E, G, I, K, M, O, Q, S, U, W, Y, AA', nrows=42)
# df_model = pd.read_excel(excel_dict[i]['model_file'], header=3, keep_default_na=False,
#                          sheet_name=data['s_sheel'], usecols='E', nrows=51)
df_source = df_source.fillna('')

print(df_source[df_source.机构号 == 441901019])
# 富华路，并入和大朗？
df_source.iloc[df_source[df_source.机构号 == 441901019].index, 1:] += df_source.iloc[df_source[df_source.机构号 == 441901321][0].index, 1:]
df_source.iloc[7, 1:] += df_source.iloc[38, 1:]
print(df_source[df_source.机构号 == 441901019])