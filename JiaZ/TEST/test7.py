from playwright.sync_api import Playwright, sync_playwright
import time

def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()

    # Open new page
    page = context.new_page()

    # Go to http://192.168.0.168:8062/Login/Index
    page.goto("http://192.168.0.168:8062/Login/Index")

    # Click [placeholder="手机号/帐号"]
    page.click("[placeholder=\"手机号/帐号\"]")

    # Fill [placeholder="手机号/帐号"]
    page.fill("[placeholder=\"手机号/帐号\"]", "04390")

    # Click [placeholder="密码"]
    page.click("[placeholder=\"密码\"]")

    # Fill [placeholder="密码"]
    page.fill("[placeholder=\"密码\"]", "123456")

    # Click #lr_login_btn
    # with page.expect_navigation(url="http://192.168.0.168:8062/Home/Index"):
    with page.expect_navigation():
        page.click("#lr_login_btn")

    time.sleep(3)
    # Click text=合同发起合同发起和审核合同归档 >> i
    page.click("text=合同发起")
    time.sleep(1)
    # Click text=合同发起和审核
    page.click("text=合同发起和审核")

    time.sleep(1)
    # Click text=创建
    # page.frame(name="lr_iframe_d0574276-13ac-4dff-9744-93debba3c55f").click("a:has-text(\"创建\")")
    print(page.frames)

    page.query_selector("#lr_release > span").click()

    input('-'*88)
    time.sleep(1)
    # Click text=名称：广州总部 编号：FQ005 >> p
    page.frame(name="layui-layer-iframe1").click("text=名称：广州总部 编号：FQ005 >> p")

    time.sleep(1)
    # Click text=确认
    page.click("text=确认")

    time.sleep(1)
    # Click text=请选择清空
    page.frame(name="wfFormIframe0").click("text=请选择清空")

    # Click text=预取合同号
    page.frame(name="layui-layer-iframe2").click("text=预取合同号")

    # Click text=GRWL-2021-053
    page.frame(name="layui-layer-iframe2").click("text=GRWL-2021-053")

    # Click text=确认
    page.click("text=确认")

    # Click input[type="text"]
    page.frame(name="wfFormIframe0").click("input[type=\"text\"]")

    # Fill input[type="text"]
    page.frame(name="wfFormIframe0").fill("input[type=\"text\"]", "20211216——1")

    # Click text===请选择==
    page.frame(name="wfFormIframe0").click("text===请选择==")

    # Click text=服务合同
    page.frame(name="wfFormIframe0").click("text=服务合同")

    # Click #h_effective_date
    page.frame(name="wfFormIframe0").click("#h_effective_date")

    # Click text=现在
    page.frame(name="wfFormIframe0").click("text=现在")

    # Click #h_termination_date
    page.frame(name="wfFormIframe0").click("#h_termination_date")

    # Click td:has-text("31")
    page.frame(name="wfFormIframe0").click("td:has-text(\"31\")")

    # Click text=确定
    page.frame(name="wfFormIframe0").click("text=确定")

    # Click text===请选择==
    page.frame(name="wfFormIframe0").click("text===请选择==")

    # Click text=供应商(非运输)
    page.frame(name="wfFormIframe0").click("text=供应商(非运输)")

    # Click text=请选择清空
    page.frame(name="wfFormIframe0").click("text=请选择清空")

    # Click text=四川万马高分子材料有限公司
    page.frame(name="layui-layer-iframe3").click("text=四川万马高分子材料有限公司")

    # Click text=确认
    page.click("text=确认")

    # Click text===请选择==
    page.frame(name="wfFormIframe0").click("text===请选择==")

    # Click text=销售类
    page.frame(name="wfFormIframe0").click("text=销售类")

    # Click text=请选择清空
    page.frame(name="wfFormIframe0").click("text=请选择清空")

    # Click text=广州总部（非经营类）
    page.frame(name="layui-layer-iframe4").click("text=广州总部（非经营类）")

    # Click text=广州总部（非经营类）
    page.frame(name="layui-layer-iframe4").click("text=广州总部（非经营类）")

    # Click text=确认
    page.click("text=确认")

    # Click text=上传
    page.frame(name="wfFormIframe0").click("text=上传")

    # Click label
    page.frame(name="layui-layer-iframe5").click("label")

    # Upload word.docx
    page.frame(name="layui-layer-iframe5").set_input_files("body:has-text(\"添加文件 试试将电脑里的文件拖拽到此上传\")", "word.docx")

    # Click #layui-layer5 >> :nth-match(a, 3)
    page.click("#layui-layer5 >> :nth-match(a, 3)")

    # Click #jfgrid_toolbar_h_files_info i
    page.frame(name="wfFormIframe0").click("#jfgrid_toolbar_h_files_info i")

    # Click #lrUploader_uploadBtn_undefined0
    page.frame(name="wfFormIframe0").click("#lrUploader_uploadBtn_undefined0")

    # Click label
    page.frame(name="layui-layer-iframe6").click("label")

    # Upload 用.docx
    page.frame(name="layui-layer-iframe6").set_input_files("body:has-text(\"添加文件 试试将电脑里的文件拖拽到此上传\")", "用.docx")

    # Click #layui-layer6 >> :nth-match(a, 3)
    page.click("#layui-layer6 >> :nth-match(a, 3)")

    # Click text=创建流程
    page.frame(name="lr_iframe_d6f8be97-fe22-4acc-b0a2-ec126a9598f6").click("text=创建流程")

    # Click text=我的合同
    page.frame(name="lr_iframe_d0574276-13ac-4dff-9744-93debba3c55f").click("text=我的合同")

    # Click text=GRWL-2021-053
    page.frame(name="lr_iframe_d0574276-13ac-4dff-9744-93debba3c55f").click("text=GRWL-2021-053")

    # Click text=查看
    page.frame(name="lr_iframe_d0574276-13ac-4dff-9744-93debba3c55f").click("text=查看")

    # Click text=流程信息
    page.frame(name="lr_iframe_82e63047-1faa-8d60-9bf8-df0cafdb4ca1").click("text=流程信息")

    # Click text=部长审批
    page.frame(name="lr_iframe_82e63047-1faa-8d60-9bf8-df0cafdb4ca1").click("text=部长审批")

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
