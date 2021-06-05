from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import pandas as pd
from datetime import date
from time import sleep
import re, time
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import smtplib
from email.header import Header
from selenium.webdriver.common.proxy import Proxy
from selenium.webdriver.common.proxy import ProxyType
import private as pv
import SendMail

# 使用无头浏览器
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument(
    'user-agent=:	Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 UBrowser/6.2.4098.3 Safari/537.36')
chrome_options.add_experimental_option('excludeSwitches', ['enable-automation'])  # 以键值对的形式加入参数 ， 以开发者模式
# 设置代理
# ie_options.add_argument("--proxy-server=http://127.0.0.1:8888")
# 一定要注意，=两边不能有空格，不能是这样--proxy-server = http://202.20.16.82:10152
browser = webdriver.Chrome(chrome_options=chrome_options)

# 查看本机ip，查看代理是否起作用
browser.get("http://httpbin.org/ip")
# print(browser.page_source)

# browser = webdriver.Chrome()
browser.maximize_window()  # 最大化
wait = WebDriverWait(browser, 10)

wx_num = 1  # 循环
print("1" * 100)


def search(idex, row):
    browser.get('https://weixin.sogou.com/')
    browser.save_screenshot(pv.poto_dir + "1.png")
    # 定位输入框
    input_box = browser.find_element_by_id('query')
    # 输入内容：
    input_box.send_keys(row['公众号'])
    browser.save_screenshot(pv.poto_dir + "2.png")
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#searchForm > div > input.swz2'))).click()
    sleep(5)
    browser.save_screenshot(pv.poto_dir + "3.png")
    print("2" * 100)
    for i in range(8):  # 需要优化为根据出现条目循环

        try:
            tar = '#sogou_vr_11002301_box_{}'.format(i)
            browser.save_screenshot(pv.poto_dir + "4.png")
            wx_en = browser.find_element_by_css_selector(tar + ' > div > div.txt-box > p.tit > a > em').text
            wx_en_1 = browser.find_element_by_css_selector(tar + ' > div > div.txt-box > p.tit > a ').text
            wx_hao = browser.find_element_by_css_selector(tar + ' > div > div.txt-box > p.info > label').text
            print("0--" * 10, wx_en, wx_en_1, wx_hao)
        except:
            wx_en, wx_en_1, wx_hao = '', '', ''

        # print("第{}条不存在".format(i+1))
        # 文章不存在
        try:
            wx_file = browser.find_element(By.CSS_SELECTOR, tar + ' > dl:nth-child(3) > dd > a > em').text
        except:
            wx_file = ''
            # print("网络访问不了，或者被屏蔽！")
        try:
            wx_file_1 = browser.find_element(By.CSS_SELECTOR, tar + ' > dl:nth-child(3) > dd > a ').text
        except:
            wx_file_1 = ''
        try:
            wx_time = browser.find_element(By.CSS_SELECTOR, tar + ' > dl:nth-child(3) > dd > span').text
        except:
            wx_time = ''
        # print(wx_hao)

        # print(wx_en + wx_en_1, wx_hao, wx_file + wx_file_1, wx_time)
        if wx_hao in WX['微信号'].values.tolist() and row['最新文章'] != wx_file + wx_file_1 and wx_time != '':

            try:
                wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, tar + ' > dl:nth-child(3) > dd > a'))).click()
            except:
                print("文章不存在！")

            # 获取打开的多个窗口句柄
            windows = browser.window_handles
            # 切换到当前最新打开的窗口
            browser.switch_to.window(windows[-1])
            sleep(2)

            scroll_width = browser.execute_script('return document.body.parentNode.scrollWidth')  # 设置宽高，便于截图
            scroll_height = browser.execute_script('return document.body.parentNode.scrollHeight')

            for num in range(0, 8000, 10):  # 缓慢滚动鼠标
                js = 'window.scrollTo(0,{})'.format(num)
                browser.execute_script(js)
                if num % 500 == 0:
                    sleep(2)
                # print(num, scroll_height)
                if scroll_height < num:  # 滚动到底部退出
                    break
            name = wx_file + wx_file_1 + date.today().strftime("%Y-%m-%d")
            name = validateTitle(name)
            file = pv.poto_dir + "{}.png".format(name)
            # pd.
            print(name, wx_file, wx_file_1, date.today().strftime("%Y-%m-%d"))
            browser.set_window_size(scroll_width, scroll_height)
            browser.get_screenshot_as_file(file)

            row['最新文章'] = wx_file + wx_file_1
            WX.iloc[idex] = pd.Series(row)
            WX_h = pd.read_excel(pv.file, sheet_name='history')
            WX_h = WX_h.append(
                [{'序号': len(WX_h) + 1, '公众号': row['公众号'], '微信号': row['微信号'], '最新文章': wx_en + wx_file + wx_file_1,
                  '发表时间': time.strftime("%Y-%m-%d %H:%M:%S")}], ignore_index=True)

            writer = pd.ExcelWriter(pv.file)
            WX.to_excel(writer, "Sheet1", index=False)
            WX_h.to_excel(writer, "history", index=False)

            writer.save()

            # 会覆盖sheet表
            # WX.to_excel('E:/TEMP/untitled111111/WX_File.xlsx', sheet_name='history', index=False)
            # WX.to_excel('E:/TEMP/untitled111111/WX_File.xlsx', sheet_name='Sheet1', index=False)
            #  发送邮件
            # send_m(wx_en + "__" + wx_file + wx_file_1, file, row['Email'])
            title = wx_en + "__" + wx_file + wx_file_1
            content = '''
            <p>{}</p>
            <p><img src="cid:image1"></p>
             '''.format(title)
            email = str(row['Email'])
            if email == '' or "@" not in email:
                recv = pv.jieshou
            else:
                recv = email.split(',')
            m = SendMail.SendMail(username=pv.fasong, passwd=pv.key, title=title, recv=recv, content=content,image=file)
            m.send_mail()

            browser.close()  # 关闭当前窗口
            browser.switch_to.window(windows[0])  # 切换回窗口A



