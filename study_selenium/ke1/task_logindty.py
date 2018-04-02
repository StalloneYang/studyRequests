#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/1 0001 下午 5:45
# @Author  : StalloneYang
# @File    : task_logindty.py
# @desc: 登录
from selenium import webdriver
import unittest, time

class task_logindty(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(10)
        cls.driver.get("http://dsy.10333.com")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


    def test_login(self):
        self.driver.find_element_by_xpath("//a[contains(.,'登录')]").click()
        time.sleep(3)
        self.driver.find_element_by_xpath("//input[@type='text']").clear()
        self.driver.find_element_by_xpath("//input[@type='text']").send_keys("13799999999")
        print("输入账号成功")
        time.sleep(1)
        self.driver.find_element_by_xpath("//input[@type='password']").clear()
        self.driver.find_element_by_xpath("//input[@type='password']").send_keys("88888888")
        print("输入密码成功")
        time.sleep(1)
        self.driver.find_element_by_xpath("//input[@systype='1']").click()
        print("点击登录")
        time.sleep(4)
        self.driver.find_element_by_css_selector(".ids.guanbituichu").click()
        print("退出成功")
        time.sleep(2)


if __name__ == "__main__":
    unittest.main()

# driver = webdriver.Firefox()
#
# driver.get("http://dsy.10333.com")
# driver.find_element_by_xpath("//a[contains(.,'登录')]").click()
# time.sleep(3)
# driver.find_element_by_xpath("//input[@type='text']").clear()
# driver.find_element_by_xpath("//input[@type='text']").send_keys("13799999999")
# print("输入账号成功")
# time.sleep(1)
# driver.find_element_by_xpath("//input[@type='password']").clear()
# driver.find_element_by_xpath("//input[@type='password']").send_keys("88888888")
# print("输入密码成功")
# time.sleep(1)
# driver.find_element_by_xpath("//input[@systype='1']").click()
# print("点击登录")
# time.sleep(4)
# driver.find_element_by_css_selector(".ids.guanbituichu").click()
# print("退出成功")
# time.sleep(2)
# driver.quit()
# print("关闭浏览器")
