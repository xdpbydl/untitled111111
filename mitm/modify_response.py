# coding: utf-8
# modify_response.py

import re
import mitmproxy.http
from mitmproxy import ctx


class Counter:
    def __init__(self):
        self.num = 0

    def request(self, flow: mitmproxy.http.HTTPFlow):
        self.num = self.num + 1
        ctx.log.info("We've seen %d flows" % self.num)

    def response(flow):
        """修改应答数据
        """
        if i in flow.request.url:
            # 屏蔽selenium检测
            for webdriver_key in ['webdriver', '__driver_evaluate', '__webdriver_evaluate', '__selenium_evaluate',
                                  '__fxdriver_evaluate', '__driver_unwrapped', '__webdriver_unwrapped',
                                  '__selenium_unwrapped', '__fxdriver_unwrapped', '_Selenium_IDE_Recorder', '_selenium',
                                  'calledSelenium', '_WEBDRIVER_ELEM_CACHE', 'ChromeDriverw', 'driver-evaluate',
                                  'webdriver-evaluate', 'selenium-evaluate', 'webdriverCommand',
                                  'webdriver-evaluate-response', '__webdriverFunc', '__webdriver_script_fn',
                                  '__$webdriverAsyncExecutor', '__lastWatirAlert', '__lastWatirConfirm',
                                  '__lastWatirPrompt', '$chrome_asyncScriptInfo', '$cdc_asdjflasutopfhvcZLmcfl_']:
                ctx.log.info('Remove "{}" from {}.'.format(webdriver_key, flow.request.url))
                flow.response.text = flow.response.text.replace('"{}"'.format(webdriver_key), '"NO-SUCH-ATTR"')
            flow.response.text = flow.response.text.replace('t.webdriver', 'false')
            flow.response.text = flow.response.text.replace('ChromeDriver', '')


addons = [
    Counter()
]