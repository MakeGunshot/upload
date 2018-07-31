# coding = utf-8
# 引入webdriver的类
from selenium import webdriver
# 线程暂停
import time
# 创建浏览器
driver = webdriver.Chrome()
# 打开一个页面
driver.get('https://www.baidu.com')

# driver.find_element_by_css_selector('#kw').send_keys('hello world')
driver.find_element_by_xpath('//*[@id="kw"]').send_keys('hello world')



time.sleep(3)
# 退出浏览器
driver.quit()