from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import pandas as pd
import pyautogui
from time import sleep


browser = webdriver.Chrome()
browser.maximize_window()  # 最大化
wait = WebDriverWait(browser, 10)

browser.get('https://mp.weixin.qq.com/s?src=11&timestamp=1592379358&ver=2405&signature=oeEmhqFpX9jhO511WgcnMDtejmMYjzarAc7ONHaFMCJfRfA2VR4isszW3kpGg2pmlIBX9sw1t12fdxHKNhA7rgUqL*6MfQb1JAa9wiIcCLKIAN4CqCBvzlI*dkY9wtKi&new=1')
browser.refresh
sleep(2)
# 取任一点  #js_author_name
img = browser.find_element(By.CSS_SELECTOR, '#meta_content > span.rich_media_meta.rich_media_meta_text')
sleep(3)
# 执行鼠标动作
actions = ActionChains(img)
# 找到元素后右键单击元素
actions.context_click(img)
actions.perform()
# 发送键盘按键，根据不同的网页，
# 右键之后按对应次数向下键，
# 找到图片另存为菜单
pyautogui.typewrite(['down', 'down', 'down', 'enter'])
# 单击图片另存之后等1s敲回车
sleep(3)
pyautogui.typewrite(['enter'])