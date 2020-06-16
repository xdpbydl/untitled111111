# #网页隐藏了数据，使用selenium尝试
# import requests
#
# data = {"type": 1,
#         "s_from": "input",
#         "query": "%E6%97%B6%E5%AF%92%E5%86%B0",
#         "ie": "utf8",
#         "_sug_": "n",
#         "_sug_type_": ""}
# headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko"}
#
# result = requests.get("http://weixin.sogou.com/weixin", params=data, headers=headers, timeout=10)
#
##
# print(result.text)


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import  time, csv
from selenium.webdriver.common.by import By

options = Options()

