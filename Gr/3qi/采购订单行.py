import pandas as pd

mingxi_file = r'E:\TEMP\6TEST\GRRPA\采购订单行明细.xlsx'
e9_file = r'E:\TEMP\6TEST\GRRPA\采购订单行明细_导入E9.xlsx'
file = r'E:\TEMP\6TEST\GRRPA\\'

excel_name = {1: '1.1.1 A03架机梁.xlsx', 2: '1.1.2 D02钢丝绳.xlsx', 3: '1.1.3 D10油压缓冲器.xlsx', 4: '1.1.4 D05对重块_B07配重块.xlsx', 20: '1.2 包装类.xlsx',
              30: '1.3 缓冲器_安全钳_.xlsx', 99: '9.9 其他未归类的.xlsx', 40: '1.4 机加工散件.xlsx', 0: '0.TEST.xlsx'}     # 20221010 1    增加 机加工散件


df = pd.read_excel(mingxi_file)
df = df.sort_values(by=['需要日期', 'PO编号'], ascending=[True, True])
df_wuliao = df[df['物料'] == 'WGXT01']

# 1/ 对照表
dzh_file = r'E:\TEMP\6TEST\GRRPA\接单_物料对应分类.xlsx'
dzh_df = pd.read_excel(dzh_file)
dzh_df = dzh_df[['明细物料', '分类']]

# 缓冲器或安全钳，或临单
df_lindan = df[(df['物料'].str.startswith('R')) | (df['物料'].str.startswith('A'))]
ld_fl = pd.merge(df_lindan, dzh_df, how='left', left_on='物料', right_on='明细物料')
df_huanc = ld_fl[ld_fl['分类'] == '安全钳']

df_huanc.drop(['明细物料', '分类'], axis=1, inplace=True)
df_huanc.to_excel(f'{file}{excel_name[30]}', index=False)

# A03架机梁
df_A03 = df_wuliao[df_wuliao['说明'].str.contains('架机梁') & df_wuliao['说明'].str.contains('A03')]
df_A03.to_excel(f'{file}{excel_name[1]}', index=False)

# D02钢丝绳
df_D02 = df_wuliao[df_wuliao['说明'].str.contains('钢丝绳') & df_wuliao['说明'].str.contains('D02')]
df_D02_ld = ld_fl[ld_fl['分类'] == '钢丝绳']
df_D02_ld.drop(['明细物料', '分类'], axis=1, inplace=True)
df_D02 = df_D02.append(df_D02_ld)
df_D02.to_excel(f'{file}{excel_name[2]}', index=False)

# D10油压缓冲器
df_D10 = df_wuliao[df_wuliao['说明'].str.contains('油压缓冲器') & df_wuliao['说明'].str.contains('D10')]
df_D10_ld = ld_fl[ld_fl['分类'] == '油压缓冲器']
df_D10_ld.drop(['明细物料', '分类'], axis=1, inplace=True)
df_D10 = df_D10.append(df_D10_ld)
df_D10.to_excel(f'{file}{excel_name[3]}', index=False)

# D05对重块、B07配重块
df_D05 = df_wuliao[df_wuliao['说明'].str.contains('对重块') & df_wuliao['说明'].str.contains('D05')]
df_B07 = df_wuliao[df_wuliao['说明'].str.contains('配重块') & df_wuliao['说明'].str.contains('B07')]
df_DB_ld = ld_fl[ld_fl['分类'] == '对重块']
df_DB_ld.drop(['明细物料', '分类'], axis=1, inplace=True)
df_DB = pd.concat([df_D05, df_B07, df_DB_ld])
df_DB.to_excel(f'{file}{excel_name[4]}', index=False)

# 包装类
df_baoz = df[df['物料'].str.startswith('X')]
df_baoz.to_excel(f'{file}{excel_name[20]}', index=False)


# 20221010 2/3    增加 机加工散件
ld_fl_T = pd.merge(df, dzh_df, how='left', left_on='物料', right_on='明细物料')
df_jjgsj_ld = ld_fl_T[ld_fl_T['分类'] == '机加工散件']
df_jjgsj_ld.drop(['明细物料', '分类'], axis=1, inplace=True)
ld_fl.to_excel(f'{file}{excel_name[0]}', index=False)
if len(df_jjgsj_ld) !=0:
    df_jjgsj_ld.to_excel(f'{file}{excel_name[40]}', index=False)
else:
    print('机加工散件, 数据为空。')

# 20221010 3/3    增加 机加工散件
# 其他未归类的
df_99 = pd.concat([df_A03, df_D02, df_D10, df_DB, df_baoz, df_huanc, df, df_jjgsj_ld]).drop_duplicates(keep=False, ignore_index=True)
if len(df_99) != 0:
    df_99.to_excel(f'{file}{excel_name[99]}', index=False)
else:
    print('没有未归类的数据。')
print([len(i) for i in [df_A03, df_D02, df_D10, df_DB, df_baoz, df_huanc, df_99, df, df_jjgsj_ld]])

# 处理导入的文件
df.insert(0, '客户', value='日立电梯（中国）有限公司广州工厂')

# df['需要日期'] = pd.to_datetime(df['需要日期'], format='%Y-%m-%d').dt.date
df['需要日期'] = pd.to_datetime(df['需要日期'], format='%Y-%m-%d').dt.strftime('%Y-%#m-%#d')
df['作业指令产出日期'] = pd.to_datetime(df['作业指令产出日期'], format='%Y-%m-%d').dt.strftime('%Y-%#m-%#d')

df.to_excel(e9_file, index=False)
# 需要日期、