# def send_m(name, file, email):
#     if email == '' or "@" not in email:
#         email = pv.jieshou
#
#     message = MIMEMultipart()  # 邮件主体
#
#     # 邮件加入文本内容
#     text = '<img src="cid:0">'  # html文本引入id为0的图片
#     m_text = MIMEText(text, 'html', 'utf-8')
#     message.attach(m_text)
#
#     # 邮件加入图片
#     m_img = MIMEBase('image', 'jpg')
#     m_img.add_header('Content-Disposition', 'attachment')
#     m_img.add_header('Content-ID', '<0>')  # 设置图片id为0
#     f = open(file, "rb")  # 读取本地图片
#     m_img.set_payload(f.read())
#     encoders.encode_base64(m_img)
#     message.attach(m_img)
#
#     message['From'] = Header('角度')  # 邮件发送者名字
#     message['To'] = Header('小蓝枣')  # 邮件接收者名字
#     message['Subject'] = Header(name)  # 邮件主题
#
#     # mail = smtplib.SMTP()  # （win7可用，win2008R2报错）win2008R2修改为：smtplib.SMTP_SSL
#     # mail.connect("smtp.qq.com")  # 连接 qq 邮箱 # win2008R2去掉了这个
#
#     mail = smtplib.SMTP_SSL("smtp.qq.com", 465)  # win2008R2的 发送服务器的端口号 （win7下可用）
#     mail.login(pv.accout, pv.key)  # 账号和授权码
#     mail.sendmail(pv.fasong, [email], message.as_string())
#     print("邮件发送成功" + "!" * 100)


def validateTitle(title):  # 文件名合法的判断
    rstr = r"[\/\\\:\*\?\"\<\>\|]"  # '/ \ : * ? " < > |'
    new_title = re.sub(rstr, "_", title)  # 替换为下划线
    return new_title


if __name__ == '__main__':

    while True:
        WX = pd.read_excel(pv.file, sheet_name='Sheet1')  # 放入无限循环内，实时刷新

        for idex, row in WX.iterrows():
            # print(row['公众号'], row['微信号'])  # 输出每一行  序号	公众号	微信号	最新文章	发表时间	Email
            search(idex, row)
        print(time.strftime("%Y-%m-%d %H:%M:%S"), "循环次数为（{}）次！！".format(wx_num))

        wx_num += 1
        sleep(60)
