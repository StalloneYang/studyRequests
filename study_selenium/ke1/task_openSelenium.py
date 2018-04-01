#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/1 0001 上午 10:20
# @Author  : StalloneYang
# @File    : task_openSelenium.py
# @desc: 用selenium启动火狐浏览器
from selenium import webdriver
from time import sleep

browser = webdriver.Firefox()

browser.get('http://www.baidu.com')
print("打开百度成功！")
browser.find_element_by_id("kw").send_keys("selenium")
browser.find_elements_by_class_name("kw")
print("在百度输入框中输入selenium")
browser.find_element_by_id("su").click()
print("点击搜索按钮")
sleep(2)
browser.quit()

