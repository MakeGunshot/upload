from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.implicitly_wait(2)

driver.get('https://www.baidu.com')
driver.find_element_by_id('kw').send_keys('hello world')
driver.find_element_by_id('kw').submit()

driver.find_element_by_xpath('//*[@id="3"]/h3').click()

wds = driver.window_handles

print('all windows:',len(wds))
index = len(wds)
driver.switch_to_window(wds[1])

h1 = driver.find_element_by_xpath('//*[@id="wgt-ask"]/h1/span')

print('h1:',h1.text)
driver.close()

