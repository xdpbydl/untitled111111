from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time

chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
# chrome_driver = r"D:\code\python\selenium_ui_auto\driver\chromedriver.exe"
# driver = webdriver.Chrome(chrome_driver, ie_options=ie_options)
driver = webdriver.Chrome(chrome_options=chrome_options)

sous = driver.find_element_by_id('kw')
sous.clear()
sous.send_keys(u'测试工程师')
key_en = driver.find_element_by_id('kw')
key_en.send_keys(Keys.ENTER)
time.sleep(1)
# driver.find_element_by_xpath(r'//*[@id="1"]/h3/a').click()

# 点击下一页
js5 = 'document.querySelector("#page > div > a.n").click();'
driver.execute_script(js5)