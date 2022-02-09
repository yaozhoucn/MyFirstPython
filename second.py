# -*- coding = utf-8 -*-
# @Time :2020/7/24 13:42
# @Author:Hang
# @File : second.py
# @Software: PyCharm

'''
age=18;
name="张三";
print("我的姓名是%s,我今年%d岁"%(name,age));
'''
nameList=['张无忌 ','谢逊','周芷若','张三丰']
for name in nameList:
    print("------增加前的名单------")
    print(name)
    nametemp=input("请输入需要增加的姓名：")
    nameList.append(nametemp)
print("------增加后的名单------")
print(name)

import bs4
import re
import urllib
import xlwt
import sqlite3