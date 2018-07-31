
import logging
from selenium import webdriver
# 把日志放到文件里
logging_file='example.log'

logging.basicConfig(filename=logging_file,level=logging.DEBUG)

logging.debug('begin selenium')

driver = webdriver.Chrome()
logging.debug('create chrome')
print(driver.capabilities['version'])
logging.debug('print chrome version')

