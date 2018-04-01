#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/31 0031 下午 1:43
# @Author  : StalloneYang
# @File    : login_dty.py
# @desc:登录接口
import requests
import ssl
import urllib3
import json
urllib3.disable_warnings()
context = ssl._create_unverified_context()
s = requests.session()
url = "https://dsylogin.10333.com/dotoyo/login"

body = {
    "username": "13799999999",
    "password": "88888888",
    "service": "http://dsyjg.10333.com/api/ent/index"
}
# r1 = s.post(url,data=body,verify=False)
r1 = requests.post(url,data=body,verify=False)
print(r1.text)


uri = json.loads(r1.text)
url_login = "https://dsyjg.10333.com/api/ent/index?ticket=" + uri['st'] + "&sysType=1"
# 模拟登录系统，获取cookie
resp = requests.get(url=url_login,verify=False)
cookie_jar = resp.request._cookies
cookie = requests.utils.dict_from_cookiejar(cookie_jar)  # Cookiejar类型转化为字典
print(cookie)
USERID_SID = cookie['USERID_SID']
print(USERID_SID)

addCookies = requests.cookies.RequestsCookieJar()
addCookies.set("USERID_SID",USERID_SID )   # 从传入登录的cookies
print(type(addCookies))
# addCookies.set("USERID_SID", "cd24db7a-ba63-45d1-b733-355f1ce94e25")   # 从fiddler4中抓过来的
s.cookies.update(addCookies)   # 更新cookies

# 访问一个登录后的请求-个人资料
url4 = "http://dsyjg.10333.com/api//org/personalCenter/getUserBasicInfo"
r4 = s.get(url4, verify=False )
print(r4.content.decode('utf-8'))
print(r4.cookies)

