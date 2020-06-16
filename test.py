from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import pyautogui
from time import sleep
# 代码的健壮性

driver = webdriver.Chrome()  # Optional argument, if not specified will search path.
driver.get('https://www.jianshu.com/')
# 选择元素
wait = WebDriverWait(driver,10)
# 右键单击图片
img = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#note-71509063 > div > div > span:nth-child(4)')))

# 执行鼠标动作
actions = ActionChains(driver)
# 找到图片后右键单击图片
actions.context_click(img)
actions.perform()
# 发送键盘按键，根据不同的网页，
# 右键之后按对应次数向下键，
# 找到图片另存为菜单
pyautogui.typewrite(['down', 'down', 'down', 'enter'])
# 单击图片另存之后等1s敲回车
sleep(3)
pyautogui.typewrite(['enter'])

