#!/usr/bin/env python2
#  coding=utf-8
# BOSS基类
__author__ = 'kayiyo'

import ConfigParser
import os.path
import time
import random

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from framework.logger import Logger

class BossBase(object):

    driver = webdriver.Chrome()

    # 打开浏览器
    def loadweb(self, url):
        self.driver.get(url)
        time.sleep(2)

    # 退出浏览器
    def quitweb(self):
        self.driver.quit()

    # 输入用户名
    def inputusername(self, user, xpath=".//*[@id='app']/div/div/form/div[1]/div/div/input"):
        inputbox = self.driver.find_element_by_xpath(xpath)
        inputbox.clear()
        inputbox.send_keys(user)
        time.sleep(1)

    # 输入密码
    def inputpassword(self, pw, xpath=".//*[@id='app']/div/div/form/div[2]/div/div/input"):
        inputbox = self.driver.find_element_by_xpath(xpath)
        inputbox.clear()
        inputbox.send_keys(pw)
        time.sleep(1)

    # 输入验证码
    def inputcode(self, code, xpath=".//*[@id='verificationCode']"):
        inputbox = self.driver.find_element_by_xpath(xpath)
        inputbox.clear()
        inputbox.send_keys(code)
        time.sleep(1)

    # 输入框输入字符
    def sendkey(self,key1,xpath):
        self.driver.find_element_by_xpath(xpath).send_keys(key1)
        time.sleep(2)

    # 登录系统Login
    def login(self, loginbutton=".//*[@id='app']/div/div/form/div[4]/div/button"):
        self.driver.find_element_by_xpath(loginbutton).click()

    # 登出系统Logout
    def logout(self, logoutbutton=".//*[@id='app']/div[1]/div[2]/p/span", surebutton="html/body/div[2]/div/div[3]/button[2]"):
        self.driver.find_element_by_xpath(logoutbutton).click()
        time.sleep(1)
        self.driver.switch_to_alert()
        self.driver.find_element_by_xpath(surebutton).click()
        time.sleep(2)

    def searchbutton(self):
        self.driver.find_element_by_xpath(".//*[@id='su']").click()

    def clickimg(self):
        self.driver.find_element_by_xpath(".//*[@id='1']/h3/a").click()

