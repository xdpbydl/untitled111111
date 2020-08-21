import pandas as pd
import numpy as np
songhuodan = r'E:\TEMP\02GR\export_soghuodan.xlsx'
save_file = r'E:\TEMP\02GR\11.xlsx'
save_guige =  r'E:\TEMP\02GR\guige.xlsx'

guige_file = r'E:\TEMP\02GR\清单900931335.xls'
#  模版
file2 = r'E:\TEMP\02GR\model\2020-7-11供应商分配第一批.xlsx'
#  新的文件
file3 = r'E:\TEMP\02GR\2020-7-11供应商分配第一批_new.xlsx'


df = pd.read_excel(songhuodan)
#  删除无效列
df = df.loc[:, ~df.columns.str.contains('Unnamed')]

index=[0, 1]


df['选择']=df.工号箱头分箱.str[:9]

############整理excel############

# print(df)
#  删除两列

df.drop(['箱头版本', '最新箱头版本'], axis=1, inplace=True)
#  清除两列数据
df['PO行号'] = ''
df['PO数量'] = ''
# print(df)
#  按两列升序排序
df1 = df.sort_values(by=['PO编号', '工号箱头分箱'], ascending=[True, True])


############规格匹配############


guige_df = pd.read_html(guige_file)

guige_df = pd.DataFrame(guige_df[0])

guige_df.columns=guige_df.iloc[0]

guige_df = guige_df[guige_df['物料号'].str.contains('R')]



def guige(x):
    x = str(x)
    if x == '':
        return ''
    else:
        x_1 = x.split(',')[0]
        return x_1


# “规格”列部分可能为空，采用“备注”列，
guige_df["备注"] = guige_df["备注"].apply(guige)
guige_df["备注"] = guige_df["备注"]+'='+ guige_df["数量"]

# print(df["规格"]+'='+ df["数量"])
guige_1 = guige_df[['工号', '备注']]
# print(guige_1)
# group = guige_1 .groupby('工号').sum()
# print(group)

guige_2=guige_1.groupby('工号')['备注'].apply(lambda x:x.str.cat(sep=r',')).reset_index()
guige_2.to_excel(save_guige, index=False)

# 匹配
# print(df1)

# DFinal = df1.merge(df1,guige_2,left_on=["工号"],right_on=["room",how="outer"],left_index=False,right_index=False)
df1 = pd.merge(df1,guige_2,how='left', left_on=["选择"],right_on=["工号"],left_index=False,right_index=False)
# print(df1)
df1['PO行号'] =df1['备注']
df1.drop(['工号', '备注'], axis=1, inplace=True)
df1.to_excel(save_file, index=False)




############合成############


#df1 = pd.read_excel(save_file, index=False)
df2 = pd.read_excel(file2, index=False)


# # 插入空行\文件名\行数
# line_no = len(df1)
# file_name = '2020-7-11供应商分配第一批_new'
# df2_no = len(df2)
# print(df2)
# for i in range(4):
#     df.loc[df2_no+i] = [np.NaN, np.NaN, np.NaN, np.NaN, np.NaN,np.NaN, np.NaN, np.NaN, np.NaN, np.NaN,np.NaN, np.NaN, np.NaN, np.NaN, np.NaN,np.NaN, np.NaN, np.NaN, np.NaN, np.NaN]
# df.loc[df2_no+5] = [np.NaN, np.NaN, file_name, line_no, np.NaN,np.NaN, np.NaN, np.NaN, np.NaN, np.NaN,np.NaN, np.NaN, np.NaN, np.NaN, np.NaN,np.NaN, np.NaN, np.NaN, np.NaN, np.NaN]
# df2.insert(3,file_name)
# print(df2)


df3 = df2.append(df1, ignore_index=True, sort=False)

df3.to_excel(file3,index=False, header=False)