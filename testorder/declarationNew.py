#!/usr/bin/env python2
# coding=utf-8

import ConfigParser
import os.path

from Order_delivery_system import declaration_new
from framework import portal_base
from framework.logger import Logger

project = "declarationNew"  # 用于读取配置文件和日志输出控制
mylogger = Logger(logger=project + "Log").getlog()
file_path = os.path.dirname(os.path.abspath('.')) + '/config/config_order.ini'
config = ConfigParser.ConfigParser()
config.read(file_path)
order = portal_base.PortalBase()
declarationNew = declaration_new.DeclarationNew()

url = config.get(project, "url")        # 读取配置文件
user = config.get(project, "user")
pw = config.get(project, "pw")
# code = config.get(project, "code")
# testtime = int(config.get(project, "testtime"))

mylogger.info("The test server url is: %s" % url)
mylogger.info("TestTask : " + project + "new")
# mylogger.info("Test Time : %s" % testtime)

order.load_web(url)  # 浏览器载入url

# for num in range(1, testtime+1):
#     order.input_username(user, xpath=".//*[@id='username']")  # 用户名
#     order.input_password(pw, xpath=".//*[@id='password']")  # 密码
#     order.login1()  # 登录系统
#     declarationNew.declaration_new()
#     order.logout1()  # 退出系统
#     mylogger.info("Test Finished : %s" % num)
# order.quit_web()  # 退出浏览器
# mylogger.info("All Test Done!")

order.input_username(user, xpath=".//*[@id='username']")  # 用户名
order.input_password(pw, xpath=".//*[@id='password']")  # 密码
order.login1()  # 登录系统
declarationNew.declaration_new()
