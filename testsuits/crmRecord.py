#!/usr/bin/env python3
#  coding=utf-8
# 客户管理/客户档案信息管理
__author__ = 'kayiyo'

import ConfigParser
import os.path
import time
import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from framework.logger import Logger

mylogger = Logger(logger="crmRecordLog").getlog()
config = ConfigParser.ConfigParser()
# file_path = os.path.dirname(os.getcwd()) + '/config/config.ini'
file_path = os.path.dirname(os.path.abspath('.')) + '/config/configuration.ini'
config.read(file_path)

driver = webdriver.Chrome()
# driver.set_window_size(800,600)
driver.maximize_window()
driver.implicitly_wait(6)


class CrmRecord(object):
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
        driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[1]/div/div/div/ul/li[4]/ul/li[2]").click()
        time.sleep(3)

    def recordcrm(self):
        # 显示新增客户当天时间
        crmtime = time.strftime("%Y-%m-%d", time.localtime())
        crmtime1 = time.strftime("%Y%m%d%H%M%S", time.localtime())
        crmtime2 = time.strftime("%H%M%S", time.localtime())
        crmtime3 = time.strftime("%d%H%M%S", time.localtime())
        crmamount = random.randint(1, 10) * 1000000
        crmemail = "crm" + crmtime2 + "@crm.com"
        crmpw = "Crm@123456"
        crmname = "CRM" + crmtime2
        global crmcode
        crmcode = "CRMCODE" + crmtime2
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

        # 点击新建客户档案按钮
        driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[2]/div/div[3]/button[1]").click()
        time.sleep(2)

        # 客户档案基本信息

        # 选择客户名称
        # 点击选择按钮
        driver.find_element_by_xpath(
            ".//*[@id='app']/div[2]/div[2]/div/div[2]/div[2]/div[1]/div/form/div[1]/div[1]/div[1]/div/button").click()
        time.sleep(5)
        driver.switch_to_alert()

        # 选择市场经办人
        time.sleep(1)
        inputbox = driver.find_element_by_xpath(
            ".//*[@id='app']/div[2]/div[2]/div/div[2]/div[2]/div[1]/div/div/div/div[2]/form/div[1]/div/div/input")
        inputbox.clear()
        inputbox.send_keys("CRM")
        time.sleep(1)

        driver.find_element_by_xpath(
            ".//*[@id='app']/div[2]/div[2]/div/div[2]/div[2]/div[1]/div/div/div/div[2]/form/div[3]/div/button").click()
        time.sleep(1)

        global readcrmrecord
        readcrmrecord = driver.find_element_by_xpath(
            ".//*[@id='app']/div[2]/div[2]/div/div[2]/div[2]/div[1]/div/div/div/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[1]/div").text

        driver.find_element_by_xpath(
            ".//*[@id='app']/div[2]/div[2]/div/div[2]/div[2]/div[1]/div/div/div/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[3]/div/button").click()
        time.sleep(1)

        # 选择客户类型
        select = driver.find_element_by_xpath(
            ".//*[@id='app']/div[2]/div[2]/div/div[2]/div[2]/div[1]/div/form/div[1]/div[2]/div[4]/div/div/div/div/div[1]/input")
        select.click()
        for iii in range(1, random.randint(2, 10)):
            select.send_keys(Keys.UP)
        select.send_keys(Keys.ENTER)
        time.sleep(0.5)

        # 选择是否油气
        a = random.randint(2, 10)
        if a % 2:
            driver.find_element_by_xpath(
                ".//*[@id='app']/div[2]/div[2]/div/div[2]/div[2]/div[1]/div/form/div[1]/div[2]/div[5]/div/label[1]/span[1]/span").click()  # 选择油气是
        else:
            driver.find_element_by_xpath(
                ".//*[@id='app']/div[2]/div[2]/div/div[2]/div[2]/div[1]/div/form/div[1]/div[2]/div[5]/div/label[2]/span[1]/span").click()  # 选择油气否

        # 公司网址
        inputbox = driver.find_element_by_xpath(
            ".//*[@id='app']/div[2]/div[2]/div/div[2]/div[2]/div[1]/div/form/div[2]/div[1]/div[2]/div/div[1]/input")
        inputbox.clear()
        inputbox.send_keys("www.%s.com" % crmname)

        # 成立日期
        inputbox = driver.find_element_by_xpath(
            ".//*[@id='app']/div[2]/div[2]/div/div[2]/div[2]/div[1]/div/form/div[2]/div[2]/div[2]/div/div/input")
        inputbox.clear()
        inputbox.send_keys(u"2010-01-01")

        # 注册资金
        inputbox = driver.find_element_by_xpath(
            ".//*[@id='app']/div[2]/div[2]/div/div[2]/div[2]/div[1]/div/form/div[2]/div[1]/div[3]/div/div[1]/input")
        inputbox.clear()
        inputbox.send_keys(crmamount)

        # 货币
        select = driver.find_element_by_xpath(
            ".//*[@id='app']/div[2]/div[2]/div/div[2]/div[2]/div[1]/div/form/div[2]/div[2]/div[3]/div/div[1]/div[1]/input")
        select.click()
        for iii in range(1, random.randint(2, 10)):
            select.send_keys(Keys.UP)
        select.send_keys(Keys.ENTER)
        time.sleep(0.5)

        # 雇员数量
        inputbox = driver.find_element_by_xpath(
            ".//*[@id='app']/div[2]/div[2]/div/div[2]/div[2]/div[1]/div/form/div[2]/div[1]/div[4]/div/div/input")
        inputbox.clear()
        inputbox.send_keys(random.randint(1, 10000))

        # 公司性质
        inputbox = driver.find_element_by_xpath(
            ".//*[@id='app']/div[2]/div[2]/div/div[2]/div[2]/div[1]/div/form/div[3]/div/div/div/div[1]/input")
        inputbox.clear()
        inputbox.send_keys(u"公司性质")

        # 子公司及名称
        inputbox = driver.find_element_by_xpath(
            ".//*[@id='app']/div[2]/div[2]/div/div[2]/div[2]/div[1]/div/form/div[4]/div/div/div/div/input")
        inputbox.clear()
        inputbox.send_keys(u"子公司及名称")

        # 地址
        inputbox = driver.find_element_by_xpath(
            ".//*[@id='app']/div[2]/div[2]/div/div[2]/div[2]/div[1]/div/form/div[5]/div/div/div/div[1]/input")
        inputbox.clear()
        inputbox.send_keys(u"地址")

        # 公司其他信息
        inputbox = driver.find_element_by_xpath(
            ".//*[@id='app']/div[2]/div[2]/div/div[2]/div[2]/div[1]/div/form/div[6]/div/div/div/div[1]/textarea")
        inputbox.clear()
        inputbox.send_keys(u"公司其他信息")

        # 财务报表/上传文件
        upload = driver.find_element_by_xpath(
            ".//*[@id='app']/div[2]/div[2]/div/div[2]/div[2]/div[1]/div/form/div[7]/div/div[1]/div/div/div/input")
        a = random.randint(2, 11)
        if a % 2:
            upload.send_keys('d:\\1fortest\word.docx')
        else:
            upload.send_keys('d:\\1fortest\pdf.pdf')
        time.sleep(3)

        # 公司人员组织架构
        upload = driver.find_element_by_xpath(
            ".//*[@id='app']/div[2]/div[2]/div/div[2]/div[2]/div[1]/div/form/div[7]/div/div[2]/div/div/div/input")
        a = random.randint(2, 11)
        if a % 2:
            upload.send_keys('d:\\1fortest\word.docx')
        else:
            upload.send_keys('d:\\1fortest\pdf.pdf')
        time.sleep(3)
        # uploadinfo = driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[2]/div/div[2]/div[2]/div[1]/div/form/div[2]/div[1]/div[4]/div/div/ul")
        # uploadinfo.get_attribute('value')
        # mylogger.info(uploadinfo)

        # # 财务报表/上传文件
        # upload = driver.find_element_by_xpath(
        #     ".//*[@id='app']/div[2]/div[2]/div/div[2]/div[2]/div[1]/div/form/div[2]/div[1]/div[4]/div/div/div/button")
        # upload.click()
        # time.sleep(2)
        #
        # # SendKeys
        # SendKeys.SendKeys('d:\\1fortest\word.docx')
        # time.sleep(2)
        # SendKeys.SendKeys("{ENTER}")
        # time.sleep(2)



        # 主要联系人
        # 名字
        inputbox = driver.find_element_by_xpath(
            ".//*[@id='app']/div[2]/div[2]/div/div[2]/div[2]/div[1]/div/form/div[8]/div[1]/div[1]/div[1]/div/div/input")
        inputbox.clear()
        inputbox.send_keys(u"贾步思%s" % crmtime2)
        # 职位
        inputbox = driver.find_element_by_xpath(
            ".//*[@id='app']/div[2]/div[2]/div/div[2]/div[2]/div[1]/div/form/div[8]/div[1]/div[2]/div[1]/div/div/input")
        inputbox.clear()
        inputbox.send_keys(u"采购经理")
        # 购买角色
        inputbox = driver.find_element_by_xpath(
            ".//*[@id='app']/div[2]/div[2]/div/div[2]/div[2]/div[1]/div/form/div[8]/div[1]/div[1]/div[2]/div/div/input")
        inputbox.clear()
        inputbox.send_keys(u"采购商")
        # 联系电话
        inputbox = driver.find_element_by_xpath(
            ".//*[@id='app']/div[2]/div[2]/div/div[2]/div[2]/div[1]/div/form/div[8]/div[1]/div[2]/div[2]/div/div/input")
        inputbox.clear()
        inputbox.send_keys(random.randint(1, 100000000))
        # 邮箱
        inputbox = driver.find_element_by_xpath(
            ".//*[@id='app']/div[2]/div[2]/div/div[2]/div[2]/div[1]/div/form/div[8]/div[1]/div[1]/div[3]/div/div/input")
        inputbox.clear()
        inputbox.send_keys(crmemail)
        # 喜好
        inputbox = driver.find_element_by_xpath(
            ".//*[@id='app']/div[2]/div[2]/div/div[2]/div[2]/div[1]/div/form/div[8]/div[1]/div[2]/div[3]/div/div/input")
        inputbox.clear()
        inputbox.send_keys(u"运动")

        for num in range(2, 9):
            num = bytes(num)
            read_box = driver.find_element_by_xpath(
                ".//*[@id='app']/div[2]/div[2]/div/div[2]/div[2]/div[1]/div/form/div[8]/div[" + num + "]/div/label").text
            input_box = driver.find_element_by_xpath(
                ".//*[@id='app']/div[2]/div[2]/div/div[2]/div[2]/div[1]/div/form/div[8]/div[" + num + "]/div/div/div/input").send_keys(read_box)


        # 上下游信息
        time.sleep(3)
        driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[2]/div/div[2]/div[1]/div/div[1]/div/div[2]").click()
        time.sleep(3)
        # 上游信息
        for num in range(1, 11):
            num = bytes(num)
            read_box = driver.find_element_by_xpath(
                ".//*[@id='app']/div[2]/div[2]/div/div[2]/div[2]/div[2]/div/form[1]/div[" + num + "]/label").text
            read_box = read_box.replace(':', '')
            try:
                input_text = driver.find_element_by_xpath(
                    ".//*[@id='app']/div[2]/div[2]/div/div[2]/div[2]/div[2]/div/form[1]/div[" + num + "]/div/div/textarea")
            except Exception as e:
                driver.find_element_by_xpath(
                    ".//*[@id='app']/div[2]/div[2]/div/div[2]/div[2]/div[2]/div/form[1]/div[" + num + "]/div/div/input").send_keys(read_box)
            else:
                input_text.send_keys(read_box)


        # 下游信息
        for num in range(1, 10):
            num = bytes(num)
            read_box = driver.find_element_by_xpath(
                ".//*[@id='app']/div[2]/div[2]/div/div[2]/div[2]/div[2]/div/form[2]/div[" + num + "]/label").text
            read_box = read_box.replace(':', '')
            try:
                input_text = driver.find_element_by_xpath(
                ".//*[@id='app']/div[2]/div[2]/div/div[2]/div[2]/div[2]/div/form[2]/div[" + num + "]/div/div/textarea")
            except Exception as e:
                driver.find_element_by_xpath(
                ".//*[@id='app']/div[2]/div[2]/div/div[2]/div[2]/div[2]/div/form[2]/div[" + num + "]/div/div/input").send_keys(read_box)
            else:
                input_text.send_keys(read_box)

        # 竞争对手信息
        for num in range(1, 5):
            num = bytes(num)
            read_box = driver.find_element_by_xpath(
                        ".//*[@id='app']/div[2]/div[2]/div/div[2]/div[2]/div[2]/div/form[3]/div[" + num + "]/label").text
            read_box = read_box.replace(':', '')
            try:
                input_text = driver.find_element_by_xpath(
                            ".//*[@id='app']/div[2]/div[2]/div/div[2]/div[2]/div[2]/div/form[3]/div[" + num + "]/div/div/textarea")
            except Exception as e:
                driver.find_element_by_xpath(
                            ".//*[@id='app']/div[2]/div[2]/div/div[2]/div[2]/div[2]/div/form[3]/div[" + num + "]/div/div/input").send_keys(
                            read_box)
            else:
                input_text.send_keys(read_box)

        # 业务基本信息
        driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[2]/div/div[2]/div[1]/div/div[1]/div/div[3]").click()
        time.sleep(2)
        # 业务基本信息/业务基本信息
        # 产品类型
        inputbox = driver.find_element_by_xpath(
            ".//*[@id='app']/div[2]/div[2]/div/div[2]/div[2]/div[3]/div/form/div[1]/div/div/input")
        inputbox.clear()
        inputbox.send_keys(u"产品类型%s" % crmtime2)
        # 采购模式
        select = driver.find_element_by_xpath(
            ".//*[@id='app']/div[2]/div[2]/div/div[2]/div[2]/div[3]/div/form/div[2]/div/div/div[1]/input")
        select.click()
        for iii in range(1, random.randint(2, 10)):
            select.send_keys(Keys.UP)
        select.send_keys(Keys.ENTER)
        time.sleep(0.5)
        # 采购周期
        select = driver.find_element_by_xpath(
            ".//*[@id='app']/div[2]/div[2]/div/div[2]/div[2]/div[3]/div/form/div[3]/div/div/div/div[1]/input")
        select.click()
        for iii in range(1, random.randint(2, 10)):
            select.send_keys(Keys.UP)
        select.send_keys(Keys.ENTER)
        time.sleep(0.5)
        # 设备以及使用情况
        inputbox = driver.find_element_by_xpath(
            ".//*[@id='app']/div[2]/div[2]/div/div[2]/div[2]/div[3]/div/form/div[4]/div/div/input")
        inputbox.clear()
        inputbox.send_keys(u"设备以及使用情况%s" % crmtime2)
        # 是否有仓库
        driver.find_element_by_xpath(
            ".//*[@id='app']/div[2]/div[2]/div/div[2]/div[2]/div[3]/div/form/div[5]/div/label[1]/span[1]/span").click()
        # 仓库所在地
        inputbox = driver.find_element_by_xpath(
            ".//*[@id='app']/div[2]/div[2]/div/div[2]/div[2]/div[3]/div/form/div[6]/div/div/input")
        inputbox.clear()
        inputbox.send_keys(u"仓库所在地%s" % crmtime2)

        # 产品服务偏好、原产地偏好、品牌偏好
        for num in range(1, 4):
            num = bytes(num)
            read_box = driver.find_element_by_xpath(
                ".//*[@id='app']/div[2]/div[2]/div/div[2]/div[2]/div[3]/div/form/div[7]/div[" + num + "]/div/label").text
            read_box = read_box.replace(':', '')
            try:
                input_text = driver.find_element_by_xpath(
                    ".//*[@id='app']/div[2]/div[2]/div/div[2]/div[2]/div[3]/div/form/div[7]/div[" + num + "]/div/div/div/input")
            except Exception as e:
                driver.find_element_by_xpath(
                    ".//*[@id='app']/div[2]/div[2]/div/div[2]/div[2]/div[3]/div/form/div[7]/div[" + num + "]/div/div/div/textarea").send_keys(
                    read_box)
            else:
                input_text.send_keys(read_box)

        # 结算基本信息
        # 会员惯用贸易术语
        select = driver.find_element_by_xpath(
            ".//*[@id='app']/div[2]/div[2]/div/div[2]/div[2]/div[3]/div/form/div[8]/div/div/div[1]/input")
        select.click()
        for iii in range(1, random.randint(2, 10)):
            select.send_keys(Keys.UP)
        select.send_keys(Keys.ENTER)
        time.sleep(0.5)
        # 结算方式
        select = driver.find_element_by_xpath(
            ".//*[@id='app']/div[2]/div[2]/div/div[2]/div[2]/div[3]/div/form/div[9]/div/div/div[1]/input")
        select.click()
        for iii in range(1, random.randint(2, 10)):
            select.send_keys(Keys.UP)
        select.send_keys(Keys.ENTER)
        time.sleep(0.5)
        # 是否本地币结算
        driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[2]/div/div[2]/div[2]/div[3]/div/form/div[10]/div[1]/div/div/label[1]/span[1]/span").click()

        # 是否与KERUI有采购关系
        driver.find_element_by_xpath(
            ".//*[@id='app']/div[2]/div[2]/div/div[2]/div[2]/div[3]/div/form/div[10]/div[2]/div/div/label[1]/span[1]/span").click()

        # 入网管理
        # 是否入网
        driver.find_element_by_xpath(
            ".//*[@id='app']/div[2]/div[2]/div/div[2]/div[2]/div[3]/div/form/div[11]/div/div/div/label[1]/span[1]/span").click()
        # 入网主体
        driver.find_element_by_xpath(
            ".//*[@id='app']/div[2]/div[2]/div/div[2]/div[2]/div[3]/div/form/div[11]/div[2]/div/div/div/label[2]/span[1]/span").click()
        # 入网时间
        inputbox = driver.find_element_by_xpath(
            ".//*[@id='app']/div[2]/div[2]/div/div[2]/div[2]/div[3]/div/form/div[12]/div[1]/div/div/div/input")
        inputbox.clear()
        inputbox.send_keys(u"2012-01-01")
        # 入网失效时间
        inputbox = driver.find_element_by_xpath(
            ".//*[@id='app']/div[2]/div[2]/div/div[2]/div[2]/div[3]/div/form/div[12]/div[2]/div/div/div/input")
        inputbox.clear()
        inputbox.send_keys(u"2020-01-01")
        # 入网产品
        inputbox = driver.find_element_by_xpath(
            ".//*[@id='app']/div[2]/div[2]/div/div[2]/div[2]/div[3]/div/form/div[14]/div/div/textarea")
        inputbox.clear()
        inputbox.send_keys(u"入网产品%s" % crmtime2)

        # 信用评价
        # 客户信用等级
        select = driver.find_element_by_xpath(
            ".//*[@id='app']/div[2]/div[2]/div/div[2]/div[2]/div[3]/div/form/div[15]/div[1]/div/div/div/div[1]/input")
        select.click()
        for iii in range(1, random.randint(2, 10)):
            select.send_keys(Keys.UP)
        select.send_keys(Keys.ENTER)
        time.sleep(0.5)
        # 授信类型
        select = driver.find_element_by_xpath(
            ".//*[@id='app']/div[2]/div[2]/div/div[2]/div[2]/div[3]/div/form/div[16]/div[1]/div/div/div/div[1]/input")
        select.click()
        for iii in range(1, random.randint(2, 10)):
            select.send_keys(Keys.UP)
        select.send_keys(Keys.ENTER)
        time.sleep(0.5)
        # 授信额度
        driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[2]/div/div[2]/div[2]/div[3]/div/form/div[15]/div[2]/div/div/div/input").send_keys(1000000)
        # 剩余授信额度
        driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[2]/div/div[2]/div[2]/div[3]/div/form/div[16]/div[2]/div/div/div/input").send_keys(200000)




        # 采购计划
        # # 采购年份
        # driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[2]/div/div[2]/div[2]/div[3]/div/form/div[15]/div[1]/div/div/input").click()
        # time.sleep(1)
        # driver.find_element_by_xpath("html/body/div[3]/div[1]/div/div[2]/table[2]/tbody/tr[3]/td[1]/a").click()
        # 采购预算
        inputbox = driver.find_element_by_xpath(
            ".//*[@id='app']/div[2]/div[2]/div/div[2]/div[2]/div[3]/div/form/div[17]/div[2]/div/div/input")
        inputbox.clear()
        inputbox.send_keys(u"采购预算%s" % crmtime2)
        # 采购计划
        inputbox = driver.find_element_by_xpath(
            ".//*[@id='app']/div[2]/div[2]/div/div[2]/div[2]/div[3]/div/form/div[17]/div[3]/div/div/textarea")
        inputbox.clear()
        inputbox.send_keys(u"采购计划%s" % crmtime2)
        # 采购计划
        upload = driver.find_element_by_xpath(
            ".//*[@id='app']/div[2]/div[2]/div/div[2]/div[2]/div[3]/div/form/div[17]/div[4]/div/div/div/div/div/input")
        a = random.randint(2, 11)
        if a % 2:
            upload.send_keys('d:\\1fortest\word.docx')
        else:
            upload.send_keys('d:\\1fortest\pdf.pdf')
        time.sleep(3)

        # 客户分析报告
        upload = driver.find_element_by_xpath(
            ".//*[@id='app']/div[2]/div[2]/div/div[2]/div[2]/div[3]/div/form/div[18]/div/div/div/div/div/div/input")
        a = random.randint(2, 11)
        if a % 2:
            upload.send_keys('d:\\1fortest\word.docx')
        else:
            upload.send_keys('d:\\1fortest\pdf.pdf')
        time.sleep(3)

        # 与KERUI/ERUI往来里程碑事件
        # 时间
        inputbox = driver.find_element_by_xpath(
            ".//*[@id='app']/div[2]/div[2]/div/div[2]/div[2]/div[3]/div/form/div[19]/div[1]/div/div/input")
        inputbox.clear()
        inputbox.send_keys(u"2017-01-01")

        for num in range(2, 5):
            num = bytes(num)
            read_box = driver.find_element_by_xpath(
                ".//*[@id='app']/div[2]/div[2]/div/div[2]/div[2]/div[3]/div/form/div[19]/div[" + num + "]/label").text
            read_box = read_box.replace(':', '')
            try:
                input_text = driver.find_element_by_xpath(
                    ".//*[@id='app']/div[2]/div[2]/div/div[2]/div[2]/div[3]/div/form/div[19]/div[" + num + "]/div/div/input")
            except Exception as e:
                driver.find_element_by_xpath(
                    ".//*[@id='app']/div[2]/div[2]/div/div[2]/div[2]/div[3]/div/form/div[19]/div[" + num + "]/div/div/textarea").send_keys(
                    read_box)
            else:
                input_text.send_keys(read_box)

        # # 电话国家码
        # readcountrycode = driver.find_element_by_xpath(
        #     ".//*[@id='app']/div[2]/div[2]/div/form/div[5]/div/div/div/div[1]/div/div/div/input").get_attribute("value")
        #
        # if readcountrycode == "NaN" or readcountrycode == "":
        #     inputbox = driver.find_element_by_xpath(
        #         ".//*[@id='app']/div[2]/div[2]/div/form/div[5]/div/div/div/div[1]/div/div/div/input")
        #     inputbox.clear()
        #     inputbox.send_keys("00")
        #     # mylogger.info("00")
        # else:
        #     # mylogger.info(readcountrycode)
        #     pass

        # 保存
        driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[2]/div/div[3]/div[1]/button").click()
        time.sleep(5)

    def crminfo(self):
        # 重置查询条件
        driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[2]/div/div[2]/form/div[3]/button[2]").click()
        # 输入CRM编码
        driver.find_element_by_xpath(
            ".//*[@id='app']/div[2]/div[2]/div/div[2]/form/div[1]/div[3]/div/div/div/input").send_keys(readcrmrecord)
        # 点击查询按钮
        driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[2]/div/div[2]/form/div[3]/button[1]").click()
        time.sleep(10)

        try:
            driver.find_element_by_xpath(
                ".//*[@id='app']/div[2]/div[2]/div/div[4]/div[1]/div[5]/div[2]/table/tbody/tr/td[26]/div/button[2]/span")
        except Exception as e:
            # mylogger.info(e)
            mylogger.info(u"客户名称：" + readcrmrecord + u"不存在！")
        else:
            driver.find_element_by_xpath(
                ".//*[@id='app']/div[2]/div[2]/div/div[4]/div[1]/div[5]/div[2]/table/tbody/tr/td[26]/div/button[2]/span").click()
            time.sleep(3)

            # 读取国家
            readcrmcountry = driver.find_element_by_xpath(
                ".//*[@id='app']/div[2]/div[2]/div/div[1]/div[1]/span[2]").text
            # 读取客户名称
            readcrmcompany = driver.find_element_by_xpath(
                ".//*[@id='app']/div[2]/div[2]/div/div[1]/div[4]/span[2]").text
            # 读取CRM客户代码
            readcrmcode = driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[2]/div/div[1]/div[6]/span[2]").text
            # 读取年采购额
            readregistered = driver.find_element_by_xpath(
                ".//*[@id='app']/div[2]/div[2]/div/div[2]/div[5]/span[2]").text
            # 读取财务报表
            readstatement = driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[2]/div/div[2]/div[7]/a").text

            readall = u"|公司名称:" + readcrmcompany + "|CRM:" + readcrmcode + u"|国家:" + readcrmcountry + u"|年采购额:" + u"[" + readregistered + u"]" + u" 财务报表{" + readstatement + u"}"

            mylogger.info(readall)


url = config.get("bossCRM", "url")
user = config.get("bossCRM", "user")
pw = config.get("bossCRM", "pw")
testTime = int(config.get("bossCRM", "testtime"))

mylogger.info("The test server url is: %s" % url)
mylogger.info("TestTask : crmNew")

testTimes = testTime + 1
mylogger.info("Test Time is : %s" % testTime)

crmRecord = CrmRecord()

for iii in range(1, testTimes):
    # 进入登录界面
    crmRecord.load(url)

    # 输入用户名
    crmRecord.inputusername(user)

    # 输入密码
    crmRecord.inputpassword(pw)

    # 输入验证码
    # inputcode()

    # 登录
    crmRecord.login()

    # 客户管理
    crmRecord.mancrm()

    # 客户档案信息管理
    crmRecord.recordcrm()

    # # 读取订单
    # crmRecord.crminfo()

    # 退出
    crmRecord.logout()
    mylogger.info('Test Finished： %s' % iii)

driver.quit()
mylogger.info("All Test Finished")
