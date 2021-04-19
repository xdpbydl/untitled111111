
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import requests
import re



"""
取数网址： https://hz.house.ifeng.com/news/2014_10_28-50087618_1.shtml
cmd命令： """
# chrome.exe --remote-debugging-port=9222 --user-data-dir="C:\Users\admin\AppData\Local\Google\Chrome\Application"
# .\chrome.exe --remote-debugging-port=9222 --user-data-dir="D:\green\Chrom80\App"


chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
chrome_driver = r"D:\\green\\Chrom80\\App\\chromedriver.exe"
driver = webdriver.Chrome(chrome_driver, chrome_options=chrome_options)
#

js = r'document.getElementById(“inputPageNum”).value = 2}'
driver.execute_script(js)
time.sleep(3)
input()


time.sleep(2)
file_path = 'E:\\TEMP\\6TEST\\SBJ\\'

try:
    driver.maximize_window()
except:
    pass
tongzhi = driver.find_elements_by_class_name('menu_list')
tongzhi[1].click()
time.sleep(1)



for m in range(51):
    page_list = driver.find_element_by_class_name('page_list')
    page_list_a = page_list.find_elements_by_tag_name('a')
    time.sleep(2)
    # for n in range(len(page_list_a)):
    for n in range(1):
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
            file_url = cont_content.find_elements_by_tag_name('a')[n1].get_attribute('href')
            if 'http://' in file_url:
                if 'http://10.' in file_url:
                    new = file_url.split('/', 3)
                    file_url = f'http://dghrss.dg.gov.cn/{new[-1]}'

                print(file_url)
                file_name = cont_content.find_elements_by_tag_name('a')[n1].get_attribute('title')
                file_path_all = f'{file_path}{time_str}_1_{file_name}'

                r = requests.get(file_url)
                with open(file_path_all, "wb") as code:
                    code.write(r.content)
        js = f'document.getElementById(“inputPageNum”).value = {str(m+2)}'
        driver.back()   #存在不能返回前一个页面
        driver.execute_script(js)
        time.sleep(3)
    driver.find_element_by_xpath("//button[contains(text(),'下一页')]").click()
    time.sleep(2)
    page_list_a, page_list = '', ''
