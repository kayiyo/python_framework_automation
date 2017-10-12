# coding=utf-8
__author__ = 'kayiyo'

import ConfigParser
import os.path
import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from framework.logger import Logger

mylogger = Logger(logger="BossInquiryLog").getlog()

config = ConfigParser.ConfigParser()
# file_path = os.path.dirname(os.getcwd()) + '/config/config.ini'
file_path = os.path.dirname(os.path.abspath('.')) + '/config/configuration.ini'
config.read(file_path)



driver = webdriver.Chrome()
# driver.set_window_size(800,600)
driver.maximize_window()
driver.implicitly_wait(6)



def load():
    url = config.get("bossinquiry", "URL")
    driver.get(url)
    time.sleep(2)
	# driver.find_element_by_xpath("html/body/div[1]/div[1]/ul/li[1]/a").click()


def inputUsername():
    user = config.get("bossinquiry", "USER")
    inputbox = driver.find_element_by_xpath(".//*[@id='app']/div/form/div[1]/div/div[1]/input")
    inputbox.clear()
    inputbox.send_keys(user)
    time.sleep(1)


def inputPassword():
    pw = config.get("bossinquiry", "PW")
    inputbox = driver.find_element_by_xpath(".//*[@id='app']/div/form/div[2]/div/div/input")
    inputbox.clear()
    inputbox.send_keys(pw)
    time.sleep(1)


def inputCode():
    CODE = config.get("bossinquiry", "CODE")
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
    driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[1]/div/div/div/ul/li[1]/div").click()
    time.sleep(1)
    driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[1]/div/div/div/ul/li[1]/ul/a/li").click()
    time.sleep(2)


