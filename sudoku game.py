start_tuple=("53.|678|.1.",
             "67.|195|..8",
             "198|.4.|567",
             "8.9|.6.|..3",
             "4..|853|7.1",
             "713|.2.|8.6",
             "961|.3.|28.",
             ".87|419|..5",
             ".4.|.86|179")

start_fixed=("53.678.1.",
             "67.195..8",
             "198.4.567",
             "8.9.6...3",
             "4..8537.1",
             "713.2.8.6",
             "961.3.28.",
             ".87419..5",
             ".4..86179")
                
start=["53.678.1.",
       "67.195..8",
       "198.4.567",
       "8.9.6...3",
       "4..8537.1",
       "713.2.8.6",
       "961.3.28.",
       ".87419..5",
       ".4..86179"]



def solved(start):
    count_of_point = 0
    for i in start:
        if i.find(".") == -1:
            count_of_point = count_of_point + 1
    if count_of_point==9:
        return True
    else:
        return False
    
#檢驗數獨完成了沒
#藉由計算"."的個數 >> 如果start中的每一欄之中沒有找到"."的次數為9次 >> 則數獨完成
          
    

def display():
    LETTER="ABCDEFGHI"
    start_format = []
    for i in start:
        front_str = i[:3]
        middle_str = i[3:6]
        behind_str = i[6:]
        new_i = front_str+"|"+middle_str+"|"+behind_str
        start_format.append(new_i)
        
    print("\n\n%24s%12sabc def ghi"%("original:","")) 
    for i in range(9):
        print("%24s%11s%12s"%(start_tuple[i],list(LETTER)[i],start_format[i]))
        if (i==2)or(i==5):
            print("             ---+---+---            ---+---+---")
    
#將start清單以數獨格式顯示(靠右顯示) >> start_format
#同時列出給定的原始start(靠左顯示) >> statr_tuple
#like:
######################################################
#
#               original:            abc def ghi
#             53.|678|.1.          A 53.|678|.1.
#             67.|195|..8          B 67.|195|..8
#             198|.4.|567          C 198|.4.|567
#             ---+---+---            ---+---+---
#             8.9|.6.|..3          D 8.9|.6.|..3
#             4..|853|7.1          E 4..|853|7.1
#             713|.2.|8.6          F 713|.2.|8.6
#             ---+---+---            ---+---+---
#             961|.3.|28.          G 961|.3.|28.
#             .87|419|..5          H .87|419|..5
#             .4.|.86|179          I .4.|.86|179
#######################################################


def choiceFormatIsGood(choice):
    LETTER="ABCDEFGHI"
    letter="abcdefghi"
    LETTER_dic = {"A":0, "B":1, "C":2, "D":3, "E":4, "F":5, "G":6, "H":7, "I":8}
    letter_dic = {"a":0, "b":1, "c":2, "d":3, "e":4, "f":5, "g":6, "h":7, "i":8}
    num_to_check = ['1','2','3','4','5','6','7','8','9','?']
    choice_lst = list(choice)
        
    if (len(choice_lst)<=4) and (choice_lst[0] in list(LETTER)) and (choice_lst[1] in list(letter)) and (choice_lst[2] == "=") and (choice_lst[3] in num_to_check):
        return True
    else:
        return False
#判定玩家輸入的指令是否符合格式:第一個字元為A~I，第二個為a~i，第三個為"="，第四個為1~9或是"?"
#例如:Ac=5或Bf=?


def TurnChoiceIntoChc(choice):
    LETTER="ABCDEFGHI"
    letter="abcdefghi"
    LETTER_dic = {"A":0, "B":1, "C":2, "D":3, "E":4, "F":5, "G":6, "H":7, "I":8}
    letter_dic = {"a":0, "b":1, "c":2, "d":3, "e":4, "f":5, "g":6, "h":7, "i":8}
    choice_lst = list(choice) 
    
    global chc
    chc = []
    for i in list(LETTER):
        if i == choice_lst[0]:
            chc.append(LETTER_dic[i])
    for i in list(letter):
        if i == choice_lst[1]:
            chc.append(letter_dic[i])
    if choice_lst[3].isdigit() == True:
        chc.append(int(choice_lst[3]))
    else:
        chc.append("?")
#將指令choice(資料型態為character)轉換為chc(資料型態為list)
#例如:"Ac=9" >> [A,c,9]
#因為chc在下面的其他函式中還會用到，故將其設為全域變數


