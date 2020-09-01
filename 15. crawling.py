# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 09:37:45 2020

@author: USER
"""
#下載特定網址資料
#import urllib.request as re
#
#src = "http://www.ntu.edu.tw/"
#
#with re.urlopen(src) as response:
#    data = response.read().decode("utf-8")  #抓取台灣大學網站的網站原始碼
#    
#print(data)

##########################################################################
##範例:
import urllib.request as request
import json

# 「臺北市內湖科技園區廠商名錄」API
url = 'https://data.taipei/opendata/datalist/apiAccess?scope=resourceAquire&rid=296acfa2-5d93-4706-ad58-e83cc951863c'

# 串接 API
with request.urlopen(url) as response:

    data = json.load(response)   # 利用 json 模組處理json資料格式
#print(data)                     #json檔案型態為dictionary
  
myList = data['result']['results'] 
##此步驟取出名為results的列表，列表中的每一項又是一個dictionary
##儲存每一公司的統編、公司名稱、統一編號、經緯度等等資料
#print(myList)  #這就是一個列表了

#myLsit列表中又是字典
#觀察字典中的結構後可以發現，公司名稱是字典中的其中一個key，對應的key value就是公司名稱
for company in myList:  
    print(company["公司名稱"])
    

# 將整理好的網路來源資料寫入檔案
with open('commercial data.txt', 'w', encoding='utf-8') as file:
    for company in myList:
        file.write(company['公司名稱']+'\n')
        
















