# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.firefox.options import Options
import time, csv
from selenium.webdriver.common.by import By

# options = Options()
# options.headless = True
# driver = webdriver.Firefox (options=options)
driver = webdriver.chrome()
driver.implicitly_wait(10)

driver.get("https://www.ydxxt.com/")

elem_user = driver.find_element_by_name("userid")
elem_user.clear()
elem_user.send_keys("150881732061")
elem_pwd = driver.find_element_by_name("psw")
elem_pwd.send_keys("1y20050917@1")
time.sleep(5)
elem_pwd.send_keys(Keys.RETURN)
time.sleep(3)
driver.find_element_by_css_selector('input[value="进入系统"]').click()
time.sleep(3)
driver.find_element_by_css_selector("#A2").click()
driver.find_element_by_css_selector(".WEBItc_list_con1 > ul:nth-child(1) > li:nth-child(9) > a:nth-child(1)").click()
time.sleep(2)

driver.switch_to_frame('mainFrame')
driver.find_element_by_link_text('学生调班').click()

aabb = '/html/body/div[1]/div[2]/div/table/tbody[1]/tr'
no = 0

output = open('data.csv', 'w', newline='')
for m in range(200):
    table = driver.find_element_by_id('xstb_list')
    table_rows = len(table.find_elements_by_tag_name('tr'))
    # print (u"总行数：", len (table_rows))
    # table_rows=len(driver.find_elements_by_tag_name ('tr'))
    print("循环到%s页，本页%s行,共获取%s" % (str(m + 1), str(table_rows - 2), str(no)))

    for i in range(1, table_rows - 1):

        try:
            s_no = driver.find_element_by_xpath(aabb + '[%s]/td[2]' % (str(i))).text
            s_name = driver.find_element_by_xpath(aabb + '[%s]/td[3]/div' % (str(i))).get_attribute('title')
            s_panji = driver.find_element_by_xpath(aabb + '[%s]/td[5]' % (str(i))).text
            s_ic = driver.find_element_by_xpath(aabb + '[%s]/td[6]' % (str(i))).text
            s_sex = driver.find_element_by_xpath(aabb + '[%s]/td[7]' % (str(i))).text
            s_pap = driver.find_element_by_xpath(aabb + '[%s]/td[8]/div' % (str(i))).get_attribute('title')
            s_tel = driver.find_element_by_xpath(aabb + '[%s]/td[9]/div' % (str(i))).get_attribute('title')

        except:
            try:
                s_pap = driver.find_element_by_xpath(aabb + '[%s]/td[1]/div' % (str(i))).get_attribute('title')
                s_tel = driver.find_element_by_xpath(aabb + '[%s]/td[2]/div' % (str(i))).get_attribute('title')
                ##(多家长)
                s_no, s_name, s_panji, s_ic, s_sex = '', '', '', '', ''
            except:
                pass

        no += 1
        writer = csv.writer(output)
        writer.writerow([no, s_no, s_name, s_panji, s_ic, s_sex, s_pap, s_tel])
        print(no, s_no, s_name, s_panji, s_ic, s_sex, s_pap, s_tel)

    output.flush()
    top = driver.find_element_by_link_text('下一页')
    driver.execute_script("arguments[0].scrollIntoView(false);", top)
    top.click()
    # driver.execute_script ("arguments[0].scrollIntoView(false);", target)
    el_list = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/table/tbody[2]/tr/td")
    page = el_list.find_element_by_xpath("//input[@name='rollhidden']").get_attribute('value')
    print("当前第%s页" % str(page) + "----" * 20)
    # print ("----当前---%s---页" % page)
    # print (int (page) != m + 2)

# time.sleep(5000)
output.close()
driver.close()
driver.quit()
