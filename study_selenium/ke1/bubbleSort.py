#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/1 0001 上午 1:10
# @Author  : StalloneYang
# @File    : bubbleSort.py
# @desc:

nums = [5,2,45,6,85,8,2,1]
print(len(nums))

def testSort(nums):
    for i in range(len(nums)-1):    # 这个循环负责设置冒泡排序进行的次数
        t = i+1
        print("--------第%s轮排序的结果---------" % t )
        for j in range(i+1,len(nums)):  # ｊ为列表下标
            if nums[i] < nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
            print("排序结果为:%s" % nums)
    return nums

print("初始值：%s" % nums)
newnums = testSort(nums)
print("----------华丽的分割线----------")

print("最终的结果：%s" % newnums)
