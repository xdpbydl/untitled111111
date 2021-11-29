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

# aa.to_excel(save_file, index=False, engine='openpyxl')
# 实时的
bb = ts.get_realtime_quotes(ts_code)
bb['price'] = bb['price'].astype('float')
bb['pre_close'] = bb['pre_close'].astype('float')
bb['zhang_fu'] = bb.apply(lambda x: (x['price'] - x['pre_close']) / x['pre_close'] * 100, axis=1).round(2)
bb = bb[['time', 'code', 'zhang_fu', 'price', 'volume']]
# bb.to_excel(save_file, index=False, engine='openpyxl')
print(bb[['time', 'code', 'zhang_fu', 'price', 'volume']])

