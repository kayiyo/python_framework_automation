#!/usr/bin/env python2
#  coding=utf-8
# BOSS基类  __author__ = 'kayiyo'

import random
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class BossBase(object):

    driver = webdriver.Chrome()

    # 打开浏览器
    def load_web(self, url):
        self.driver.get(url)
        self.driver.maximize_window()
        time.sleep(2)

    # 退出浏览器
    def quit_web(self):
        self.driver.quit()

    # 输入用户名
    def input_username(self, user, xpath=".//*[@id='app']/div/div/form/div[1]/div/div/input"):
        input_box = self.driver.find_element_by_xpath(xpath)
        input_box.clear()
        input_box.send_keys(user)
        time.sleep(1)

    # 输入密码
    def input_password(self, pw, xpath=".//*[@id='app']/div/div/form/div[2]/div/div/input"):
        input_box = self.driver.find_element_by_xpath(xpath)
        input_box.clear()
        input_box.send_keys(pw)
        time.sleep(1)

    # 输入验证码
    def input_code(self, code, xpath=".//*[@id='verificationCode']"):
        input_box = self.driver.find_element_by_xpath(xpath)
        input_box.clear()
        input_box.send_keys(code)
        time.sleep(1)

    # 输入框输入字符
    def send_key(self, key1, xpath):
        self.driver.find_element_by_xpath(xpath).send_keys(key1)
        time.sleep(1)

    # 点击按钮
    def click_button(self, xpath):
        self.driver.find_element_by_xpath(xpath).click()
        time.sleep(1)

    # 下拉框数据选择
    def select_list(self, key1, xpath):
        select = self.driver.find_element_by_xpath(xpath)
        select.click()
        for key1 in range(1, random.randint(2, key1)):
            select.send_keys(Keys.UP)
        select.send_keys(Keys.ENTER)
        time.sleep(1)

    # 登录系统Login
    def login(self, loginbutton=".//*[@id='app']/div/div/form/div[4]/div/button"):
        time.sleep(2)
        self.driver.find_element_by_xpath(loginbutton).click()
        time.sleep(2)

    # 登出系统Logout
    def logout(self, logoutbutton=".//*[@id='app']/div[1]/div[2]/p/span",
               surebutton="html/body/div[2]/div/div[3]/button[2]"):
        self.driver.find_element_by_xpath(logoutbutton).click()
        time.sleep(1)
        self.driver.switch_to_alert()
        self.driver.find_element_by_xpath(surebutton).click()
        time.sleep(2)

    def search_button(self):
        self.driver.find_element_by_xpath(".//*[@id='su']").click()

    def click_img(self):
        self.driver.find_element_by_xpath(".//*[@id='1']/h3/a").click()