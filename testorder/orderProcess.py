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

    order_process_list = ['orderNew',
                     'projectManager',
                     'projectExecute',
                     'exportNotice',
                     'purchaseRequest',
                     'purchaseOrder',
                     'declarationNew',
                     'checkIn',
                     'operationIn',
                     'shipmentNotice',
                     'checkSubmit',
                     'checkOut',
                     'operationOut',
                     'logisticsTrack',
                     'financialPayment',
                     ]
    for order_process in order_process_list:
        mylogger.info(order_process + " is executing. Please wait...")
        user = config.get(order_process, "user")
        pw = config.get(order_process, "pw")
        order.input_username(user, xpath=".//*[@id='username']")  # 用户名
        order.input_password(pw, xpath=".//*[@id='password']")  # 密码
        order.login1()  # 登录系统
        if order_process == 'orderNew':                     # 1新建订单
            order_xsht = orderNew.new_order()
            mylogger.info("OrderXSHT NO:" + order_xsht)
        elif order_process == 'projectManager':             # 2管理项目
            projectManager.project_manager(order_xsht)
        elif order_process == 'projectExecute':             # 3执行项目
            projectExecute.project_execute(order_xsht)
        elif order_process == 'exportNotice':               # 4出口通知
            exportNotice.export_notice(order_xsht)
        elif order_process == 'purchaseRequest':            # 5采购申请
            order_xmh = purchaseRequest.purchase_request(order_xsht)
            mylogger.info("OrderXMH NO:" + order_xmh)
        elif order_process == 'purchaseOrder':              # 6采购订单
            order_xmh = order_xmh
            purchaseOrder.purchase_order(order_xmh)
        elif order_process == 'declarationNew':             # 7新增报检单
            declarationNew.declaration_new(order_xsht)
        elif order_process == 'checkIn':                    # 8入库质检
            checkIn.check_in(order_xsht)
        elif order_process == 'operationIn':                # 9办理入库
            operationIn.operation_in(order_xsht)
        elif order_process == 'shipmentNotice':             # 10新建看货通知
            shipmentNotice.shipment_notice()
        elif order_process == 'checkSubmit':                # 11提交质检
            checkSubmit.check_submit(order_xsht)
        elif order_process == 'checkOut':                   # 12出库质检
            checkOut.check_out(order_xsht)
        elif order_process == 'operationOut':               # 13办理出库
            operationOut.operation_out(order_xsht)
        elif order_process == 'logisticsTrack':             # 14物流跟踪
            logisticsTrack.logistics_track(order_xsht)
        elif order_process == 'financialPayment':           # 15财务收款
            financialPayment.financial_payment(order_xsht)
        order.logout1()  # 退出系统
        mylogger.info(order_process + " completed")

    mylogger.info("Test Finished : %s" % num)

order.quit_web()  # 退出浏览器
mylogger.info("All Test Done!")
