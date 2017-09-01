# -*- coding:utf-8 -*-

import ConfigParser
import os.path
from selenium import webdriver
from framework.logger import Logger

logger = Logger(logger="useConfig").getlog()

config = ConfigParser.ConfigParser()
# file_path = os.path.dirname(os.getcwd()) + '/config/config.ini'
file_path = os.path.dirname(os.path.abspath('.')) + '/config/configuration.ini'
config.read(file_path)

url = config.get("bossQuote", "URL")
logger.info("url is: %s" % url)
user = config.get("bossQuote", "USER")
logger.info("user is: %s" % user)
pw = config.get("bossQuote", "PW")
logger.info("pw is: %s" % pw)
testtime = config.get("bossQuote", "TESTTIME")
logger.info("testtime is: %s" % testtime)

url = config.get("bossinquiry", "URL")
logger.info("url is: %s" % url)
user = config.get("bossinquiry", "USER")
logger.info("user is: %s" % user)
pw = config.get("bossinquiry", "PW")
logger.info("pw is: %s" % pw)
testtime = config.get("bossinquiry", "TESTTIME")
logger.info("testtime is: %s" % testtime)