#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/07/25 13:20
# @Author  : zc
# @File    : desired_capabilities.py



from appium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import datetime


def appium_desired():

    desired_cap = {
        # "deviceName": "vivo",  # 真机名称
        "deviceName": "MI 8 SE",  # 真机名称
        "platformName": "android",  # 使用的移动端：android、ios
        # "platformVersion": "8.1",  # 移动端版本
        "platformVersion": "9",  # 移动端版本
        "appPackage": "com.csks.businesses",  # 被测试软件Package名
        "appActivity": "cn.soft_x.supplies.ui.SplashAty",  # 被测试软件Activity名
        # "noReset":True,                              # 重置应用状态:True，不重置，false重置清空登录
        "automationName":"UiAutomator2"                # Toast内容

    }

    driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_cap)
    driver.implicitly_wait(10)

    # 屏幕size
    size = driver.get_window_size()
    print(size)


    def windowSize():
        width = driver.get_window_size()['width']
        height = driver.get_window_size()['height']
        return width,height


    def swipeRight():

        width = windowSize()[0]
        height = windowSize()[1]
        driver.swipe(4/5*width,1/2*height,1/5*width,1/2*height)


    def swipeUp():

        width = windowSize()[0]
        height = windowSize()[1]
        driver.swipe(1/2*width,4/5*height,1/2*width,1/5*height)


    def timeSwipeUp(num):

        for i in range(num):
            width = windowSize()[0]
            height = windowSize()[1]
            driver.swipe(688,1972,688,1810)
            # driver.swipe(540,1972,540,1810)


    for i in range(2):
        swipeRight()
        sleep(0.5)

    # ID定位
    driver.find_element(By.ID,"com.csks.businesses:id/lead_into").click()

    # 利用index角标定位
    # inputs = driver.find_elements(By.CLASS_NAME,"android.widget.EditText")
    # inputs[0].send_keys("18602603111")
    # inputs[1].send_keys("123123")

    # className定位(但是不准)
    driver.find_element(By.CLASS_NAME,"android.widget.EditText").send_keys("18602603111")
    # Xpath，利用组合定位
    driver.find_element(By.XPATH,"//*[@text='请输入密码' and @resource-id='com.csks.businesses:id/edt_password']").send_keys("123123")
    driver.find_element(By.CLASS_NAME, "android.widget.EditText").click()
    # 点击登录按钮
    driver.find_element(By.ID,"com.csks.businesses:id/tv_login").click()
    # Xpath，利用text定位
    driver.find_element(By.XPATH,"//*[@text='规格描述：AAAAA']").click()

    # 寻找元素，并点击
    # while 1<10:
    #     try:
    #         # 模糊定位
    #         driver.find_element(By.XPATH,"//*[contains(@text,'规格描述：276373')]").click()
    #         break
    #     except:
    #         print("未找到，继续上滑")
    #         swipeUp()


    # 点击页面的坐标
    sleep(1)
    driver.tap([(0, 1905), (540, 2028)], 500)

    # 提交订单
    driver.find_element(By.ID,"com.csks.businesses:id/btn_ok").click()

    # toast提示信息
    while 1<2:
        try:
            toast = driver.find_element(By.XPATH,"//*[contains(@text,'供货数量不能为空')]").text
            break
        except:
            driver.find_element(By.ID, "com.csks.businesses:id/btn_ok").click()


    # toast = driver.find_element(By.XPATH,"//*[@text='请输入手机号']").text
    # toast = driver.find_element(By.XPATH,"//*[contains(@text,'请输入手机号')]").text
    print(toast)


    driver.find_element(By.XPATH,"//*[@text='请输入供货数量']").send_keys("1000")
    driver.find_element(By.ID,"com.csks.businesses:id/edt_number1").send_keys("津A80801")
    driver.find_element(By.ID,"com.csks.businesses:id/tv_time").click()

    arrivalTime = "2020.08.15"
    arrivalDate = arrivalTime.split(".",3)[2]
    # 获取当前日期的日子
    now_time = str(datetime.datetime.now())
    now_date = now_time.split(" ")[0].split("-", 3)[2]

    num = (int(arrivalDate)-int(now_date))

    timeSwipeUp(num)

    driver.find_element(By.XPATH,"//*[@text='确定']").click()

    driver.find_element(By.ID, "com.csks.businesses:id/btn_ok").click()

    toast = driver.find_element(By.XPATH, "//*[contains(@text,'请对您的货品')]").text
    print(toast)




if __name__ == '__main__':
    appium_desired()