# chrome.exe --remote-debugging-port=9222 --user-data-dir="D:\green\Chrome80\App"

import time

from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC

chrome_options = webdriver.ChromeOptions()
# 下面这行解决崩溃问题 也可能是driver和chrome不匹配
chrome_options.add_argument('--no-sandbox')
# 谷歌文档提到需要加上这个属性来规避bug
chrome_options.add_argument('--disable-gpu')
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")

driver = webdriver.Chrome(executable_path=r'D:\green\Chrome80\App\chromedriver.exe', chrome_options=chrome_options)
# driver.get("http://dghrss.dg.gov.cn/sbzw/")

input('0'*18)
# try:

wait = WebDriverWait(driver, 40, 1, ignored_exceptions=None)
# wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'menu_list')))
# driver.find_element_by_class_name('menu_list').click()



def key_up_down(flag='up', driver=driver):
    actions = ActionChains(driver)
    if flag == 'up':
        # 松开按住的shift建
        actions.key_up(Keys.SHIFT)
        actions.perform()
    elif flag == 'down':
        # 按住shift键
        actions.key_down(Keys.SHIFT)
        actions.perform()


def def_set():
    print('1' * 18)

    # try:
    # wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.fa_home')))
    WebDriverWait(driver, 40, 1, ignored_exceptions=None).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.fa_home')))
    driver.find_element_by_css_selector('.fa_home').click()
    print('2' * 18)
    # except:
    #     print('3' * 18, '超时。')
    #     time.sleep(3)
    # 按住shift键
    key_up_down(flag='down')

    # try:
    #     # wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'ft-top')))
    wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'ft-top')))
    driver.find_element_by_class_name('ft-top').click()
    # except:
    #     print('4' * 18, '超时。')
    #     time.sleep(3)
    # 松开按住的shift建
    key_up_down()
def_set()