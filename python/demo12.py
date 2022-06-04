#random亂數
import random

#隨機選取(單選)
data1 = random.choice([1,5,6,10,20]) #random.choice([])在列表中隨機選取一個數
print(data1)

#隨機選取(複選)
data2 = random.sample([1,5,6,10,20],3) ##random.sample([],選幾個)在列表中隨機選取定義的量
print(data2)

#隨機調換順序(洗牌概念)
data3 = [1,5,8,20]
random.shuffle(data3) #random.shuffle(變數)能將變數的值調換順序
print(data3)

#隨機亂數
data4 = random.random() #random.random()，0~1之間的隨機亂數
print(data4)

data5 = random.uniform(0.0,1.0) #random.uniform(範圍)，範圍之間的隨機亂數(會有小數點)
print(data5)

data6 = random.randint(1,10) #random.randint(範圍)，範圍之間的隨機亂數(整數)
print(data6)

#取常態分配亂數
#平均數100，標準差10，得到的資料多數在90~100之間
data7 = random.normalvariate(100,10) #random.normalvariate(平均數,標準差)
print(data7)

#統計模組
import statistics as stat

#平均數
data8 = stat.mean([1,4,5,8]) #stat.mean([])，取列表中，值的平均數
print(data8)

#中位數
data9 = stat.median([1,2,3,4,5,8,100]) #stat.median([])，取列表中，值的中位數
print(data9)

#標準差
data10 = stat.stdev([1,2,3,4,5,8,10]) #stat.stdev([])，取列表中，值的標準差
print(data10)