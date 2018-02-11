#!/usr/bin/env python2
#  coding=utf-8
# portal基类  __author__ = 'kayiyo'

from framework import portal_base

portal = portal_base.PortalBase()


class NewRfq(object):
    def new_rfq(self):
        # 新增询单
        portal.switch_window(xpath="html/body/div[4]/div[3]/div[2]/div[3]/a")
        # for num in range(1, 50):
        #     portal.click_button(xpath="//*[@id='inquiry_right']/div[2]/ul/li[2]/div/span[2]")
        portal.send_key(key1=50, xpath=".//*[@id='inquiry_right']/div[2]/ul/li[2]/div/input")
        portal.click_button(xpath=".//*[@id='inquiry_left']/div[2]/ul/li[1]/input")
        portal.click_button(xpath=".//*[@id='inquiry']/ul[2]/li/a")
        portal.switch_alert()
        portal.click_button(xpath="/html/body/div[7]/div[2]/div/a[1]")
        for num in range(1, 10):
            portal.click_button(xpath=".//*[@id='trsku']/tr[1]/td[6]/div/a[2]")
        portal.click_button(xpath=".//*[@id='trsku']/tr[2]/td[7]/a")
        portal.send_key(key1="Other requirements1, Other requirements2, Other requirements3",
                        xpath=".//*[@id='quick_inquiry']/div[2]/fieldset[1]/textarea")
        portal.upload_file(file1="d:\\1fortest\word.docx", xpath="//*[@id='file']")
        portal.send_key(key1="2019-03-21", xpath=".//*[@id='quick_inquiry']/div[2]/fieldset[3]/div[5]/div/input")
        portal.key_tab(xpath=".//*[@id='quick_inquiry']/div[2]/fieldset[3]/div[5]/div/input")
        portal.select_text(text="CIF", xpath=".//*[@id='TradeTerms']")
        portal.select_text(text="Mali", xpath=".//*[@id='country_02']")
        portal.select_text(text="CAD", xpath=".//*[@id='currency']")
        portal.send_key(key1="Cash", xpath=".//*[@id='quick_inquiry']/div[2]/fieldset[4]/div[2]/div/input")
        portal.move(".//*[@id='contact_zipcode']")
        portal.moveto(xpath="//*[@id='contact_zipcode']", xoffset=80, yoffset=55)
