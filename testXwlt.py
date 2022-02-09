# -*- coding = utf-8 -*-
# @Time :2020/8/4 10:10
# @Author:Hang
# @File : testXwlt.py
# @Software: PyCharm

import xlwt
workbook = xlwt.Workbook(encoding="utf-8")  #创建workbook对象
'''
worksheet = workbook.add_sheet('详细信息') #创建sheet页
worksheet.write(0,0,'hello，python')   #写入数据，第一行参数“行”，第二各参数“列”，第三个参数就是内容
workbook.save("student.xls") #保存数据
'''
worksheet = workbook.add_sheet("乘法表")
for i in range(0,9):
    for j in range(0,i+1):
        worksheet.write(i,j,"%d * %d = %d"%(i+1,j+1,(i+1)*(j+1)))
workbook.save("student.xls")