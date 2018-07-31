
# coding=utf-8
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC

class Login():
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://118.31.19.120:3000/')
    def login(self,username,psw):
        element = WebDriverWait(self.driver,30,0.5).until


