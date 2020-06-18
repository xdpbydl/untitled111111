from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import pyautogui
from time import sleep

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
browser = webdriver.Chrome(chrome_options=chrome_options)

# browser = webdriver.Chrome()
browser.get(
    'https://weixin.sogou.com/')
# 选择元素
wait = WebDriverWait(browser, 10)

check_height = browser.execute_script("return document.body.scrollHeight;")
# print(check_height)
for i in range(0, 8000, 10):  # 缓慢滚动鼠标
    js = 'window.scrollTo(0,{})'.format(i)
    browser.execute_script(js)
    if i % 500 == 0:
        sleep(2)
        print(i, check_height,"8"*100)

    if check_height < i:  # 滚动到底部退出
        print(i,check_height,type(i),type(check_height))
        break

browser.save_screenshot("E:/TEMP/google/app1.png")
browser.close()

# # 右键单击图片
# img = wait.until(EC.element_to_be_clickable(
#     (By.TAG_NAME, '#copyright_logo')))
# # 执行鼠标动作
# actions = ActionChains(driver)
# # 找到图片后右键单击图片
# actions.context_click(img)
# actions.perform()
# # 发送键盘按键，根据不同的网页，
# # 右键之后按对应次数向下键，
# # 找到图片另存为菜
# #
#
# pyautogui.typewrite(['down', 'down', 'down', 'enter'])
# # 单击图片另存之后等1s敲回车
# sleep(2)
# pyautogui.typewrite(['enter'])
# print("*"*15)

#
