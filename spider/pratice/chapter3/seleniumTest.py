# from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager
#
# driver = webdriver.Firefox()
# driver.get("https://www.dianping.com/search/category/7/10/p1")
#


from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

from selenium.webdriver.common.by import By

options = Options()
options.page_load_strategy = 'normal'
driver = webdriver.Chrome(options=options)
driver.get("https://test.longdaoyun.com/search/opportunity/")

# elements = driver.find_elements(by=By.CLASS_NAME, value='purchase-block')l
for i in range(0, 2):
    elements = driver.find_elements(by=By.CSS_SELECTOR, value='li.purchase-block')
    for j in range(0, len(elements)):
        print(elements.__getitem__(j).find_element(by=By.TAG_NAME, value='h4').text)
        print(elements.__getitem__(j).find_element(by=By.TAG_NAME, value='a').get_attribute('href'))
    driver.find_element(by=By.CSS_SELECTOR, value='a.layui-laypage-next').click()

driver.quit()
