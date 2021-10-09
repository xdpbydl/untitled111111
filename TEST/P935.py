import pandas as pd


file = r'E:\TEMP\6TEST\GRWL\P935\20210914_1\GRWL888888.xlsx'
save_file = r'E:\TEMP\6TEST\GRWL\P935\20210914_1\GRWL888888_SAVE.xlsx'
save_file_1 = r'E:\TEMP\6TEST\GRWL\P935\20210914_1\GRWL888888_SAVE——1.xlsx'
file_p = ''.join(file.split('.')[0:-1])
print(type(file_p))
print(file_p)
df_gr = pd.read_excel(file)

df_fqy = df_gr[~df_gr['包装物材质'].str.contains('简易包装')]
df_gr = df_gr[df_gr['箱头供应商'].str.contains('广州花都通用集团有限公司|佛山欧汇电梯配件有限公司|广州广日物流有限公司')]
df_gr = df_gr[df_gr['包装物材质'].str.contains('简易包装')]
df_gr.drop(['包装物单价'], axis=1, inplace=True)


df_gr.to_excel(save_file, index=False)
df_fqy.to_excel(save_file_1, index=False)
