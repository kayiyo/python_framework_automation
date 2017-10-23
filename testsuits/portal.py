# coding=utf-8

import ConfigParser
import os.path
import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from framework.logger import Logger


config = ConfigParser.ConfigParser()
# file_path = os.path.dirname(os.getcwd()) + '/config/config.ini'
file_path = os.path.dirname(os.path.abspath('.')) + '/config/configuration.ini'
config.read(file_path)

url = config.get("portal", "url")
user = config.get("portal", "user")
pw = config.get("portal", "pw")
code = config.get("portal", "code")

def load(self):
    self.driver.find_element_by_xpath("html/body/div[1]/div[1]/ul/li[1]/a").click()
    time.sleep(2)


def inputUsername(self):
    self.driver.find_element_by_xpath(".//*[@id='exampleInputEmail']").clear()
    self.driver.find_element_by_xpath(".//*[@id='exampleInputEmail']").send_keys(user)
    time.sleep(2)


def inputPassword(self):
    self.driver.find_element_by_xpath(".//*[@id='exampleInputPassword']").clear()
    self.driver.find_element_by_xpath(".//*[@id='exampleInputPassword']").send_keys(pw)
    time.sleep(2)


def inputCode(self):
    self.driver.find_element_by_xpath(".//*[@id='verificationCode']").clear()
    self.driver.find_element_by_xpath(".//*[@id='verificationCode']").send_keys(code)
    time.sleep(2)


def login(self):
    self.driver.find_element_by_xpath(".//*[@id='loginSubmit']").click()


def logout(self):
    self.driver.find_element_by_xpath("html/body/div[1]/div[1]/ul/li[2]/a").click()
    time.sleep(2)


def test_baidu_search(self):
    for i in range(1, 101):
        # 进入登录界面
        self.load();

        # 输入用户名
        self.inputUsername();

        # 输入密码
        self.inputPassword();

        # 输入验证码
        self.inputCode();

        # 登录
        self.login();

        # 退出
        self.logout();

    try:
        assert 'selenium' in self.driver.title
        print ('Test Pass.')
    except Exception as e:
        print ('Test Fail.', format(e))