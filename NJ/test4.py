import cv2 as cv
from playwright.sync_api import Playwright, sync_playwright
import random, os, configparser, base64, time, hashlib
from zeep import Client
def run1(playwright: Playwright) -> None:
    # 获取配置文件
    file = os.path.join(os.path.abspath('.'), 'config.ini')
    config = configparser.ConfigParser()
    # config.read(file, encoding="utf-8")
    config.read(file, encoding="utf-8-sig")
    try:
        user = config['set']['user']
        pwd = config['set']['pwd']
        jk_url = config['jiekou']['jk_url']
        xt_key = config['jiekou']['xt_key']
        sep_time = config['jiekou']['sep_time']
        sep_time = float(sep_time)
        chrome_path = config['set']['chrome_path']
        # j_debug = config['system']['debug']
        # j_hang_no = int(j_hang_no)fl
    except Exception as r:
        print(f'config.ini文件加载错误！{r}')

    # browser = playwright.chromium.launch(executable_path=chrome_path, headless=True)
    # context = browser.new_context()
    # # Open new page
    # page = context.new_page()

    # browser = playwright.chromium.connect_over_cdp("http://localhost:12345")
    # default_context = browser.contexts[0]
    # page = default_context.pages[0]

    # chromium = playwright.chromium
    # browser = chromium.connect_over_cdp('http://localhost:12345', timeout=120000)
    # page = browser.contexts[2].pages[2]
    # print(page)
    #
    # print(page.url)
    # input()

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
    browser = chromium.connect_over_cdp('http://localhost:12345', timeout=60000)
    # browser = chromium.connect_over_cdp('http://114.132.51.65:12345', timeout=60000)
    page = browser.contexts[0].pages[0]
    # print([i for i in browser.contexts[0].pages])
    print(page.url)
    # page.goto("http://www.baidu.com")
    # # page.locator('''//*[@id="hotsearch-refresh-btn"]/span''').click()
    # page.locator("#kw").fill('shoushou')
    # page.locator("#su").click()
    # page.goto("http://www.163.com")
    # mod_news_tab > div > div.tab_panel.tab_panel_yaowen >  #mod_news_tab > div > div.tab_panel.local_tab_news.show_local_tab.current > ul:nth-child(5)
    ul = '//*[@id="mod_news_tab"]/div/div[2]/ul'
    p_all = page.query_selector_all(ul)
    # for i in p_all:
    #     print(i.text_content())
    # print(len(p_all), p_all)
    # p_all = page.click("div.tab_panel.local_tab_news.show_local_tab.current:has(.cm_ul_round)")
    # # print(len(p_all))
    # print( p_all)

    for i in range(len(p_all)):

        p_all_2 = page.query_selector_all(f'{ul}[{i+1}]/li')
        print()
        for m in range(len(p_all_2)):
            ul_1 = f'{ul}[{i + 1}]/li[{m+1}]/a'
            print(ul_1)
            n_url = page.get_attribute(ul_1, 'href')  # 获取元素值
            n_txt = page.text_content(ul_1)   # 获取文本
            print(n_url, n_txt)
    input()
"""
//*[@id="mod_news_tab"]/div/div[2]/ul[1]/li[1]
//*[@id="mod_news_tab"]/div/div[2]/ul[1]/li[2]/a
//*[@id="mod_news_tab"]/div/div[2]/ul[2]/li[1]/a
//*[@id="mod_news_tab"]/div/div[1]/div[1]/div[1]/ul[1]
//*[@id="mod_news_tab"]/div/div[1]/div[1]/div[1]/ul[1]/li[1]
"""
with sync_playwright() as playwright:
    run(playwright)


# now_time = time.time()
# xt_key = '9c7e6cf9a1f64fe6b16146c954f27d96'
# # 毫秒级
# now_time = str(int(round(now_time * 1000)))
# token = hashlib.sha256((now_time + xt_key).encode('utf-8')).hexdigest()
# print(now_time, token)
# wsdl='http://192.168.0.167:8090/webservice1.asmx?wsdl'
# url = 'http://39.103.140.108:8777/view/691?id=691&configId=5069&userId=329264033140805&userType=1&token=eyJhbGciOiJIUzUxMiJ9.eyJsb2dpbl91c2VyX2tleSI6ImMwYzIzYWFmLWE1OTktNDA0OS04YTZlLTFiNzAyYmZiN2M1MiJ9.2zV8HDE3XSNklFfrkfPI9Mi3mzOTP0F3nPAEk6VfIwzV6DF6YGIxZ8tUNpuQsJRIjJUnE7UQMCGr2ex8RwcA8A&see=view&title=%25E5%258D%2597%25E4%25BA%25AC%25E5%2582%25AC%25E5%258C%2596%25E5%2589%2582%25E6%2599%25BA%25E8%2583%25BD%25E5%25AE%2589%25E5%2585%25A8%25E7%25B3%25BB%25E7%25BB%259F&menuId=329264033140805'
#
# def request_webservice(wsdl, token, timekey, url):
#     client = Client(wsdl)
#     s1 = client.bind('WebService1', 'WebService1Soap')
#     s = s1.ResetTowerUrl(token, timekey, url)
#     return s
#
# request_webservice(wsdl, token, now_time, url)


# < token > string < / token >
# < timekey > string < / timekey >
# < url > string < / url >
