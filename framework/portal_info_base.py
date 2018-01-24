#!/usr/bin/env python2
#  coding=utf-8
# portal基类  __author__ = 'kayiyo'

from framework import portal_base

portal = portal_base.PortalBase()


class PortalInfo(object):

    def info_user(self):
        info_user = portal.read_info(xpath="html/body/div[2]/div/div[2]/p[1]/a")
        return info_user

    def hot_key(self):
        for num in range(1, 9):
            num = bytes(num)
            portal.click_button(xpath="html/body/div[2]/div/div[1]/ul/li[" + num + "]/a")
            info1 = portal.read_info("html/body/div[4]/div[3]/div[1]/i[1]")
            info2 = portal.read_info("html/body/div[4]/div[3]/div[1]/i[2]")
            info3 = portal.read_info("html/body/div[2]/div/div[1]/ul/li[" + num + "]/a")
            hot_key = "[" + num + "] " + info1 + " Products," + info2 + " Commodities found for ' " + info3 + " '"
            # info = str(portal.read_info("html/body/div[4]/div[3]/div[1]"))
            # info.strip()
            # info.replace("\n", "")
        return hot_key

    def first_hot(self):
        for num in range(1, 4):
            num = bytes(num)
            portal.click_button(xpath="html/body/div[3]/p/a[" + num + "]")
            info1 = portal.read_info("html/body/div[4]/div[3]/div[1]/i[1]")
            info2 = portal.read_info("html/body/div[4]/div[3]/div[1]/i[2]")
            info3 = portal.read_info("html/body/div[3]/p/a[" + num + "]")
            first_hot = "[" + num + "] " + info1 + " Products," + info2 + " Commodities found for ' " + info3 + " '"
        return first_hot
