#!/usr/bin/env python3
#  coding=utf-8
# 客户管理/客户管理
__author__ = 'kayiyo'

import ConfigParser
import os.path
import time
import random

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from framework.logger import Logger

mylogger = Logger(logger="crmNewLog").getlog()
config = ConfigParser.ConfigParser()
# file_path = os.path.dirname(os.getcwd()) + '/config/config.ini'
file_path = os.path.dirname(os.path.abspath('.')) + '/config/configuration.ini'
config.read(file_path)

driver = webdriver.Chrome()
# driver.set_window_size(800,600)
driver.maximize_window()
driver.implicitly_wait(6)

class crmNew(object):
    def load(self, url):
        driver.get(url)
        time.sleep(2)

    def inputusername(self, user):
        inputbox = driver.find_element_by_xpath(".//*[@id='test']/div/form/div[1]/div/div/input")
        inputbox.clear()
        inputbox.send_keys(user)
        time.sleep(1)

    def inputpassword(self, pw):
        inputbox = driver.find_element_by_xpath(".//*[@id='test']/div/form/div[2]/div/div/input")
        inputbox.clear()
        inputbox.send_keys(pw)
        time.sleep(1)

    def inputcode(self, code):
        inputbox = driver.find_element_by_xpath(".//*[@id='verificationCode']")
        inputbox.clear()
        inputbox.send_keys(code)
        time.sleep(1)

    def login(self):
        driver.find_element_by_xpath(".//*[@id='test']/div/form/div[4]/div/button").click()

    def logout(self):
        driver.find_element_by_xpath(".//*[@id='app']/div[1]/div[2]/p/span").click()
        time.sleep(1)
        driver.switch_to_alert()
        driver.find_element_by_xpath("html/body/div[2]/div/div[3]/button[2]").click()
        time.sleep(2)

    def mancrm(self):
        driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[1]/div/div/div/ul/li[4]/div").click()
        time.sleep(0.5)
        driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[1]/div/div/div/ul/li[4]/ul/a[1]/li").click()
        time.sleep(3)

    def newcrm(self):
        # 显示新增客户当天时间
        crmtime = time.strftime("%Y-%m-%d", time.localtime())
        crmtime1 = time.strftime("%Y%m%d%H%M%S", time.localtime())
        crmtime2 = time.strftime("%H%M%S", time.localtime())
        crmtime3 = time.strftime("%d%H%M%S", time.localtime())

        # 点击新增客户按钮
        driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[2]/div/div[2]/button").click()
        time.sleep(2)

        # 客户基本信息
        crmemail = "crm" + crmtime2 + "@crm.com"
        crmpw = "Crm@123456"
        crmname = "CRM" + crmtime2

        # 邮箱
        inputbox = driver.find_element_by_xpath(
            ".//*[@id='app']/div[2]/div[2]/div/form/div[2]/div/div/div/input")
        inputbox.clear()
        inputbox.send_keys(crmemail)

        # 密码
        inputbox = driver.find_element_by_xpath(
            ".//*[@id='app']/div[2]/div[2]/div/form/div[3]/div/div/div/input")
        inputbox.clear()
        inputbox.send_keys(crmpw)

        # 选择国家
        select = driver.find_element_by_xpath(
            ".//*[@id='app']/div[2]/div[2]/div/form/div[4]/div/div/div[1]/input")
        select.click()
        for iii in range(1, random.randint(2, 300)):
            select.send_keys(Keys.UP)
        select.send_keys(Keys.ENTER)
        time.sleep(0.5)

        # 电话
        inputbox = driver.find_element_by_xpath(
            ".//*[@id='app']/div[2]/div[2]/div/form/div[5]/div/div/div/div[2]/div/div/div/input")
        inputbox.clear()
        inputbox.send_keys(crmtime3)

        # 姓名
        inputbox = driver.find_element_by_xpath(
            ".//*[@id='app']/div[2]/div[2]/div/form/div[6]/div/div/div/input")
        inputbox.clear()
        inputbox.send_keys(crmname)

        # 企业信息
        crmcompany = crmname + " Co.,Ltd."
        crmscope = u"国际上主要的石油、天然气和石油化工的生产商，同时也是全球最大的汽车燃油和润滑油零售商。它亦为液化天然气行业的先驱，并在融资、管理和经营方面拥有丰富的经验。业务遍及全球90多个国家和地区，雇员约93000人，油、气产量分别占世界总产量的3%和3.5%。"
        crmpro = u"包括润滑油生产、加油站业务、沥青、天然气制油燃料、与中海油合作的南海石化项目以及其他石化产品包括乙烯、乙二醇、苯乙烯、高碳烯烃及衍生物、多元醇、溶剂和丙二醇/聚对苯二甲酸丙二酯等"
        crmamount = random.randint(1, 10) * 1000000
        global crmcode
        crmcode = "CRMCODE" + crmtime2

        # 公司名称
        inputbox = driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[2]/div/form/div[8]/div/div/div/input")
        inputbox.clear()
        inputbox.send_keys(crmcompany)

        # 经营范围
        inputbox = driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[2]/div/form/div[9]/div/div[1]/div/input")
        inputbox.clear()
        inputbox.send_keys(crmscope)

        # 意向产品
        inputbox = driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[2]/div/form/div[10]/div/div[1]/div/textarea")
        inputbox.clear()
        inputbox.send_keys(crmpro)

        # 预计年采购额
        inputbox = driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[2]/div/form/div[11]/div/div/div/input")
        inputbox.clear()
        inputbox.send_keys(crmamount)

        # CRM编码
        inputbox = driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[2]/div/form/div[12]/div/div[1]/div/input")
        inputbox.clear()
        inputbox.send_keys(crmcode)

        # 提交
        driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[2]/div/form/div[13]/div/button[1]").click()
        time.sleep(3)

    def crminfo(self):

        # 重置查询条件
        driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[2]/div/div[1]/form/div[4]/div[2]/div/div/button").click()
        # 输入CRM编码
        driver.find_element_by_xpath(
            ".//*[@id='app']/div[2]/div[2]/div/div[1]/form/div[1]/div[2]/div/div/div/input").send_keys(crmcode)
        # 点击查询按钮
        driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[2]/div/div[1]/form/div[4]/div[1]/div/div/button").click()

        try:
            driver.find_element_by_xpath(
                ".//*[@id='app']/div[2]/div[2]/div/div[2]/div[1]/div[3]/table/tbody/tr/td[7]/div/button")
        except Exception as e:
            # mylogger.info(e)
            mylogger.info(u"CRM编码：" + crmcode + u"不存在！")
        else:
            # 查看该订单
            driver.find_element_by_xpath(
                ".//*[@id='app']/div[2]/div[2]/div/div[2]/div[1]/div[3]/table/tbody/tr/td[7]/div/button").click()
            time.sleep(1)

            # 读取公司名称
            readcrmcompany = driver.find_element_by_xpath(
                ".//*[@id='app']/div[2]/div[2]/div/form/div[7]/div/div/div/input").text

            # 读取国家
            readcrmcountry = driver.find_element_by_xpath(
                ".//*[@id='app']/div[2]/div[2]/div/form/div[3]/div/div/div/input").text

            # 读取年采购额
            readcrmamount = driver.find_element_by_xpath(
                ".//*[@id='app']/div[2]/div[2]/div/form/div[10]/div/div/div/input").text

            readall = u"|CRM:" + crmcode + u"|公司名称:" + readcrmcompany + u"|国家:" + readcrmcountry +u"|年采购额:" + u"[" + readcrmamount +u"]"

            mylogger.info(readall)

url = config.get("bossCRM", "url")
user = config.get("bossCRM", "user")
pw = config.get("bossCRM", "pw")
testTime = int(config.get("bossCRM", "testtime"))

mylogger.info("The test server url is: %s" % url)
mylogger.info("TestTask : crmNew")

testTimes = testTime + 1
mylogger.info("Test Time is : %s" % testTime)

crmNew = crmNew()


for iii in range(1, testTimes):
    # 进入登录界面
    crmNew.load(url)

    # 输入用户名
    crmNew.inputusername(user)

    # 输入密码
    crmNew.inputpassword(pw)

    # 输入验证码
    # inputcode()

    # 登录
    crmNew.login()

    # 订单管理
    crmNew.mancrm()

    # 新建订单
    crmNew.newcrm()

    # # 读取订单
    # crmNew.crminfo()

    # 退出
    crmNew.logout()

    mylogger.info("Test Passed= %s" % iii)
    # print time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), "Test Passed =", i

driver.quit()

mylogger.info("All Test Passed")
