#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/09/11 15:53
# @Author  : zc
# @File    : base_page.py

from page_object.common.desired_cap import Desired_capabilities as dc


class Page(object):

    def __init__(self,webdriver = dc().desired_cap()):
        self.driver = webdriver
        self.driver.implicitly_wait(10)
        self.timeout = 10


    def find_element(self,loc):
        '''查找元素'''
        return self.driver.find_element(loc)


    def sendKeys(self,loc,text):
        '''输入事件'''
        self.find_element(loc).send_keys(text)


    def click(self,loc):
        '''点击事件'''
        self.find_element(loc).click()


    def getToast(self,loc):
        '''获取toast提示信息'''
        return self.find_element(loc).text


    def windowSize(self):
        '''获取屏幕宽和高'''
        windowSize = self.driver.get_window_size()
        self.width = windowSize['width']
        self.height = windowSize['height']


    def swipeLeft(self):
        '''屏幕左滑动'''
        self.driver.swipe(4/5*self.width,1/2*self.height,1/5*self.width,1/2*self.height)


    def swipeUp(self):
        '''屏幕上滑动'''
        self.driver.swipe(1/2*self.width,4/5*self.height,1/2*self.width,1/5*self.height)


    def timeSwipeUp(self,num):
        '''日期控件上滑动'''
        for i in range(num):
            self.driver.swipe(688,1972,688,1810)