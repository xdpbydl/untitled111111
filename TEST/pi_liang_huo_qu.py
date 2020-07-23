from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait


# 使用无头浏览器
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument(
    'user-agent=:	Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 UBrowser/6.2.4098.3 Safari/537.36')
chrome_options.add_experimental_option('excludeSwitches', ['enable-automation'])  # 以键值对的形式加入参数 ， 以开发者模式

browser = webdriver.Chrome(chrome_options=chrome_options)


# browser = webdriver.Chrome()
browser.maximize_window()  # 最大化
wait = WebDriverWait(browser, 10)

url = r'http://www.370kk.com/dm/27532'
browser.get(url)
lian_jie = browser.find_elements_by_class_name('thunder_url')
for i in range(len(lian_jie)):
    print(lian_jie[i].get_attribute("value"))
browser.quit()