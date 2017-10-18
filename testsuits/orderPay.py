#!/usr/bin/env python3
#  coding=utf-8
# 订单管理/收款信息/增加一条收款信息
__author__ = 'kayiyo'

import ConfigParser
import os.path
import time
import random

from selenium import webdriver

from framework.logger import Logger

mylogger = Logger(logger="orderPayLog").getlog()
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


def delivery():
    # 点击订单管理
    driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[1]/div/div/div/ul/li/div").click()
    time.sleep(0.5)
    # 点击收款信息
    driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[1]/div/div/div/ul/li[1]/ul/a[6]/li").click()
    time.sleep(0.5)

    ordersn = int(config.get("bossOrder", "ordersn"))
    runforever = True

    while runforever:
        ordertime = time.strftime("%Y-%m-%d", time.localtime())
        ordertime1 = time.strftime("%Y%m%d%H%M%S", time.localtime())
        ordertime2 = time.strftime("%Y%m%d", time.localtime())
        serachcode = ordertime2 + "%04d\n" % ordersn
        ordersn = ordersn + 1

        # 重置搜索条件
        driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[2]/div/form/div/div[8]/div/div/div/button[2]").click()
        # 输入平台订单号
        driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[2]/div/form/div/div[1]/div/div/div/div/input").send_keys(
            serachcode)
        # 点击搜索按钮
        driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[2]/div/form/div/div[8]/div/div/div/button[1]").click()

        try:
            driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[2]/div/div[1]/div[4]/div[2]/table/tbody/tr/td[9]/div/a[2]/button")
        except Exception as e:
            # mylogger.info(e)
            mylogger.info(u"平台订单号：" + serachcode + u"不存在！")
            runforever = False
        else:
            # 点击收款按钮
            driver.find_element_by_xpath(
                ".//*[@id='app']/div[2]/div[2]/div/div[1]/div[4]/div[2]/table/tbody/tr/td[9]/div/a[2]/button").click()
            time.sleep(1)

            # 读取订单号
            readordercode = driver.find_element_by_xpath(
                ".//*[@id='app']/div[2]/div[2]/div/table/tr[1]/td[1]/span").text

            # 添加一条收款记录按钮
            driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[2]/div/div/button[1]").click()
            driver.switch_to_alert()

            # 描述
            inputbox = driver.find_element_by_xpath(
                ".//*[@id='app']/div[2]/div[2]/div/div/div[1]/div/div[2]/div/form/div[1]/div/div/input")
            inputbox.clear()
            inputbox.send_keys(u"收到订单号：" + readordercode + u"款项ddgl")

            # 金额
            shoukuan = random.randint(1, 10)*10000
            inputbox = driver.find_element_by_xpath(
                ".//*[@id='app']/div[2]/div[2]/div/div/div[1]/div/div[2]/div/form/div[2]/div/div/input")
            inputbox.clear()
            inputbox.send_keys(shoukuan)

            # 收款时间
            inputbox = driver.find_element_by_xpath(
                ".//*[@id='app']/div[2]/div[2]/div/div/div[1]/div/div[2]/div/form/div[3]/div/div/div/div/div/input")
            inputbox.clear()
            inputbox.send_keys(ordertime)

            # 保存收款记录
            driver.find_element_by_xpath(
                ".//*[@id='app']/div[2]/div[2]/div/div/div[1]/div/div[3]/span/button[2]").click()

            mylogger.info(u"平台订单号：" + readordercode + u"收款成功|收款金额： %s" % shoukuan)
            time.sleep(2)

            # 返回交收信息列表
            driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[1]/div/div/div/ul/li[1]/ul/a[6]/li").click()



# testTime = int(config.get("bossOrder", "testtime"))
url = config.get("bossOrder", "url")
mylogger.info("The test server url is: %s" % url)
mylogger.info("TestTask : deliverOrder")

# testTimes = testTime + 1
# mylogger.info("Test Time is : %s" % testTime)

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

# 出库信息
delivery();

# 退出
logout();

driver.quit()

mylogger.info("All Test Passed")