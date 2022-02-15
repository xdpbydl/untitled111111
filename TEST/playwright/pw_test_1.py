from playwright.sync_api import Playwright, sync_playwright
import time

def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()

    # Open new page
    page = context.new_page()

    # Go to https://new.qq.com/ch/finance/
    page.goto("https://so.eastmoney.com/web/s?keyword=000625")
    input('111')
    # Click input[name="cl"]
    page.frame(url="https://finance.qq.com/new_finance.htm").click("input[name=\"cl\"]")

    # Fill input[name="cl"]
    page.frame(url="https://finance.qq.com/new_finance.htm").fill("input[name=\"cl\"]", "000625")

    # Click input[name="submitbtn"]
    # with page.expect_navigation(url="https://gu.qq.com/sz000625/gp"):
    with page.expect_navigation():
        with page.expect_popup() as popup_info:
            page.frame(url="https://finance.qq.com/new_finance.htm").click("input[name=\"submitbtn\"]")
        page1 = popup_info.value
    time.sleep(5)
    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
