#!/usr/bin/env python2
#  coding=utf-8
# order出口通知  __author__ = 'kayiyo'

from framework import portal_base
import time
import random

order = portal_base.PortalBase()


class ExportNotice(object):
    def export_notice(self, order_xsht):
        order_time = time.strftime("%Y%m%d%H%M%S", time.localtime())         # 所有用到的编号

        # order.click_button(".//*[@id='sider']/div/div[2]/div[1]/div[1]")       # 项目管理
        order.link_text(u"订单列表")        # 订单列表
        time.sleep(5)
        order.send_key(key1=order_xsht,
                       xpath=".//*[@id='order_list']/div[1]/div[1]/div/div[2]/span/input[1]")     # 销售合同号搜索
        order.select(key1=4,
                     xpath=".//*[@id='order_list']/div[3]/div[2]/div/div[2]/span/input[1]")     # 项目状态未执行搜索
        order.link_text(u"搜索")      # 搜索
        time.sleep(3)
        order.link_text(u"生成出口通知单")      # 生成出口通知单
        time.sleep(5)

        xpath = ".//*/div[2]/div[2]/div/div[3]/div[1]/div/div[2]/span/input[1]"
        order.click_button(xpath)  # 要求物流到货日期
        order.key_enter(xpath)

        xpath = ".//*/div[2]/div[2]/div/div[2]/div[2]/div/div[2]/span/input[1]"
        order.click_button(xpath)  # 填表日期
        order.key_enter(xpath)

        xpath = ".//*/div[2]/div[2]/div/div[3]/div[2]/div/div[2]/span/input[1]"
        order.click_button(xpath)  # 市场订舱要求日期
        order.key_enter(xpath)

        # 商品数量
        read_num = order.read_info(xpath=
                                  ".//*[@id='datagrid-row-r4-2-0']/td[4]/div")
        order.send_key(key1 = int(read_num),
                       xpath=".//*[@id='datagrid-row-r4-2-0']/td[9]/div/span/input[1]")

        # # 备注信息
        # order.send_key(key1=order_xmgl_bz,
        #                xpath=".//*/div[6]/div[2]/div/div/div/div[2]/span/textarea")
        time.sleep(1)
        order.link_text(u"提交物流")
        time.sleep(3)
        order.link_text(u"确定")
        time.sleep(3)
