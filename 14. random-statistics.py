# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 09:19:01 2020

@author: USER
"""

#####################################################################
import random as r
data = r.choice([2,5,6,-8,89,502,-1003,568]) #隨機選取一個
print(data)

data2 = r.sample(range(1,10000), 10) #隨機選取多個
print(data2) 

data3 = [1,2,3,4,5,6,7,8,9]
r.shuffle(data3)  #隨機調換順序
print(data3)

data4 = r.random() #從~0~1之間隨機選取
print(data4)

data5 = r.uniform(95.0,100.0) #均勻分配的隨機選取
print(data5)

data6 = r.normalvariate(10,2)   #常態分配的隨機選取
print(data6)

#####################################################################
import statistics as s
data7 = s.mean([1,56,87,-45,6987,2013,-15123]) #平均數
print(data7)

data8 = s.median([1,56,87,-45,6987,2013,-15123])  #中位數
print(data8)

data9 = s.stdev([1,56,87,-45,6987,2013,-15123]) #標準差
print(data9)
