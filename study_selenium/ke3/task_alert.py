#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/2 0002 下午 9:55
# @Author  : StalloneYang
# @File    : task_alert.py
# @desc:1.百度搜索设置-设置每页显示条数，点保存设置，弹出alert，打印出alert内容和点确定按钮。代码截图提交
import time
from selenium import webdriver
import unittest
from selenium.webdriver.common.action_chains import ActionChains

class TaskAlert(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.get("https://www.baidu.com")
        cls.driver.implicitly_wait(10)
        # cls.driver.maximize_window()


    @classmethod
    def tearDownClass(cls):
        print("关闭浏览器")
        # cls.driver.quit()

    def test_alert(self):
        print("开始进行设置")
        # 寻找设置元素
        # setting = self.driver.find_element_by_xpath("//a[@class='pf']")
        setting = self.driver.find_element_by_link_text("设置")
        # news = self.driver.find_element_by_xpath("//a[@class='mnav firepath-matching-node']")
        time.sleep(1)
        ActionChains(self.driver).move_to_element(setting).perform()
        print("鼠标移动到了设置按钮上面")
        time.sleep(2)
        self.driver.find_element_by_id("//a[@class='setpref']").click()
        time.sleep(1)
        self.driver.find_element_by_id("nr").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//option[@value='20']").click()
        time.sleep(1)
        self.driver.find_element_by_class_name("prefpanelgo").click()
        time.sleep(1)


if __name__ == "__main__":
    unittest.main()

