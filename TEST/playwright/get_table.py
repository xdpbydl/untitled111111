from playwright.sync_api import Playwright, sync_playwright
import time
import pandas as pd
from io import StringIO

def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context()
    # Open new page
    page = context.new_page()
    # Go to
    page.goto("https://finance.sina.com.cn/mac/")
    time.sleep(2)
    f = ".btable"
    n = 1
    table = page.query_selector_all(f)
    print(f"长度:{len(table)}， 类型:{type(table)}" )
    excel_file = pd.ExcelWriter(f'E:\\TEMP\\6TEST\\0000\\file.xlsx', engine='openpyxl')
    for i in table:
        print(i.inner_text())
        i_txt = StringIO(i.inner_text())
        print(i_txt)
        df = pd.read_csv(i_txt, sep="\t")
        df.to_excel(excel_writer=excel_file, sheet_name=str(n), index=False)
        # print(df)
        n += 1

        # print([x.inner_text() for x in i.query_selector_all('thead')])
        # print([x.inner_text() for x in i.query_selector_all('tbody')])
        # input('1' * 88)

    excel_file.save()
    excel_file.close()
    input('-'*88)
    # ---------------------
    context.close()
    browser.close()
with sync_playwright() as playwright:
    run(playwright)

