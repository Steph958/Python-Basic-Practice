
#PART 1: 類別 &類別屬性


#類別的定義與使用
class IO:
    supportedSrcs = ["console","file"]  #類別屬性1 
    def read(src):                     #類別屬性2 
        if src not in IO.supportedSrcs:
            print("Not Supported.")
        else:
            print("Read from: ", src)
        

#使用類別
print(IO.supportedSrcs) #此屬性為變數型態
IO.read("file")          #此屬性為函式型態
IO.read("Internet")


    