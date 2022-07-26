import pandas as pd

mingxi_file = r'E:\TEMP\6TEST\GRRPA\采购订单行明细.xlsx'
file = r'E:\TEMP\6TEST\GRRPA\\'
excel_name = {1: '1.1.1 A03架机梁.xlsx', 2: '1.1.2 D02钢丝绳.xlsx', 3: '1.1.3 D10油压缓冲器.xlsx', 4: '1.1.4 D05对重块_B07配重块.xlsx', 20: '1.2 包装类.xlsx', 30: '1.3 缓冲器_安全钳_.xlsx'}

df = pd.read_excel(mingxi_file)
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

