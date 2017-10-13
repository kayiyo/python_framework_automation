#!/usr/bin/env python3
#  coding=utf-8
# 订单管理/新增订单
__author__ = 'kayiyo'

import ConfigParser
import os.path
import time
import random

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from framework.logger import Logger

mylogger = Logger(logger="orderNewLog").getlog()
config = ConfigParser.ConfigParser()
# file_path = os.path.dirname(os.getcwd()) + '/config/config.ini'
file_path = os.path.dirname(os.path.abspath('.')) + '/config/configuration.ini'
config.read(file_path)

driver = webdriver.Chrome()
# driver.set_window_size(800,600)
driver.maximize_window()
driver.implicitly_wait(6)


def load():
    url = config.get("bossOrder", "url")
    driver.get(url)
    time.sleep(2)


def inputusername():
    user = config.get("bossOrder", "user")
    inputbox = driver.find_element_by_xpath(".//*[@id='app']/div/form/div[1]/div/div[1]/input")
    inputbox.clear()
    inputbox.send_keys(user)
    time.sleep(1)


def inputpassword():
    pw = config.get("bossOrder", "pw")
    inputbox = driver.find_element_by_xpath(".//*[@id='app']/div/form/div[2]/div/div/input")
    inputbox.clear()
    inputbox.send_keys(pw)
    time.sleep(1)


def inputcode():
    code = config.get("bossOrder", "code")
    inputbox = driver.find_element_by_xpath(".//*[@id='verificationCode']")
    inputbox.clear()
    inputbox.send_keys(code)
    time.sleep(1)


def login():
    driver.find_element_by_xpath(".//*[@id='app']/div/form/div[4]/div/button").click()


def logout():
    driver.find_element_by_xpath(".//*[@id='app']/div[1]/div[2]/p/span").click()
    time.sleep(1)
    driver.switch_to_alert()
    driver.find_element_by_xpath("html/body/div[2]/div/div[3]/button[2]").click()
    time.sleep(2)


def manorder():
    driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[1]/div/div/div/ul/li/div").click()
    time.sleep(1)
    driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[1]/div/div/div/ul/li/ul/a[1]/li").click()
    time.sleep(2)


