import random
myArray = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
#建立1個4x4矩陣，且16個區塊皆賦值為0
num = [2,4]
inducerlist = [0,1,2,3]
myArray[random.choice(inducerlist)][random.choice(inducerlist)] = random.choice(num)
myArray[random.choice(inducerlist)][random.choice(inducerlist)] = random.choice(num)
#在16個區塊中隨機指定兩區塊，並於兩區塊內隨機產生2或4

def users_choice(myArray,user_input):
    if user_input == "u":    #玩家向上滑
        i=0
        for j in range(0,4):
            if myArray[i][j]!=0 or myArray[i+1][j]!=0 or myArray[i+2][j]!=0 or myArray[i+3][j]!=0:
                if myArray[i][j]==0:
                    while myArray[i][j]==0:
                        myArray[i][j]=myArray[i+1][j]
                        myArray[i+1][j]=myArray[i+2][j]
                        myArray[i+2][j] = myArray[i+3][j]
                        myArray[i+3][j]=0
                if myArray[i+1][j]==0 and (myArray[i+2][j]!=0 or myArray[i+3][j]!=0):
                    while myArray[i+1][j]==0:
                        
                        myArray[i+1][j]=myArray[i+2][j]
                        myArray[i+2][j]=myArray[i+3][j]
                        myArray[i+3][j]=0
                if myArray[i+2][j]==0 and (myArray[i+3][j]!=0):
                    while myArray[i+2][j]==0:
                        myArray[i+2][j]=myArray[i+3][j]
                        myArray[i+3][j]=0
        i=0
        for j in range(0,4):
            if myArray[i][j]==myArray[i+1][j]:
                myArray[i][j]=myArray[i][j]+myArray[i+1][j]
                myArray[i+1][j]=myArray[i+2][j]
                myArray[i+2][j]=myArray[i+3][j]
                myArray[i+3][j]=0
            if myArray[i+1][j]==myArray[i+2][j]:
                myArray[i+1][j]=myArray[i+1][j]+myArray[i+2][j]
                myArray[i+2][j]=myArray[i+3][j]
                myArray[i+3][j]=0
            if myArray[i+2][j]==myArray[i+3][j]:
                myArray[i+2][j]=myArray[i+2][j]+myArray[i+3][j]
                myArray[i+3][j]=0
                        
                        
          
    elif user_input == "d":    #玩家向下滑
        i=0
        for j in range(0,4):
            if myArray[i][j]!=0 or myArray[i+1][j]!=0 or myArray[i+2][j]!=0 or myArray[i+3][j]!=0:    
			#這裡單純處理移動的部分 >> 遇到相同數字須加總的問題不在這裡解決
			#確保每一欄的4個數字中至少有1個不為0
			    if myArray[i+3][j]==0:    
                    while myArray[i+3][j]==0:
                        myArray[i+3][j]=myArray[i+2][j]
                        myArray[i+2][j]=myArray[i+1][j]
                        myArray[i+1][j]=myArray[i][j]
                        myArray[i][j]=0
		        #如果某一欄第4個值為0的話
		        #使該欄第4個值被第3個值取代、第3個值被第2個值取代、第2個值被第1個值取代、第1個值被0取代
		        #直到該欄第4個值不為0時才停止迴圈
				
                if myArray[i+2][j]==0 and (myArray[i+1][j]!=0 or myArray[i][j]!=0):
                    while myArray[i+2][j]==0:
                        myArray[i+2][j]=myArray[i+1][j]
                        myArray[i+1][j]=myArray[i][j]
                        myArray[i][j]=0
                #如果某一欄第3個值為0且(該欄第2個值不為0 或是 該欄第1個值不為0)的話
				#使該欄第3個值被第2個值取代、第2個值被第1個值取代、第一個值被0取代
				#直到該欄第3個值不為0才停止迴圈
				
                if myArray[i+1][j]==0 and myArray[i][j]!=0:
                    while myArray[i+1][j]==0:
                        myArray[i+1][j]=myArray[i][j]
                        myArray[i][j]=0
				#如果某一欄第2個值為0且第1個值不為0的話
				#使該欄第2個值被第1個值取代
				#直到該欄第2個值不為0時才停止迴圈
		
        #這裡處理同一欄中有相同數字存在而需要加總的狀況	
		#注意這裡無需考慮特定欄中有沒有0的問題，上一個迴圈已經處理完了
        i=0
        for j in range(0,4):
            if myArray[i+1][j]==myArray[i][j]:
                myArray[i+1][j]=myArray[i+1][j]+myArray[i][j]
                myArray[i][j]=0
            #如果某一欄第2個值和第1個值相同的話
			#第2個值會變成第2和第1個值的加總
			#第1個值被0取代
			
			if myArray[i+2][j]==myArray[i+1][j]:
                myArray[i+2][j]=myArray[i+2][j]+myArray[i+1][j]
                myArray[i+1][j]=myArray[i][j]
                myArray[i][j]=0
			#如果某一欄第3個值和第2個值相同的話
			#第3個值會變成第3和第2個值的加總
			#第2個值被第1個值取代
			#第1個值被0取代
			
			if myArray[i+3][j]==myArray[i+2][j]:
                myArray[i+3][j]=myArray[i+3][j] + myArray[i+2][j]
                myArray[i+2][j]=myArray[i+1][j]
                myArray[i+1][j]=myArray[i][j]
				myArray[i][j]=0
			#如果某一欄第4個值與第3個值相同的話
			#第4個值會變成第4和第3個值的加總
			#第3個值被第2個值取代
			#第2個值被第1個值取代
			#第1個值被0取代

        #特定欄像是[2,2,2,4]不能向下滑一次就變成[0,0,2,8]
		#2048遊戲向下滑一次只會做最下方的加總一次:[2,2,2,4] >> [0,2,4,4]
		#需要再向下滑一次才會變成[0,0,2,8]
		#因此這個for迴圈內的if迴圈順序可以隨機
		
    elif user_input == "l":    #玩家向左滑
        j=0
        for i in range(0,4):

            if myArray[i][j]!=0 or myArray[i][j+1]!=0 or myArray[i][j+2]!=0 or myArray[i][j+3]!=0:
                if myArray[i][j]==0:
                    while myArray[i][j]==0:
                        myArray[i][j]=myArray[i][j+1]
                        myArray[i][j+1]=myArray[i][j+2]
                        myArray[i][j+2] = myArray[i][j+3]
                        myArray[i][j+3]=0
                if myArray[i][j+1]==0 and (myArray[i][j+2]!=0 or myArray[i][j+3]!=0):
                    while myArray[i][j+1]==0:
                        myArray[i][j+1]=myArray[i][j+2]
                        myArray[i][j+2]=myArray[i][j+3]
                        myArray[i][j+3]=0
                if myArray[i][j+2]==0 and (myArray[i][j+3]!=0):
                    while myArray[i][j+2]==0:
                        myArray[i][j+2]=myArray[i][j+3]
                        myArray[i][j+3]=0
        j=0
        for i in range(0,4):
            if myArray[i][j]==myArray[i][j+1]:
                myArray[i][j]=myArray[i][j]+myArray[i][j+1]
                myArray[i][j+1]=myArray[i][j+2]
                myArray[i][j+2]=myArray[i][j+3]
                myArray[i][j+3]=0
            if myArray[i][j+1]==myArray[i][j+2]:
                myArray[i][j+1]=myArray[i][j+1]+myArray[i][j+2]
                myArray[i][j+2]=myArray[i][j+3]
                myArray[i][j+3]=0
            if myArray[i][j+2]==myArray[i][j+3]:
                myArray[i][j+2]=myArray[i][j+2]+myArray[i][j+3]
                myArray[i][j+3]=0
    elif user_input == "r":    #玩家向右滑
        j=0
        for i in range(0,4):
            if myArray[i][j]!=0 or myArray[i][j+1]!=0 or myArray[i][j+2]!=0 or myArray[i][j+3]!=0:
                if myArray[i][j+3]==0:
                    while myArray[i][j+3]==0:
                        myArray[i][j+3]=myArray[i][j+2]
                        myArray[i][j+2]=myArray[i][j+1]
                        myArray[i][j+1]=myArray[i][j]
                        myArray[i][j]=0
                if myArray[i][j+2]==0 and (myArray[i][j+1]!=0 or myArray[i][j]!=0):
                    while myArray[i][j+2]==0:
                        myArray[i][j+2]=myArray[i][j+1]
                        myArray[i][j+1]=myArray[i][j]
                        myArray[i][j]=0

                if myArray[i][j+1]==0 and myArray[i][j]!=0:
                    while myArray[i][j+1]==0:
                        myArray[i][j+1]=myArray[i][j]
                        myArray[i][j]=0
        j=0
        for i in range(0,4):
            if myArray[i][j+3]==myArray[i][j+2]:
                myArray[i][j+3]=myArray[i][j+3] + myArray[i][j+2]
                myArray[i][j+2]=myArray[i][j+1]
                myArray[i][j+1]=myArray[i][j]
                myArray[i][j]=0
            if myArray[i][j+2]==myArray[i][j+1]:
                myArray[i][j+2]=myArray[i][j+2]+myArray[i][j+1]
                myArray[i][j+1]=myArray[i][j]
                myArray[i][j]=0
            if myArray[i][j+1]==myArray[i][j]:
                myArray[i][j+1]=myArray[i][j+1]+myArray[i][j]
                myArray[i][j]=0
                
                
while True:
    print myArray[0][0],"\t",myArray[0][1],"\t",myArray[0][2],"\t",myArray[0][3],"\n"
    print myArray[1][0],"\t",myArray[1][1],"\t",myArray[1][2],"\t",myArray[1][3],"\n"
    print myArray[2][0],"\t",myArray[2][1],"\t",myArray[2][2],"\t",myArray[2][3],"\n"
    print myArray[3][0],"\t",myArray[3][1],"\t",myArray[3][2],"\t",myArray[3][3],"\n"
    user_input = raw_input("u for upward direction, d for downwards, l for left and r for Right")
    users_choice(myArray,user_input)
    listfori = []
    listforj = []
    count = 0
    for i in range(0,4):
        for j in range(0,4):
            if myArray[i][j]==0:
                count+=1
                listfori.append(i)
                listforj.append(j)
    if count > 0:
        if count > 1:
            randomindex = listfori.index(random.choice(listfori))
            myArray[listfori[randomindex]][listforj[randomindex]]=2
        else:
            myArray[listfori[0]][listforj[0]]=2
    else:
        break
print "Game over"