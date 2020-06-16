from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import re, time

# from pyquery import PyQuery as pq

browser = webdriver.Chrome()
browser.maximize_window()  # 最大化
wait = WebDriverWait(browser, 10)
WX = pd.read_excel('E:/TEMP/untitled111111/WX_File.xlsx')


# print(WX['微信号'])

def search():
    browser.get('https://weixin.sogou.com/')
    # 定位输入框
    input_box = browser.find_element_by_id('query')
    # 输入内容：
    input_box.send_keys('时寒冰')
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#searchForm > div > input.swz2'))).click()
    for i in range(8):
        tar = '#sogou_vr_11002301_box_{}'.format(i)
        wx_en = browser.find_element(By.CSS_SELECTOR, tar + ' > div > div.txt-box > p.tit > a > em').text
        wx_en_1 = browser.find_element(By.CSS_SELECTOR, tar + ' > div > div.txt-box > p.tit > a ').text
        wx_hao = browser.find_element(By.CSS_SELECTOR, tar + ' > div > div.txt-box > p.info > label').text
        # 文章不存在
        try:
            wx_file = browser.find_element(By.CSS_SELECTOR, tar + ' > dl:nth-child(3) > dd > a > em').text
            wx_file_1 = browser.find_element(By.CSS_SELECTOR, tar + ' > dl:nth-child(3) > dd > a ').text
            wx_time = browser.find_element(By.CSS_SELECTOR, tar + ' > dl:nth-child(3) > dd > span').text
        except:
            wx_file, wx_time, wx_file_1 = 'NULL', 'NULL', 'NULL'

        if wx_hao in WX['微信号']:
            print(wx_en + wx_en_1, wx_hao, wx_file + wx_file_1, wx_time)
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, tar + ' > dl:nth-child(3) > dd > a'))).click()



def html_to_file(page):
    get_html = "get_html.html"
    # 打开文件，准备写入
    f = open(get_html, 'wb')
    # 写入文件
    f.write(page.page_source.encode("gbk", "ignore"))  # 忽略非法字符
    print('写入成功')
    # 关闭文件
    f.close()

        # wx_en_1 = wx_en.value
        # # wx_en_all = wx_en + wx_en_1
        # wx_file_1 = wx_file.text
        # # wx_file_all = wx_file + wx_file_1
        # print(wx_en_1, wx_file_1, type(wx_en_1), type(wx_file_1))
        # print(wx_en_all, wx_hao, wx_file_all, wx_time)

        # browser.quit()

        #
        # def eline():
        #     for i in range(1, 25):
        #         flag = '#songs > div > div:nth-child({}) > div.info > p:nth-child(1) > strong > a'.format(i)
        #         submit = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, flag)))
        #         submit.click()
        #         brower.switch_to_window(brower.window_handles[1])
        #         title = brower.find_element(By.CSS_SELECTOR, '#title > h1').text
        #         shit = brower.find_element(By.CSS_SELECTOR, '#play_count_num').text[:-3]
        #         fenx = brower.find_element(By.CSS_SELECTOR, '#sidebar > div.music_counts > ul > li:nth-child(2)').text[:-3]
        #         pingl = brower.find_element(By.CSS_SELECTOR, '#sidebar > div.music_counts > ul > li:nth-child(3) > a').text[:-3]
        #         # link = brower.find_element (By.CSS_SELECTOR, '#sidebar > div.music_counts > ul > li:nth-child(3) > a').text
        #         print(title, shit, fenx, pingl)
        #         print('----------------------')
        #         brower.close()
        #         brower.switch_to_window(brower.window_handles[0])
        #         time.sleep(100)


if __name__ == '__main__':
    search()