def neworder():
    # 显示新增订单当天时间
    ordertime = time.strftime("%Y-%m-%d", time.localtime())
    ordertime1 = time.strftime("%Y%m%d%H%M%S", time.localtime())

    # 点击新建订单按钮
    driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[2]/div/button").click()
    time.sleep(2)

    # PO号
    global orderpono
    orderpono = "PO" + ordertime1 + "ddgl"
    inputbox = driver.find_element_by_xpath(
        ".//*[@id='app']/div[2]/div[2]/div/div[2]/div[1]/form/div[2]/div[2]/span[2]/div/div/div[1]/input")
    inputbox.clear()
    inputbox.send_keys(orderpono)

    # 订单签约日期
    inputbox = driver.find_element_by_xpath(
        ".//*[@id='app']/div[2]/div[2]/div/div[2]/div[1]/form/div[3]/div[2]/span[2]/div/input")
    inputbox.clear()
    inputbox.send_keys(ordertime)

    # 执行单号
    inputbox = driver.find_element_by_xpath(
        ".//*[@id='app']/div[2]/div[2]/div/div[2]/div[1]/form/div[3]/div[1]/span[2]/div/div/div/input")
    inputbox.clear()
    inputbox.send_keys("EX" + ordertime1 + "ddgl")

    # 选择客户
    # 点击选择按钮
    driver.find_element_by_xpath(
        ".//*[@id='app']/div[2]/div[2]/div/div[2]/div[1]/form/div[4]/div[1]/span[3]").click()
    driver.switch_to_alert()

    # 清空搜索框
    driver.find_element_by_xpath(
        ".//*[@id='app']/div[2]/div[2]/div/div[2]/div[1]/div[5]/div/div[2]/form/div/div[2]/div/button[2]").click()

    # 输入客户名称
    driver.find_element_by_xpath(
        ".//*[@id='app']/div[2]/div[2]/div/div[2]/div[1]/div[5]/div/div[2]/form/div/div[1]/div/div/input").send_keys(
        "Bruce.Lee")
    driver.find_element_by_xpath(
        ".//*[@id='app']/div[2]/div[2]/div/div[2]/div[1]/div[5]/div/div[2]/form/div/div[2]/div/button[1]").click()
    # 选择客户
    driver.find_element_by_xpath(
        ".//*[@id='app']/div[2]/div[2]/div/div[2]/div[1]/div[5]/div/div[2]/div[1]/div[4]/div[2]/table/tbody/tr/td[5]/div/button").click()
    time.sleep(1)

    # 选择市场经办人
    # 点击选择按钮
    driver.find_element_by_xpath(
        ".//*[@id='app']/div[2]/div[2]/div/div[2]/div[1]/form/div[4]/div[2]/span[3]").click()
    driver.switch_to_alert()

    # 选择市场经办人
    driver.find_element_by_xpath(
        ".//*[@id='app']/div[2]/div[2]/div/div[2]/div[1]/div[6]/div/div[2]/div/div[3]/table/tbody/tr/td[4]/div/button").click()
    time.sleep(1)

    # # 输入市场经办人邮箱(市场经办人邮箱自动带出）
    # inputbox = driver.find_element_by_xpath(
    #     ".//*[@id='app']/div[2]/div[2]/div/div[2]/div[1]/form/div[8]/div[2]/span[2]/div/div/div/input")
    # inputbox.clear()
    # inputbox.send_keys("xujie@group.com")

    # 输入订单金额
    orderaccount = random.randint(1, 10) * 1000000
    inputbox = driver.find_element_by_xpath(
        ".//*[@id='app']/div[2]/div[2]/div/div[2]/div[1]/form/div[9]/div[1]/span[2]/div/div/div[1]/input")
    inputbox.clear()
    inputbox.send_keys(orderaccount)

    # 选择货币
    select = driver.find_element_by_xpath(
        ".//*[@id='app']/div[2]/div[2]/div/div[2]/div[1]/form/div[9]/div[1]/span[2]/div/div/div[2]/div[1]/input")
    select.click()
    for iii in range(1, random.randint(2, 10)):
        select.send_keys(Keys.UP)
    select.send_keys(Keys.ENTER)
    time.sleep(0.5)

    # 选择贸易条款
    select = driver.find_element_by_xpath(
        ".//*[@id='app']/div[2]/div[2]/div/div[2]/div[1]/form/div[10]/div[1]/span[2]/div/div/div/div[1]/input")
    select.click()
    for iii in range(1, random.randint(2, 20)):
        select.send_keys(Keys.UP)
    select.send_keys(Keys.ENTER)
    time.sleep(0.5)

    # 选择运输方式
    select = driver.find_element_by_xpath(
        ".//*[@id='app']/div[2]/div[2]/div/div[2]/div[1]/form/div[10]/div[2]/span[2]/div/div/div/div[1]/input")
    select.click()
    for iii in range(1, random.randint(2, 10)):
        select.send_keys(Keys.UP)
    select.send_keys(Keys.ENTER)
    time.sleep(0.5)

    # 选择起运地
    select = driver.find_element_by_xpath(
        ".//*[@id='app']/div[2]/div[2]/div/div[2]/div[1]/form/div[11]/div[1]/span[2]/div/div/div[1]/div[1]/input")
    select.click()
    for iii in range(1, random.randint(2, 200)):
        select.send_keys(Keys.UP)
    select.send_keys(Keys.ENTER)
    time.sleep(3)

    # 选择目的地
    select = driver.find_element_by_xpath(
        ".//*[@id='app']/div[2]/div[2]/div/div[2]/div[1]/form/div[11]/div[2]/span[2]/div/div/div[1]/div[1]/input")
    select.click()
    for iii in range(1, random.randint(2, 200)):
        select.send_keys(Keys.UP)
    select.send_keys(Keys.ENTER)
    time.sleep(3)

    # 输入详细地址
    inputbox = driver.find_element_by_xpath(
        ".//*[@id='app']/div[2]/div[2]/div/div[2]/div[1]/form/div[12]/div/span[2]/div/div/div/input")
    inputbox.clear()
    inputbox.send_keys(u"中国山东省东营市东营")

    # 保存订单
    driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[2]/div/div[2]/div[1]/div[1]/button").click()
    time.sleep(3)

    # # 读取平台订单号
    # ordercode = driver.find_element_by_xpath(
    #     ".//*[@id='app']/div[2]/div[2]/div/div[1]/div[3]/table/tbody/tr[1]/td[1]/div").text
    # mylogger.info(u"平台订单号：" + ordercode)

