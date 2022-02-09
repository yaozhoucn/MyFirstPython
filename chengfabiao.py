# -*- coding = utf-8 -*-
# @Time :2020/7/24 15:49
# @Author:Hang
# @File : chengfabiao.py
# @Software: PyCharm


'''
for i in range(1,10):
    for j in range(1,10):
        if i>=j:
            print(i, "*", j, "=", i * j, end="\t")
    print(" ")

'''

i=1
j=1
while i<=9:
    while j<=i:
        print(j, "*", i, "=", i * j, end="\t")
        j=j+1
    j=1
    i=i+1
    print(" ")





