from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get(f'http://yige.org/tags/yige.php?filename=table_test')
# time.sleep(2)

# driver.find_element_by_id('kw').send_keys('今天')
# driver.find_element_by_css_selector ('input[value="百度一下"]').click ()  #ok
# driver.find_element_by_css_selector('input[class="bg s_btn"]').click()

print(f'-------------------')
# table = driver.switch_to_frame('iframeResult')
driver.switch_to_frame(0)
# driver.switch_to_frame(1)

# driver.find_elements_by_tag_name("iframe")[0]
# driver.find_elements_by_tag_name("iframe")[1]

table = driver.find_element_by_css_selector('table[border="1"]')
# table = driver.find_elements_by_xpath('/html/body/table')

# table = driver.find_elements_by_tag_name('table')
print(table.text)
input()
table_rows = len(table.find_elements_by_tag_name('tr'))

print(table_rows)
input()
driver.quit()
