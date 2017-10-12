#!/usr/bin/env python2
# coding=utf-8
__author__ = 'kayiyo'

import ConfigParser
import os.path
import time

from selenium import webdriver

from framework.logger import Logger

mylogger = Logger(logger="AssignProlineLog").getlog()

config = ConfigParser.ConfigParser()
# file_path = os.path.dirname(os.getcwd()) + '/config/config.ini'
file_path = os.path.dirname(os.path.abspath('.')) + '/config/configuration.ini'
config.read(file_path)


driver = webdriver.Chrome()
# driver.set_window_size(800,600)
driver.maximize_window()
driver.implicitly_wait(6)

def load():
    url = config.get("assignProline", "URL")
    driver.get(url)
    time.sleep(2)


def inputUsername():
    user = config.get("assignProline", "USER")
    inputbox = driver.find_element_by_xpath(".//*[@id='app']/div/form/div[1]/div/div[1]/input")
    inputbox.clear()
    inputbox.send_keys(user)
    time.sleep(1)


def inputPassword():
    pw = config.get("assignProline", "PW")
    inputbox = driver.find_element_by_xpath(".//*[@id='app']/div/form/div[2]/div/div/input")
    inputbox.clear()
    inputbox.send_keys(pw)
    time.sleep(1)


def inputCode():
    CODE = config.get("assignProline", "CODE")
    inputbox = driver.find_element_by_xpath(".//*[@id='verificationCode']")
    inputbox.clear()
    inputbox.send_keys(CODE)
    time.sleep(1)


def login():
    driver.find_element_by_xpath(".//*[@id='app']/div/form/div[4]/div/button").click()


def logout():
    driver.find_element_by_xpath(".//*[@id='app']/div[1]/div[2]/p/span").click()
    time.sleep(1)
    driver.switch_to_alert()
    driver.find_element_by_xpath("html/body/div[2]/div/div[3]/button[2]").click()
    time.sleep(2)

def manProject():
    driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[1]/div/div/div/ul/li/div").click()
    time.sleep(1)
    driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[1]/div/div/div/ul/li/ul/a/li").click()
    time.sleep(2)

def assignLine():

    #清空搜索记录
    driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[2]/div/div[1]/form/div[7]/div/button[2]").click()
    time.sleep(0.5)

    # 搜索询单状态：方案中心已确认
    select = driver.find_element_by_xpath(
        ".//*[@id='app']/div[2]/div[2]/div/div[1]/form/div[1]/div/div/div[1]/input")
    select.click()
    for i in range(1,13):
        select.send_keys(Keys.UP)
    select.send_keys(Keys.ENTER)
    time.sleep(0.5)
    driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[2]/div/div[1]/form/div[7]/div/button[1]").click()

    # 选择第一个未办理的询单点击办理
    driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[2]/div/div[2]/div[1]/div[4]/div[2]/table/tbody/tr[1]/td[10]/div/button").click()

    # 读取流程编码
    processcode = driver.find_element_by_xpath(
        ".//*[@id='app']/div[2]/div[2]/div/div[1]/div[2]/div[2]/div[2]/div[1]/div/span[2]").text
    mylogger.info(processcode)

    # 选择SKU
    driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[2]/div/div[1]/div[2]/div[2]/div[4]/div[3]/table/tbody/tr/td[1]/div/label/span/span").click()

    # 点击划分产品线
    # 弹出划分产品线窗口
    driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[2]/div/div[1]/div[2]/div[2]/button").click()
    driver.switch_to_alert()
    select = driver.find_element_by_xpath(
        ".//*[@id='app']/div[2]/div[2]/div/div[1]/div[2]/div[2]/div[3]/div/div[2]/div/div/div/div/form/div/div/div/div[1]/input")
    time.sleep(1)
    select.click()
    for i in range(1,6):
        select.send_keys(Keys.UP)
    select.send_keys(Keys.ENTER)
    time.sleep(0.5)

    driver.find_element_by_xpath(
        ".//*[@id='app']/div[2]/div[2]/div/div[1]/div[2]/div[2]/div[3]/div/div[3]/span/button[2]").click()
    time.sleep(1)

    # 点击按钮提交产品线报价
    driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[2]/div/div[1]/div[2]/div[2]/div[1]/button[3]").click()
    time.sleep(2)



testTime = int(config.get("assignProline", "TESTTIME"))
url = config.get("assignProline", "URL")
mylogger.info("The test server url is: %s" % url)
mylogger.info("TestTask : assignProline")

testTimes = testTime + 1
mylogger.info("Test Time is : %s" % testTime)

for i in range(1, testTimes):
    # 进入登录界面
    load();

    # 输入用户名
    inputUsername();

    # 输入密码
    inputPassword();

    # 输入验证码
    # inputCode();

    # 登录
    login();

    # 项目经理菜单
    manProject();

    # 划分产品线
    assignLine();

    # 退出
    logout();

    mylogger.info("Test Passed= %s" % i)
    # print time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), "Test Passed =", i

driver.quit()

mylogger.info("All Test Passed")