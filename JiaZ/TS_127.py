# -*- coding : utf-8-*-
import re
import ast
import urllib.request
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

while 1:
    print(get_guige(get_daily('sz003032,sz000001')))
    time.sleep(1)