import win32com.client


# win32com.client.Dispatch("ket.Application")

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
chrome_options.binary_location = r'D:\green\chrome\chrome.exe'
chrome_driver = r"D:\green\chrome\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver, chrome_options=chrome_options)

# js1 = 'document.querySelector("#tiy_btn_tryit > a");'
# driver.execute_script(js1)

js0 = '''document.querySelector("#kw").value = '';
document.querySelector("#kw").value = '测试';
document.querySelector("#su").click();'''
driver.execute_script(js0)
# driver.find_element_by_id('kw').send_keys(u'测试工程师小站')

js2 = '''document.querySelector("#\\31  > h3 > a").click();'''
driver.execute_script(js2)