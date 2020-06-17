from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import pyautogui
from time import sleep

# 使用无头浏览器



chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')  # 对应下面参数 chrome_options
bro = webdriver.Chrome(chrome_options=chrome_options)
driver = webdriver.Chrome(chrome_options=chrome_options)  # Optional argument, if not specified will search path.

# driver=webdriver.PhantomJS()
# driver = webdriver.Chrome()
driver.get(
    'https://mp.weixin.qq.com/s?__biz=MzI3MDM5OTAwOQ==&mid=2247485377&idx=1&sn=bb4e98aae58c3d437322f82ef2f09c49&chksm=ead0e48fdda76d99853ccdb1ddc0e150a32dc98f7d29024bccf7f7201d2f0743b5c4cac9e964&scene=126&sessionid=1592388924&key=2d632f0a7a934684b682815f733ae37de1a1999444a26da0cffb1b02e2f375e1ca6bccf8fdd94a81fc751baeec74b4c00b5bb7d7d4aa6991fcacbcfd39ae9b6626fc754247f8da3883f34954bf2c83b7&ascene=1&uin=MjAzMDA0MTg3Mw%3D%3D&devicetype=Windows+7+x64&version=62090070&lang=zh_CN&exportkey=A6mtwdQCQC826Q%2Fsc5qbfTc%3D&pass_ticket=G5pUWM3U3V0xyUDrI5rSTmuiX7pcKwGvMeOBWyZfiJDAMz5NJIO4J6V6g%2BHtqLKA')
# 选择元素
wait = WebDriverWait(driver, 10)
for i in range(3):
    # 滚动鼠标
    js = 'window.scrollBy(500,100000)'
    driver.execute_script(js)
    sleep(2)
    #
    js1 = 'window.scrollBy(0,0)'
    driver.execute_script(js1)
    sleep(2)
    print("{}***".format(i))


driver.save_screenshot("E:/TEMP/google/app1.png")

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
