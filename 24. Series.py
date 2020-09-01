

#######數值計算##############################################
import pandas as pd
data1 = pd.Series([20,21,36,100,15,89,-78,569])
data2 = pd.Series([20,21,36,100,15,89,-78,569],
                  index=["a","b","c","d","e","f","g","h"])
print(data1)

print("===============================")

print(data2)

print("===============================")

print("資料型態:",data2.dtype)
print("資料量:",data2.size)
print("資料索引:",data2.index)

print("===============================")

print(data2*2)

print("===============================")

print(data2[2],data2[3],data2["e"],data2["f"])

print("===============================")

data2 = data2 == 21 #逐項比較
print(data2)

print("===============================")

print("最大值:",data2.max())
print("中位數:",data2.median())
print("總和:",data2.sum())
print("標準差:",data2.std())
print("最大的三個值:",data2.nlargest(3))


########字串操作################################################

data3 = pd.Series(["您好","PYTHON","PANDAS","運作中"])

print("===============================")

print(data3.str.len()) #計算每個字串長度
#
print("===============================")
#
print(data3.str.lower()) #轉小寫
#
print("===============================")
#
print(data3.str.cat(sep = ","))  #把字串連接起來，可自訂連接符號
#
print("===============================")
#
print(data3.str.cat(sep = "-"))   #把字串連接起來，可自訂連接符號
#
print("===============================")
#
print(data3.str.contains("P"))  #判斷字串中是否包含了目標字元
#
print("===============================")
#
print(data3.str.replace("您好","HELLO")) #用"HELLO"取代"您好"
#
#












        









