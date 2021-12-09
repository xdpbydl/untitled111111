from playwright.sync_api import Playwright, sync_playwright
import time

def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()

    # Open new page
    page = context.new_page()

    # Go to https://192.168.0.160/portal/ui/login?service=https://192.168.0.160:443/portal/
    page.goto("https://192.168.0.160/portal/ui/login?service=https://192.168.0.160:443/portal/")

    # Go to https://192.168.0.160/portal/ui/login?service=https%3A%2F%2F192.168.0.160%3A443%2Fportal%2F
    page.goto("https://192.168.0.160/portal/ui/login?service=https%3A%2F%2F192.168.0.160%3A443%2Fportal%2F")

    # Click [placeholder="请输入用户名"]
    page.click("[placeholder=\"请输入用户名\"]")

    # Fill [placeholder="请输入用户名"]
    page.fill("[placeholder=\"请输入用户名\"]", "admin")

    # Press Tab
    page.press("[placeholder=\"请输入用户名\"]", "Tab")

    # Fill [placeholder="请输入密码"]
    page.fill("[placeholder=\"请输入密码\"]", "SuperSuper168!")

    # Click button:has-text("登录")
    # with page.expect_navigation(url="https://192.168.0.160/portal/ui/index"):
    with page.expect_navigation():
        page.click("button:has-text(\"登录\")")

    # Click div:nth-child(4) .content div:nth-child(2) img
    page.click("div:nth-child(4) .content div:nth-child(2) img")

    time.sleep(5)
    # Click li:has-text("人员出入事件")
    page.click("li:has-text(\"人员出入事件\")")




    # ---------------------
    # context.close()
    # browser.close()


with sync_playwright() as playwright:
    run(playwright)
