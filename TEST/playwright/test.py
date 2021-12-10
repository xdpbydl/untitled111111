from playwright.sync_api import Playwright, sync_playwright

def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    # Open new page
    page = context.new_page()
    # Go to https://www.baidu.com/
    page.goto("https://www.baidu.com/")
    # Click input[name="wd"]
    page.click("input[name=\"wd\"]")
    # Fill input[name="wd"]
    page.fill("input[name=\"wd\"]", "playwright教程")
    # Press ArrowDown
    page.press("input[name=\"wd\"]", "ArrowDown")
    # Click text=百度一下
    # with page.expect_navigation(url="https://www.baidu.com/s?ie=utf-8&f=3&rsv_bp=1&rsv_idx=1&tn=baidu&wd=playwright%E6%95%99%E7%A8%8B&fenlei=256&rsv_pq=fb0269c100013040&rsv_t=c1d6F6v22Go9kylNjFlSm6vYJoOa0odjrxeQBTH%2BmCRdqrDMSx6gjuMfXCA&rqlang=cn&rsv_enter=0&rsv_dl=ts_0&rsv_sug3=9&rsv_sug1=9&rsv_sug7=100&rsv_btype=i&prefixsug=playwri&rsp=0&inputT=12964&rsv_sug4=20028&rsv_jmp=fail"):
    with page.expect_navigation():
        page.click("text=百度一下")
    # assert page.url == "https://www.baidu.com/s?ie=utf-8&f=3&rsv_bp=1&rsv_idx=1&tn=baidu&wd=playwright%E6%95%99%E7%A8%8B&fenlei=256&rsv_pq=fb0269c100013040&rsv_t=c1d6F6v22Go9kylNjFlSm6vYJoOa0odjrxeQBTH%2BmCRdqrDMSx6gjuMfXCA&rqlang=cn&rsv_enter=0&rsv_dl=ts_0&rsv_sug3=9&rsv_sug1=9&rsv_sug7=100&rsv_btype=i&prefixsug=playwri&rsp=0&inputT=12964&rsv_sug4=20028"
    # Click text=Playwright快速上手指南 - 行者AI - 博客园
    # with page.expect_navigation(url="https://www.cnblogs.com/xingzheai/p/14360714.html"):
    with page.expect_navigation():
        with page.expect_popup() as popup_info:
            page.click("text=Playwright快速上手指南 - 行者AI - 博客园")
        page1 = popup_info.value
    # Click text=page = context.newPage() def Whether_intercept() -> bool: return True #进行拦截 # re
    page1.click("text=page = context.newPage() def Whether_intercept() -> bool: return True #进行拦截 # re")
    # Click text=page = context.newPage() def Whether_intercept() -> bool: return True #进行拦截 # re
    page1.click("text=page = context.newPage() def Whether_intercept() -> bool: return True #进行拦截 # re")
    # ---------------------
    context.close()
    browser.close()
with sync_playwright() as playwright:
    run(playwright)
