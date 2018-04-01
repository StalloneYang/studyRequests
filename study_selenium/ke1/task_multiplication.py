#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/1 0001 上午 11:16
# @Author  : StalloneYang
# @File    : task_multiplication.py
# @desc:九九乘法口诀

for i in range(1,10) :
    for j in range (1, i+1):
        match = j*i
        print(str(j) + '*' + str(i) + '=' + str(match) + " ",end="")  # 知识点 ,end="" 打印的时候不换行
    print()
