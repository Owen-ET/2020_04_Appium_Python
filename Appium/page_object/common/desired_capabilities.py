#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/07/25 13:20
# @Author  : zc
# @File    : desired_capabilities.py



from appium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


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
        # "automationName":"UiAutomator2"

    }

    driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_cap)
    driver.implicitly_wait(10)

    # 屏幕size
    size = driver.get_window_size()
    print(size)

    def swipe():

        width = driver.get_window_size()['width']
        height = driver.get_window_size()['height']
        driver.swipe(4/5*width,1/2*height,1/5*width,1/2*height)

    for i in range(2):
        swipe()
        sleep(0.5)

    # ID定位
    driver.find_element(By.ID,"com.csks.businesses:id/lead_into").click()

    # 利用index角标定位
    # inputs = driver.find_elements(By.CLASS_NAME,"android.widget.EditText")
    # inputs[0].send_keys("18602603111")
    # inputs[1].send_keys("123123")

    # className定位(但是不准)
    driver.find_element(By.CLASS_NAME,"android.widget.EditText").send_keys("18602603111")
    # Xpath，利用text定位
    driver.find_element(By.XPATH,"//*[@text='请输入密码']").send_keys("123123")

    driver.find_element(By.ID,"com.csks.businesses:id/tv_login").click()

    driver.find_element(By.XPATH,"//*[@text='规格描述：AAAAA']").click()
    driver.find_element()



if __name__ == '__main__':
    appium_desired()