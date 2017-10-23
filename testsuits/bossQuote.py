#!/usr/bin/env python2
# coding=utf-8
__author__ = 'kayiyo'

import ConfigParser
import os.path
import time
from selenium import webdriver
from framework.logger import Logger
from selenium.webdriver.common.keys import Keys

mylogger = Logger(logger="BossQuoteLog").getlog()

config = ConfigParser.ConfigParser()
# file_path = os.path.dirname(os.getcwd()) + '/config/config.ini'
file_path = os.path.dirname(os.path.abspath('.')) + '/config/configuration.ini'
config.read(file_path)




driver = webdriver.Chrome()
# driver.set_window_size(800,600)
driver.maximize_window()
driver.implicitly_wait(6)


def load():
    url = config.get("bossQuote", "URL")
    driver.get(url)
    time.sleep(2)
	# driver.find_element_by_xpath("html/body/div[1]/div[1]/ul/li[1]/a").click()


def inputUsername():
    user = config.get("bossQuote", "USER")
    inputbox = driver.find_element_by_xpath(".//*[@id='app']/div/form/div[1]/div/div[1]/input")
    inputbox.clear()
    inputbox.send_keys(user)
    time.sleep(1)


def inputPassword():
    pw = config.get("bossQuote", "PW")
    inputbox = driver.find_element_by_xpath(".//*[@id='app']/div/form/div[2]/div/div/input")
    inputbox.clear()
    inputbox.send_keys(pw)
    time.sleep(1)


def inputCode():
    CODE = config.get("bossQuote", "CODE")
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


def manQuote():
    driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[1]/div/div/div/ul/li/div").click()
    time.sleep(1)
    driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[1]/div/div/div/ul/li/ul/a/li").click()
    time.sleep(2)


def quoteInquiry():
    #清空搜索记录
    driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[2]/div/div[1]/form/div[8]/div/button[2]").click()
    time.sleep(0.5)

    # 搜索未报价询单
    select = driver.find_element_by_xpath(
        ".//*[@id='app']/div[2]/div[2]/div/div[1]/form/div[1]/div/div/div[1]/input")
    select.click()
    for i in range(1, 5):
        select.send_keys(Keys.UP)
    select.send_keys(Keys.ENTER)
    time.sleep(0.5)
    driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[2]/div/div[1]/form/div[8]/div/button[1]").click()

    # 选择第一个未办理的询单
    driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[2]/div/div[2]/div[1]/div[5]/div[2]/table/tbody/tr[1]/td[10]/div/div[1]/button[1]").click()

    # 读取流程编码
    processcode = driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[2]/div/div/div[2]/div[2]/form/div[2]/div/div[1]/span[2]").text
    mylogger.info(processcode)

    # 开始填写报价信息
    driver.find_element_by_xpath(
        ".//*[@id='app']/div[2]/div[2]/div/div/div[2]/div[2]/div/div[3]/table/tbody/tr/td[12]/div/a/button").click()
    driver.switch_to_alert()
    driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[2]/div/div[2]/div[3]/table/tbody/tr[1]/td[5]/div/button").click()

    # 填写品牌
    inputbox = driver.find_element_by_xpath(
        ".//*[@id='app']/div[2]/div[2]/div/div/div[2]/div[2]/div/div[3]/table/tbody/tr/td[11]/div/div/input")
    # inputbox.clear()
    inputbox.send_keys(u"知名品牌")

    # 报价产品描述
    inputbox = driver.find_element_by_xpath(
        ".//*[@id='app']/div[2]/div[2]/div/div/div[2]/div[2]/div/div[3]/table/tbody/tr/td[13]/div/div/input")
    # inputbox.clear()
    inputbox.send_keys(u"知名产品详细描述信息")

    # 采购单价
    inputbox = driver.find_element_by_xpath(
        ".//*[@id='app']/div[2]/div[2]/div/div/div[2]/div[2]/div/div[3]/table/tbody/tr/td[14]/div/div/input")
    # inputbox.clear()
    inputbox.send_keys("5")

    # 净重
    inputbox = driver.find_element_by_xpath(
        ".//*[@id='app']/div[2]/div[2]/div/div/div[2]/div[2]/div/div[3]/table/tbody/tr/td[16]/div/div/input")
    # inputbox.clear()
    inputbox.send_keys("2")

    # 毛重
    inputbox = driver.find_element_by_xpath(
        ".//*[@id='app']/div[2]/div[2]/div/div/div[2]/div[2]/div/div[3]/table/tbody/tr/td[17]/div/div/input")
    # inputbox.clear()
    inputbox.send_keys("3")

    # 包装体积
    inputbox = driver.find_element_by_xpath(
        ".//*[@id='app']/div[2]/div[2]/div/div/div[2]/div[2]/div/div[3]/table/tbody/tr/td[18]/div/div/input")
    # inputbox.clear()
    inputbox.send_keys("3")

    # 包装方式
    inputbox = driver.find_element_by_xpath(
        ".//*[@id='app']/div[2]/div[2]/div/div/div[2]/div[2]/div/div[3]/table/tbody/tr/td[19]/div/div/input")
    # inputbox.clear()
    inputbox.send_keys(u"木箱")

    # 存放地
    inputbox = driver.find_element_by_xpath(
        ".//*[@id='app']/div[2]/div[2]/div/div/div[2]/div[2]/div/div[3]/table/tbody/tr/td[21]/div/div/input")
    # inputbox.clear()
    inputbox.send_keys(u"东营")

    # 交货期
    inputbox = driver.find_element_by_xpath(
        ".//*[@id='app']/div[2]/div[2]/div/div/div[2]/div[2]/div/div[3]/table/tbody/tr/td[22]/div/div/input")
    # inputbox.clear()
    inputbox.send_keys(u"35")

    # 报价有效期
    inputbox = driver.find_element_by_xpath(
        ".//*[@id='app']/div[2]/div[2]/div/div/div[2]/div[2]/div/div[3]/table/tbody/tr/td[23]/div/div/input")
    # inputbox.clear()
    inputbox.send_keys("2017-12-15 12:01:31")

    # 选择采购币种
    select = driver.find_element_by_xpath(
        ".//*[@id='app']/div[2]/div[2]/div/div/div[2]/div[2]/div/div[3]/table/tbody/tr/td[15]/div/div/div[1]/input")
    time.sleep(1)
    select.click()
    select.send_keys(Keys.UP)
    select.send_keys(Keys.ENTER)
    time.sleep(0.5)

    # 选择产品来源
    select = driver.find_element_by_xpath(
        ".//*[@id='app']/div[2]/div[2]/div/div/div[2]/div[2]/div/div[3]/table/tbody/tr/td[20]/div/div/div[1]/input")
    time.sleep(1)
    select.click()
    select.send_keys(Keys.UP)
    select.send_keys(Keys.ENTER)
    time.sleep(0.5)

    # 提交产品线负责人审核
    button = driver.find_element_by_xpath(
        ".//*[@id='app']/div[2]/div[2]/div/div/div[2]/div[2]/form/div[1]/div/button[3]")
    button.click()
    time.sleep(2)




testTime = int(config.get("bossQuote", "TESTTIME"))
url = config.get("bossQuote", "URL")
mylogger.info("The test server url is: %s" % url)
mylogger.info("TestTask : bossQuote")
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

    # 询单管理
    manQuote();

    # 新增询单
    quoteInquiry();

    # 退出
    logout();

    mylogger.info("Test Passed= %s" % i)
    # print time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), "Test Passed =", i

driver.quit()

mylogger.info("All Test Passed")
