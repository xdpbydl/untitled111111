# !/usr/bin/env python
# -*- coding: utf-8 -*-

"""
__title__  =
__Time__   = 2020/3/25 17:52
__Author__ = 小菠萝测试笔记
__Blog__   = https://www.cnblogs.com/poloyy/
"""

from selenium import webdriver

driver = webdriver.Chrome()

driver.get("https://weixin.sogou.com/weixin?type=1&query=%E6%97%B6%E5%AF%92%E5%86%B0&ie=utf8&s_from=input&_sug_=n&_sug_type_=")
driver.maximize_window()

# 截取整个页面
driver.get_screenshot_as_file("test.png")
driver.save_screenshot("tests.png")

# # 找到搜索框
# inputElement = driver.find_element_by_id("kw")vv
#
# # 截取搜索框元素
# inputElement.screenshot("inputElement.png")
