# -*- coding: utf-8 -*-
"""
Created on Thu Jul  2 14:04:40 2020

@author: USER
"""

#檔案操作流程
#開啟 >> 讀取或寫入 >> 關閉
########################################################################

#開啟檔案
#file = open("data.txt", mode = "w", encoding = "utf-8")
#file.write("""請各位中國人翻譯以下見面詞:
#    Hello, you fuck.
#    I come from Taiwan.
#    Not the motherfucXXXX China!""")
#file.close()

#實務上作法(可不必執行關閉檔案)
#with open ("data.txt", mode = "w", encoding = "utf-8") as file:
#    file.write("""Please translate following into Chinese:
#    Hello, you fuck.
#    I come from Taiwan.
#    Not the motherfucXXXX China!""")
#     
        

        
########################################################################
        
#讀取檔案
#with open ("data.txt", mode = "r", encoding = "utf-8") as file: 
#    data = file.read()
#print(data)


#sum = [] #要放置每一行字數的列表
#num = 0 #總字數
#with open ("data.txt", mode = "r", encoding = "utf-8") as file: 
#    for line in file:  #逐行讀取
#        n = int(len(line))
#        sum.append(n)
#        num+=n
#        
#print(sum,num)


######################################################################

#讀取、複寫Json檔案
#import json
#with open ("config.json", mode = "r") as file:
#    data = json.load(file)
##print(data) #是一個字典檔案
##print("Name: ", data["Name"])
#
#    
import json
with open ("config.json", mode = "r") as file:
    data = json.load(file)    
data["Name"] = "Haushiung Lee" #修改變數中的資料
with open ("config.json", mode = "w") as file:
    json.dump(data,file) #複寫入檔案
    
    



































