#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/09/11 15:52
# @Author  : zc
# @File    : login_page.py

from page_object.page.base_page import Page
from selenium.webdriver.common.by import By
from time import sleep


class Login(Page):

    # 立即体验
    experience_loc = (By.ID, "com.csks.businesses:id/lead_into")


    def loginBefore(self):
        '''登录前步骤'''
        for i in range(2):
            self.swipeLeft()
            sleep(0.5)

        # ID定位
        self.click()