def orderinfo():

        # 重置搜索条件
        driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[2]/div/form/div/div[8]/div/div/div/button[2]").click()
        # 输入平台订单号
        driver.find_element_by_xpath(
            ".//*[@id='app']/div[2]/div[2]/div/form/div/div[4]/div/div/div/div/input").send_keys(
            orderpono)
        # 点击搜索按钮
        driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[2]/div/form/div/div[8]/div/div/div/button[1]").click()

        try:
            driver.find_element_by_xpath(
                ".//*[@id='app']/div[2]/div[2]/div/div[1]/div[4]/div[2]/table/tbody/tr/td[9]/div/button[1]")
        except Exception as e:
            # mylogger.info(e)
            mylogger.info(u"PO：" + orderpono + u"不存在！")
        else:
            # 查看该订单
            driver.find_element_by_xpath(
                ".//*[@id='app']/div[2]/div[2]/div/div[1]/div[4]/div[2]/table/tbody/tr/td[9]/div/button[1]").click()

            # 读取PO号
            readpo = driver.find_element_by_xpath(
                ".//*[@id='app']/div[2]/div[2]/div/div[2]/div[1]/form/div[2]/div[2]/span[2]/input").text

            # 读取平台订单号
            readorderno = driver.find_element_by_xpath(
                ".//*[@id='app']/div[2]/div[2]/div/div[2]/div[1]/form/div[2]/div[1]/span[2]").text

            # 读取客户编号
            readcusno = driver.find_element_by_xpath(
                ".//*[@id='app']/div[2]/div[2]/div/div[2]/div[1]/form/div[4]/div[1]/span[2]").text

            # 读取市场经办人
            readmarket = driver.find_element_by_xpath(
                ".//*[@id='app']/div[2]/div[2]/div/div[2]/div[1]/form/div[4]/div[2]/span[2]").text

            # 读取订单金额
            readorderaccount = driver.find_element_by_xpath(
                ".//*[@id='app']/div[2]/div[2]/div/div[2]/div[1]/form/div[9]/div[1]/span[2]").text

            # 读取贸易条款
            readclause = driver.find_element_by_xpath(
                ".//*[@id='app']/div[2]/div[2]/div/div[2]/div[1]/form/div[10]/div[1]/span[2]").text

            # 读取运输方式
            readway = driver.find_element_by_xpath(
                ".//*[@id='app']/div[2]/div[2]/div/div[2]/div[1]/form/div[10]/div[2]/span[2]").text

            # 读取起运地
            readstart = driver.find_element_by_xpath(
                ".//*[@id='app']/div[2]/div[2]/div/div[2]/div[1]/form/div[11]/div[1]/span[2]").text

            # 读取目的地
            readend = driver.find_element_by_xpath(
                ".//*[@id='app']/div[2]/div[2]/div/div[2]/div[1]/form/div[11]/div[2]/span[2]").text

            readall = u"|PO." + readpo + u"|客户编号:" + readcusno + u"{" + readmarket + u"}" +u"|订单金额:" + readorderaccount + u"|clause:" + readclause + u"|起运方式:" + readway + u"[" + readstart + u"-->" + readend + u"]"

            mylogger.info(u"平台订单号：" + readorderno)
            mylogger.info(readall)


testTime = int(config.get("bossOrder", "testtime"))
url = config.get("bossOrder", "url")
mylogger.info("The test server url is: %s" % url)
mylogger.info("TestTask : orderNew")

testTimes = testTime + 1
mylogger.info("Test Time is : %s" % testTime)

for iii in range(1, testTimes):
    # 进入登录界面
    load();

    # 输入用户名
    inputusername();

    # 输入密码
    inputpassword();

    # 输入验证码
    # inputcode();

    # 登录
    login();

    # 订单管理
    manorder();

    # 新建订单
    neworder();

    # 读取订单
    orderinfo();

    # 退出
    logout();

    mylogger.info("Test Passed= %s" % iii)
    # print time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), "Test Passed =", i

driver.quit()

mylogger.info("All Test Passed")
