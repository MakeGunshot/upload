# coding=utf-8

from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get('http://10.7.111.196:9999/mposmsNew/index.html#/login')
time.sleep(3)

driver.add_cookie({'name':'BAIDUID','value':'JSESSIONID'})

driver.add_cookie({'name':'BDUSS','value':'E85135D7745C68262438D4FF070ED687'})
time.sleep(3)

driver.refresh()
time.sleep(3)
