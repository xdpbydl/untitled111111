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

"""
取数网址： https://hz.house.ifeng.com/news/2014_10_28-50087618_1.shtml
cmd命令： """
# chrome.exe --remote-debugging-port=9222 --user-data-dir="C:\Users\admin\AppData\Local\Google\Chrome\Application"
# chrome.exe --remote-debugging-port=9222 --user-data-dir="D:\green\Chrome80\App"


chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
chrome_driver = r"D:\\green\\Chrome80\\App\\chromedriver.exe"
driver = webdriver.Chrome(chrome_driver, chrome_options=chrome_options)
driver.get("http://dghrss.dg.gov.cn/sbzw/")



time.sleep(2)
file_path = 'E:\\TEMP\\6TEST\\SBJ\\'

try:
    driver.maximize_window()
except:
    pass
tongzhi = driver.find_elements_by_class_name('menu_list')
tongzhi[1].click()
time.sleep(1)

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



for m in range(51):
    page_list = driver.find_element_by_class_name('page_list')
    page_list_a = page_list.find_elements_by_tag_name('a')
    time.sleep(2)
    for n in range(len(page_list_a)):
    # for n in range(1):
        # page_list、page_list_a需要重新定义，因为driver.back()导致元素ID不同，这是个坑！
        page_list = driver.find_element_by_class_name('page_list')
        page_list_a = page_list.find_elements_by_tag_name('a')

        print(page_list.find_elements_by_tag_name('a')[n].get_attribute('title'))
        # input('-------' * 18)
        title = page_list.find_elements_by_tag_name('a')[n].get_attribute('title')
        time_str = page_list.find_elements_by_class_name('list_date')[n].text
        page_list.find_elements_by_tag_name('a')[n].click()

        time_str = re.sub(r"[-:\s]*", "", time_str)
        word_name = f"{time_str}_{title}.docx"
        word_path = "E:\\TEMP\\6TEST\SBJ\\"
        word_file = word_path + word_name


        cont_content = driver.find_element_by_class_name('cont_content')
        cont_content_a = cont_content.find_elements_by_tag_name('a')
        for n1 in range(len(cont_content_a)):
            if n1 < 10:
                continue
            file_url = cont_content.find_elements_by_tag_name('a')[n1].get_attribute('href')
            if 'http://' in file_url:
                if 'http://10.' in file_url:
                    new = file_url.split('/', 3)
                    file_url = f'http://dghrss.dg.gov.cn/{new[-1]}'

                print(file_url)
                file_name = cont_content.find_elements_by_tag_name('a')[n1].get_attribute('title')
                file_path_all = f'{file_path}{time_str}__附件__{file_name}'

                r = requests.get(file_url)
                with open(file_path_all, "wb") as code:
                    code.write(r.content)

        wait = WebDriverWait(driver, 40, 1, ignored_exceptions=None)
        driver.find_element_by_css_selector('.fa_home').click()
        print('2' * 18)
        try:
            wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.fa_home')))
        except:
            print('3' * 18, '超时。')
            time.sleep(3)
        print('3.1---' * 18, 'WebDriverWait,卡死')
        # 按住shift键
        key_up_down(flag='down')

        try:
            # wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'ft-top')))
            wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'ft-top')))
        except:
            print('4' * 18, '超时。')
            time.sleep(3)
        driver.find_element_by_class_name('ft-top').click()
        # 松开按住的shift建
        key_up_down()

        driver.back()   #存在不能返回前一个页面
        set_page = driver.find_element_by_id('inputPageNum')
        set_page.clear()
        time.sleep(2)
        set_page.send_keys(m+2)
        driver.find_element_by_xpath("""//button[@onclick="changePage('getPageNum')"]""").click()
        time.sleep(3)
    driver.find_element_by_xpath("//button[contains(text(),'下一页')]").click()
    time.sleep(2)
    page_list_a, page_list = '', ''
