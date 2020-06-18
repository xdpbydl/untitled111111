#!/usr/bin/env python
# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

chrome_option = webdriver.ChromeOptions()
chrome_option.add_experimental_option('excludeSwitches', ['enable-automation'])  # 以开发者模式

driver = webdriver.Chrome(options=chrome_option)
wait = WebDriverWait(driver, 10)


def search():
    driver.get('https://www.taobao.com')
    try:
        search_input = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '#q'))
        )
        search_submit = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '#J_TSearchForm > div.search-button > button'))
        )
        driver.save_screenshot("E:/TEMP/google/q1.png")
    finally:
        pass
    search_input.send_keys('美食'.decode('utf-8'))
    driver.save_screenshot("E:/TEMP/google/q2.png")
    search_submit.click()
    driver.save_screenshot("E:/TEMP/google/q3.png")
    login()


def login():
    try:
        login_before = wait.until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, '#J_QRCodeLogin > div.login-links > a.forget-pwd.J_Quick2Static'))
        )
        login_before.click()

        username = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '#TPL_username_1'))
        )
        password = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '#TPL_password_1'))
        )
        driver.save_screenshot("E:/TEMP/google/q4.png")
        username.send_keys('xxxxx')  # 用户名
        password.send_keys('xxxxx')  # 密码
        driver.save_screenshot("E:/TEMP/google/q5.png")
        login_submit = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '#J_SubmitStatic'))
        )
        login_submit.click()
    finally:
        pass


def main():
    search()


if __name__ == '__main__':
    main()