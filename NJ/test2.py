from playwright.sync_api import Playwright, sync_playwright
import cv2 as cv
import random, os, configparser, base64


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
        # j_hang_no = config['system']['hang_no']
        # j_debug = config['system']['debug']
        # j_hang_no = int(j_hang_no)
    except Exception as r:
        print(f'config.ini文件加载错误！{r}')

    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    # Open new page
    page = context.new_page()
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
    # Click text=数字看板
    page.wait_for_timeout(1000)
    page.locator("text=数字看板").click()
    # Click button:has-text("登 录")
    page.wait_for_timeout(2000)
    page.locator("button:has-text(\"登 录\")").click()
    page.wait_for_timeout(1000)
    # Click text=向右滑动完成验证
    # time.sleep(8)
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
        page.locator(xt).click()
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
        print(is_ok)
        if is_ok:
            break
    # input('11' * 88)

    with page.expect_popup() as popup_info:
        page.locator("text=南京催化剂智能安全系统").click()
    page1 = popup_info.value
    # Click text=塔机监测
    page1.locator("text=塔机监测").click()
    page1.url
    print(page1.url)

    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
