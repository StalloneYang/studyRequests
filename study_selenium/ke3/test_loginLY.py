#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/2 0002 下午 10:42
# @Author  : StalloneYang
# @File    : test_loginLY.py
# @desc: 银联登录

from selenium import webdriver
import unittest, time

class task_logindty(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(10)
        cls.driver.get("http://www.51lianying.com/")

    @classmethod
    def tearDownClass(cls):
        print("关闭浏览器")
        # cls.driver.quit()


    def test_login(self):
        self.driver.find_element_by_xpath("//a[@href='/login.html']").click()
        time.sleep(1)

        # 点击弹出的气泡
        self.driver.find_element_by_xpath("/html/body/div[9]/div[1]").click()

        self.driver.find_element_by_xpath("//input[@placeholder='手机号']").send_keys("13799999999")
        self.driver.find_element_by_xpath("//input[@placeholder='密码']").send_keys("99999999")
        print("输入账号成功")
        time.sleep(1)
        self.driver.find_element_by_id("btn-login").click()
        print("点击登录按钮")
        time.sleep(3)

if __name__ == "__main__":
    unittest.main()
