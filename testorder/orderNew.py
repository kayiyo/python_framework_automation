#!/usr/bin/env python2
# coding=utf-8

import ConfigParser
import os.path
from framework import portal_base
from framework import order_new
from framework.logger import Logger

project = "order"  # 用于读取配置文件和日志输出控制
mylogger = Logger(logger=project + "newLog").getlog()
file_path = os.path.dirname(os.path.abspath('.')) + '/config/configuration.ini'
config = ConfigParser.ConfigParser()
config.read(file_path)
order = portal_base.PortalBase()
orderNew = order_new.NewOrder()

url = config.get(project, "url")        # 读取配置文件
user = config.get(project, "user")
pw = config.get(project, "pw")
code = config.get(project, "code")
testtime = int(config.get(project, "testtime"))

mylogger.info("The test server url is: %s" % url)
mylogger.info("TestTask : " + project + "new")
# mylogger.info("Test Time : %s" % testtime)

order.load_web(url)  # 浏览器载入url

order.input_username(user, xpath=".//*[@id='username']")  # 用户名

order.input_password(pw, xpath=".//*[@id='password']")  # 密码

order.login1()  # 登录系统

orderNew.new_order()

order.logout1()  # 退出系统

order.quit_web()  # 退出浏览器

mylogger.info("All Test Done!")
