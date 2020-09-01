# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 18:45:29 2020

@author: USER
"""

import pandas as pd

#讀取資料
data = pd.read_csv("googleplaystore.csv")
#print(data)
#
#print("資料數量",data.shape)
##資料數量 (10841, 13)
#print("資料欄位",data.columns)
#資料欄位 Index(['App', 'Category', 'Rating', 'Reviews', 'Size', 'Installs', 'Type',
#       'Price', 'Content Rating', 'Genres', 'Last Updated', 'Current Ver',
#       'Android Ver'],
#      dtype='object')


#分析資料
#data = data[data["Rating"]<=5]
#print(data["Rating"])
#print("平均數",data["Rating"].mean())
#print("中位數",data["Rating"].median())
#print("前1000個應用程式的平均",data["Rating"].nlargest(1000).mean())


#print(data["Installs"])
#0            10,000+
#1           500,000+
#2         5,000,000+
#3        50,000,000+
#4           100,000+
#    
#10836         5,000+
#10837           100+
#10838         1,000+
#10839         1,000+
#10840    10,000,000+
#Name: Installs, Length: 10841, dtype: object

#資料型態轉換
#data["Installs"] = pd.to_numeric(data["Installs"])
#ValueError: Unable to parse string "10,000+" at position 0

#data["Installs"] = pd.to_numeric(data["Installs"].str.replace("[,+]",""))
#ValueError: Unable to parse string "Free" at position 10472

#print(data["Installs"][10472])
# Free #字串

data["Installs"] = pd.to_numeric(data["Installs"].str.replace("[,+]","").replace("Free",""))

print(data["Installs"])
#0           10000.0
#1          500000.0
#2         5000000.0
#3        50000000.0
#4          100000.0
#   
#10836        5000.0
#10837         100.0
#10838        1000.0
#10839        1000.0
#10840    10000000.0
#Name: Installs, Length: 10841, dtype: float64



#print("安裝數量大於100,000的應用程式數量為",
#      data[data["Installs"]>100000].shape)
#安裝數量大於100,000的應用程式數量為 (4950, 13)

#print("安裝數量大於100,000的應用程式數量為",
#      data[data["Installs"]>100000].shape[0],"個")


#基於資料的應用
#關鍵字搜尋應用程式名稱

keyw = input("請輸入關鍵字:")
condition = data["App"].str.contains(keyw, case = False) #忽略大小寫差異
print("包含使用者輸入關鍵字之App數量共有",data[condition].shape[0],"個")
print("==========================================================")
print(data[condition]["App"])























