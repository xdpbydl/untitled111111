import pandas as pd
import re
import ast
import urllib.request
import tushare as ts
import time
from datetime import datetime
import configparser
import os


def get_daily(code):
    # 沪市前面加0，深市前面加1，比如0000001，是上证指数，1000001是中国平安
    # http://api.money.126.net/data/feed/1159949,1000625
    url = f"http://api.money.126.net/data/feed/{code}"
    response = urllib.request.urlopen(url)  # 请求站点获得一个HTTPResponse对象
    data = response.read().decode('utf-8')
    return data


def get_code():
    pass


def is_jy():
    jy_date = [['9:30', '11:31'], ['13:00', '18:01']]
    # 判断当前时间是否在范围时间内
    for i in jy_date:
        # 当前时间
        n_time = datetime.now()
        w_d = n_time.isoweekday()
        # 范围时间
        d_time = datetime.strptime(str(datetime.now().date()) + i[0], '%Y-%m-%d%H:%M')
        d_time1 = datetime.strptime(str(datetime.now().date()) + i[1], '%Y-%m-%d%H:%M')
        if n_time.isoweekday() in (6, 7):  #
            return 0
        elif n_time > d_time and n_time < d_time1:
            return 1
        elif i == 1:
            return 0
    # pro = ts.pro_api()
    # d = datetime.today()
    # # print(pro.trade_cal(exchange='SSE'))


def processing_data(data):
    pattern = re.compile("_ntes_quote_callback\((.*)\);")
    data_1 = pattern.findall(data)[0]
    data_d = ast.literal_eval(data_1)
    return data_d


if __name__ == "__main__":
    # 获取配置文件
    file = os.path.join(os.path.abspath('.'), 'config.ini')
    config = configparser.ConfigParser()
    config.read(file, encoding="utf8")
    try:
        j_code = config['system']['code']
        j_time = config['system']['time']
    except Exception as r:
        print(f'config.ini文件错误！{r}')
    j_time = int(j_time)
    while 1:
        while is_jy():
            # j_code = '1000625,1000830,0000001,1399001'    # '1000625,1000830'
            # j_time = 3
            print('')
            try:
                data_d = processing_data(get_daily(j_code))
                for k, v in data_d.items():
                    print(v['time'], v['symbol'], v['price'], format(v['percent'], '.2%'), format(v['turnover'] / 10 ** 8, '.5'))
                time.sleep(3)
            except Exception as r:
                print(f'获取数据失败！{r}')

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
