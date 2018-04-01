#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/1 0001 下午 10:40
# @Author  : StalloneYang
# @File    : run_main.py
# @desc:运行的主函数

import unittest
from ke6.report import HTMLTestRunner
import os
import time

casePath = "F:\\workspace_py\\studyRequests\\ke6\\testcase\\"
discover = unittest.defaultTestLoader.discover(casePath, pattern="test*.py", top_level_dir=None)

# print(discover)

reportPath = "F:\\workspace_py\\studyRequests\\ke6\\report\\result.html"

# fp = open(reportPath,"wb")  # r 只读  w 写入 b以二进制写入
# runner = HTMLTestRunner.HTMLTestRunner(fp,verbosity=2,title="测试报告",description="报告描述")  # verbosity 用例报告显示规则
# runner.run(discover)
# fp.close()  # 打开的文件要记得关掉

runner = unittest.TextTestRunner()
runner.run(discover)
