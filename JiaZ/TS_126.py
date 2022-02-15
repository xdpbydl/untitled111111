import pandas as pd
import re


#沪市前面加0，深市前面加1，比如0000001，是上证指数，1000001是中国平安
# http://api.money.126.net/data/feed/1159949,1000625

def get_daily(code):
    url = f"http://api.money.126.net/data/feed/{code}"
    df = pd.read_csv(url, encoding="utf-8")
    data = str(df.columns)
    data = re.findall(r'_ntes_quote_callback(.*)', data)
    return data

def get_code():
    pass

print(get_daily('1159949,1000625'))


###获取历史数据###
# 沪市前面加0，深市前面加1，比如0000001，是上证指数，1000001是中国平安
# def get_daily(code, start='19900101', end=''):
#     url_mod = "http://quotes.money.163.com/service/chddata.html?code=%s&start=%s&end=%s"
#     url = url_mod % (code, start, end)
#     df = pd.read_csv(url, encoding='gb2312')
#     return df
#
#
# df = get_daily('0000001')  # 获取上证指数
# print(df)
###获取历史数据###
