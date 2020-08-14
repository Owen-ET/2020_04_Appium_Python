#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/08/13 16:02
# @Author  : zc
# @File    : functions.py

import yaml
import os

class Function():


    def upPath(self):
        return os.path.dirname(os.path.dirname(__file__))


    def getCommonYaml(self):
        CommonYamlPath = self.upPath() + "/data/commonYaml.yaml"
        with open(CommonYamlPath,'r',encoding='utf-8') as file:
            return yaml.load(file)


    def getYaml(self,yamlName):
        yamlPath = self.upPath() + self.getCommonYaml()[yamlName]
        with open(yamlPath,'r',encoding='utf-8') as file:
            return yaml.load(file)



if __name__ == '__main__':
    print(Function().getYaml("desired_capabilities")['desired_cap']['deviceName'])
