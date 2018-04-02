#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/2 0002 下午 11:04
# @Author  : StalloneYang
# @File    : test_openbrowser.py
# @desc:
from selenium import webdriver

driver = webdriver.Firefox()

driver.get("https://www.baidu.com")