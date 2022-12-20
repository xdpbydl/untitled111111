from playwright.sync_api import Playwright, sync_playwright, expect
import pandas as pd

def run(playwright: Playwright) -> None:
    chromium = playwright.chromium
    browser = chromium.connect_over_cdp('http://localhost:12345/')
    page1 = browser.contexts[0].pages[0]
    print(page1.url)
    #调用已打开的网页，进入chrome安装目录，在CMD执行以下命令行
    # .\chrome.exe --remote-debugging-port=12345 -–incognito -–start-maximized --user-data-dir="C:\selenium\chrome" --new-window https://www.baidu.com
    #
    # browser = playwright.chromium.launch(headless=False)
    # context = browser.new_context()
    # # Open new page
    # page = context.new_page()

    # Go to https://chjapp.com:7777/
    page1.goto("https://chjapp.com:7777/")
    # Click [placeholder="手机号\/帐号"]
    page1.locator("[placeholder=\"手机号\\/帐号\"]").fill("system")
    # Press Tab
    page1.locator("[placeholder=\"手机号\\/帐号\"]").press("Tab")
    # Fill [placeholder="密码"]
    page1.locator("[placeholder=\"密码\"]").fill("Pass123!")
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
    # Click textarea >> nth=3
    page1.frame_locator("iframe[name=\"layui-layer-iframe1\"]").locator("textarea").nth(3).click()
    # Press a with modifiers
    page1.frame_locator("iframe[name=\"layui-layer-iframe1\"]").locator("textarea").nth(3).press("Control+a")
    # Fill textarea >> nth=3
    page1.frame_locator("iframe[name=\"layui-layer-iframe1\"]").locator("textarea").nth(3).fill(
        "http://39.103.140.108:8777/view/691?id=691&configId=5069&userId=329264033140805&userType=1&token=eyJhbGciOiJIUzUxMiJ9.eyJsb2dpbl91c2VyX2tleSI6IjE0MzY5YWZmLWRjMTUtNGNlZC1iMjMzLTIyZDYyODRjZmJjMSJ9.LDqQnniSz0HI7eQjtV3jZLW1EpRGHEFs2oAwgPSyngu-Nymfnwj4NCGXqM_Iof7GpCACUT5IF6CpRiHrra9Nbg&see=view&title=%25E5%258D%2597%25E4%25BA%25AC%25E5%2582%25AC%25E5%258C%2596%25E5%2589%2582%25E6%2599%25BA%25E8%2583%25BD%25E5%25AE%2589%25E5%2585%25A8%25E7%25B3%25BB%25E7%25BB%259F&menuId=329264033140805")
    # Click a:has-text("确认")
    page1.locator("a:has-text(\"确认\")").click()
    input('22'*88)



    # page.locator("text=低风险区").click()
    # input("--"*88)
    def level_qf(txt_qf):
        """
        获取不同风险等级,默认展示高风险
        :return: data_list
        """
        data_list = []
        # Click text=低风险区
        if txt_qf == "低风险区":
            page.locator("text=低风险区").click()
        page_no = page.query_selector_all(".pages-box>button")
        page_no_str = page_no[-3].inner_text()
        # print(page_no_str)
        # input('11' * 88)
        def get_page_data():
            """
            获取每一页的数据
            :return:
            """
            info_tables = page.query_selector_all(".risk-info-table")
            # print(len(info_tables))
            for i in info_tables:
                title = i.query_selector(".risk-info-table-title").inner_text()     # 街道
                # print(title)
                inner = i.query_selector_all(".risk-info-table-inner>tr")       # 具体地区的个数
                print(title, len(inner))
                data_list.append([title, f'{len(inner)} 个'])
                for n in inner:
                    # even = n.query_selector("css=.even >> td")   # 'css=article >> css=.bar > .baz >> css=span[attr=value]'
                    level = n.query_selector("td").inner_text()      # 具体地区
                    # print(level)
                    data_list.append([level, txt_qf])


        # page_no_str = "1"
        for i in range(int(page_no_str)):
            get_page_data()
            # Click text=下一页
            print(f"已经导出{txt_qf},第{i+1}页数据")
            # if i == int(page_no_str) - 1:
            #     pass   # 最后一页，不用点击翻页
            # else:
            try:
                page.locator("text=下一页").click()
            except:
                print(f"导出{txt_qf},第{i+1}页数据出错……")
        return data_list
    dengji = ["高风险区", "低风险区"]
    for i in dengji:
        qf_data = level_qf(i)
        if i == "高风险区":
            df_g = pd.DataFrame(data=qf_data, columns=['街道/地区', '数量/等级'])
        elif i == "低风险区":
            df_d = pd.DataFrame(data=qf_data, columns=['街道/地区', '数量/等级'])
        # print(qf_data)
        # input("22"*88)

    with pd.ExcelWriter(f"d:\\yiqing\\{jiezhi_t}.xlsx") as xlsx:
        df_g.to_excel(xlsx, sheet_name=dengji[0], index=False)
        df_d.to_excel(xlsx, sheet_name=dengji[1], index=False)



    # # Click text=北京市 朝阳区 呼家楼街道
    # page.locator("text=北京市 朝阳区 呼家楼街道").click()
    #
    # # Click text=呼家楼街道（除高风险区外的其他地区）
    # page.locator("text=呼家楼街道（除高风险区外的其他地区）").click()
    #
    # # Click text=呼家楼街道（除高风险区外的其他地区） 低风险 >> td >> nth=1
    # page.locator("text=呼家楼街道（除高风险区外的其他地区） 低风险 >> td").nth(1).click()


    # Close page
    page.close()

    # ---------------------

    browser.close()


with sync_playwright() as playwright:
    run(playwright)
