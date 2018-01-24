#!/usr/bin/env python2
#  coding=utf-8
# 客户管理/客户管理/同步CRM
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
file_path = os.path.dirname(os.path.abspath('.')) + '/config/configuration.ini'
config.read(file_path)

driver = webdriver.Chrome()
# driver.set_window_size(800,600)
driver.maximize_window()
driver.implicitly_wait(6)


class CrmNew(object):
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
        time.sleep(2)
        driver.switch_to_alert()
        driver.find_element_by_xpath("html/body/div[3]/div/div[3]/button[2]").click()
        time.sleep(2)

    def mancrm(self):
        driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[1]/div/div/div/ul/li[4]/div").click()
        time.sleep(0.5)
        driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[1]/div/div/div/ul/li[4]/ul/li[1]").click()
        time.sleep(3)

    def newcrm(self):
        # 显示新增客户当天时间
        crmtime = time.strftime("%Y-%m-%d", time.localtime())
        crmtime1 = time.strftime("%Y%m%d%H%M%S", time.localtime())
        crmtime2 = time.strftime("%H%M%S", time.localtime())
        crmtime3 = time.strftime("%d%H%M%S", time.localtime())

        global crmcode
        crmcode = "CRMCODE" + crmtime2 + str(random.randint(1, 100))

        # 点击新增客户按钮
        driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[2]/div/div[2]/button").click()
        time.sleep(2)

        # 客户基本信息
        crmemail = "crm" + crmtime2 + "@crm.com"
        crmpw = "Crm@123456"
        crmname = "CRM" + crmtime2

        # CRM编码
        inputbox = driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[2]/div/form/div[2]/div/div/div/input")
        inputbox.clear()
        inputbox.send_keys(crmcode)
        time.sleep(5)

        # 邮箱
        inputbox = driver.find_element_by_xpath(
            ".//*[@id='app']/div[2]/div[2]/div/form/div[3]/div[2]/div/div/div/input")
        inputbox.clear()
        inputbox.send_keys(crmemail)

        # 密码
        inputbox = driver.find_element_by_xpath(
            ".//*[@id='app']/div[2]/div[2]/div/form/div[3]/div[3]/div/div/div/input")
        inputbox.clear()
        inputbox.send_keys(crmpw)

        # 选择国家
        select = driver.find_element_by_xpath(
            ".//*[@id='app']/div[2]/div[2]/div/form/div[3]/div[4]/div/div/div[1]/input")
        select.click()
        for iii in range(1, 136):
            select.send_keys(Keys.UP)
        select.send_keys(Keys.ENTER)
        time.sleep(0.5)

        # 电话
        inputbox = driver.find_element_by_xpath(
            ".//*[@id='app']/div[2]/div[2]/div/form/div[3]/div[5]/div/div/div/div[2]/div/div/div/input")
        inputbox.clear()
        inputbox.send_keys(crmtime3)

        # 姓名
        inputbox = driver.find_element_by_xpath(
            ".//*[@id='app']/div[2]/div[2]/div/form/div[3]/div[6]/div/div/div/input")
        inputbox.clear()
        inputbox.send_keys(crmname)

        # 企业信息
        crmcompany = crmname + " Co.,Ltd."
        crmscope = u"国际上主要的石油、天然气和石油化工的生产商，" \
                   u"同时也是全球最大的汽车燃油和润滑油零售商。" \
                   u"它亦为液化天然气行业的先驱，并在融资、管理和经营方面拥有丰富的经验。" \
                   u"业务遍及全球90多个国家和地区，雇员约93000人，" \
                   u"油、气产量分别占世界总产量的3%和3.5%。"
        crmpro = u"包括润滑油生产、加油站业务、沥青、天然气制油燃料、" \
                 u"与中海油合作的南海石化项目以及其他石化产品包括乙烯、" \
                 u"乙二醇、苯乙烯、高碳烯烃及衍生物、多元醇、" \
                 u"溶剂和丙二醇/聚对苯二甲酸丙二酯等"
        crmamount = random.randint(1, 10) * 1000000


        # 公司名称
        inputbox = driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[2]/div/form/div[3]/div[8]/div/div/div/input")
        inputbox.clear()
        inputbox.send_keys(crmcompany)

        # 经营范围
        inputbox = driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[2]/div/form/div[3]/div[9]/div/div/div/input")
        inputbox.clear()
        inputbox.send_keys(crmscope)

        # 意向产品
        inputbox = driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[2]/div/form/div[3]/div[10]/div/div/div/textarea")
        inputbox.clear()
        inputbox.send_keys(crmpro)

        # 预计年采购额
        inputbox = driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[2]/div/form/div[3]/div[11]/div/div/div/input")
        inputbox.clear()
        inputbox.send_keys(crmamount)



        # 电话国家码
        readcountrycode = driver.find_element_by_xpath(
            ".//*[@id='app']/div[2]/div[2]/div/form/div[3]/div[5]/div/div/div/div[1]/div/div/div/input").get_attribute("value")

        if readcountrycode == "NaN" or readcountrycode == "":
            inputbox = driver.find_element_by_xpath(
                ".//*[@id='app']/div[2]/div[2]/div/form/div[3]/div[5]/div/div/div/div[1]/div/div/div/input")
            inputbox.clear()
            inputbox.send_keys("00")
            # mylogger.info("00")
        else:
            # mylogger.error(readcountrycode)
            pass

        # 提交
        driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[2]/div/form/div[3]/div[12]/div/button[1]").click()
        time.sleep(5)

    def crminfo(self):
        time.sleep(2)
        # 重置查询条件
        driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[2]/div/div[1]/form/div[4]/button[2]").click()
        # 输入CRM编码
        driver.find_element_by_xpath(
            ".//*[@id='app']/div[2]/div[2]/div/div[1]/form/div[1]/div[2]/div/div/div/input").send_keys(crmcode)
        # 点击查询按钮
        driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[2]/div/div[1]/form/div[4]/button[1]").click()

        try:
            driver.find_element_by_xpath(
                ".//*[@id='app']/div[2]/div[2]/div/div[2]/div[1]/div[3]/table/tbody/tr/td[7]/div/button")
        except Exception as e:
            # mylogger.info(e)
            mylogger.error(u"CRM编码：" + crmcode + u"不存在！")
        else:
            time.sleep(3)
            # 读取客户编号
            readcode = driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[2]/div/div[2]/div[1]/div[3]/table/tbody/tr/td[1]/div").text
            # 读取审核状态
            readstatus = driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[2]/div/div[2]/div[1]/div[3]/table/tbody/tr/td[5]/div").text
            # 读取会员等级
            readlevel = driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[2]/div/div[2]/div[1]/div[3]/table/tbody/tr/td[6]/div/span").text
            # 点击查询按钮
            driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[2]/div/div[2]/div[1]/div[3]/table/tbody/tr/td[7]/div/button").click()
            time.sleep(3)

            # 读取公司名称
            # readcrmcompany = driver.find_element_by_xpath(
            #     ".//*[@id='app']/div[2]/div[2]/div/form/div[7]/div/div/span").get_attribute("value")
            readcrmcompany = driver.find_element_by_xpath(
                ".//*[@id='app']/div[2]/div[2]/div/form/div[7]/div/div/span").text

            # 读取国家
            readcrmcountry = driver.find_element_by_xpath(
                ".//*[@id='app']/div[2]/div[2]/div/form/div[3]/div/div/span").text

            # 读取年采购额
            readcrmamount = driver.find_element_by_xpath(
                ".//*[@id='app']/div[2]/div[2]/div/form/div[10]/div/div/span").text

            readall = u"|客户编号:" + readcode +"|CRM:" + crmcode + u"|公司名称:" + readcrmcompany + u"|国家:" + readcrmcountry + u"|年采购额:" + u"[" + readcrmamount +u"]" + u" {" + readlevel + u"}" + u" {" + readstatus + u"}"

            mylogger.info(readall)

    def first_verify(self):
        driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[1]/div/div/div/ul/li[4]/ul/li[5]").click()
        driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[2]/div/div[1]/form/div[1]/div[2]/div/div/div/input").send_keys(crmcode)
        driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[2]/div/div[1]/form/div[4]/button[1]").click()
        time.sleep(5)
        driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[2]/div/div[2]/div[1]/div[3]/table/tbody/tr/td[8]/div/button").click()
        time.sleep(3)
        driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[2]/div/form/div[12]/div/div/button[1]").click()
        driver.switch_to_alert()
        driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[2]/div/div[1]/div/div[2]/form/div[2]/div/div/div/textarea").send_keys(u"初审通过")
        driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[2]/div/div[1]/div/div[2]/form/div[3]/button[1]").click()
        time.sleep(5)

    def verify(self):
        driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[1]/div/div/div/ul/li[4]/ul/li[6]").click()
        time.sleep(5)
        driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[2]/div/div[1]/form/div[1]/div[2]/div/div/div/input").send_keys(crmcode)
        driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[2]/div/div[1]/form/div[4]/button[1]").click()
        time.sleep(3)
        driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[2]/div/div[2]/div[1]/div[3]/table/tbody/tr/td[8]/div/button[1]/span").click()
        time.sleep(3)

        driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[2]/div/form/div[12]/div/div/button[1]").click()
        driver.switch_to_alert()
        driver.find_element_by_xpath(
            ".//*[@id='app']/div[2]/div[2]/div/div[1]/div/div[2]/form/div[2]/div/div/div/textarea").send_keys(u"复审通过")
        driver.find_element_by_xpath(
            ".//*[@id='app']/div[2]/div[2]/div/div[1]/div/div[2]/form/div[3]/button[1]").click()
        time.sleep(3)

        # 设置市场经办人
        time.sleep(3)
        driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[2]/div/div[2]/div[1]/div[3]/table/tbody/tr/td[8]/div/button[2]").click()
        driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[2]/div/form/div[1]/div/div/input").send_keys(u"林凯")
        driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[2]/div/form/div[3]/div/button[1]").click()
        driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[2]/div/div[1]/div[3]/table/tbody/tr/td[1]/div/label/span/span").click()
        time.sleep(1)
        driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[2]/div/div[2]/button[1]").click()
        time.sleep(3)

        # 设置客户等级
        driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[2]/div/div[2]/div[1]/div[3]/table/tbody/tr/td[8]/div/button[3]").click()
        driver.switch_to_alert()
        select = driver.find_element_by_xpath(
            ".//*[@id='app']/div[2]/div[2]/div/div[3]/div/div[2]/form/div/div/div/div[1]/input")
        select.click()
        for iii in range(1, random.randint(2, 10)):
            select.send_keys(Keys.UP)
        select.send_keys(Keys.ENTER)
        time.sleep(0.5)
        driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[2]/div/div[3]/div/div[3]/div/button[2]").click()
        time.sleep(5)

        # 读取会员等级
        readlevel = driver.find_element_by_xpath(
            ".//*[@id='app']/div[2]/div[2]/div/div[2]/div[1]/div[3]/table/tbody/tr/td[5]/div/span").text

        mylogger.info(u"设定会员等级：" + "{" + readlevel + "}")

url = config.get("bossCRM", "url")
user = config.get("bossCRM", "user")
pw = config.get("bossCRM", "pw")
testtime = int(config.get("bossCRM", "testtime"))

mylogger.info("The test server url is: %s" % url)
mylogger.info("TestTask : crmNew")
mylogger.info("Test Time : %s" % testtime)


for testtimes in range(1, testtime+1):
    crmNew = CrmNew()
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

    # 客户管理
    crmNew.mancrm()

    # 新增客户
    crmNew.newcrm()

    # 读取客户信息
    crmNew.crminfo()

    # 初审
    crmNew.first_verify()

    # 复审
    crmNew.verify()

    # 退出
    crmNew.logout()
    mylogger.info("Test Finished : %s" % testtimes)

driver.quit()
mylogger.info("All Test Done !")