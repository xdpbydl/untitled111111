
# chrome.exe --remote-debugging-port=9222 --user-data-dir="D:\green\Chrome80\App"


# coding:utf-8
import time

from selenium import webdriver

# driver = webdriver.Chrome()

# 增加下面3句，防止浏览器崩溃
chrome_options = webdriver.ChromeOptions()
# 下面这行解决崩溃问题 也可能是driver和chrome不匹配
chrome_options.add_argument('--no-sandbox')
# 谷歌文档提到需要加上这个属性来规避bug
chrome_options.add_argument('--disable-gpu')
# ie_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")

# 禁止图片的加载，但不支持CMD启动的方式？
prefs = {"profile.managed_default_content_settings.images": 2}
chrome_options.add_experimental_option("prefs", prefs)

driver = webdriver.Chrome(executable_path=r'D:\green\Chrome80\App\chromedriver.exe', chrome_options=chrome_options)
driver.maximize_window()



driver.get("http://www.cnblogs.com/yoyoketang/")

time.sleep(2)
input('1'*18)

# 定位首页管理按钮：id=blog_nav_contact
js1 = 'document.getElementById("blog_nav_contact").click();'
driver.execute_script(js1)

# 输入账号
# js2 = 'document.getElementsByClassName("input-text")[0].value="上海-悠悠";'
js2 = 'document.getElementById("mat-input-0").value="22";'
driver.execute_script(js2)

# 输入密码
js3 = 'document.getElementById("mat-input-1").value="111111111111";'
driver.execute_script(js3)

# 勾选记住密码
js4 = 'document.querySelectorAll(".mat-checkbox-inner-container")[0].click();'
# js4 = 'document.getElementsByClassName("mat-checkbox-inner-container").click();'
driver.execute_script(js4)

# 点击登录按钮
js5 = 'document.querySelectorAll(".action-button > .mat-button-wrapper")[0].click();'
driver.execute_script(js5)