def newInquiry():
    # 点击新增询单按钮
    driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[2]/div/div[2]/div[1]/div/div/button[1]").click()
    time.sleep(2)

    # 读取流程编码
    processcode = driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[2]/div/div[1]/div[2]/div[1]/form/div[1]/div[2]/div[1]/div[1]").text
    mylogger.info(processcode)

    # 选择客户
    driver.find_element_by_xpath(
        ".//*[@id='app']/div[2]/div[2]/div/div[1]/div[2]/div[1]/form/div[1]/div[3]/div[2]/div[1]/div/button").click()
    driver.switch_to_alert()
    driver.find_element_by_xpath(
        ".//*[@id='app']/div[2]/div[2]/div/div[2]/div/div[2]/form/div[2]/div/button[2]").click()
    driver.find_element_by_xpath(
        ".//*[@id='app']/div[2]/div[2]/div/div[2]/div/div[2]/form/div[1]/div/div/input").send_keys("PARTS")
    driver.find_element_by_xpath(
        ".//*[@id='app']/div[2]/div[2]/div/div[2]/div/div[2]/form/div[2]/div/button[1]").click()
    driver.find_element_by_xpath(
        ".//*[@id='app']/div[2]/div[2]/div/div[2]/div/div[2]/div[1]/div[4]/div[2]/table/tbody/tr/td[5]/div/button").click()
    time.sleep(1)

    # 新增一行SKU
    driver.find_element_by_xpath(
        ".//*[@id='app']/div[2]/div[2]/div/div[1]/div[2]/div[1]/form/div[2]/div[2]/div[2]/div/input").clear()
    driver.find_element_by_xpath(
        ".//*[@id='app']/div[2]/div[2]/div/div[1]/div[2]/div[1]/form/div[2]/div[2]/div[2]/div/input").send_keys("1")
    driver.find_element_by_xpath(
        ".//*[@id='app']/div[2]/div[2]/div/div[1]/div[2]/div[1]/form/div[2]/div[2]/div[2]/button").click()
    time.sleep(1)

    # 选择SKU
    driver.find_element_by_xpath(
        ".//*[@id='app']/div[2]/div[2]/div/div[1]/div[2]/div[1]/form/div[2]/div[3]/div/div[3]/table/tbody/tr/td[3]/div/button").click()
    driver.switch_to_alert()
    # driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[2]/div/div[1]/div[2]/div[1]/form/div[2]/div[4]/div/div[2]/form/div[5]/div/button[2]").click()
    # driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[2]/div/div[1]/div[2]/div[1]/form/div[2]/div[4]/div/div[2]/form/div[4]/div/div/input").send_keys("旋塞阀")
    # driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[2]/div/div[1]/div[2]/div[1]/form/div[2]/div[4]/div/div[2]/form/div[5]/div/button[1]").click()
    driver.find_element_by_xpath(
        ".//*[@id='app']/div[2]/div[2]/div/div[1]/div[2]/div[1]/form/div[2]/div[4]/div/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[8]/div/button").click()
    # driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[2]/div/div[1]/div[2]/div[1]/form/div[2]/div[3]/div/div[5]/div[2]/table/tbody/tr/td[13]/div/button").click()
    time.sleep(1)

    # 填写客户询单号
    inputbox = driver.find_element_by_xpath(
        ".//*[@id='app']/div[2]/div[2]/div/div[1]/div[2]/div[1]/form/div[2]/div[3]/div/div[3]/table/tbody/tr/td[4]/div/div/input")
    inputbox.clear()
    inputbox.send_keys("KHXDH1381")

    # 填写外文品名
    inputbox = driver.find_element_by_xpath(
        ".//*[@id='app']/div[2]/div[2]/div/div[1]/div[2]/div[1]/form/div[2]/div[3]/div/div[3]/table/tbody/tr/td[5]/div/div/input")
    inputbox.clear()
    inputbox.send_keys("WWPM23478")

    # 填写中文品名
    inputbox = driver.find_element_by_xpath(
        ".//*[@id='app']/div[2]/div[2]/div/div[1]/div[2]/div[1]/form/div[2]/div[3]/div/div[3]/table/tbody/tr/td[6]/div/div/input")
    inputbox.clear()
    inputbox.send_keys(u"中文品名85")

    # 填写型号
    inputbox = driver.find_element_by_xpath(
        ".//*[@id='app']/div[2]/div[2]/div/div[1]/div[2]/div[1]/form/div[2]/div[3]/div/div[3]/table/tbody/tr/td[7]/div/div/input")
    inputbox.clear()
    inputbox.send_keys("Sn230-12D")

    # 填写客户需求描述(外文)
    inputbox = driver.find_element_by_xpath(
        ".//*[@id='app']/div[2]/div[2]/div/div[1]/div[2]/div[1]/form/div[2]/div[3]/div/div[3]/table/tbody/tr/td[8]/div/div/input")
    inputbox.clear()
    inputbox.send_keys("KHXQMS34214JDKF.DSFFD123DSDF")

    # 填写客户需求描述(中文)
    inputbox = driver.find_element_by_xpath(
        ".//*[@id='app']/div[2]/div[2]/div/div[1]/div[2]/div[1]/form/div[2]/div[3]/div/div[3]/table/tbody/tr/td[9]/div/div/input")
    inputbox.clear()
    inputbox.send_keys(u"客户需求描述3241132客户需求描述")

    # 填写数量
    inputbox = driver.find_element_by_xpath(
        ".//*[@id='app']/div[2]/div[2]/div/div[1]/div[2]/div[1]/form/div[2]/div[3]/div/div[3]/table/tbody/tr/td[10]/div/div/input")
    inputbox.clear()
    inputbox.send_keys("5")

    # 填写单位
    inputbox = driver.find_element_by_xpath(
        ".//*[@id='app']/div[2]/div[2]/div/div[1]/div[2]/div[1]/form/div[2]/div[3]/div/div[3]/table/tbody/tr/td[11]/div/div/input")
    inputbox.clear()
    inputbox.send_keys(u"台")

    # 填写品牌
    inputbox = driver.find_element_by_xpath(
        ".//*[@id='app']/div[2]/div[2]/div/div[1]/div[2]/div[1]/form/div[2]/div[3]/div/div[3]/table/tbody/tr/td[12]/div/div/input")
    inputbox.clear()
    inputbox.send_keys(u"名牌SLKD")

    # 点击保存按钮
    driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[2]/div/div[1]/div[2]/div[1]/form/div[2]/div[3]/div/div[5]/div[2]/table/tbody/tr/td[13]/div/button").click()



    # 填写项目信息
    # 填写项目代码
    driver.find_element_by_xpath(
        ".//*[@id='app']/div[2]/div[2]/div/div[1]/div[2]/div[1]/form/div[3]/div[2]/div[1]/div/div/div/input").clear()
    driver.find_element_by_xpath(
        ".//*[@id='app']/div[2]/div[2]/div/div[1]/div[2]/div[1]/form/div[3]/div[2]/div[1]/div/div/div/input").send_keys(
        "XMDMTEST537")

    # 填写项目名称
    driver.find_element_by_xpath(
        ".//*[@id='app']/div[2]/div[2]/div/div[1]/div[2]/div[1]/form/div[3]/div[2]/div[2]/div/div/div/input").clear()
    driver.find_element_by_xpath(
        ".//*[@id='app']/div[2]/div[2]/div/div[1]/div[2]/div[1]/form/div[3]/div[2]/div[2]/div/div/div/input").send_keys(
        "XMMCTEST289")

    # 预计报价时间
    inputbox = driver.find_element_by_xpath(
        ".//*[@id='app']/div[2]/div[2]/div/div[1]/div[2]/div[1]/form/div[3]/div[4]/div[1]/div/div/div/div/input")
    # inputbox.clear()
    inputbox.send_keys("2017-11-17")

    # 填写付款方式
    driver.find_element_by_xpath(
        ".//*[@id='app']/div[2]/div[2]/div/div[1]/div[2]/div[1]/form/div[3]/div[4]/div[2]/div/div/div[1]/textarea").clear()
    driver.find_element_by_xpath(
        ".//*[@id='app']/div[2]/div[2]/div/div[1]/div[2]/div[1]/form/div[3]/div[4]/div[2]/div/div/div[1]/textarea").send_keys(
        "Cash+Cheque")

    # 输入发运起始地
    inputbox = driver.find_element_by_xpath(
        ".//*[@id='app']/div[2]/div[2]/div/div[1]/div[2]/div[1]/form/div[3]/div[5]/div[2]/div[3]/div/div/div[1]/input")
    inputbox.clear()
    inputbox.send_keys(u"东营")

    # 输入目的地
    inputbox = driver.find_element_by_xpath(
        ".//*[@id='app']/div[2]/div[2]/div/div[1]/div[2]/div[1]/form/div[3]/div[5]/div[3]/div[3]/div/div/div[1]/textarea")
    inputbox.clear()
    inputbox.send_keys(u"青岛")
    time.sleep(0.5)

    # 输入项目背景描述
    inputbox = driver.find_element_by_xpath(
        ".//*[@id='app']/div[2]/div[2]/div/div[1]/div[2]/div[1]/form/div[3]/div[6]/div/div/textarea")
    inputbox.clear()
    inputbox.send_keys(u"项目背景描述1")
    time.sleep(0.5)

    # 输入报价备注
    inputbox = driver.find_element_by_xpath(
        ".//*[@id='app']/div[2]/div[2]/div/div[1]/div[2]/div[1]/form/div[3]/div[7]/div/div/textarea")
    inputbox.clear()
    inputbox.send_keys(u"报价备注2")
    time.sleep(0.5)

    # 输入客户检验要求
    inputbox = driver.find_element_by_xpath(
        ".//*[@id='app']/div[2]/div[2]/div/div[1]/div[2]/div[1]/form/div[3]/div[8]/div/div/textarea")
    inputbox.clear()
    inputbox.send_keys(u"客户检验要求3")
    time.sleep(0.5)

    # 选择贸易术语
    select = driver.find_element_by_xpath(
        ".//*[@id='app']/div[2]/div[2]/div/div[1]/div[2]/div[1]/form/div[3]/div[5]/div[1]/div[1]/div/div/div/div[1]/input")
    time.sleep(1)
    # lis = driver.find_elements_by_xpath("//ul[@class='el-scrollbar__view el-select-dropdown__list']/li")
    #
    # for li in lis:
    #     if "CIF" in li.text:
    #         li.click()
    #         break
    # time.sleep(2)
    select.click()
    select.send_keys(Keys.UP)
    select.send_keys(Keys.ENTER)
    time.sleep(0.5)

    # 选择运输方式
    select = driver.find_element_by_xpath(
        ".//*[@id='app']/div[2]/div[2]/div/div[1]/div[2]/div[1]/form/div[3]/div[5]/div[1]/div[2]/div/div/div/div[1]/input")
    time.sleep(1)
    select.click()
    select.send_keys(Keys.UP)
    select.send_keys(Keys.ENTER)
    time.sleep(0.5)

    # 选择起运港
    select = driver.find_element_by_xpath(
        ".//*[@id='app']/div[2]/div[2]/div/div[1]/div[2]/div[1]/form/div[3]/div[5]/div[2]/div[1]/div/div/div/div[1]/input")
    time.sleep(1)
    select.click()
    for i in range(1, 6):
        select.send_keys(Keys.UP)
    select.send_keys(Keys.ENTER)
    time.sleep(0.5)

    # 选择目的港
    select = driver.find_element_by_xpath(
        ".//*[@id='app']/div[2]/div[2]/div/div[1]/div[2]/div[1]/form/div[3]/div[5]/div[3]/div[1]/div/div/div/div[1]/input")
    time.sleep(1)
    select.click()
    for i in range(1, 8):
        select.send_keys(Keys.UP)
    select.send_keys(Keys.ENTER)
    time.sleep(0.5)

    # 暂存询单
    # button = driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[2]/div/div[1]/div[2]/div[1]/form/div[1]/div[1]/button[1]")
    # button.click()
    # print"暂存成功"
    # time.sleep(0.5)

    # 提交方案中心
    button = driver.find_element_by_xpath(
        ".//*[@id='app']/div[2]/div[2]/div/div[1]/div[2]/div[1]/form/div[1]/div[1]/button[3]")
    button.click()
    time.sleep(2)


testTime = int(config.get("bossinquiry", "TESTTIME"))
url = config.get("bossinquiry", "URL")
mylogger.info("The test server url is: %s" % url)
mylogger.info("TestTask : bossinquiry")

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
    manInquiry();

    # 新增询单
    newInquiry();

    # 退出
    logout();

    mylogger.info("Test Passed= %s" % i)
    # print time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), "Test Passed =", i

driver.quit()

mylogger.info("All Test Passed")