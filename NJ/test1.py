from playwright.sync_api import Playwright, sync_playwright, expect
import time, os
import pandas as pd
import configparser

def run(playwright: Playwright, url, user, pwd) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()

    # Open new page
    page = context.new_page()

    # Go to url
    page.goto(url)

    # Click [placeholder="手机号\/帐号"]
    page.locator("[placeholder=\"手机号\\/帐号\"]").click()

    # Fill [placeholder="手机号\/帐号"]
    page.locator("[placeholder=\"手机号\\/帐号\"]").fill(user)

    # Click [placeholder="密码"]
    page.locator("[placeholder=\"密码\"]").click()

    # Fill [placeholder="密码"]
    page.locator("[placeholder=\"密码\"]").fill(pwd)

    # Click #lr_login_btn
    # with page.expect_navigation(url=""):
    with page.expect_navigation():
        page.locator("#lr_login_btn").click()

    time.sleep(5)
    # Click text=人员管理
    page.locator("text=人员管理").click()

    # Click text=人员档案
    page.locator("text=人员档案").click()
    ss = get_data(file)
    for index, i in ss.iterrows():
        # Click text=新增
        print(i[['*姓名', '*性别', '*组织路径', '*证件号码', '手机号码']])
        input('--' * 88)
        time.sleep(5)
        page.frame_locator("iframe").nth(1).locator("text=新增").click()

        # Click #F_Name
        page.frame_locator("iframe[name=\"layui-layer-iframe1\"]").locator("#F_Name").click()
        page.frame_locator("iframe[name=\"layui-layer-iframe1\"]").locator("#F_Name").fill(i['*姓名'])

        # Click #F_MobileNo
        page.frame_locator("iframe[name=\"layui-layer-iframe1\"]").locator("#F_MobileNo").click()
        page.frame_locator("iframe[name=\"layui-layer-iframe1\"]").locator("#F_MobileNo").fill(str(i['手机号码']))

        # Click text=岗位信息
        page.frame_locator("iframe[name=\"layui-layer-iframe1\"]").locator("text=岗位信息").click()

        # Click #F_Company >> text===请选择==
        page.frame_locator("iframe[name=\"layui-layer-iframe1\"]").locator("#F_Company >> text===请选择==").click()

        # Click text=中石化第四建设有限公司
        text = f'text={i["*组织路径"]}'
        page.frame_locator("iframe[name=\"layui-layer-iframe1\"]").locator(text).click()

        # Check input[name="F_ACAreaSelect"]
        page.frame_locator("iframe[name=\"layui-layer-iframe1\"]").locator("input[name=\"F_ACAreaSelect\"]").check()

        # Click #F_FirstTime
        page.frame_locator("iframe[name=\"layui-layer-iframe1\"]").locator("#F_FirstTime").click()
        page.frame_locator("iframe[name=\"layui-layer-iframe1\"]").locator("#F_FirstTime").fill(i['2022-09-09'])

        # # Click text=确定
        # page.frame_locator("iframe[name=\"layui-layer-iframe1\"]").locator("text=确定").click()

        # Click #F_EndTime
        page.frame_locator("iframe[name=\"layui-layer-iframe1\"]").locator("#F_EndTime").click()
        page.frame_locator("iframe[name=\"layui-layer-iframe1\"]").locator("#F_EndTime").fill(i['2022-09-09'])

        # # Click text=2022年
        # page.frame_locator("iframe[name=\"layui-layer-iframe1\"]").locator("text=2022年").click()
        #
        # # Click text=2023年
        # page.frame_locator("iframe[name=\"layui-layer-iframe1\"]").locator("text=2023年").click()
        #
        # # Click text=确定
        # page.frame_locator("iframe[name=\"layui-layer-iframe1\"]").locator("text=确定").click()

        # Click a:has-text("关闭")
        page.locator("a:has-text(\"关闭\")").click()

    # ---------------------
    context.close()
    browser.close()


def get_data(file):
    df = pd.read_excel(file)
    return df[['*姓名', '*性别', '*组织路径', '*证件号码', '手机号码']]


# 获取配置文件
file = os.path.join(os.path.abspath('.'), 'config.ini')
config = configparser.ConfigParser()
# config.read(file, encoding="utf-8")
config.read(file, encoding="utf-8-sig")
try:
    url = config['set']['url']
    user = config['set']['user']
    pwd = config['set']['pwd']
    file = config['file']['file']
    # j_hang_no = int(j_hang_no)
except Exception as r:
    print(f'config.ini文件加载错误！{r}')


# photo_path = r'D:\ZCXX\Project\广州中石科技\3. 部署配置\1.2入场人员录入\20220909\\'
# file = f'{photo_path}2000吨吸附剂项目入场人员门禁信息导入表 - 2022.09.7.xls'

with sync_playwright() as playwright:
    print(playwright, url, user, pwd)
    run(playwright, url, user, pwd)
