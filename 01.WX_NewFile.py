from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import pandas as pd
from datetime import date
from time import sleep
import re
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import smtplib
from email.header import Header

# 使用无头浏览器
# chrome_options = Options()
# chrome_options.add_argument('--headless')
# chrome_options.add_argument('--disable-gpu')
# chrome_options.add_experimental_option('excludeSwitches', ['enable-automation'])  # 以键值对的形式加入参数 ， 以开发者模式
# browser = webdriver.Chrome(chrome_options=chrome_options)

browser = webdriver.Chrome()
browser.maximize_window()  # 最大化
wait = WebDriverWait(browser, 10)
WX = pd.read_excel('E:/TEMP/untitled111111/WX_File.xlsx')


def search(h):
    browser.get('https://weixin.sogou.com/')
    browser.save_screenshot("E:/TEMP/google/1.png")
    # 定位输入框
    input_box = browser.find_element_by_id('query')
    # 输入内容：
    input_box.send_keys(h)
    browser.save_screenshot("E:/TEMP/google/2.png")
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#searchForm > div > input.swz2'))).click()
    sleep(5)
    browser.save_screenshot("E:/TEMP/google/3.png")
    for i in range(8):  # 需要优化为根据出现条目循环

        try:
            tar = '#sogou_vr_11002301_box_{}'.format(i)
            browser.save_screenshot("E:/TEMP/google/4.png")
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
        try:
            wx_file_1 = browser.find_element(By.CSS_SELECTOR, tar + ' > dl:nth-child(3) > dd > a ').text
        except:
            wx_time = ''
        try:
            wx_time = browser.find_element(By.CSS_SELECTOR, tar + ' > dl:nth-child(3) > dd > span').text
        except:
            wx_file_1 = ''
        # print(wx_hao)

        print(wx_en + wx_en_1, wx_hao, wx_file + wx_file_1, wx_time)
        if wx_hao in WX['微信号'].values.tolist():

            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, tar + ' > dl:nth-child(3) > dd > a'))).click()

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
                print(num, scroll_height)
                if scroll_height < num:  # 滚动到底部退出
                    break
            name = wx_file + wx_file_1 + date.today().strftime("%Y-%m-%d")
            name = validateTitle(name)
            file = "E:/TEMP/google/{}.png".format(name)

            print(name, wx_file, wx_file_1, date.today().strftime("%Y-%m-%d"))
            browser.set_window_size(scroll_width, scroll_height)
            browser.get_screenshot_as_file(file)

            send_m(wx_file + wx_file_1, file)

            browser.close()  # 关闭当前窗口
            browser.switch_to.window(windows[0])  # 切换回窗口A

def send_m1(name, file):
    import smtplib

    from email.mime.text import MIMEText

    from email.header import Header

    # 第三方 SMTP 服务

    mail_host = "smtp.qq.com"   # 设置服务器

    mail_user = "46311295@qq.com"   # 用户名

    mail_pass = "xefqwobdzspgbijb"  # 口令

    sender = '46311295@qq.com'

    receivers = ['46311295@qq.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

    message = MIMEText('Python 邮件发送测试...', 'plain', 'utf-8')

    message['From'] = Header(mail_user, 'utf-8')

    message['To'] = Header(sender, 'utf-8')

    subject = name

    message['Subject'] = Header(subject, 'utf-8')



    # smtpObj= smtplib.SMTP()

    # smtpObj.connect(email_host,25)

    # 抛出异常：smtplib.SMTPServerDisconnected: Connection unexpectedly closed

    # QQ邮箱是支持安全邮件的，需要通过SSL发送的邮件，如下：

    smtpObj = smtplib.SMTP_SSL(mail_host)

    smtpObj.connect(mail_host, 465)  # 465 为 SMTP 端口号

    smtpObj.login(mail_user, mail_pass)

    smtpObj.sendmail(sender, receivers, message.as_string())

    print("邮件发送成功")

def send_m(name, file):
    message = MIMEMultipart()  # 邮件主体

    # 邮件加入文本内容
    text = '<img src="cid:0">'  # html文本引入id为0的图片
    m_text = MIMEText(text, 'html', 'utf-8')
    message.attach(m_text)

    # 邮件加入图片
    m_img = MIMEBase('image', 'jpg')
    m_img.add_header('Content-Disposition', 'attachment')
    m_img.add_header('Content-ID', '<0>')  # 设置图片id为0
    f = open(file, "rb")  # 读取本地图片
    m_img.set_payload(f.read())
    encoders.encode_base64(m_img)
    message.attach(m_img)

    message['From'] = Header('小爱')  # 邮件发送者名字
    message['To'] = Header('小蓝枣')  # 邮件接收者名字
    message['Subject'] = Header(name)  # 邮件主题

    mail = smtplib.SMTP()
    mail.connect("smtp.qq.com")  # 连接 qq 邮箱
    mail.login("46311295@qq.com", "xefqwobdzspgbijb")  # 账号和授权码
    mail.sendmail("46311295@qq.com", ["46311295@qq.com"], message.as_string())





def validateTitle(title):  # 文件名合法的判断
    rstr = r"[\/\\\:\*\?\"\<\>\|]"  # '/ \ : * ? " < > |'
    new_title = re.sub(rstr, "_", title)  # 替换为下划线
    return new_title


# def html_to_file(page):
#     get_html = "get_html.html"
#     # 打开文件，准备写入
#     f = open(get_html, 'wb')
#     # 写入文件
#     f.write(page.page_source.encode("gbk", "ignore"))  # 忽略非法字符
#     print('写入成功')
#     # 关闭文件
#     f.close()


if __name__ == '__main__':
    for i in WX['公众号']:
        search(i)
