#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/09/11 15:11
# @Author  : zc
# @File    : desired_cap.py

from page_object.common.functions import Function as Fun
from appium import webdriver


class Desired_capabilities(object):

    def desired_cap(self):
        yaml_data = Fun().getYaml("desired_capabilities")
        desired_cap = yaml_data['desired_cap']
        url = yaml_data['url']

        driver = webdriver.Remote(url,desired_cap)
        return driver