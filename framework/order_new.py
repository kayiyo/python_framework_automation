#!/usr/bin/env python2
#  coding=utf-8
# order新建基类  __author__ = 'kayiyo'

from framework import portal_base
import time
import random

order = portal_base.PortalBase()


class NewOrder(object):
    def new_order(self):
        order_time = time.strftime("%Y%m%d%H%M%S", time.localtime())         # 所有用到的编号
        order_po = "PO" + order_time + "ddgl"                                # PO号
        order_kjxy = "KJXY" + order_time + "ddgl"                            # 框架协议号
        order_xsht = "XSHT" + order_time + "ddgl"                            # 销售合同号
        order_hwxsht = "HWXSHT" + order_time + "ddgl"                        # 海外销售合同号
        order_wlbjd = "WLBJD" + order_time + "ddgl"                          # 物流报价单号
        # order.click_button(xpath=".//*[@id='sider']/div/div[1]/div[1]/div[1]")      # 订单管理
        order.click_button(xpath=".//*[@id='sider']/div/div[1]/div[2]/ul/li/a")     # 订单列表
        time.sleep(3)
        order.link_text(u"新建")
        # order.click_button(xpath=".//*[@id='orderList']/div/div[1]/div/div[1]/a[1]/span/span")      # 新建订单
        time.sleep(3)
        order.send_key(key1=order_po,
                       xpath=".//*[@id='tt']/div[1]/div[2]/div/div[2]/div[2]/div/div[2]/span/input[1]")
        order.send_key(key1=order_kjxy,
                       xpath=".//*[@id='tt']/div[1]/div[2]/div/div[1]/div[2]/div/div[2]/span/input[1]")
        order.send_key(key1=order_xsht,
                       xpath=".//*[@id='tt']/div[1]/div[2]/div/div[1]/div[1]/div/div[2]/span/input[1]")
        order.send_key(key1=order_hwxsht,
                       xpath=".//*[@id='tt']/div[1]/div[2]/div/div[2]/div[1]/div/div[2]/span/input[1]")
        order.send_key(key1=order_wlbjd,
                       xpath=".//*[@id='tt']/div[1]/div[2]/div/div[3]/div[1]/div/div[2]/span/input[1]")
        order.select_list(key1=3,
                          xpath=".//*[@id='tt']/div[1]/div[2]/div/div[3]/div[2]/div/div[2]/span/input[1]")      # 订单类型
        order.click_button(
            xpath=".//*[@id='tt']/div[1]/div[2]/div/div[4]/div[1]/div/div[2]/span/input[1]")     # 签约日期
        order.key_enter(xpath=".//*[@id='tt']/div[1]/div[2]/div/div[4]/div[1]/div/div[2]/span/input[1]")
        order.click_button(
            xpath=".//*[@id='tt']/div[1]/div[2]/div/div[4]/div[2]/div/div[2]/span/input[1]")        # 合同交货日期
        order.key_enter(xpath=".//*[@id='tt']/div[1]/div[2]/div/div[4]/div[2]/div/div[2]/span/input[1]")
        order.select_list(key1=20,
                          xpath=".//*[@id='tt']/div[1]/div[2]/div/div[5]/div[1]/div/div[2]/span/input[1]")  # 签约主体公司
        order.click_button(xpath=".//*[@id='tt']/div[1]/div[2]/div/div[5]/div[2]/div/div[2]/span/a/span/span")  # 市场经办人
        # order.switch_alert()
        time.sleep(3)
        order.send_key(key1="10001",
                       xpath=".//*[@id='dialog']/div/div[1]/div/form/table/tbody/tr/td[1]/span/input[1]")
        order.link_text(u" 搜 索 ")
        xpath = ".//*[@id='dialog']/div/div[2]/div/div/div/div[1]/div[2]/div[1]/div/table/tbody/tr/td[2]/div/span[1]"
        order.move(xpath)
        order.moveto(xpath, xoffset=38, yoffset=38)
        time.sleep(1)
        order.link_text("确定")
        time.sleep(1)
        # 执行分公司
        order.click_button(".//*[@id='tt']/div[1]/div[2]/div/div[6]/div[1]/div/div[2]/span/a/span")  # 执行分公司
        # order.switch_alert()
        time.sleep(3)
        order.link_text(u" 清 空 ")
        order.send_key(key1=u"波兰办事处",
                       xpath=".//*[@id='dialog']/div/div[1]/div/form/table/tbody/tr/td[1]/span/input[1]")
        order.link_text(u" 搜 索 ")
        xpath = ".//*[@id='dialog']/div/div[2]/div/div/div/div/div[2]/div[1]/div/table/tbody/tr/td/div/span[1]"
        order.move(xpath)
        order.moveto(xpath, xoffset=38, yoffset=38)
        time.sleep(1)
        order.link_text("确定")
        time.sleep(1)

        order.select_list(key1=20,
                          xpath=".//*[@id='tt']/div[1]/div[2]/div/div[7]/div[1]/div/div[2]/span/input[1]")      # 分销部

        order.select_list(key1=20,
                          xpath=".//*[@id='tt']/div[1]/div[2]/div/div[7]/div[2]/div/div[2]/span/input[1]")      # 国家

        # CRM客户代码
        button = ".//*[@id='tt']/div[1]/div[2]/div/div[8]/div[1]/div/div[2]/span/a/span"
        search_key = "CRM"
        search = ".//*[@id='dialog']/div/div[1]/div/form/table/tbody/tr/td[2]/span/input[1]"
        move = ".//*[@id='dialog']/div/div[2]/div/div/div/div[1]/div[2]/div[1]/div/table/tbody/tr/td[1]/div/span[1]"
        order.choose(button, search_key, search, move, wait=20)

        order.select_list(key1=5,
                          xpath=".//*[@id='tt']/div[1]/div[2]/div/div[8]/div[2]/div/div[2]/span/input[1]")      # 客户类型
        # 回款责任人
        button = ".//*[@id='tt']/div[1]/div[2]/div/div[9]/div[1]/div/div[2]/span/a/span"
        search_key = "001448"
        search = ".//*[@id='dialog']/div/div[1]/div/form/table/tbody/tr/td[1]/span/input[1]"
        move = ".//*[@id='dialog']/div/div[2]/div/div/div/div[1]/div[2]/div[1]/div/table/tbody/tr/td[1]/div"
        order.choose(button, search_key, search, move)

        # 事业部
        button = ".//*[@id='tt']/div[1]/div[2]/div/div[9]/div[2]/div/div[2]/span/a/span"
        search_key = u"钻装事业部"
        search = ".//*[@id='dialog']/div/div[1]/div/form/table/tbody/tr/td[1]/span/input[1]"
        move = ".//*[@id='dialog']/div/div[2]/div/div/div/div/div[2]/div[1]/div/table/tbody/tr/td/div/span[1]"
        order.choose(button, search_key, search, move)

        # 商务技术经办人
        button = ".//*[@id='tt']/div[1]/div[2]/div/div[10]/div[1]/div/div[2]/span/a/span"
        search_key = "011016"
        search = ".//*[@id='dialog']/div/div[1]/div/form/table/tbody/tr/td[1]/span/input[1]"
        move = ".//*[@id='dialog']/div/div[2]/div/div/div/div[1]/div[2]/div[1]/div/table/tbody/tr/td[1]/div/span[1]"
        order.choose(button, search_key, search, move)

        order.select_list(key1=4,
                          xpath=".//*[@id='tt']/div[1]/div[2]/div/div[10]/div[2]/div/div[2]/span/input[1]")     # 授信情况
        order.select_list(key1=20,
                          xpath=".//*[@id='tt']/div[1]/div[2]/div/div[11]/div[1]/div/div[2]/span/input[1]")     # 是否预投
        order.select_list(key1=20,
                          xpath=".//*[@id='tt']/div[1]/div[2]/div/div[11]/div[2]/div/div[2]/span/input[1]") # 是否融资项目
        order.select_list(key1=8,
                          xpath=".//*[@id='tt']/div[1]/div[2]/div/div[12]/div[1]/div/div[2]/span/input[1]")     # 贸易术语
        order.select_list(key1=7,
                          xpath=".//*[@id='tt']/div[1]/div[2]/div/div[12]/div[2]/div/div[2]/span/input[1]")     # 运输方式
        order.select_list(key1=120,
                          xpath=".//*[@id='tt']/div[1]/div[2]/div/div[14]/div[2]/div/div[2]/span/input[1]")     # 目的国
        order.send_key(key1=(random.randint(1, 10) * 1000000),
                       xpath=".//*[@id='tt']/div[5]/div[2]/div[1]/div[1]/div/div[2]/span/input[1]")     # 合同总价
        order.select_list(key1=3,
                          xpath=".//*[@id='tt']/div[5]/div[2]/div[1]/div[1]/div/div[3]/span/input[1]")  # 币种
        order.select_list(key1=3,
                          xpath=".//*[@id='tt']/div[5]/div[2]/div[2]/div[1]/div/div[2]/span/input[1]")      # 收款方式
        order.select_list(key1=3,
                          xpath=".//*[@id='tt']/div[5]/div[2]/div[1]/div[2]/div/div[2]/span/input[1]")     # 是否含税

        time.sleep(5)
        order.link_text(u"提交立项")
        time.sleep(3)
        order.link_text(u"确定")
        time.sleep(3)