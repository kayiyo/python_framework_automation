#!/usr/bin/env python2
# coding=utf-8

import ConfigParser
import os.path

from Order_delivery_system import order_new
from Order_delivery_system import project_manager
from Order_delivery_system import project_execute
from Order_delivery_system import export_notice
from Order_delivery_system import purchase_request
from Order_delivery_system import purchase_order
from Order_delivery_system import declaration_new
from Order_delivery_system import check_in
from Order_delivery_system import operation_in
from Order_delivery_system import shipment_notice
from Order_delivery_system import check_submit
from Order_delivery_system import check_out
from Order_delivery_system import operation_out
from Order_delivery_system import logistics_track
from Order_delivery_system import financial_payment
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
projectExecute = project_execute.ProjectExecute()
exportNotice = export_notice.ExportNotice()
purchaseRequest = purchase_request.PurchaseRequest()
purchaseOrder = purchase_order.PurchaseOrder()
declarationNew = declaration_new.DeclarationNew()
checkIn = check_in.CheckIn()
operationIn = operation_in.OperationIn()
shipmentNotice = shipment_notice.ShipmentNotice()
checkSubmit = check_submit.CheckSubmit()
checkOut = check_out.CheckOut()
operationOut = operation_out.OperationOut()
logisticsTrack = logistics_track.LogisticsTrack()
financialPayment = financial_payment.FinancialPayment()

url = config.get("order", "url")        # 读取配置文件
testtime = int(config.get("order", "testtime"))

mylogger.info("The test server url is: %s" % url)
mylogger.info("TestTask : " + project)
mylogger.info("Test Time : %s" % testtime)

order.load_web(url)  # 浏览器载入url

