#!/usr/bin/env python2
# coding=utf-8
__author__ = 'kayiyo'

import ConfigParser
import os.path
import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from framework.logger import Logger

mylogger = Logger(logger="CheckInquiryLog").getlog()

config = ConfigParser.ConfigParser()
# file_path = os.path.dirname(os.getcwd()) + '/config/config.ini'
file_path = os.path.dirname(os.path.abspath('.')) + '/config/configuration.ini'
config.read(file_path)


driver = webdriver.Chrome()
# driver.set_window_size(800,600)
driver.maximize_window()
driver.implicitly_wait(6)

def load():
    url = config.get("checkInquiry", "URL")
    driver.get(url)
    time.sleep(2)
	# driver.find_element_by_xpath("html/body/div[1]/div[1]/ul/li[1]/a").click()


def inputUsername():
    user = config.get("checkInquiry", "USER")
    inputbox = driver.find_element_by_xpath(".//*[@id='app']/div/form/div[1]/div/div[1]/input")
    inputbox.clear()
    inputbox.send_keys(user)
    time.sleep(1)


def inputPassword():
    pw = config.get("checkInquiry", "PW")
    inputbox = driver.find_element_by_xpath(".//*[@id='app']/div/form/div[2]/div/div/input")
    inputbox.clear()
    inputbox.send_keys(pw)
    time.sleep(1)


def inputCode():
    CODE = config.get("checkInquiry", "CODE")
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

def manInquiry():
    driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[1]/div/div/div/ul/li/div").click()
    time.sleep(1)
    driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[1]/div/div/div/ul/li/ul/a/li").click()
    time.sleep(2)

def checkInquiry():

    # 清空搜索记录
    driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[2]/div/div[1]/form/div[8]/div/button[2]").click()
    time.sleep(0.5)

    # 搜索询单状态：方案中心审核中
    select = driver.find_element_by_xpath(
        ".//*[@id='app']/div[2]/div[2]/div/div[1]/form/div[1]/div/div/div[1]/input")
    select.click()
    for i in range(1, 14):
        select.send_keys(Keys.UP)
    select.send_keys(Keys.ENTER)
    time.sleep(0.5)
    driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[2]/div/div[1]/form/div[8]/div/button[1]").click()

    # 选择第一个未办理的询单点击办理
    driver.find_element_by_xpath(
        ".//*[@id='app']/div[2]/div[2]/div/div[2]/div[2]/div[4]/div[2]/table/tbody/tr[1]/td[10]/div/button").click()

    # 读取流程编码
    processcode = driver.find_element_by_xpath(
        ".//*[@id='app']/div[2]/div[2]/div/div[1]/div[2]/div[1]/form/div[1]/div[2]/div[1]/div[1]").text
    mylogger.info(processcode)

    # 点击按钮提交项目经理审核
    driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[2]/div/div[1]/div[2]/div[1]/form/div[1]/div[1]/button[3]").click()
    time.sleep(2)

    # 弹窗选择项目经理
    driver.switch_to_alert()
    driver.find_element_by_xpath(
        ".//*[@id='app']/div[2]/div[2]/div/div[5]/div/div[2]/form/div[3]/div/button[2]").click()
    driver.find_element_by_xpath(
        ".//*[@id='app']/div[2]/div[2]/div/div[5]/div/div[2]/form/div[2]/div/div/input").send_keys("xmjl")
    driver.find_element_by_xpath(
        ".//*[@id='app']/div[2]/div[2]/div/div[5]/div/div[2]/form/div[3]/div/button[1]").click()
    driver.find_element_by_xpath(
        ".//*[@id='app']/div[2]/div[2]/div/div[5]/div/div[2]/div[1]/div[3]/table/tbody/tr/td[4]/div/button").click()
    time.sleep(1)



testTime = int(config.get("checkInquiry", "TESTTIME"))
url = config.get("checkInquiry", "URL")
mylogger.info("The test server url is: %s" % url)
mylogger.info("TestTask : checkInquiry")

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

    # 询单管理菜单
    manInquiry();

    # 方案中心分配项目经理
    checkInquiry();

    # 退出
    logout();

    mylogger.info("Test Passed= %s" % i)
    # print time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), "Test Passed =", i

driver.quit()

mylogger.info("All Test Passed")