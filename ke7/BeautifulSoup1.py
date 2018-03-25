#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/18 0018 下午 10:59
# @Author  : StalloneYang
# @File    : BeautifulSoup1.py
# @desc:

import requests
import urllib3
from bs4 import BeautifulSoup
import re

urllib3.disable_warnings()
url = "https://ishuo.cn/duanzi"
req = requests.get(url, verify=False)
reqCon = req.content
# print(reqCon)

soup1 = BeautifulSoup(reqCon, "html.parser")
soup = soup1.a

# print(soup1)
# print(type(soup1))
# title = soup1.title
# print(title)
#
# string_ = soup1.string
# print(string_)

att = soup.attrs
print(att)
hre = att["href"]
print(hre)

# duanzi = soup1.find_all(class_="content")
# for i in duanzi:
#     print(i.get_text().replace("\n", ""))
#     print("+++++++++++++++++++++++++++++++++华丽的分割线++++++++++++++++++++++++++++++")

s3=soup1.div
s4=s3.ul
print(s3)
duanzi2 = s3.find_all(href="/subject/")
for i in duanzi2:

    print(i.get_text().replace("\n", ""))
    print("+++++++++++++++++++++++++++++++++华丽的分割线++++++++++++++++++++++++++++++")


# res = r'<a .*?>(.*?)</a>'
# mm = re.findall(res, duanzi2, re.S|re.M)
# for value in mm:
#     print (value)