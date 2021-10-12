import pandas as pd

file = r'E:\TEMP\6TEST\GRWL\P935\GRWL888888.xlsx'
print(file)
if file == 0:
    print(file)
    #return 0
file_p = ''.join(file.split('.')[0:-1])
print(file_p)
save_file_fqy = f'{file_p}_非简易包装.xlsx'
save_file = f'{file_p}_简易包装.xlsx'
# save_file_hd = f'{file_p}_简易包装_花都导入_总.xlsx'

df_gr = pd.read_excel(file)

df_fqy = df_gr[~df_gr['包装物材质'].str.contains('简易包装')]
df_fqy.to_excel(save_file_fqy, index=False)
df_gr = df_gr[df_gr['箱头供应商'].str.contains('广州花都通用集团有限公司|佛山市欧汇电梯配件有限公司|广州广日物流有限公司')]
df_gr = df_gr[df_gr['包装物材质'].str.contains('简易包装')]
df_gr.drop(['包装物单价'], axis=1, inplace=True)

df_gr.to_excel(save_file, index=False)
df_fqy.to_excel(save_file_fqy, index=False)

print(len(df_gr))
xt_ch = {'佛山市欧汇电梯配件有限公司': '欧汇包装半成品仓', '广州花都通用集团有限公司': '花都包装半成品仓'}
df_gr['仓库'] = df_gr['箱头供应商'].replace(xt_ch)
# im_df = df_gr[df_gr['箱头供应商'] == '广州花都通用集团有限公司']
# im_ouhui = df_gr[df_gr['箱头供应商'] == '佛山欧汇电梯配件有限公司']


im_df = df_gr[['工号', '箱号', '分箱', '仓库']]
im_df.rename(columns={'工号': '产出工号', '箱号': '产出箱号', '分箱': '产出分箱号'}, inplace=True)
im_df = im_df.copy() #
# if im_df.duplicated:
im_df = im_df.drop_duplicates().reset_index(drop=True)

xh_wlno = {'A03': 'MX01RL90A0301HTY', 'D03': 'MX01RL90D0301HTY', 'D16': 'MX01RL90D1601KTY'}
im_df['物料编码'] = im_df['产出箱号'].replace(xh_wlno)
# im_df[['物料名称', '物料规格']] = ''
# im_df['数量'] = 1
im_df = im_df.assign(物料名称='', 物料规格='', 数量=1)
im_df = im_df[['产出工号', '产出箱号', '产出分箱号', '物料名称', '物料规格', '数量', '仓库']]

row_no = 500    #
for k, v in xt_ch.items():
    n = 0
    if k == '广州花都通用集团有限公司':
        f_name = '花都'
    elif k == '佛山市欧汇电梯配件有限公司':
        f_name = '欧汇'
    im_df_fen = im_df[im_df['仓库'] == v]
    for i in range(0, len(im_df_fen), row_no):
        n += 1
        im_temp = im_df_fen.loc[i: i+row_no]
        # if len(im_temp) == 0:
        #     print(f'{file_p}_简易包装_{f_name}导入_{n}.xlsx 文件0行')
        #     break
        im_temp.to_excel(f'{file_p}_简易包装_{f_name}导入_{n}.xlsx', index=False)
    if len(im_df_fen) == 0:
        print(f'{file_p}_简易包装_{f_name}导入_总.xlsx 文件0行')
    im_df_fen.to_excel(f'{file_p}_简易包装_{f_name}导入_总.xlsx', index=False)

print('000')