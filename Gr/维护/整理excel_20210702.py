import pandas as pd
import re


file_path = 'E:\\TEMP\\6TEST\\GRWL\\'
songhuodan = f'{file_path}export_soghuodan.xlsx'
save_file = f'{file_path}11.xlsx'
save_guige = f'{file_path}guige.xlsx'

guige_file = f'{file_path}清单_all.xls'
#  模版
file2 = f'{file_path}model\\2020-7-11供应商分配第一批.xlsx'
#  新的文件
file3 = f'{file_path}2020-7-11供应商分配第一批_new.xlsx'




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


guige_df = pd.read_excel(guige_file, index=False)

# guige_df = pd.DataFrame(guige_df[0])

guige_df.to_excel(f'{file_path}0704_11.xlsx')
# 20210702 ，排除”物料号“为X，"图号"为FA开始  的数据
guige_df = guige_df[~guige_df['物料号'].str.startswith('X')]
guige_df.to_excel(f'{file_path}0704_12.xlsx')
guige_df["图号"]=guige_df["图号"].astype(str)
guige_df.to_excel(f'{file_path}0704_13.xlsx')
# guige_df['图号'].fillna('@@@', inplace=True)
# clean_z[clean_z==''] = '@@@'
# guige_df['图号'] = clean_z

guige_df = guige_df[~guige_df['图号'].str.startswith('F')]
guige_df.to_excel(f'{file_path}0704_14.xlsx')

# print(guige_df['物料号'])



def guige(x):
#    x = str(x)
#    if x == r'备注':
#        pass
#    elif x == '':
#        return ''
#    else:
#        x_1 = x.split(r',')[0]
#        x_2 = x_1.split(r'，')[0]  # 分隔符,写一起报错
#        x_3 = x_2.split()[0]
#        return x_3
#
    if x != '':
        x1 = re.findall(r'\d{1,}×\d{1,}×\d{1,}', str(x))
        if len(x1) == 0:
            x1 = re.findall(r'\d{1,}×\d{1,}', str(x))
            if len(x1) == 0:
                return ''
        return x1[0]
    else:
        return ''


# “规格”列部分可能为空，采用“备注”列，

# 2021-04-09增加
guige_df["规格"] = guige_df["规格"].apply(guige)
guige_df["备注"] = guige_df["备注"].apply(guige)
# 备注 为""时，使用规格,不为空时，使用原值。
guige_df["备注"].mask(guige_df["备注"]=="", guige_df["规格"], inplace=True)

#print(guige_df[guige_df["备注"]=="# /"])



# 转换为字符串
guige_df = guige_df.applymap(str)

# 删除"备注" 为空的行  20201116
guige_df = guige_df[guige_df["备注"] != '']

guige_df["备注"] = guige_df["备注"]+'='+ guige_df["数量"]

#print(str(guige_df["备注"]))
guige_1 = guige_df[['工号', '分箱', '备注']]   # 2020-10-19   增加根据分箱号，决定规格


guige_2=guige_1.groupby(['工号', '分箱'])['备注'].apply(lambda x:x.str.cat(sep=r',')).reset_index()         # 2020-10-19   增加根据分箱号，决定规格
guige_2.to_excel(save_guige, index=False)

# 匹配
# print(df1)
df1['分箱'] = df1['工号箱头分箱'].str[-1]       # 2020-10-19   增加根据分箱号，决定规格

df1 = pd.merge(df1,guige_2,how='left', left_on=['分箱', "选择"],right_on=['分箱', "工号"],left_index=False,right_index=False)
# print(df1)
df1['PO行号'] =df1['备注']
df1.drop(['工号','分箱', '备注'], axis=1, inplace=True)
df1.to_excel(save_file, index=False)




############合成############


#df1 = pd.read_excel(save_file, index=False)
df2 = pd.read_excel(file2, index=False)



# # 插入空行\文件名\行数
line_no = len(df1)
file_name = 'riqi0702' + '供应商分配_new'
df2_no = len(df2)
for i in range(5):      # 5行
    df2.loc[df2_no+i] = ['' for n in range(21)]   # 21列
df2.iloc[df2_no+4, 1] = file_name
df2.iloc[df2_no+4, 2] = line_no




df3 = df2.append(df1, ignore_index=True, sort=False)

df3.to_excel(file3,index=False, header=False)
