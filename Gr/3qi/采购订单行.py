import pandas as pd

mingxi_file = r'E:\TEMP\6TEST\GRRPA\采购订单行明细.xlsx'
e9_file = r'E:\TEMP\6TEST\GRRPA\采购订单行明细_导入E9.xlsx'
file = r'E:\TEMP\6TEST\GRRPA\\'
excel_name = {1: '1.1.1 A03架机梁.xlsx', 2: '1.1.2 D02钢丝绳.xlsx', 3: '1.1.3 D10油压缓冲器.xlsx', 4: '1.1.4 D05对重块_B07配重块.xlsx', 20: '1.2 包装类.xlsx', 30: '1.3 缓冲器_安全钳_.xlsx', 99: '9.9 其他未归类的.xlsx'}

df = pd.read_excel(mingxi_file)
df = df.sort_values(by=[ '需要日期', 'PO编号'], ascending=[True, True])
df_wuliao = df[df['物料'] == 'WGXT01']

# A03架机梁
df_A03 = df_wuliao[df_wuliao['说明'].str.contains('架机梁') & df_wuliao['说明'].str.contains('A03')]
df_A03.to_excel(f'{file}{excel_name[1]}', index=False)


# D02钢丝绳
df_D02 = df_wuliao[df_wuliao['说明'].str.contains('钢丝绳') & df_wuliao['说明'].str.contains('D02')]
df_D02.to_excel(f'{file}{excel_name[2]}', index=False)


# D10油压缓冲器
df_D10 = df_wuliao[df_wuliao['说明'].str.contains('油压缓冲器') & df_wuliao['说明'].str.contains('D10')]
df_D10.to_excel(f'{file}{excel_name[3]}', index=False)


# D05对重块、B07配重块
df_D05 = df_wuliao[df_wuliao['说明'].str.contains('对重块') & df_wuliao['说明'].str.contains('D05')]
df_B07 = df_wuliao[df_wuliao['说明'].str.contains('配重块') & df_wuliao['说明'].str.contains('B07')]
df_DB = df_D05.append(df_B07)
df_DB.to_excel(f'{file}{excel_name[4]}', index=False)


# 包装类
df_baoz = df[df['物料'].str.startswith('X')]
df_baoz.to_excel(f'{file}{excel_name[20]}', index=False)


# 缓冲器或安全钳，或临单
df_huanc = df[(df['物料'].str.startswith('R')) | (df['物料'].str.startswith('A'))]
df_huanc.to_excel(f'{file}{excel_name[30]}', index=False)


# 其他未归类的
df_99 = pd.concat([df_A03, df_D02, df_D10, df_DB, df_baoz, df_huanc, df]).drop_duplicates(keep=False, ignore_index=True)
if len(df_99) != 0:
    df_99.to_excel(f'{file}{excel_name[99]}', index=False)
else:
    print('没有未归类的数据。')
# print([len(i) for i in [df_A03, df_D02, df_D10, df_DB, df_baoz, df_huanc, df, df_99]])

# 处理导入的文件
df.insert(0, '客户', value='日立电梯（中国）有限公司广州工厂')

# df['需要日期'] = pd.to_datetime(df['需要日期'], format='%Y-%m-%d').dt.date
df['需要日期'] = pd.to_datetime(df['需要日期'], format='%Y-%m-%d').dt.strftime('%Y-%#m-%#d')
df['作业指令产出日期'] = pd.to_datetime(df['作业指令产出日期'], format='%Y-%m-%d').dt.strftime('%Y-%#m-%#d')

df.to_excel(e9_file, index=False)
# 需要日期、