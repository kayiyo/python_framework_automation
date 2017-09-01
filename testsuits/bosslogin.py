# coding=utf-8

import time
from selenium import webdriver

driver = webdriver.Chrome()
#driver.set_window_size(800,600)
driver.maximize_window()
driver.implicitly_wait(6)


# localurl = "http://172.18.18.196:88"
url = "http://172.18.18.196:8089"

# User = "Brucejet"
# User = "Victortony159@outlook.com"
User = "900000"
# PW = "Bruce12345"
PW = "Qa123"
#CODE = "test"


def load():
	driver.get(url)
	# driver.find_element_by_xpath("html/body/div[1]/div[1]/ul/li[1]/a").click()
	time.sleep(2)

def inputUsername():
    driver.find_element_by_xpath(".//*[@id='app']/div/form/div[1]/div/div[1]/input").clear()
    driver.find_element_by_xpath(".//*[@id='app']/div/form/div[1]/div/div[1]/input").send_keys(User)
    time.sleep(1)

def inputPassword():
    driver.find_element_by_xpath(".//*[@id='app']/div/form/div[2]/div/div/input").clear()
    driver.find_element_by_xpath(".//*[@id='app']/div/form/div[2]/div/div/input").send_keys(PW)
    time.sleep(1)

# def inputCode():
#     driver.find_element_by_xpath(".//*[@id='verificationCode']").clear()
#     driver.find_element_by_xpath(".//*[@id='verificationCode']").send_keys(CODE)

def login():
    driver.find_element_by_xpath(".//*[@id='app']/div/form/div[4]/div/button").click()

def logout():
    driver.find_element_by_xpath(".//*[@id='app']/div[1]/div[2]/p/span").click()
    time.sleep(2)
    driver.switch_to_alert()
    driver.find_element_by_xpath("html/body/div[2]/div/div[3]/button[2]").click()
    time.sleep(2)



print"TestURL is", url
for i in range(1, 11):
        # 进入登录界面
        load();

        # 输入用户名
        inputUsername();

        # 输入密码
        inputPassword();

        # 输入验证码
        # inputCode();

        # 登录
        login();




        # 退出
        logout();

        print time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),"Test Passed =", i

driver.quit()

print"All Test Passed"