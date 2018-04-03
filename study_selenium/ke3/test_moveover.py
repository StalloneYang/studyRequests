#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/2 0002 下午 11:32
# @Author  : StalloneYang
# @File    : test_moveover.py
# @desc:
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Firefox()
driver.get("https://www.baidu.com")
time.sleep(3)
mouse = driver.find_elements_by_xpath(".//*[@id='u1']/a[8]")
ActionChains(driver).move_to_element(mouse).perform()
time.sleep(1)
driver.find_element_by_link_text("搜索设置").click()
time.sleep(3)
