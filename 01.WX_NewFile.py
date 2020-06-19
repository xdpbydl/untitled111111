from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import pandas as pd
from datetime import date
from time import sleep
import re

# 使用无头浏览器
# chrome_options = Options()
# chrome_options.add_argument('--headless')
# chrome_options.add_argument('--disable-gpu')
# chrome_options.add_experimental_option('excludeSwitches', ['enable-automation'])  # 以键值对的形式加入参数 ， 以开发者模式
# browser = webdriver.Chrome(chrome_options=chrome_options)


browser = webdriver.Chrome()
# browser.maximize_window()  # 最大化
wait = WebDriverWait(browser, 10)
WX = pd.read_excel('E:/TEMP/untitled111111/WX_File.xlsx')


def search(h):
    browser.get('https://weixin.sogou.com/')
    browser.save_screenshot("E:/TEMP/google/1.png")
    # 定位输入框
    input_box = browser.find_element_by_id('query')
    # 输入内容：
    input_box.send_keys(h)
    browser.save_screenshot("E:/TEMP/google/2.png")
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#searchForm > div > input.swz2'))).click()
    sleep(5)
    browser.save_screenshot("E:/TEMP/google/3.png")
    for i in range(8):  # 需要优化为根据出现条目循环

        try:
            tar = '#sogou_vr_11002301_box_{}'.format(i)
            browser.save_screenshot("E:/TEMP/google/4.png")
            wx_en = browser.find_element_by_css_selector(tar + ' > div > div.txt-box > p.tit > a > em').text
            wx_en_1 = browser.find_element_by_css_selector(tar + ' > div > div.txt-box > p.tit > a ').text
            wx_hao = browser.find_element_by_css_selector(tar + ' > div > div.txt-box > p.info > label').text
            print("0--" * 10, wx_en, wx_en_1, wx_hao)
        except:
            wx_en, wx_en_1, wx_hao = 'NULL', 'NULL', 'NULL'

        # print("第{}条不存在".format(i+1))
        # 文章不存在
        try:
            wx_file = browser.find_element(By.CSS_SELECTOR, tar + ' > dl:nth-child(3) > dd > a > em').text
        except:
            wx_file = 'NULL'
        try:
            wx_file_1 = browser.find_element(By.CSS_SELECTOR, tar + ' > dl:nth-child(3) > dd > a ').text
        except:
            wx_time = 'NULL'
        try:
            wx_time = browser.find_element(By.CSS_SELECTOR, tar + ' > dl:nth-child(3) > dd > span').text
        except:
            wx_file_1 = 'NULL'
        # print(wx_hao)

        print(wx_en + wx_en_1, wx_hao, wx_file + wx_file_1, wx_time)
        if wx_hao in WX['微信号'].values.tolist():

            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, tar + ' > dl:nth-child(3) > dd > a'))).click()

            # 获取打开的多个窗口句柄
            windows = browser.window_handles
            # 切换到当前最新打开的窗口
            browser.switch_to.window(windows[-1])
            sleep(2)

            scroll_width = browser.execute_script('return document.body.parentNode.scrollWidth')  # 设置宽高，便于截图
            scroll_height = browser.execute_script('return document.body.parentNode.scrollHeight')

            # eles = browser.find_element_by_xpath('//html')
            #
            # width = int(eles.size['width'])
            # height = int(eles.size['height'])
            # print(scroll_width, scroll_height, type(scroll_height), "**" * 55)
            # print(width, height, type(height))

            check_height = browser.execute_script("return document.body.scrollHeight;")
            for num in range(0, 8000, 10):  # 缓慢滚动鼠标
                js = 'window.scrollTo(0,{})'.format(num)
                browser.execute_script(js)
                if num % 500 == 0:
                    sleep(2)
                print(num, check_height)
                if check_height < num:  # 滚动到底部退出
                    break
            name = wx_file + wx_file_1 + date.today().strftime("%Y-%m-%d")
            name = validateTitle(name)

            print(name, wx_file, wx_file_1, date.today().strftime("%Y-%m-%d"))
            browser.set_window_size(scroll_width, scroll_height)
            browser.get_screenshot_as_file("E:/TEMP/google/{}.png".format(name))
            browser.save_screenshot("E:/TEMP/google/{}_1.png".format(name))

            browser.close()  # 关闭当前窗口
            browser.switch_to.window(windows[0])  # 切换回窗口A


def validateTitle(title):  # 文件名合法的判断
    rstr = r"[\/\\\:\*\?\"\<\>\|]"  # '/ \ : * ? " < > |'
    new_title = re.sub(rstr, "_", title)  # 替换为下划线
    return new_title


# def html_to_file(page):
#     get_html = "get_html.html"
#     # 打开文件，准备写入
#     f = open(get_html, 'wb')
#     # 写入文件
#     f.write(page.page_source.encode("gbk", "ignore"))  # 忽略非法字符
#     print('写入成功')
#     # 关闭文件
#     f.close()


if __name__ == '__main__':
    for i in WX['公众号']:
        search(i)
