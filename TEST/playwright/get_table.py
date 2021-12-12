from playwright.sync_api import Playwright, sync_playwright
import time

def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    # Open new page
    page = context.new_page()
    # Go to https://www.w3school.com.cn/tiy/t.asp?f=eg_html_table_test
    page.goto("https://www.w3school.com.cn/tiy/t.asp?f=eg_html_table_test")
    time.sleep(5)
    f = "[id='iframewrapper']"
    f = "[id='iframeResult']"
    table = page.query_selector(f).content_frame()
    # table = page.query_selector(""".iframeResult""").content_frame()
    print(page.frames)
    print(type(table))
    print(table)
    input('-'*88)
    # ---------------------
    context.close()
    browser.close()
with sync_playwright() as playwright:
    run(playwright)

