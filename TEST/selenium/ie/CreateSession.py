from selenium import webdriver
import sys

sys.path.append("..")
from ReuseIe import *
import configparser

ie_driver = r"C:\\Program Files\\Internet Explorer\\IEDriverServer.exe"
driver = webdriver.Ie(executable_path=ie_driver)
url = driver.command_executor._url
session_id = driver.session_id
print(driver.session_id)
print(driver.command_executor._url)

config = configparser.ConfigParser()
config.add_section("IE")
config.set("IE", "url", url)
config.set("IE", "session_id", session_id)

with open("session.ini", "w+") as f:
    config.write(f)
f.close()
