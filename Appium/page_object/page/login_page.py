#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/09/11 15:52
# @Author  : zc
# @File    : login_page.py

from page_object.page.base_page import Page
from page_object.common.functions import Function as fun
from selenium.webdriver.common.by import By
from time import sleep


class Login(Page):


    # 获取登录yaml的值
    loginData = fun().getYaml("login")['login']



    # 立即体验
    experience_loc = (By.ID,loginData['experience'])
    # 用户名
    username_loc = (By.CLASS_NAME,)


    def loginAction(self):
        '''登录前步骤'''
        for i in range(2):
            self.swipeLeft()
            sleep(0.5)


        # 点击立即体验
        self.click(self.experience_loc)
        # 输入用户名
        self.sendKeys()


        driver.find_element(By.CLASS_NAME, "android.widget.EditText").send_keys("18602603111")
        # Xpath，利用组合定位
        driver.find_element(By.XPATH, "//*[@text='请输入密码' and @resource-id='com.csks.businesses:id/edt_password']").send_keys("123123")
        driver.find_element(By.CLASS_NAME, "android.widget.EditText").click()
        # 点击登录按钮
        driver.find_element(By.ID, "com.csks.businesses:id/tv_login").click()

