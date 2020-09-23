#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/09/15 19:00
# @Author  : zc
# @File    : supply_page.py

import datetime
from page_object.page.login_page import Login
from page_object.common.functions import Function as Fun
from selenium.webdriver.common.by import By
from time import sleep


class Supply(Login):


    # 获取供货yaml的值
    supplyData = Fun().getYaml("supply")['data']
    # 供货数量yaml的值
    supplyNumData = supplyData['supplyNum']
    # 车牌号yaml的值
    carNumData = supplyData['carNum']
    # 预计到厂时间yaml的值
    expectArrivalTimeData = supplyData['expectArrivalTime']


    # 行情信息元素
    quotation_loc = (By.XPATH, supplyData['quotation'])
    # 提交订单元素
    commitButton_loc = (By.ID, supplyData['commitButton'])
    # 供货数量toast
    supplyNumToast_loc = (By.XPATH, supplyNumData['toast'])
    # 供货数量输入框元素
    supplyNum_loc = (By.XPATH, supplyNumData)
    # 供货数量输入框值
    supplyNumValue = supplyNumData['value']
    # 车牌号输入框元素
    carNum_loc = (By.ID, carNumData)
    # 车牌号输入框值
    carNumValue = carNumData['value']
    # 预计到厂时间元素
    expectArrivalTime_loc = (By.ID, expectArrivalTimeData)
    # 预计到厂时间值
    arrivalTime = expectArrivalTimeData['arrivalTime']




    def findSupplyInfo(self):
        '''寻找元素，并点击'''
        while 1<10:
            try:
                # 模糊定位
                self.click(self.quotation_loc)
                sleep(1)
                break
            except:
                print("未找到，继续上滑")
                self.swipeUp()


    def dateSwipeUpAction(self):
        '''日期滑动时间'''
        arrivalTime = self.arrivalTime
        arrivalDate = arrivalTime.split(".", 3)[2]
        # 获取当前日期的日子
        now_time = str(datetime.datetime.now())
        now_date = now_time.split(" ")[0].split("-", 3)[2]

        num = (int(arrivalDate) - int(now_date))

        self.timeSwipeUp(num)


    def addSupplyInfo(self):
        '''添加供货信息'''

        # 点击"我要供货"【点击页面的坐标】
        self.driver.tap([(0, 1905), (540, 2028)], 500)
        # 点击提交订单
        self.click(self.commitButton_loc)
        # toast提示信息
        while 1 < 2:
            try:
                toast = self.getToast(self.supplyNumToast_loc)
                break
            except:
                self.click(self.commitButton_loc)
        print(toast)
        # 输入供货数量
        self.sendKeys(self.supplyNum_loc,self.supplyNumValue)
        # 输入车牌号
        self.sendKeys(self.carNum_loc,self.carNumValue)
        # 选择预计到厂时间
        self.click(self.expectArrivalTime_loc)
        self.dateSwipeUpAction()




    def addSupply_action(self):

        self.findSupplyInfo()
        self.addSupplyInfo()




