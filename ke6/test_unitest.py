#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/31 0031 下午 1:45
# @Author  : StalloneYang
# @File    : test_unitest.py
# @desc:
import unittest

# help(unittest)


class IntegerArithmeticTestCase(unittest.TestCase):
    def testAdd(self):  ## test method names begin 'test*'
        self.assertEqual((1 + 2), 3)
        self.assertEqual(0 + 1, 1)

    def testMultiply(self):
        self.assertEqual((0 * 10), 0)
        self.assertEqual((5 * 8), 40)


if __name__ == '__main__':
    unittest.main()