for num in range(1, testtime+1):
    mylogger.info(u"新建订单执行中")   # 1新建订单
    process = "orderNew"
    user = config.get(process, "user")
    pw = config.get(process, "pw")
    order.input_username(user, xpath=".//*[@id='username']")  # 用户名
    order.input_password(pw, xpath=".//*[@id='password']")  # 密码
    order.login1()  # 登录系统
    orderNew.new_order()
    order.logout1()  # 退出系统
    mylogger.info(u"新建订单执行完毕")

    mylogger.info(u"管理项目执行中")   # 2管理项目
    process = "projectManager"
    user = config.get(process, "user")
    pw = config.get(process, "pw")
    order.input_username(user, xpath=".//*[@id='username']")  # 用户名
    order.input_password(pw, xpath=".//*[@id='password']")  # 密码
    order.login1()  # 登录系统
    projectManager.project_manager()
    order.logout1()  # 退出系统
    mylogger.info(u"管理项目执行完毕")

    mylogger.info(u"执行项目执行中")   # 3执行项目
    process = "projectExecute"
    user = config.get(process, "user")
    pw = config.get(process, "pw")
    order.input_username(user, xpath=".//*[@id='username']")  # 用户名
    order.input_password(pw, xpath=".//*[@id='password']")  # 密码
    order.login1()  # 登录系统
    projectExecute.project_execute()
    order.logout1()  # 退出系统
    mylogger.info(u"执行项目执行完毕")

    mylogger.info(u"出口通知执行中")   # 4出口通知
    process = "exportNotice"
    user = config.get(process, "user")
    pw = config.get(process, "pw")
    order.input_username(user, xpath=".//*[@id='username']")  # 用户名
    order.input_password(pw, xpath=".//*[@id='password']")  # 密码
    order.login1()  # 登录系统
    exportNotice.export_notice()
    order.logout1()  # 退出系统
    mylogger.info(u"出口通知执行完毕")

    mylogger.info(u"采购申请执行中")   # 5采购申请
    process = "purchaseRequest"
    user = config.get(process, "user")
    pw = config.get(process, "pw")
    order.input_username(user, xpath=".//*[@id='username']")  # 用户名
    order.input_password(pw, xpath=".//*[@id='password']")  # 密码
    order.login1()  # 登录系统
    purchaseRequest.purchase_request()
    order.logout1()  # 退出系统
    mylogger.info(u"采购申请执行完毕")

    mylogger.info(u"采购订单执行中")   # 6采购订单
    process = "purchaseOrder"
    user = config.get(process, "user")
    pw = config.get(process, "pw")
    order.input_username(user, xpath=".//*[@id='username']")  # 用户名
    order.input_password(pw, xpath=".//*[@id='password']")  # 密码
    order.login1()  # 登录系统
    purchaseOrder.purchase_order()
    order.logout1()  # 退出系统
    mylogger.info(u"采购订单执行完毕")

    mylogger.info(u"新增报检单执行中")  # 7新增报检单
    process = "declarationNew"
    user = config.get(process, "user")
    pw = config.get(process, "pw")
    order.input_username(user, xpath=".//*[@id='username']")  # 用户名
    order.input_password(pw, xpath=".//*[@id='password']")  # 密码
    order.login1()  # 登录系统
    declarationNew.declaration_new()
    order.logout1()  # 退出系统
    mylogger.info(u"新增报检单执行完毕")

    mylogger.info(u"入库质检执行中")   # 8入库质检
    process = "checkIn"
    user = config.get(process, "user")
    pw = config.get(process, "pw")
    order.input_username(user, xpath=".//*[@id='username']")  # 用户名
    order.input_password(pw, xpath=".//*[@id='password']")  # 密码
    order.login1()  # 登录系统
    checkIn.check_in()
    order.logout1()  # 退出系统
    mylogger.info(u"入库质检执行完毕")

    mylogger.info(u"办理入库执行中")   # 9办理入库
    process = "operationIn"
    user = config.get(process, "user")
    pw = config.get(process, "pw")
    order.input_username(user, xpath=".//*[@id='username']")  # 用户名
    order.input_password(pw, xpath=".//*[@id='password']")  # 密码
    order.login1()  # 登录系统
    operationIn.operation_in()
    order.logout1()  # 退出系统
    mylogger.info(u"办理入库执行完毕")

    mylogger.info(u"新建看货通知执行中") # 10新建看货通知
    process = "shipmentNotice"
    user = config.get(process, "user")
    pw = config.get(process, "pw")
    order.input_username(user, xpath=".//*[@id='username']")  # 用户名
    order.input_password(pw, xpath=".//*[@id='password']")  # 密码
    order.login1()  # 登录系统
    shipmentNotice.shipment_notice()
    order.logout1()  # 退出系统
    mylogger.info(u"新建看货通知执行完毕")

    mylogger.info(u"提交质检执行中")   # 11提交质检
    process = "checkSubmit"
    user = config.get(process, "user")
    pw = config.get(process, "pw")
    order.input_username(user, xpath=".//*[@id='username']")  # 用户名
    order.input_password(pw, xpath=".//*[@id='password']")  # 密码
    order.login1()  # 登录系统
    checkSubmit.check_submit()
    order.logout1()  # 退出系统
    mylogger.info(u"提交质检执行完毕")

    mylogger.info(u"出库质检执行中")   # 12出库质检
    process = "checkOut"
    user = config.get(process, "user")
    pw = config.get(process, "pw")
    order.input_username(user, xpath=".//*[@id='username']")  # 用户名
    order.input_password(pw, xpath=".//*[@id='password']")  # 密码
    order.login1()  # 登录系统
    checkOut.check_out()
    order.logout1()  # 退出系统
    mylogger.info(u"出库质检执行完毕")

    mylogger.info(u"办理出库执行中")   # 13办理出库
    process = "operationOut"
    user = config.get(process, "user")
    pw = config.get(process, "pw")
    order.input_username(user, xpath=".//*[@id='username']")  # 用户名
    order.input_password(pw, xpath=".//*[@id='password']")  # 密码
    order.login1()  # 登录系统
    operationOut.operation_out()
    order.logout1()  # 退出系统
    mylogger.info(u"办理出库执行完毕")

    mylogger.info(u"物流跟踪执行中")   # 14物流跟踪
    process = "logisticsTrack"
    user = config.get(process, "user")
    pw = config.get(process, "pw")
    order.input_username(user, xpath=".//*[@id='username']")  # 用户名
    order.input_password(pw, xpath=".//*[@id='password']")  # 密码
    order.login1()  # 登录系统
    logisticsTrack.logistics_track()
    order.logout1()  # 退出系统
    mylogger.info(u"物流跟踪执行完毕")

    mylogger.info(u"财务收款执行中")   # 15财务收款
    process = "financialPayment"
    user = config.get(process, "user")
    pw = config.get(process, "pw")
    order.input_username(user, xpath=".//*[@id='username']")  # 用户名
    order.input_password(pw, xpath=".//*[@id='password']")  # 密码
    order.login1()  # 登录系统
    financialPayment.financial_payment()
    order.logout1()  # 退出系统
    mylogger.info(u"财务收款执行完毕")

    mylogger.info("Test Finished : %s" % num)

order.quit_web()  # 退出浏览器
mylogger.info("All Test Done!")
