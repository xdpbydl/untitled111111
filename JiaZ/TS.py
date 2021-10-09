import tushare as ts
import pandas as pd

# print(ts.__version__)
token_file = r'E:\JiaZhi\0.9 LH\token.xlsx'
df = pd.read_excel(token_file)
my_token = df[df['平台'] == 'tushare'].token.values[0]
print(my_token)
ts.set_token(my_token)
pro = ts.pro_api()
df = pro.trade_cal(exchange='', start_date='20180901', end_date='20181001', fields='exchange,cal_date,is_open,pretrade_date', is_open='0')
print(df)