
import pandas as pd

data = pd.DataFrame({
        "Name":["Vince","Princessdolly","Aoki","goldbaby"],
        "Figure":[165,178,160,170],
        "Weight":[51,56,49,48],
        "Ages":[24,26,28,35],
        "Interest":["Anal","DP","Spanking","Blowjob"],
        "isHentai":[False,False,True,True]
        }, index=["V","P","A","G"])  #預設為0,1,2,3


print(data)

print("=================================================================")
#篩選練習

condition = data["Figure"] >= 169
print(condition)
print(data[condition])
#print(data[data["Figure"]>=169]) #同上


print("=================================================================")

condition = data["Name"] == "Aoki"
print(condition)
print(data[condition])
#print(data[data["Name"] == "Aoki"]) #同上

print("=================================================")
print("資料數量:",data.size)
print("資料狀態:",data.shape)
print("資料索引:",data.index)  

print("=================================================")

print("取得Interest欄位資料:",data["Interest"],sep="\n") 

print("=================================================")

print("依照順序取得資料:",data.iloc[1],sep="\n")  #數字索引  

print("=================================================")

print("依照索引取得資料:",data.loc["P"],sep="\n")   #自訂符號所引

print("=================================================")

NAMES = data["Name"]  #NAMES是一個Series資料
print("把Name欄位的資料全部轉為大寫:", NAMES.str.upper(),sep = "\n")

print("=================================================")

Figures = data["Figure"]  #Figures是一個Series資料
print("尺寸的平均值:" + str(Figures.mean()) + "公分")

print("=================================================")

#建立新欄位
data["LikeBigCock"] = [False,False,True,False] #方法一
data["Cup"] = pd.Series(["None","36C","34D","37B"], 
                   index=["V","P","A","G"]) #方法二 #此方法須留意index
data["BMI"] = data["Weight"] / ( data["Figure"]/100 )**2 #方法三
print(data)

























     