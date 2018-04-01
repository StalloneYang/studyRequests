#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/1 0001 下午 10:21
# @Author  : StalloneYang
# @File    : testadd.py
# @desc: 加法
import unittest

class TestAdd(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testadd3(self):
        a = 1
        b = 2
        print("第三个测试用例: ", end="")
        print(a+b)
        return a+b

    def testad42(self):
        a = 3
        b = 4
        print("第四个测试用例: ", end="")
        print(a+b)
        return a+b
if __name__ == "__main__":
    unittest.main()

