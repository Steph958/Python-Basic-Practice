

#PART 2: 類別 & 實體物件 & 實體屬性
###############################################################################
#範例1:
#class Cat:
#    def __init__(self, name):  #建立一個實例的時候Python會自動呼叫此函式!
#        self.name = name       #這種我們很少自己用但 Python 會幫我們呼叫的特殊函式俗稱「魔術函式」（magic functions）
#    def meow(self):
#        print(self.name +': Meow!')
#    def __str__(self):         #當 Python 需要印出東西時就會使用魔術函式 __str__，詢問一個物件它想被轉成什麼樣的字串
#        return 'Cat: ' + self.name
#    
#    
#Vincent = Cat("Vincent")    # __init__ 需要 name（注意 self 不用給，Python 會負責）
#Vincent.meow()
#print(Vincent)

#以上就是 Python 的實體物件、實體屬性的用法。
#一個物件可以包含一些變數（self.name），也可以在裡面定義只有該類型物件才能使用的函式。
#有些函式的名稱比較特殊，是 Python 會自動呼叫的魔術函式
#例如 __init__ 和 __str__ 等等。


###############################################################################
#範例2:

#類別與實體物件、實體屬性、實體方法
#實體屬性:封裝在實體物件中的變數
#實體方法:封裝在實體物件中的函式

class point:
    def __init__(self,x,y):
        self.x = x     #定義實體屬性一
        self.y = y     #定義實體屬性二
    def show(self):    #定義實體方法一
        print(self.x,self.y)
    def distance(self,targetx,targety):   #定義實體方法二
        return   ((self.x-targetx)**2+(self.y-targety)**2 )**0.5

#建立第一個實體物件        
p1=point(4,5)
print(p1.x,p1.y)

#建立第二個實體物件
p2=point(6,7)
print(p2.x,p2.y)

#建立第三個實體物件        
youfuck = point(10,100)   #建立實體物件 #並呼叫實體屬性
youfuck.show()           #呼叫實體方法一
result = youfuck.distance(0,0)  #呼叫實體方法二
print(result)
###############################################################################      
#範例3:

class File:
    def __init__(self,name):
        self.name = name
        self.file = None #初始值為None,因為尚未開啟檔案
    def open(self):
        self.file = open(self.name,mode="r",encoding = "utf-8") 
        #利用此函式開啟檔案後，將檔案存入self.file屬性中
    def read(self):
        return self.file.read()
    
    
#讀取第一個檔案
F1 = File("Chinese.txt")
F1.open()
data1 = F1.read()
print(data1)

print("-------------------")
#讀取第二個檔案
F2 = File("English.txt")
F2.open()
data2 = F2.read()
print(data2)

