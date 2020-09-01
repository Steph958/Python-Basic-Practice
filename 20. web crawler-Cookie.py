# -*- coding: utf-8 -*-
"""
Created on Fri Jul  3 11:17:19 2020

@author: USER
"""


#Cookie
#網站存放在瀏覽器中的一小段內容
#連線時放在Request Headers中送出

#追蹤連結#連續抓取頁面

################################################################################################################################################################################################
#從特定網頁爬取資料 >> 取得網頁原始碼

import urllib.request as re

def getData(url): #20-59行全數放入函式中
    #建立一個Request物件，並附加Request Headers的資訊，喬裝為正常登入者
    #八卦版進入前有一個18歲審查機制
    #PTT八卦版 > 開發人員工具 > Application > Storage > Cookies
    #PTT八卦版 > 開發人員工具 > Network >按一下重新整理 > index.html > Headers > Request Headers > cookie
    request = re.Request(url,headers={
            "cookie":"over18=1",      #八卦版進入前有一個18歲審查機制
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"}) 
    
    with re.urlopen(request) as response:
        data = response.read().decode("utf-8")
        
    #print(data)  #全部網頁原始碼
    
    
   #分析所取得的網頁原始碼 >> 擷取
    
    #安裝第三方套件
    ##pip install beautifulsoup4 ##要直接輸入在console裡面
    
    import bs4
    root = bs4.BeautifulSoup(data,"html.parser")
    
    titles = root.find_all("div", class_ = "title") #尋找所有class為title的div標籤及其內容
    #print(titles)    #title是一個列表
    
    for i in titles:
        if i.a != None:
            print(i.a.string)
        
    
    #抓取下一頁的連結
    
    #觀察原始碼結構:
            #<a class="btn wide" href="/bbs/Gossiping/index39367.html">‹ 上頁</a>
            
    nextLink = root.find("a",string="‹ 上頁") #找出內文是 上頁的<a>標籤 #注意符號
    #print(nextLink)
    #print(nextLink["href"])
    return nextLink["href"]  # "/bbs/Gossiping/index39367.html"

    #函式結束

################################################################################################################################################################################################
#檢驗函式輸出:
#PageUrl = "https://www.ptt.cc/bbs/Gossiping/index.html"
#getData(PageUrl) #印出所有標題
#print(getData(PageUrl)) #印出函式最後return的東西

################################################################################################################################################################################################
#希望連續抓取X頁的資料
#利用迴圈

#PageUrl = "https://www.ptt.cc/bbs/Gossiping/index.html"
#PageUrl = "https://www.ptt.cc" + getData(PageUrl)  #神奇!會同時呼叫函式並更改連結網址!
#print(PageUrl)
   
PageUrl = "https://www.ptt.cc/bbs/Gossiping/index.html" #要抓取的第一頁
count = 0


while count < 5:  #希望連續抓取5頁的資料
    print("--------------------------------------------------------------------")
    print("當前網址: " + PageUrl)
    #getData(PageUrl) 下行程式碼已具備呼叫函式的作用
    PageUrl = "https://www.ptt.cc" + getData(PageUrl)
    #第一頁連結被置入函式中運作:
    #列印出標題
    #並把第二頁的連結回傳入PageUrl變數中複寫過去
    print( " 下頁網址為: "+ PageUrl)
    print("--------------------------------------------------------------------")
    count+=1   
    #迴圈在將第二頁連結至入函式中運作，以此類推
    
#print(PageUrl)






















        
    