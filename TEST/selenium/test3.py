import time
import requests
import re
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


# chrome.exe --remote-debugging-port=9222 --user-data-dir="C:\Users\admin\AppData\Local\Google\Chrome\Application"
# chrome.exe --remote-debugging-port=9222 --user-data-dir="D:\green\Chrome80\App"


chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
chrome_driver = r"D:\\green\\Chrome80\\App\\chromedriver.exe"
driver = webdriver.Chrome(chrome_driver, chrome_options=chrome_options)
driver.get("http://dghrss.dg.gov.cn/sbzw/")
