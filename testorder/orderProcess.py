#!/usr/bin/env python2
# coding=utf-8

import ConfigParser
import os.path

from Order_delivery_system import order_new
from Order_delivery_system import project_manager
from Order_delivery_system import project_execute
from framework import portal_base
from framework.logger import Logger

project = "orderProcess"  # 用于读取配置文件和日志输出控制
mylogger = Logger(logger=project + "Log").getlog()
file_path = os.path.dirname(os.path.abspath('.')) + '/config/config_order.ini'
config = ConfigParser.ConfigParser()
config.read(file_path)
order = portal_base.PortalBase()
orderNew = order_new.NewOrder()
projectManager = project_manager.ProjectManager()
projectExexute = project_execute.ProjectExecute()

url = config.get("order", "url")        # 读取配置文件
testtime = int(config.get("order", "testtime"))

mylogger.info("The test server url is: %s" % url)
mylogger.info("TestTask : " + project)
mylogger.info("Test Time : %s" % testtime)

order.load_web(url)  # 浏览器载入url

for num in range(1, testtime+1):
    # 新建订单
    mylogger.info(u"新建订单执行中")
    process = "ordernew"
    user = config.get(process, "user")
    pw = config.get(process, "pw")
    order.input_username(user, xpath=".//*[@id='username']")  # 用户名
    order.input_password(pw, xpath=".//*[@id='password']")  # 密码
    order.login1()  # 登录系统
    orderNew.new_order()
    order.logout1()  # 退出系统
    mylogger.info(u"新建订单执行完毕")

    # 项目管理
    mylogger.info(u"项目管理执行中")
    process = "projectmanage"
    user = config.get(process, "user")
    pw = config.get(process, "pw")
    order.input_username(user, xpath=".//*[@id='username']")  # 用户名
    order.input_password(pw, xpath=".//*[@id='password']")  # 密码
    order.login1()  # 登录系统
    projectManager.project_manager()
    order.logout1()  # 退出系统
    mylogger.info(u"项目管理执行完毕")

    # 项目办理
    mylogger.info(u"项目办理执行中")
    process = "projectexecute"
    user = config.get(process, "user")
    pw = config.get(process, "pw")
    order.input_username(user, xpath=".//*[@id='username']")  # 用户名
    order.input_password(pw, xpath=".//*[@id='password']")  # 密码
    order.login1()  # 登录系统
    projectExexute.project_execute()
    order.logout1()  # 退出系统
    mylogger.info(u"项目办理执行完毕")

    mylogger.info("Test Finished : %s" % num)

order.quit_web()  # 退出浏览器
mylogger.info("All Test Done!")
