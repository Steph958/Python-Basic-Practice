#函式基礎

def cal(num):
    sum = 0
    for i in range(1,num+1):
        sum+=i
    print(sum)

cal(100)
cal(1000)


#函式進階

def power(base,exp=0): #預設值為0
    print(base**exp)
    
power(10,2)
power(123456789)
power(exp=3,base=10)

#無限/不定參數函式

def AVG(ns): #輸入List
    sum = 0
    for i in ns:
        sum+=i
    print(sum/len(ns))
    
list_1 = []
for i in range(1,15986):
    list_1.append(i)

#print(list_1)   
AVG(list_1)


def AVG(*ns): #輸入Tuple 
    sum = 0
    for i in ns:
        sum+=i
    print(sum/len(ns))

AVG(2,5,8,9,6,5,4,7,8,9,123)
