#-*- coding = utf-8 -*-
#@Time : 2020/8/1 21:24
#@Author : hang
#@File : testUrllib.py
#@Software : PyCharm


import urllib.request,urllib.error
from bs4 import BeautifulSoup
import re
import xlwt
import sqlite3
import sys


def main():
    print("开始爬取数据。。。。。。。。。。。。")
    baseurl= "https://movie.douban.com/top250?start="
    #1.爬取网页
    datalist = getData(baseurl)
    savepath = "豆瓣电影Top250.xls" #保存路径
    # 3.保存数据
    saveData(datalist,savepath)

    #askUrl("https://movie.douban.com/top250?start=0")
#影片详情链接的规则
findLink = re.compile(r'<a href="(.*?)">')  #创建正则表达式对象，表示规则（字符串的模式）
#影片图片的链接

findImage = re.compile(r'<img.*src="(.*?)"',re.S)  #re.S让换行符包含在字符中

#影片的片名
findTitle = re.compile(r'<span class="title">(.*)</span>')

#影片评分
findRating = re.compile(r'<span class="rating_num" property="v:average">(.*)</span>')

#评价人数
fingJudge = re.compile(r'<span>(\d*)人评价</span>')

#找到概况
findInq = re.compile(r'<span class="inq">(.*)</span>')

#找到影片的具体 内容
findBd = re.compile(r'<p class="">(.*?)</p>',re.S)

#得到一个指定url的网页内容
def askUrl(url):
    head = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"
    }
    request=urllib.request.Request(url,headers=head)
    html=""
    try:
        response = urllib.request.urlopen(request)
        html = response.read().decode("utf-8")
        #print(html)
    except urllib.error.URLError as e :
        if hasattr(e,"code"):
            print(e.code)
        if hasattr(e,"reason"):
            print(e.reason)
    return html

    #2.解析数据





#爬取网页
def getData(baseurl):
    datalist = []
    #逐一解析数据
    for i in range(0,10):  #调用获取页面信息的函数，调用10次
        url = baseurl + str(i*25)
        html = askUrl(url)  #保存获取到的网页源码

        #逐一解析数据
        soup = BeautifulSoup(html,"html.parser")
        for item in soup.find_all("div",class_="item"):  #查找符合要求的字符串，形成列表
            #print(item) #测试：查看电影item全部信息
            data = []
            item = str(item)

            link = re.findall(findLink,item)[0]  #re库用来通过正则表达式查找制定的字符串
            data.append(link)

            imSrc = re.findall(findImage,item)[0]
            data.append(imSrc)


            titles = re.findall(findTitle,item)
            if(len(titles)==2):
                ctitle = titles[0]
                data.append(ctitle)
                otitle = titles[1].replace("/","") # 去掉无关的符号
                data.append(otitle)
            else:
                data.append(titles[0])
                data.append(' ') #外国名字留空


            rating = re.findall(findRating,item)[0]
            data.append(rating)



            judgeNumber = re.findall(fingJudge,item)[0]
            data.append(judgeNumber)

            inq = re.findall(findInq,item)
            if len(inq) != 0:
                inq = inq[0].replace("。","") #去掉句号
                data.append(inq)
            else:
                data.append(" ")

            bd = re.findall(findBd,item)[0]
            bd = re.sub('<br(\s+)?/>(\s+)?'," ",bd) #去掉</br>
            bd = re.sub('/'," ",bd)
            data.append(bd.strip()) # 去掉前后的空格

            datalist.append(data) #把处理好的一部电影信息放入datalist

            #print(data)

    #print(datalist)

    return datalist


#保存数据
def saveData(datalist,savepath):

    moviebook = xlwt.Workbook(encoding="utf-8",style_compression=0) #创建workbook对象,压缩样式
    moviesheet = moviebook.add_sheet("豆瓣电影Top250详细信息",cell_overwrite_ok=True)  #创建sheet页
    col = ("电影详情链接","图片链接","影片中文名","影片英文名","评分","评价数","概况","相关信息")
    for i in range(0,8):
        moviesheet.write(0,i,col[i]) #写入列名

    for i in range(0,250):
        #print("第%d部" %(i+1))
        data = datalist[i]
        for j in range(0,8):
            moviesheet.write(i+1,j,data[j])
    moviebook.save(savepath)  #保存
    print("数据已保存")

if __name__ == '__main__':
    main()
    print("数据爬取结束")