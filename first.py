'''
for i in range(0,20,5):
    print(i,"\t")



cityname="xian"
for x in cityname:
    print(x)
'''

'''
a = ["aa","bb","cc","dd"]
for y in range(len(a)):
    print(y,a[y])
for x in a:
    print(x,end="\t")
'''


'''
i = 0
while i<5 :
    print("这是第%d次输出"%(i+1))
    print("i=%d"%i)
    i = i +1
'''
'''1-100的求和'''

'''
i = 0
j = 0
while i<100:
    i=i+1
    j=i+j

    print(j)
'''

'''
x = 100
sum =0
counter = 1
while counter<=x:
    sum = sum + counter
    counter += 1

print("1-%d的相加的和为%d"%(x,sum))
'''

'''
i = 1
while i<5:
    print(i,"小于5")
    i +=1
else:
    print(i,"大于或等于5")

'''
i = 1
while i<10:
    i =i+1;
    if i==6:
        continue
    print("当前i的值为%d"%i)

namesList = ['xiaoWang', 'xiaoZhang', 'xiaoHua']
for name in namesList:
    print(name)
