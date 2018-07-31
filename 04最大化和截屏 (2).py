# coding = utf-8
# 引入webdriver的类
from selenium import webdriver
# 线程暂停
import time

# 引入PATH变量
from os import path

d = path.dirname(__file__)
xinwen = path.join(d,"xinwen.png")
index = path.join(d,"index.png")

# 创建浏览器
driver = webdriver.Chrome()
# 打开一个页面
driver.get('https://www.baidu.com')
time.sleep(2)
driver.find_element_by_link_text("新闻").click()
time.sleep(2)
# 截屏
driver.save_screenshot(xinwen)
driver.back()

time.sleep(2)
driver.save_screenshot(index)

time.sleep(2)
# 退出浏览器
driver.quit()