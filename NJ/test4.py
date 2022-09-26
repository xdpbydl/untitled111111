import cv2 as cv
from playwright.sync_api import Playwright, sync_playwright
import random, os, configparser, base64, time, hashlib
from zeep import Client


def get_distance(bg_img_path, slider_img_path):
    """获取滑块移动距离"""
    # 测试可行

    # 背景图片处理
    bg_img = cv.imread(bg_img_path, 0)  # 读入灰度图片
    bg_img = cv.GaussianBlur(bg_img, (3, 3), 0)  # 高斯模糊去噪
    bg_img = cv.Canny(bg_img, 50, 150)  # Canny算法进行边缘检测
    # 滑块做同样处理
    slider_img = cv.imread(slider_img_path, 0)
    slider_img = cv.GaussianBlur(slider_img, (3, 3), 0)
    slider_img = cv.Canny(slider_img, 50, 150)
    # 寻找最佳匹配
    res = cv.matchTemplate(bg_img, slider_img, cv.TM_CCOEFF_NORMED)
    # 最小值，最大值，并得到最小值, 最大值的索引
    min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)
    # 例如：(-0.05772797390818596, 0.30968162417411804, (0, 0), (196, 1))
    top_left = max_loc[0]  # 横坐标
    # 展示圈出来的区域
    # w, h = image.shape[::-1]  # 宽高,例如(320, 160)
    # cv.rectangle(template, (x, y), (x + w, y + h), (7, 249, 151), 2)
    # cv.imshow('Show', bg_img)
    # cv.waitKey(0)
    # cv.destroyAllWindows()
    print(top_left)
    return top_left


# get_distance('max.png', 'xiaotu.png')
def run(playwright: Playwright) -> None:
    chromium = playwright.chromium
    browser = chromium.connect_over_cdp('http://localhost:12345/')
    page = browser.contexts[0].pages[0]
    print(page.url)
    page.locator('''//*[@id="hotsearch-refresh-btn"]/span''').click()


# with sync_playwright() as playwright:
#     run(playwright)


now_time = time.time()
xt_key = '9c7e6cf9a1f64fe6b16146c954f27d96'
# 毫秒级
now_time = str(int(round(now_time * 1000)))
token = hashlib.sha256((now_time + xt_key).encode('utf-8')).hexdigest()
print(now_time, token)
wsdl='http://192.168.0.167:8090/webservice1.asmx?wsdl'
url = 'http://39.103.140.108:8777/view/691?id=691&configId=5069&userId=329264033140805&userType=1&token=eyJhbGciOiJIUzUxMiJ9.eyJsb2dpbl91c2VyX2tleSI6ImMwYzIzYWFmLWE1OTktNDA0OS04YTZlLTFiNzAyYmZiN2M1MiJ9.2zV8HDE3XSNklFfrkfPI9Mi3mzOTP0F3nPAEk6VfIwzV6DF6YGIxZ8tUNpuQsJRIjJUnE7UQMCGr2ex8RwcA8A&see=view&title=%25E5%258D%2597%25E4%25BA%25AC%25E5%2582%25AC%25E5%258C%2596%25E5%2589%2582%25E6%2599%25BA%25E8%2583%25BD%25E5%25AE%2589%25E5%2585%25A8%25E7%25B3%25BB%25E7%25BB%259F&menuId=329264033140805'

def request_webservice(wsdl, token, timekey, url):
    client = Client(wsdl)
    s1 = client.bind('WebService1', 'WebService1Soap')
    s = s1.ResetTowerUrl(token, timekey, url)
    return s

request_webservice(wsdl, token, now_time, url)

input()
# < token > string < / token >
# < timekey > string < / timekey >
# < url > string < / url >
