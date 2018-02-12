#!/usr/bin/env python2
#  coding=utf-8
# order采购申请  __author__ = 'kayiyo'

from framework import portal_base
import time
import random

order = portal_base.PortalBase()


class PurchaseRequest(object):
    def purchase_request(self):
        order_time = time.strftime("%Y%m%d%H%M%S", time.localtime())         # 所有用到的编号
        order_xmh = "XMH" + order_time + "ddgl"                           # 项目名称
        order_xmgl_bz = "XMGLBZ" + order_time + "ddgl-XMJL"                      # 项目备注

        # order.click_button(".//*[@id='sider']/div/div[2]/div[1]/div[1]")       # 项目管理
        order.link_text(u"项目列表")        # 订单列表
        time.sleep(5)
        order.send_key(key1="XMMC",
                       xpath=".//*[@id='project_list']/div[1]/div[2]/div/div[2]/span/input[1]")     # 项目名称搜索
        order.select(key1=3,
                     xpath=".//*[@id='project_list']/div[3]/div[1]/div/div[2]/span/input[1]")     # 项目状态正常执行搜索
        order.link_text(u"搜索")      # 搜索
        time.sleep(3)
        order.link_text(u"生成采购申请")      # 办理
        time.sleep(5)

        xpath = ".//*/div[1]/div[2]/div/div[2]/div[2]/div/div[2]/span/input[1]"
        order.click_button(xpath)  # 下发日期
        order.key_enter(xpath)

        # 项目号
        order.send_key(key1=order_xmh,
                       xpath=".//*/div[1]/div[2]/div/div[1]/div[1]/div/div[2]/span/input[1]")
        order.select(key1=2,  # 贸易方式
                     xpath=".//*/div[1]/div[2]/div/div[3]/div[1]/div/div[2]/span/input[1]")
        order.select(key1=2,  # 是否厂家直接发货
                     xpath=".//*/div[1]/div[2]/div/div[4]/div[1]/div/div[2]/span/input[1]")
        order.send_key(key1=u"东营",      #交付地点
                       xpath=".//*/div[1]/div[2]/div/div[4]/div[2]/div/div[2]/span/input[1]")
        order.send_key(key1=u"客户文件要求无",  # 客户文件要求
                       xpath=".//*/div[1]/div[2]/div/div[5]/div/div/div[2]/span/input[1]")

        # 商品信息
        order.select(key1=2,  # 产品分类
                     xpath=".//*/td[2]/div/span/input[1]")

        time.sleep(1)
        order.link_text(u"提交")
        time.sleep(3)
        order.link_text(u"确定")
        time.sleep(3)
        order.link_text(u"确定")
        time.sleep(3)

        # for num in range(1, 2000):
        #     try:
        #         order.click_button(
        #             ".//*[@id='update_project_*']/div[1]/div[2]/div/div[1]/div[1]/div/div[2]/span/input[1]")
        #     except Exception as e:
        #         pass
        #     else:
        #         xpath = ".//*/div[1]/div[2]/div/div[1]/div[1]/div/div[2]/span/input[1]"
        #         order.click_button(xpath)  # 项目开始时间