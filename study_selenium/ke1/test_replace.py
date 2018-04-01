#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/31 0031 下午 9:08
# @Author  : StalloneYang
# @File    : test_replace.py
# @desc: 赋值
a =1
b = 2

def testte(a,b):
    c=a
    a=b
    b=c
    print(a, b)
    return a,b

# testte(1,3)
#
# a = 1
# b = 2
# a, b = b, a
# print(a, b)
#
# a = b = c = 1
# print (a, b, c)
# d, e, f = 1, 2, "hello"
# print (d, e, f)

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
print("最终的结果：%s" % newnums)

# def bubbleSort1(nums):
#     for i in range(len(nums)-1):    # 这个循环负责设置冒泡排序进行的次数
#         print("--------%s---------" % i)
#         for j in range(len(nums)-i-1):  # ｊ为列表下标
#             if nums[j] > nums[j+1]:
#                 nums[j], nums[j+1] = nums[j+1], nums[j]
#             print("逆向思维：%s" % nums)
#     return nums
# print("初始值：%s" % nums)
# newnums1 = bubbleSort1(nums)
# print("最终的结果：%s" % newnums1)