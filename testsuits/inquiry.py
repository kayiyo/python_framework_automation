# coding=utf-8
__author__ = 'kayiyo'

import time
from selenium import webdriver

driver = webdriver.Chrome()
#driver.set_window_size(800,600)
driver.maximize_window()
driver.implicitly_wait(6)


# localurl = "http://172.18.18.196:88"

# User = "Brucejet"
User = "Victortony159@outlook.com"
PW = "Bruce12345"
CODE = "test"


def load():
	driver.get(url)
	driver.find_element_by_xpath("html/body/div[1]/div[1]/ul/li[1]/a").click()
	time.sleep(2)

def inputUsername():
    driver.find_element_by_xpath(".//*[@id='exampleInputEmail']").clear()
    driver.find_element_by_xpath(".//*[@id='exampleInputEmail']").send_keys(User)
    time.sleep(1)

def inputPassword():
    driver.find_element_by_xpath(".//*[@id='exampleInputPassword']").clear()
    driver.find_element_by_xpath(".//*[@id='exampleInputPassword']").send_keys(PW)
    time.sleep(1)

def inputCode():
    driver.find_element_by_xpath(".//*[@id='verificationCode']").clear()
    driver.find_element_by_xpath(".//*[@id='verificationCode']").send_keys(CODE)

def login():
    driver.find_element_by_xpath(".//*[@id='loginSubmit']").click()

def logout():
    driver.find_element_by_xpath("html/body/div[1]/div[1]/ul/li[2]/a").click()
    time.sleep(2)

def search():
    driver.find_element_by_xpath("html/body/div[1]/div[2]/div/div/div[1]/input").clear()
    driver.find_element_by_xpath("html/body/div[1]/div[2]/div/div/div[1]/input").send_keys("glass")
    driver.find_element_by_xpath("html/body/div[1]/div[2]/div/div/div[2]/span").click()

    # 获取当前窗口的句柄
    now_handle = driver.current_window_handle
    # print now_handle  # 输出当前获取的窗口句柄

    driver.find_element_by_xpath("html/body/div[2]/div[2]/div[2]/ul/li[1]/div/div[1]/div/a/p").click()
    time.sleep(1)

    # 获取所有窗口的句柄
    all_handles = driver.window_handles
    for handle in all_handles:
        if handle == now_handle:
            driver.close()
        elif handle != now_handle:
            # print handle  # 输出待选择的窗口句柄
            driver.switch_to_window(handle)



def add():

    driver.find_element_by_xpath(".//*[@id='inquiry_right']/div[2]/ul[1]/li[4]/div/input").clear()
    driver.find_element_by_xpath(".//*[@id='inquiry_right']/div[2]/ul[1]/li[4]/div/input").send_keys("5")
    for i in range(4):
        driver.find_element_by_xpath(".//*[@id='inquiry_right']/div[2]/ul[2]/li[4]/div/span[2]").click()
    driver.find_element_by_xpath(".//*[@id='inquiry']/ul[2]/li/a").click()
    driver.find_element_by_xpath(".//*[@id='trade']").find_element_by_xpath("//option[@value='CPT']").click()
    # driver.find_element_by_xpath(".//*[@id='trade']").find_element_by_xpath(".//*[@id='trade']/option[3]").click()
    driver.find_element_by_xpath(".//*[@id='transport']").find_element_by_xpath("//option[@value='Ocean']").click()
    driver.find_element_by_xpath(".//*[@id='country']").find_element_by_xpath("//option[@value='Australia']").click()
    driver.find_element_by_xpath(".//*[@id='port']").find_element_by_xpath("//option[@value='Sydney']").click()
    # driver.find_element_by_xpath(".//*[@id='tocountry']").find_element_by_xpath("//option[@value='Kazakhstan']").click()
    # driver.find_element_by_xpath(".//*[@id='toport']").find_element_by_xpath("//option[@value='Almaty']").click()
    driver.find_element_by_xpath(".//*[@id='destination']").send_keys("Shandong")
    driver.find_element_by_xpath(".//*[@id='edate']").send_keys("2018/7/6")
    driver.find_element_by_xpath(".//*[@id='pay-method']").send_keys("Cheque")
    driver.find_element_by_xpath(".//*[@id='lastname']").send_keys("Tony")
    # 上传附件
    # driver.find_element_by_xpath(".//*[@id='myforms']/div[1]/div/div[1]/div/div[1]/div[1]").send_keys('D:\Python\Upload\info.xlsx')
    # time.sleep(5)
    # 提交
    driver.find_element_by_xpath(".//*[@id='submit']").click()
    time.sleep(3)



print"TestURL is", url
for i in range(1, 101):
        # 进入登录界面
        load();

        # 输入用户名
        inputUsername();

        # 输入密码
        inputPassword();

        # 输入验证码
        inputCode();

        # 登录
        login();

        # 搜索
        search();

        # 增加询单
        add();



        # 退出
        logout();

        print time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),"Test Passed =", i

driver.quit()

print"All Test Passed"
