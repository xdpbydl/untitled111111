# -*- coding : utf-8-*-

import time
from datetime import datetime
import configparser
import os
import requests

# https://blog.csdn.net/geofferysun/article/details/114386084
def get_daily(code):
    url = f"https://qt.gtimg.cn/q={code}"
    data = {"keywords": "itcast"}
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"}
    response = requests.get(url, headers=headers, params=data)

    return response.text



def get_guige(data):
    data = data.split(';')
    data_a = []
    for i in data:
        if len(i) != 1:
            data_a.append(i.split('~'))
    for i in data_a:
        riqi = time.strptime(i[30], "%Y%m%d%H%M%S")
        riqi = f'{riqi.tm_mday}.{riqi.tm_hour}.{riqi.tm_min}.{riqi.tm_sec}'
        print(f"{riqi}\t{i[2]}\t{i[3]}\t{i[32]}\t{format(float(i[57]) / 10 ** 4, '.5')}")
    return ''

def is_jy(j_debug):
    if j_debug == 'Y' or j_debug == 'y':
        return 1
    jy_date = [['9:30', '11:35'], ['13:00', '15:33']]
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
while 1:
    # 获取配置文件
    file = os.path.join(os.path.abspath('.'), 'config.ini')
    config = configparser.ConfigParser()
    # config.read(file, encoding="utf-8")
    config.read(file, encoding="utf-8-sig")
    try:
        j_code = config['system']['tx_code']
        j_time = config['system']['time']
        j_hang = config['system']['hang']
        j_hang_no = config['system']['hang_no']
        j_debug = config['system']['debug']
        j_time = int(j_time)
        j_hang_no = int(j_hang_no)
    except Exception as r:
        print(f'config.ini文件加载错误！{r}')
        break
    if is_jy(j_debug):
        print(get_guige(get_daily(j_code)))
    time.sleep(1)