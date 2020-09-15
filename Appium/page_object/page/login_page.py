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


    # 立即体验元素
    experience_loc = (By.ID,loginData['experience'])
    # 用户名元素
    username_loc = (By.CLASS_NAME,loginData['username'])
    # 用户名值
    usernameValue_loc = loginData['usernameValue']
    # 密码元素
    password_loc = (By.XPATH,loginData['password'])
    # 密码值
    passwordValue_loc = loginData['passwordValue']
    # 关输入法元素
    rmInput_loc = (By.CLASS_NAME,loginData['rmInput'])
    # 登录按钮元素
    loginButton_loc = (By.ID,loginData['loginButton'])


    def loginAction(self):
        '''登录步骤'''


        # 向左滑动屏幕两次
        for i in range(2):
            self.swipeLeft()
            sleep(0.5)


        # 点击立即体验
        self.click(self.experience_loc)
        # 输入用户名
        self.sendKeys(self.username_loc,self.usernameValue_loc)
        # 输入密码
        self.sendKeys(self.password_loc,self.passwordValue_loc)
        # 去掉输入法
        self.click(self.rmInput_loc)
        # 点击登录按钮
        self.click(self.loginButton_loc)


if __name__ == '__main__':
    Login().loginAction()


