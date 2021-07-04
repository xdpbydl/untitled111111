from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import pandas as pd
import time

'''
取数网址： https://hz.house.ifeng.com/news/2014_10_28-50087618_1.shtml
cmd命令： chrome.exe --remote-debugging-port=9222 --user-data-dir="D:\green\chrome" 
'''

chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
driver = webdriver.Chrome(chrome_options=chrome_options)

aa = 'e0fe394964bbd9fef7d310c80353afdd-scss'
table_html = driver.find_elements_by_class_name(aa)

for m, i in enumerate(table_html):
    if m == 1:
        i.click()
        time.sleep(5)
        n = driver.window_handles
        txt = driver.find_element_by_tag_name('h1')
        video = driver.find_element_by_xpath('video')
        video_source = video.find_elements_by_xpath('video')[1]
        video_url = video_source.text
        print(video_url)
        input("暂停")
    print('-----------')
# table_row = table_html.find_elements_by_tag_name('tr')
# r_counter = 0
# t_ha = []
# t_li = []
#
# for r in table_row:     # 行
#     t_cols = r.find_elements_by_tag_name('td')
#     for c in t_cols:    # 列
#         t_li.append(c.text)
#     t_ha.append(t_li)
#     t_li = []
#
#
# df = pd.DataFrame(t_ha[1:],index=None, columns=None)
# df.to_excel('d:\\text.xlsx', index=False, header=False)
