import re
import pandas as pd

riqi = '2022-07-26'
gv_File_Path = r'E:\TEMP\6TEST\GRRPA\DuiChongKuai\\'
gv_Save_Path = r'E:\TEMP\6TEST\GRRPA\DuiChongKuai\20220726_1\\'

#
songhuodan = f'{gv_Save_Path}export_soghuodan.xlsx'
save_file = f'{gv_Save_Path}11.xlsx'
save_guige = f'{gv_Save_Path}guige.xlsx'
guige_file = f'{gv_Save_Path}清单_all.xls'



#  模版
file2 = f'{gv_File_Path}model\\2020-7-11供应商分配第一批.xlsx'
#  新的文件
file3 = f'''{gv_Save_Path}{riqi.replace('-','')}供应商分配第一批_new.xlsx'''

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

# 2022-08-17 1/3 修改guige_df，为guige_df_0
guige_df_0 = pd.read_excel(guige_file, index=False)

# guige_df = pd.DataFrame(guige_df[0])
# 2022-08-17 2/3 增加对照表，采用对照表中的规格。
duizhao_file = f'{gv_File_Path}Model\\日立对重块 规格对照表.xlsx'
duizhao_df = pd.read_excel(duizhao_file, index=False)
duizhao_df.drop(['序号', '图号', '备注'], axis=1, inplace=True)
guige_df = pd.merge(guige_df_0, duizhao_df, how='left', left_on=['物料号'], right_on=['物料编码'], left_index=False, right_index=False)
guige_df['备注'] = guige_df['型号']
guige_df['备注'] = guige_df['备注'].str.replace('*', '×')


# 20201126 ，不是只取R的物料
# guige_df = guige_df[guige_df['物料号'].str.contains('R')]

# 20210704 ，排除”物料号“为X，"图号"为F开始  的数据
guige_df = guige_df[~guige_df['物料号'].str.startswith('X')]
guige_df["图号"]=guige_df["图号"].astype(str)
guige_df = guige_df[~guige_df['图号'].str.startswith('F')]


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

# 2021-07-04增加
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
# 2022-06-30 1/5 增加'作业'列
guige_1 = guige_df[['工号', '分箱', '备注', '作业']]   # 2020-10-19   增加根据分箱号，决定规格

# 2022-06-30 2/5 增加'作业'列
guige_2=guige_1.groupby(['工号', '分箱', '作业'])['备注'].apply(lambda x:x.str.cat(sep=r',')).reset_index()         # 2020-10-19   增加根据分箱号，决定规格
guige_2.to_excel(save_guige, index=False)

# 匹配
# print(df1)
df1['分箱'] = df1['工号箱头分箱'].str[-1]       # 2020-10-19   增加根据分箱号，决定规格

df1 = pd.merge(df1,guige_2,how='left', left_on=['分箱', "选择"],right_on=['分箱', "工号"],left_index=False,right_index=False)
# print(df1)
df1['PO行号'] =df1['备注']
df1.drop(['工号','分箱', '备注'], axis=1, inplace=True)

# 2022-06-30 3/5 增加'作业'列，改变列顺序
df_id = df1['作业']
df1 = df1.drop('作业' ,axis=1)
df1.insert(5, '作业' ,df_id)

df1.to_excel(save_file, index=False)


# # 2022-01-11 # # 新增配重块到分配表
# 2022-08-17 3/3 物料编码.xlsx统一改为 日立对重块 规格对照表.xlsx文件
# wuliao_file = gv_File_Path + r'\model\物料编码.xlsx'
wuliao_df = pd.read_excel(duizhao_file)
qingdan_df = pd.read_excel(guige_file)
# 取‘物料编码.xlsx’中的配重块规格
wuliao_df = wuliao_df[wuliao_df['备注'] == '配重块']
wuliao_df['型号'] = wuliao_df['型号'].str.replace('*', '×')
# 送货单去重
df['PO编号'].drop_duplicates(inplace=True)
# 清单_all 【物料名称】 选取’配重块‘
qingdan_df = qingdan_df[qingdan_df['物料名称'] == '配重块']
qingdan_df = pd.merge(qingdan_df, wuliao_df, how='left', left_on='物料号', right_on='物料编码', left_index=False, right_index=False)
peichong_df = pd.DataFrame()

for k, i in df['PO编号'].iteritems():
    i_v = pd.DataFrame()
    i_v = qingdan_df[qingdan_df['PO号'] == i]
    if len(i_v) != 0:
        peichong_df = peichong_df.append(i_v, ignore_index=True)

# 20220729 配重块不存在时，异常try处理
try:
    peichong_df[['数量']] = peichong_df[['数量']].applymap(str)
    peichong_df['规格'] = peichong_df['型号'] + '=' + peichong_df['数量']
    peichong_list = peichong_df[['PO号', '工号', '规格']].values.tolist()
except:
    peichong_list = []

for k, i, g in peichong_list:
    k_i_g = pd.DataFrame()
    k_i_g = df1[(df1['PO编号'] == k) & (df1['选择'] == i)]
    if len(k_i_g) != 0:
        k_i_g.loc[:, ['工号箱头分箱', '箱头描述', 'PO行号']] = '', '配重块', g
        df1 = df1.append(k_i_g, ignore_index=True, sort=False)

#  按两列升序排序
df1 = df1.sort_values(by=['PO编号', '选择'], ascending=[True, True])
# # 2022-01-11 # # 新增配重块到分配表



############合成############


#df1 = pd.read_excel(save_file, index=False)
df2 = pd.read_excel(file2, index=False)



# # 插入空行\文件名\行数
# 2022-06-30 4/5 增加'作业'列，改变列数   #
# 2022-06-30 5/5 'model'模板中增加'作业'列
line_no = len(df1)
file_name = riqi + '供应商分配_new'
df2_no = len(df2)
for i in range(5):      # 5行
    df2.loc[df2_no+i] = ['' for n in range(22)]   # 21列
df2.iloc[df2_no+4, 1] = file_name
df2.iloc[df2_no+4, 2] = line_no




df3 = df2.append(df1, ignore_index=True, sort=False)

df3.to_excel(file3,index=False, header=False)
