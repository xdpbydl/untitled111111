from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import pandas as pd
import os

# 执行命令
com_flag = '''start chrome.exe --remote-debugging-port=9222 --user-data-dir="D:\green\chrome"  https://www.baidu.com'''
os.system(com_flag)
# tvar_2021012510003559652=ics.do_popen_exe(command=com_flag,block=False)   # RPA

txt = "python"
save_file = f"E:\\TEMP\\baidu_{txt}.xlsx"
chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
driver = webdriver.Chrome(chrome_options=chrome_options)

search_str = f'document.getElementById("kw").value="{txt}";'
driver.execute_script(search_str)

click_daidu = 'document.querySelector("#su").click();'
driver.execute_script(click_daidu)

time.sleep(5)
title_all = []

for c in range(10):
    # 点击下一页
    if c == 1:
        next_page = 'document.querySelector("#page > div > a.n").click()'
        driver.execute_script(next_page)
    elif c > 1:
        next_page = 'document.querySelector("#page > div > a:nth-child(12)").click()'
        driver.execute_script(next_page)
    time.sleep(3)

    # 控制翻页, 25页之后才点击
    if c < 0:
        continue
    baidu_length = driver.execute_script('return document.getElementsByTagName("h3").length')

    for i in range(int(baidu_length)):
        txt_title_list = []
        is_click = ''
        url = ''
        # 点击
        click_daidu_list_0 = f'document.getElementsByTagName("h3")[{i}]'
        click_daidu_list = f'{click_daidu_list_0}.getElementsByTagName("a")[0]'

        try:
            txt_title = driver.execute_script('return ' + click_daidu_list_0 + ".innerText;")
            try:
                driver.execute_script(click_daidu_list + ".click();")
                # document.getElementsByTagName("h3")[0].getElementsByTagName("a")[0].attributes["href"].nodeValue;
                url = driver.execute_script('return ' + click_daidu_list + '.attributes["href"].nodeValue;')
            except:
                try:
                    driver.execute_script(click_daidu_list_0 + '.click();')
                    url = driver.execute_script(
                        'return ' + click_daidu_list_0 + '.parentNode.attributes["href"].nodeValue;')
                    print(f'--11---当前第{c + 1}页，第{i + 1}条点击失败。-------')
                except:
                    print(f'--1.5---当前第{c + 1}页，第{i + 1}条点击失败。-------')
            time.sleep(2)
            handle = driver.window_handles
            driver.switch_to.window(handle[1])
            #            # 获取当前页面的url地址
            #            url = driver.current_url
            driver.close()
            time.sleep(1)
            driver.switch_to.window(handle[0])
        except:
            is_click = '未点击'
            print(click_daidu_list + ".innerText;")
            print(f'--22---当前第{c + 1}页，第{i + 1}条点击失败。-------')
        print(txt_title)
        txt_title_list = [f'{c + 1}_{i + 1}', txt_title, is_click, url]
        title_all.append(txt_title_list)

df = pd.DataFrame(title_all, columns=['位置', 'title', '是否点击', 'URL'])
df.to_excel(excel_writer=save_file, index=False)
