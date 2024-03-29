import random, os, configparser, base64, time, hashlib
from playwright.sync_api import Playwright, sync_playwright
import cv2 as cv
from zeep import Client


def targetx():
    img_datu = cv.imread('max.png', 0)  # 裁剪后的大图
    edges_datu = cv.Canny(img_datu, 100, 200)

    img_xiaotu = cv.imread('xiaotu.png', 0)  # 小图
    edges_xiaotu = cv.Canny(img_xiaotu, 100, 200)

    method = cv.TM_CCOEFF
    res = cv.matchTemplate(edges_datu, edges_xiaotu, method)
    min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)
    print(min_val, max_val, min_loc, max_loc)
    top_left = min_loc
    x_target = top_left[0]
    print('x_target=' + str(x_target))
    return x_target


def get_track(distance):  # distance为传入的总距离
    track = []
    current = 0
    mid = distance * 3 / 5
    t = 0.2
    v = 1
    while current < distance:
        if current < mid:
            a = 4
        else:
            a = -2
        v0 = v
        v = v0 + a * t
        move = v0 * t + 1 / 2 * a * t * t
        current += move
        track.append(round(move))
    return track


def get_distance(bg_img_path, slider_img_path):
    """获取滑块移动距离"""

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
    return top_left + 10  # 10偏移值


