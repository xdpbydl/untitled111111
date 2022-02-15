from playwright.sync_api import Playwright, sync_playwright
import time


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    cookies = [{'name': 'QCARJSESSIONID', 'value': 'BBmPcsfClCknfQX1cN2MLMgKXZGtFWqsBvjN9mbM9tmbL38hMmw4!1426878101', 'path': '/','domain': 'qcar.apiins.com', 'secure': False, 'httpOnly': True},
               {'name': 'BIGipServercar_qcar_poool', 'value': '1191316140.16671.0000', 'path': '/', 'domain': 'qcar.apiins.com', 'secure': False,'httpOnly': False},
               {'name': 'chinainsuranceJSESSIONID', 'value': 'rkgncsfG8pnrhh8x1CvNy46zHplyLkTjyv1LL2hk4wDrkD9Mjz9Y!2078734058', 'path': '/','domain': 'qcar.apiins.com', 'secure': False, 'httpOnly': True},
               {'name': 'BIGipServercar_core_pool', 'value': '1191316140.17951.0000', 'path': '/', 'domain': 'qcar.apiins.com', 'secure': False,'httpOnly': False}]
    context.add_cookies(cookies=cookies)
    # Open new page
    page = context.new_page()

    # Go to https://www.baidu.com/
    page.goto("https://www.baidu.com/")

    # Click input[name="wd"]
    page.click("input[name=\"wd\"]")

    # Fill input[name="wd"]
    page.fill("input[name=\"wd\"]", "playwright教程")

    # Click input[name="wd"]
    page.click("input[name=\"wd\"]")

    # Click input[name="wd"]
    page.click("input[name=\"wd\"]")

    with page.expect_navigation():
        page.click("text=百度一下")
        time.sleep(4)
    # f = """[class='result c-container new-pmd']"""
    f = "c-container"
    # f = '''div[srcid='1599']'''
    n = 1

    try:
        while 1:
            try:
                is_no = page.is_enabled("text=下一页 >")
            except:
                print(f"{'-' * 18}获取完成！{'-' * 18}")

            aa = page.query_selector_all(f"""div.{f}>h3>a""")
            for i in aa:
                txt = i.inner_text()  # 返回str，获取a标签（你下面标签）的全部文本
                txt2 = i.get_property('href')  # 获取 href 属性内容
                # txt = i.t
                print(f"{n}---{txt},  url:{txt2}")
                n += 1

            time.sleep(2)
            page.click("text=下一页 >")
            time.sleep(5)

    except:
        print("获取错误")
    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
