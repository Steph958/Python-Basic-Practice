# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 15:28:53 2020

@author: USER
"""
################################################################################################################################################################################################
#從特定網頁爬取資料 >> 取得網頁原始碼

import urllib.request as re
url = "https://www.ptt.cc/bbs/movie/index.html"

#建立一個Request物件，並附加Request Headers的資訊，喬裝為正常登入者
#PTT電影版 > 開發人員工具 > Network > 按一下重新整理 > index.html > Headers > Request Headers > user-agent >複製其內容
request = re.Request(url,headers={
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36"
        }) 

with re.urlopen(request) as response:
    data = response.read().decode("utf-8")
    
print(data)  #全部網頁原始碼


################################################################################################################################################################################################
#分析所取得的網頁原始碼 >> 擷取

#安裝第三方套件
##pip install beautifulsoup4 ##要直接輸入在console裡面

import bs4
root = bs4.BeautifulSoup(data,"html.parser")
#print(root) #全部網頁原始碼

#觀察網頁原始碼結構如下:
# <div class="r-ent">
#                        <div class="nrec"><span class="hl f2">2</span></div>
#                        <div class="title">
#                        
#                                <a href="/bbs/movie/M.1593713592.A.53C.html">[ 好雷]  聲之形－每個人都害怕失敗</a>
#                        
#                        </div>

#titles = root.find("div", class_ = "title") #尋找class為title的div標籤及其內容 #後一項參數為搜尋條件
#print(titles)              # html標題標籤 <title><title/>
#print(titles.a.string)     # 向下鑽研到<a><a/>中的字串內容


titles = root.find_all("div", class_ = "title") #尋找所有class為title的div標籤及其內容
print(titles)    #title是一個列表

for i in titles:
    if i.a != None:
        print(i.a.string)
        
    
    
    
