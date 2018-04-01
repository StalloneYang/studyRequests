#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/1 0001 下午 12:41
# @Author  : StalloneYang
# @File    : task_flower.py
# @desc:仙花数是指一个 n 位数 ( n≥3 ),它的每个位上的数字的 n 次幂之和等于它本身.
#       （例如：1^3 + 5^3 + 3^3 = 153），1+125+27
#       用Python算出100-1000的所有水仙花数，打印出来
#       n位数，123就是3位数，1212就是四位数，12345就是五位数。。。。所以n就是3

for num in range(100, 1000):
    a = num // 100  # 取n的百位数
    b = num % 100 // 10  # 取n的十位数
    c = num - a * 100 - b * 10  # 取n的个位数
    # print(a,b,c)
    if (a**3 + b**3 + c**3) == num:  # 所以n就是3
        print("当前水仙花数是： %d " % num)




# for num in range(100, 1000):
#     a = num // 100  # 取n的百位数
#     b = num % 100 // 10  # 取n的十位数
#     c = num - a * 100 - b * 10  # 取n的个位数
#     # print(a,b,c)
#     if (a**3 + b**3 + c**3) == num:
#         print(num)