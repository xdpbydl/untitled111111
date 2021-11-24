import tushare as ts
import pandas as pd

# print(ts.__version__)
token_file = r'E:\JiaZhi\0.9 LH\token.xlsx'
save_file = r'E:\JiaZhi\0.9 LH\save\23.xlsx'
ts_code = ['000625', '000830']

df = pd.read_excel(token_file)
my_token = df[df['平台'] == 'tushare']['token'].values[0]
ts.set_token(my_token)
pro = ts.pro_api()
pa = pro.stock_basic(ts_code=ts_code)
# print(pa)
riqi = '20211123'
aa = pro.daily(ts_code='000625.SZ', start_date=riqi, end_date=riqi)
print(aa)
print(type(aa))

# aa.to_excel(save_file, index=False, engine='openpyxl')
# 实时的
bb = ts.get_realtime_quotes(ts_code)
print(bb)
