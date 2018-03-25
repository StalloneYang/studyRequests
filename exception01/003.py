#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/18 0018 上午 10:11
# @Author  : StalloneYang
# @File    : 003.py
# @desc:

# class myError(Exception):
#     pass
# a = 102
#
# if a>123:
#     raise myError("自定义异常信息")

class myError2(Exception):
    def __init__(self, err='大小错误'):
        Exception.__init__(self, err)


a = 102
if a > 100:
    raise myError2()