def run(playwright: Playwright) -> None:
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

        #安全系统的用户、密码
        aq_user = config['set']['aq_user']
        aq_pwd = config['set']['aq_pwd']
        aq_url = config['set']['aq_url']
        # j_debug = config['system']['debug']
        # j_hang_no = int(j_hang_no)fl
    except Exception as r:
        print(f'config.ini文件加载错误！{r}')

    browser = playwright.chromium.launch(executable_path=chrome_path, headless=False)
    context = browser.new_context()
    # Open new page
    page = context.new_page()

    # chromium = playwright.chromium
    # browser = chromium.connect_over_cdp('http://localhost:12345/')
    # page = browser.contexts[0].pages[0]

    # # 关闭Webdriver属性
    js = """Object.defineProperties(navigator, {webdriver:{get:()=>undefined}});"""
    page.add_init_script(js)
    # Go to http://39.103.140.108:8089/login
    page.goto("http://39.103.140.108:8089/login")
    print(page.title())
    # Fill [placeholder="账号"]

    page.wait_for_timeout(1000)
    page.locator("[placeholder=\"账号\"]").fill(user)
    # Fill [placeholder="密码"]
    page.wait_for_timeout(1000)
    page.locator("[placeholder=\"密码\"]").click()
    page.locator("[placeholder=\"密码\"]").fill(pwd)

    # Click button:has-text("登 录")
    page.wait_for_timeout(2000)
    page.locator("button:has-text(\"登 录\")").click()
    page.wait_for_timeout(1000)
    # Click text=向右滑动完成验证
    time.sleep(8)

    def login():
        dt = '//*[@id="app"]/div/div[2]/div[2]/form/div[4]/div/div[2]/div/div[1]/div/img'
        dt_text = page.get_attribute(dt, 'src').replace('data:image/png;base64,', '')
        with open('max.png', 'wb') as f:
            f.write(base64.b64decode(dt_text))

        xt = '//*[@id="app"]/div/div[2]/div[2]/form/div[4]/div/div[2]/div/div[2]/div/div/div/img'
        text = page.get_attribute(xt, 'src').replace('data:image/png;base64,', '')
        with open('xiaotu.png', 'wb') as f:
            f.write(base64.b64decode(text))

        # img = cv.imread("max.png", flags=1)  # flags=1 读取彩色图像(BGR)
        element = page.query_selector('//*[@id="app"]/div/div[2]/div[2]/form/div[4]/div/div[2]/div/div[2]/div/div')  # xpath 滑块小元素
        box = element.bounding_box()
        # 点击导致被检测到？？
        # page.locator(xt).click()
        page.wait_for_timeout(2000)

        x = int(box["x"] + box["width"] / 2)
        y = int(box["y"] + box["height"] / 2)
        page.mouse.move(x + random.randint(-5, 5), y + random.randint(-5, 5))  # 小滑动拖动的滑块中心位置
        page.wait_for_timeout(500)
        page.mouse.down()
        page.wait_for_timeout(500)

        x_target = get_distance('max.png', 'xiaotu.png')
        print(x_target)

        track_list = get_track(x_target)
        i = 0
        for track in track_list:
            page.mouse.move(x + track, y + random.randint(-2, 2), steps=2)
            x = x + track
            if i < 0.8 * track_list.__len__():
                page.wait_for_timeout(random.randint(50, 80))
            else:
                page.wait_for_timeout(random.randint(150, 200))
            i = i + 1
        page.wait_for_timeout(1000)
        page.mouse.up()

    for i in range(3):
        login()
        # 元素是否存在
        page.wait_for_timeout(3000)
        is_ok = page.is_visible("text=南京催化剂智能安全系统")
        # input("1"*88)
        if is_ok:
            break

    with page.expect_navigation():
        page.locator("text=南京催化剂智能安全系统").click()

    # # # 点击，数字工地 文本
    page.locator("text=数字工地").click()
    # #
    # # 点击，数据看板 文本
    page.locator("text=数据看板").click()

    # 点击，查看
    with page.expect_popup() as popup_info:
        page.click('''xpath=//*[@id="app"]/div/div[2]/section/div/div[1]/div/div[2]/div/div/div[3]/table/tbody/tr[5]/td[7]/div/button[1]/span''')

    # 点击，塔机检测
    page1 = popup_info.value
    page1.click('''xpath=//*[@id="container"]/div[1]/div[2]/ul/li[2]/a''')
    p_url = page1.url
    print(f"获取地址成功：{page1.url}")

    page1.goto(aq_url)
    # Click [placeholder="手机号\/帐号"]
    page1.locator("[placeholder=\"手机号\\/帐号\"]").fill(aq_user)
    # Press Tab
    page1.locator("[placeholder=\"手机号\\/帐号\"]").press("Tab")
    # Fill [placeholder="密码"]
    page1.locator("[placeholder=\"密码\"]").fill(aq_pwd)
    # Press Enter
    # with page1.expect_navigation(url="https://chjapp.com:7777/Home/Index"):
    with page1.expect_navigation():
        page1.locator("[placeholder=\"密码\"]").press("Enter")
    # Click [id="\32 "]
    page1.locator("[id=\"\\32 \"]").click()
    # Click text=系统配置
    page1.locator("text=系统配置").click()
    # Click text=塔机监测URL
    page1.frame_locator("iframe").nth(1).locator("text=塔机监测URL").click()
    # Click text=编辑
    page1.frame_locator("iframe").nth(1).locator("text=编辑").click()
    # input('1'*88)
    # Click textarea >> nth=3
    page1.frame_locator("iframe[name=\"layui-layer-iframe1\"]").locator("textarea").nth(3).click()
    # Press a with modifiers
    page1.frame_locator("iframe[name=\"layui-layer-iframe1\"]").locator("textarea").nth(3).press("Control+a")
    # Fill textarea >> nth=3
    page1.frame_locator("iframe[name=\"layui-layer-iframe1\"]").locator("textarea").nth(3).fill(p_url)
    # Click a:has-text("确认")
    page1.locator("a:has-text(\"确认\")").click()
    print(r"设置地址成功。")



    # page1.url， 传入webservice
    now_time = time.time()
    # 毫秒级
    now_time = str(int(round(now_time * 1000)))
    token = hashlib.sha256((now_time + xt_key).encode('utf-8')).hexdigest()

    def request_webservice(wsdl, token, timekey, url):
        """
        实际部署时失效，
        """
        client = Client(wsdl)
        s1 = client.bind('WebService1', 'WebService1Soap')
        s = s1.ResetTowerUrl(token, timekey, url)
        return s

    # request_webservice(jk_url, token, now_time, page.url)




    context.close()
    browser.close()
    print(f'等待运行……，等待{sep_time}小时。')
    time.sleep(int(sep_time*3600))
    print('--'*88)






with sync_playwright() as playwright:
    while 1:
        try:
            run(playwright)
        except  Exception as r:
            print(f'运行错误{r},间隔4小时再次运行。')
            time.sleep(int(4 * 3600))

