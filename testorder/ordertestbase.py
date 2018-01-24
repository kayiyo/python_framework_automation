#!/usr/bin/env python2
# coding=utf-8

import ConfigParser
import os.path
from framework import portal_base
from framework.logger import Logger

project = "order"  # 用于读取配置文件和日志输出控制
mylogger = Logger(logger=project + "newLog").getlog()
file_path = os.path.dirname(os.path.abspath('.')) + '/config/configuration.ini'
config = ConfigParser.ConfigParser()
config.read(file_path)
order = portal_base.PortalBase()

# 读取配置文件
url = config.get(project, "url")
user = config.get(project, "user")
pw = config.get(project, "pw")
code = config.get(project, "code")
testtime = int(config.get(project, "testtime"))

mylogger.info("The test server url is: %s" % url)
mylogger.info("TestTask : " + project + "new")
# mylogger.info("Test Time : %s" % testtime)

# 浏览器载入url
order.load_web(url)

# 用户名
order.input_username(user, xpath=".//*[@id='username']")

# 密码
order.input_password(pw, xpath=".//*[@id='password']")

# 登录
order.login(loginbutton="html/body/div[1]/div[3]/a/span")

for num in range(2, 11):
    num = bytes(num)
    a1 = ".//*[@id='sider']/div/div[" + num + "]/div[1]/div[1]"
    order.click_button(a1)
    info1 = order.read_info(xpath=".//*[@id='sider']/div/div[" + num + "]/div[1]/div[1]")
    info2 = order.read_info(xpath=".//*[@id='sider']/div/div[" + num + "]/div[2]/ul/li/a")
    mylogger.info(info1)
    # if info2 != "None":
    #     mylogger.info(info2)
    for num1 in range(1, 3):
        num1 = bytes(num1)
        a3 = ".//*[@id='sider']/div/div[" + num + "]/div[2]/ul/li[" + num1 + "]/a"
        order.click_button(a3)
        info3 = order.read_info(xpath=".//*[@id='sider']/div/div[" + num + "]/div[2]/ul/li[" + num1 + "]/a")
        mylogger.info(info3)

# 退出浏览器
order.quit_web()
mylogger.info("All Test Done!")
