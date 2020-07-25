#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/07/25 13:20
# @Author  : zc
# @File    : desired_capabilities.py



from appium import webdriver


def appium_desired():

    desired_cap = {
        "deviceName": "vivo",  # 真机名称
        "platformName": "android",  # 使用的移动端：android、ios
        "platformVersion": "8.1",  # 移动端版本
        "appPackage": "com.csks.businesses",  # 被测试软件Package名
        "appActivity": "cn.soft_x.supplies.ui.SplashAty",  # 被测试软件Activity名
        # "noReset":True,                              # 重置应用状态:True，不重置，false重置清空登录
        # "automationName":"UiAutomator2"

    }

    driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_cap)
    driver.implicitly_wait(10)

    #





if __name__ == '__main__':
    appium_desired()