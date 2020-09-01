#載入內建的sys模組並取得資訊
#import sys
#print(sys.platform)
#print(sys.maxsize)

#import sys as s
#print(s.platform)
#print(s.maxsize)


#建立geometry模組，載入使用
#import geometry as G
#x = G.dis(1,2,7,10)
#print(x)
#
#y = G.slope(5,9,15,29)
#print(y)

#建立一個模組專用的資料夾modules並將geometry置入
#因為模組路徑改變，載入失敗
#調整搜尋模組的路徑
import sys
sys.path.append("modules") #新增的資料夾 >> 新增路徑
print(sys.path) #印出模組的搜尋路徑的列表

#再次嘗試載入模組並使用
import geometry as G
x = G.dis(1,2,7,10)
print(x)

y = G.slope(5,9,15,29)
print(y)