def choiceIsEmpty(choice):
    LETTER="ABCDEFGHI"
    letter="abcdefghi"
    LETTER_lst = list(LETTER)
    letter_lst = list(letter)
    LETTER_dic = {"A":0, "B":1, "C":2, "D":3, "E":4, "F":5, "G":6, "H":7, "I":8}
    letter_dic = {"a":0, "b":1, "c":2, "d":3, "e":4, "f":5, "g":6, "h":7, "i":8}
    input_allowed =["1","2","3","4","5","6","7","8","9"]
    choice_lst = list(choice)
    for i in LETTER_lst:
        if choice_lst[0] == i:
            target_item = list(start_fixed[LETTER_dic[i]])
    for s in letter_lst:
        if choice_lst[1] == s:
            global target_num
            target_num = target_item[letter_dic[s]]
    
    if target_num in input_allowed:
        print("The place you choose is a GIVEN NUM!!")
        return False 
    else:
        return True
#檢驗玩家指令所指的位置是否為空的(表示該指令所指的值是".")


def rowHasItAlready(chc):
    target_row = list(start[chc[0]])
    if str(chc[2]) in target_row:
        print("The row has it already!!")
    else:
        return True
#檢驗同一欄之中的數字有無和指令中的數字重複
		
        
        
def columnHasItAlready(chc):
    num_to_check = []
    for i in start:
        num_to_check.append(list(i)[chc[1]])
    if str(chc[2]) in num_to_check:   
        print("The column has it already!!")
    else:
        return True
#檢驗同一列之中的數字有無和指令中的數字重複
  
        
def squareHasItAlready(chc):
    target_to_append = []
    if 0<= chc[0] <=2:
        if 0<= chc[1] <=2:
            new_str1 = start[0][:3] + start[1][:3] + start[2][:3]
            target_to_append = list(new_str1)
        elif 3<= chc[1] <=5:
            new_str2 = start[0][3:6] + start[1][3:6] + start[2][3:6]
            target_to_append = list(new_str2)
        else:
            new_str3 = start[0][6:] + start[1][6:] + start[2][6:]
            target_to_append = list(new_str3)
    
    elif 3<= chc[0] <= 5:     
        if 0<= chc[1] <=2:
            new_str4 = start[3][:3] + start[4][:3] + start[5][:3]
            target_to_append = list(new_str4)
        elif 3<= chc[1] <=5:
            new_str5 = start[3][3:6] + start[4][3:6] + start[5][3:6]
            target_to_append = list(new_str5)
        else:
            new_str6 = start[3][6:] + start[4][6:] + start[5][6:]
            target_to_append = list(new_str6)
            
    else:
        if 0<= chc[1] <=2:
            new_str7 = start[6][:3] + start[7][:3] + start[8][:3]
            target_to_append = list(new_str7)
        elif 3<= chc[1] <=5:
            new_str8 = start[6][3:6] + start[7][3:6] + start[8][3:6]
            target_to_append = list(new_str8)
        else:
            new_str9 = start[6][6:] + start[7][6:] + start[8][6:]
            target_to_append = list(new_str9)
      
    
    if str(chc[2]) in target_to_append:
        print("The square has it already!!")
    else:
        return True
#檢驗每一個3x3方塊(共有9個方塊)中的數字有無和指令中的數字重複

    

def updateBoard(chc):
    target_item = start[chc[0]]
    front_split = target_item[:chc[1]]
    behind_split = target_item[(int(chc[1])+1):]
    if str(chc[2]) == "?":
         new_str = front_split + "." + behind_split
    else:
        new_str = front_split + str(chc[2]) + behind_split
    start[chc[0]] = new_str
#確認上述含是檢驗皆沒有問題之後，根據輸入指令去更新右方的數獨表格，左方仍維持原樣


times_correction = 0                               #為了計算修正錯誤的次數(chc輸入"?"的次數)，預設值為0
while not solved(start):
    choice = input("Enter your chc:")             #輸入字串choice
    choice_lst=list(choice)
    if choice_lst[3] == "?":
        times_correction += 1                     #計算修正(chc輸入"?")的次數
    if choiceFormatIsGood(choice) == True:       #確認choice字串格式是否正確
        TurnChoiceIntoChc(choice)               #將choice字串轉換成chc陣列
    else:
        print("The format of chc is wrong!!")
        continue
        
    if choiceIsEmpty(choice) == True:          #檢驗所選位置是否為數字
        rowHasItAlready(chc)
    else:
        print("The site you choose is not empty!!")
        continue
    if rowHasItAlready(chc) == True:           #檢驗同一欄沒有相同之數字
         columnHasItAlready(chc)
    else:
        print("Rule offended!The row has it already!!")
        continue
        
    if columnHasItAlready(chc) == True:         #檢驗同一列沒有相同之數字
        squareHasItAlready(chc)
    else:
        print("Rule offended!The column has it already!")
        continue
        
    if squareHasItAlready(chc) == True:         #檢驗同一個九宮格區塊沒有相同之數字
        updateBoard(chc)                        #更新start清單
        display()                               #將清單以數獨格式顯示
    else:
        print("Rule offended!The square has it already!!")
        continue
        
    if solved(start) == True:
        print("Congratulations! You solved it with" + " " + str(times_correction) +" " + "corrections.")
   