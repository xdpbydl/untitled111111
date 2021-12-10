from playwright.sync_api import Playwright, sync_playwright
import time
import pandas as pd

def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)  #
    context = browser.new_context()

    # Open new page
    page = context.new_page()

    # Go to
    page.goto("https://192.168.0.160/")

    # Click [placeholder="请输入用户名"]
    # page.click("[placeholder=\"请输入用户名\"]")

    # Fill [placeholder="请输入用户名"]
    page.fill("[placeholder=\"请输入用户名\"]", "admin")

    # Press Tab
    # page.press("[placeholder=\"请输入用户名\"]", "Tab")

    # Fill [placeholder="请输入密码"]
    page.fill("[placeholder=\"请输入密码\"]", "SuperSuper168!")

    # Click button:has-text("登录")
    # with page.expect_navigation(url="https://192.168.0.160/portal/ui/index"):
    with page.expect_navigation():
        page.click("button:has-text(\"登录\")")

    # Click div:nth-child(4) .content div:nth-child(2) img
    page.click("div:nth-child(4) .content div:nth-child(2) img")

    time.sleep(3)
    # Click li:has-text("人员出入事件")
    page.click("li:has-text(\"权限下载记录\")")

    # page.frame(name="iSecure Center_c010300").click("#app div div:has-text(\"*任务编号**控制器**门禁点**所在区域**下载类型* ctrl_tick Created with Sketch. 计划模板 ctrl_tick Creat\")")
    # aa = page.query_selector('''xpath: //*[@id="app"]/div/div[1]/div[2]/div/div[1]/div[3]''')

    aa = page.text_content('''xpath=//*[@id="app"]/div/div[1]/div[2]/div/div[1]/div[3]''')

    print(aa)
    input('--'*5)


    # ---------------------
    # context.close()
    # browser.close()


with sync_playwright() as playwright:
    run(playwright)
