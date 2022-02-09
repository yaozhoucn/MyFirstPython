# -*- coding = utf-8 -*-
# @Time :2020/8/4 13:56
# @Author:Hang
# @File : testSqlite.py
# @Software: PyCharm

import sqlite3
#1.连接数据库
conn =sqlite3.connect("test.db")  #打开或创建数据库文件

print("database open successful")


#2.创建数据表
c=conn.cursor() #获取游标
sql='''create table company
        (id int primary key not null,
        name text not null,
        age int not null,
        address char(50),
        salary real)
        '''
c.execute(sql)
conn.commit() #提交数据库
conn.cursor() #关闭数据库连接
print("建表成功")