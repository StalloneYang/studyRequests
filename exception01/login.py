#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/19 0019 下午 9:04
# @Author  : StalloneYang
# @File    : login.py
# @desc:地方

from selenium import webdriver
import time

driver = webdriver.Firefox()

driver.get("http://www.cnblogs.com/yoyoketang/p/6123834.html")
time.sleep(1)
cookies = driver.get_cookie("gid")
print(type(cookies))
print(cookies)
time.sleep(1)
driver.quit()
# test
# 删除
# 增加
# 修改
# test