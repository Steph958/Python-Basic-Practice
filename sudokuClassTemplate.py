LETTER="ABCDEFGHI"
class Sudoku(object):
    """A Sudoku object has methods to modify and inspect a sudoku board.
    It also can compare boards and iterate through empty spots on a board."""
    #########################
    # FYI, the solution is: #
    #       abc def ghi     #
    #     A 534|678|912     #
    #     B 672|195|348     #
    #     C 198|342|567     #
    #       ---+---+---     #
    #     D 859|761|423     #
    #     E 426|853|791     #
    #     F 713|924|856     #
    #       ---+---+---     #
    #     G 961|537|284     #
    #     H 287|419|635     #
    #     I 345|286|179     #
    #########################
    start=("53.678.1.","67.195..8","198.4.567",
           "8.9.6...3","4..8537.1","713.2.8.6",
           "961.3.28.",".87419..5",".4..86179") #遊戲起始的board(不會變動) >> 這個board後面以Sudoku.start的方式呼叫		   
    LETTER="ABCDEFGHI"
    
    def __init__(self):
        """This sets the board to the starting values."""
        # That means that we need to initialize an instance variable that holds
        # the board state. It should be a list that is a copy of the class
        # variable "start". In addition, we keep track of user mistakes, so
        # we need to set a counter to 0.
        self.start = list(Sudoku.start)   #變成清單之後表示可以變動了 >> 這個board後面以self.start的方式呼叫				self.counter = 0

    def __restart(self):
        """This restarts the board."""
        # This resets everything to the initial state, including the mistake
        # counter.
        # The way to accomplish this is to invoke the __init__() method.				return self.start, self.counter				
        
    #以下6個函數是要幹嗎??
    def __le__(self,other):  #<=
        """This compares two sudoku boards. If board "B" has every "." that 
        board "other" has and if it does not have any numbers where "other" 
        has a "." then we say that B <= other. (The meaning is that "B" has 
        no information that "other" doesn't also have). """
        #Hint: zip 		#???????????				self.board = list(zip(*self.start))   #self.board是經過zip函數處理的self.start >> 後面以self.board的方式呼叫				#the "self.board" is like:		#################################################		#[('5', '6', '1', '8', '4', '7', '9', '.', '.'), 		#('3', '7', '9', '.', '.', '1', '6', '8', '4'), 		#('.', '.', '8', '9', '.', '3', '1', '7', '.'), 		#('6', '1', '.', '.', '8', '.', '.', '4', '.'), 		#('7', '9', '4', '6', '5', '2', '3', '1', '8'), 		#('8', '5', '.', '.', '3', '.', '.', '9', '6'), 		#('.', '.', '5', '.', '7', '8', '2', '.', '1'), 		#('1', '.', '6', '.', '.', '.', '8', '.', '7'), 		#('.', '8', '7', '3', '1', '6', '.', '5', '9')]		##################################################				for i,j in self.board, self.other:           #loop through the 9 line-strings-pairs of the 2 boards
            for x,y in i,j:                        #loop through the 9 pairs of values on one line pair
                if x != ".":                    #If x != '.' then y & x must be the same if self<=other
                    return False              #Otherwise we know that it is not <=
        return True      #x是"."且y是"."或數字 
    def __ge__(self,other):  #>=
        """This is defined similarly to __le__()"""				 for i,j in self.board, self.other:                       for x,y in i,j:                                        if y == ".":                                       return False              
        return True     #x是"."或數字且y是"." #How can we use <= to solve this?
    def __eq__(self,other): #==
        """The two boards should have identical information""" 				 for i,j in self.board, self.other:                      for x,y in i,j:                                       if  x != y:                                        return False        
        return self.board==other  #不論x、y都可能是"."或數字，但無論如何兩者相同
    def __ne__(self,other):  #!=		    for i,j in self.board, self.other:                      for x,y in i,j:                                       if  x == y:                                        return False       
        return self.board!=other  #不論x、y都可能是"."或數字，但無論如何兩者不同
    def __lt__(self,other):  #<
        """ The < symbol indicates "<=" but not "==". """				for i,j in self.board, self.other:                      for x,y in i,j:                                       if  x != "." or y == ".":                                        return False                return self.board < other  #x只能是"."且y只能是數字 #How can some combination of <=,>=,==, and != solve this?
    def __gt__(self,other):  #>
        """ The > symbol indicates ">=" but not "==". But note: we are dealing
        with partial orders here. I mean: "print (A<B,A<=B,A==B,A>B,A>=B)" 
        could produce "False False False False False". """				for i,j in self.board, self.other:                      for x,y in i,j:                                       if  x == "." or y != ".":                                        return False                return self.board < other  #x只能是數字且y只能是"."  #How can some combination of <=,>=,==,!=,and < solve this?#####################################################################################################################################					#以上6個函數的說明#遊戲頁面有2個表格#self 表示最初起始的start(不會變動)#other 表示填寫過程、變動中的數獨表格#__lt__	小於(<)#self是"."，other是數字 >> self < other#__le__	小於等於(<=)#self是"."，而other對應的值可能是數字或"." >> self <= other#__eq__	等於(==)#1. other和self都是數字，但是他們恰巧相同 >> self == other#2. other和self都是"."#__ne__	不等於(!=)#other和self都是數字，但是他們恰巧不同 >> self != other (表示玩家出錯)#__gt__	大於(>)#other是"."，self是數字 >> self > other (理應不該發生，數獨有遊戲規則是不能去更動起始表格中已經是數字的值)#__ge__	大於等於(>=)#other是"."，而self對應的值可能是數字或"."  >> self >= other (理應不該發生，數獨有遊戲規則是不能去更動起始表格中已經是數字的值)#####################################################################################################################################

    def getcount(self):
        return self.counter   #Lets you access the instance varialble that counts mistakes 		#????????????????????

    def setcount(self):
        self.counter = counter #Lets you update the instance varialble that counts mistakes 		#???????????????????		

    def __getitem__(self,a):
        """This returns the value at the column and row position indicated by
        the tuple a. For example, if you type "print(B[1,0])" it will print 3. 
        Notice that Python turned the 1,0 into a tuple.
        If anything goes wrong, an error should not be raised. Instead, just
        return None."""				#已經對start使用了zip函數所以[1,0]才會是3		#output is the "tuple a" and is like:		#################################################		#[('5', '6', '1', '8', '4', '7', '9', '.', '.'), 		#('3', '7', '9', '.', '.', '1', '6', '8', '4'), 		#('.', '.', '8', '9', '.', '3', '1', '7', '.'), 		#('6', '1', '.', '.', '8', '.', '.', '4', '.'), 		#('7', '9', '4', '6', '5', '2', '3', '1', '8'), 		#('8', '5', '.', '.', '3', '.', '.', '9', '6'), 		#('.', '.', '5', '.', '7', '8', '2', '.', '1'), 		#('1', '.', '6', '.', '.', '.', '8', '.', '7'), 		#('.', '8', '7', '3', '1', '6', '.', '5', '9')]		##################################################
        try:
            (x,y)= input().split()    #Notice this interesting way to assign 2 variables at once						self.a = (x,y)
            return self.board[x][y]     #Return the character at that position.
        except:                   # This handles the case that the the requested position is invalid
            return None         # Here, return the built-in constant that means no-value			
    def __setitem__(self,a,b):
        """This allows you to say things like "B[2,0]=4" (which is, in fact, a
        a correct assignment -- as can be seen by looking at the solution class
        variable). When you type "B[2,0]=4, the parameter a gets the tuple
        (2,0) and the parameter b gets the integer 4.
        The effect of this method is to set the indicated position to the given
        value. But there are many ways that this might fail."""
        (x,y)=input().split()    #Assign 2 variables at once, just like __getitem__				self.a = (x,y)				self.b = b
        v = self.board[y][x]     # This uses __getitem__, but using "[x,y]" to do it.
        if v:        #表示選取位置的方式正確
            if Sudoku.start[y][x]!=".":    #表示所選位置最初就是數字的條件(遊戲規則上不可以去做更改)			                               #注意self.start(可變動)										   #Sudoku.start(不可變動)										   #self.board(經過zip後的self.start)										   #三者之間的差別                				raise TypeError("Position is fixed.")  
            elif b=="?":                   #在所選位置是數字(並非最初就是數字)的情形下賦予其值為"?" >> 玩家在進行錯誤修正
                if v != ".":                   
                    self.counter += 1         # >> Update the counter instance variable
                    r = list(self.board[y])   #This line saves the string of the row that we update
                    r[x] = "."                #Puts '.' in that position. Hint: strings are immutable
            elif b.isdigit() == False:      # 如果b不是數字的條件下
                raise TypeError("Only numbers from 1 to 9 are allowed.")
            else:                          #如果b是僅由數字組成、且v的位置上是"."、且無違反數字不可重複的規則 >> 能夠成功更動
                r=list(self.board[y])      #This line saves the string of the row that we update
                r[x] = b                  #Puts the b-value in the specified position.
                if __conflicted__():     #Tests to see if it is not __conflicted__()
                    if r[x]!=".": ...   # update the counter
                    return
                self.board[y]=r        # We do this when the move was rejected
                raise TypeError("Value conflicts with what's been placed.")
        else:                       #在v所指的位置沒有值的條件下，表示選取位置的方式錯誤
            raise TypeError("That is not a valid position.")

    def __iter__(self):
        """This initializes the iteraterator. The iterator is a tuple. The
        first value is the column, and the second is the row. 
        The initial value is the first position containing a "."."""
        for i in self.board:                             			if i.find(".") != -1:						    y = i.index(".")								break				
                                                     for j in self.start:		    			if i.find(".") != -1:			    				x = j.index(".")				break		self.location = (x,y)		    #Loop through the 9 rows of the board	#This creates an instance variable that is the tuple of the
    #(x,y) position of the first "." in this row.	#Note: Use the find method of the string of that row.    #Also note: there might not be any '.' to find. Then you get -1	# If you didn't get -1			    
                return ... # Return yourself. Hint review examples of __iter__								
        return ... # Return yourself. (In this case, there was no '.')

    def __next__(self):
        """This iteraterates through the unsolved postions on the board. It
        starts in the upper-left, and moves left-to-right then top-to-bottom"""
        # I leave this method up to you to write. Look at some example of
        # __next__ implementations to get an idea. I can give four hints:
        # 1. You want to itterate to the next '.', which might be in the same
        #    row or a later row.
        # 2. When you return the answer, it is not the new value that you just
        #    found. It is the value that you begin with.
        # 3. When you return the answer, you return two values: the x and y.
        # 4. When you reach the end, you raise StopIteration.        		for i,j in self.board, self.start:                             			if i.find(".") != -1 and if j.find(".") != -1:			    				x = j.index(".")								y = i.index(".")								return (x,y)												
    def __contains__(self,a):
        """If 2 values are given, they are the column and the row of a position
        the board. In this case, return a boolean indicating if that position
        is filled (ie, contains a digit).
        If just 1 value is given, then that value should be an integer between
        1 and 9. In this case, the meaning is very different. You will return a
        boolean indicating if any row doesn't contain the supplied digit. (The
        meaning here is that the supplied digit is not yet fully placed, so it
        is still "contained" in the search space.)"""
        if len(a) == 2: # If the parameter a has two values            			if self.board[a[0]][a[1]] is in ["1","2","3","4","5","6","7","8","9"]:
                				return True        #Boolean indicating if this position is a digit of string
        if a.isdigit() == True:     # If the parameter a is a string representing a digit
            return False
        for i in self.board:     #Loop through the 9 strings of the rows of the board
            if ...: # Tests if the value of parameter a is not in this string >> ???????????????????????????????????
                return True
        return False

    def __str__(self):
        """This displays the original and current boards, side-by-side.
        It involves concatenating strings. I've done some of it for you."""
        St="\n\n            Original:                  abc def ghi\n"
        for i in range(9):
            print(St+="            "+Sudoku.start[i][:3]+"|"+Sudoku.start[i][3:6]+"|"+Sudoku.start[i][6:]+"              "+Sudoku.LETTER[i]+" "+self.board[i][:3]+"|"+self.board[i][3:6]+"|"+self.board[i][6:]+"\n")
            if (i==2)or(i==5):
                print(St=St+"            ---+---+---                ---+---+---\n")
        St+="\n"
        return St

    def __ThreeLists(self):
        """This returns 3 lists. The first list is the 9 strings for the 9 
        rows. The second is for the 9 columns. The third is for the 9 3x3 
        squares."""
        from functools import reduce
        C1=[list(self.board[i]) for i in range(9)]
        C2=list(zip(*C1))
        COL=[reduce(lambda x,y:x+y,i) for i in C2]
        dim=[slice(3*i,3*i+3) for i in range(3)]
        SQ=list(reduce(lambda x,y:x+y, reduce(lambda x,y:x+y, list(zip(*C1[dim[i]]))[dim[j]])) for i in range(3) for j in range(3))
        return self.board,COL,SQ				#in another solution:		#C1 = [list(i) for i in start]         #C2 = list(zip(*C1))         #COL = [''.join(i) for i in C2]         #dim = [(i[:3],i[3:6],i[6:9] ) for i in COL]         #SQ = [''.join(i) for i in ( list(zip(*dim[:3]))+ list(zip(*dim[3:6])) + list(zip(*dim[6:9])) )] 

    def __conflicted__(self):
        """This returns true if any position violates any of the three rules
        (ie, if any row, column, or 3x3 square has more than one copy of a 
        digit)."""				#檢測同一欄有沒有重複數字				C1 = [list(i) for i in self.start] 					#C1 is like:		################################################		#[['5', '3', '.', '6', '7', '8', '.', '1', '.'],		#['6', '7', '.', '1', '9', '5', '.', '.', '8'],		#['1', '9', '8', '.', '4', '.', '5', '6', '7'], 		#['8', '.', '9', '.', '6', '.', '.', '.', '3'], 		#['4', '.', '.', '8', '5', '3', '7', '.', '1'],		#['7', '1', '3', '.', '2', '.', '8', '.', '6'],		#['9', '6', '1', '.', '3', '.', '2', '8', '.'],		#['.', '8', '7', '4', '1', '9', '.', '.', '5'],		#['.', '4', '.', '.', '8', '6', '1', '7', '9']]	    #################################################					for i in C1:		    if i is not in list(set(i))			    return False			else:			    return True							#檢測同一列中有沒有重複數字		C2 = [list(i) for i in self.board] 					#C2 is like:		###################################################		#[['5', '6', '1', '8', '4', '7', '9', '.', '.'],		#['3', '7', '9', '.', '.', '1', '6', '8', '4'], 		#['.', '.', '8', '9', '.', '3', '1', '7', '.'],		#['6', '1', '.', '.', '8', '.', '.', '4', '.'],		#['7', '9', '4', '6', '5', '2', '3', '1', '8'],		#['8', '5', '.', '.', '3', '.', '.', '9', '6'],		#['.', '.', '5', '.', '7', '8', '2', '.', '1'],		#['1', '.', '6', '.', '.', '.', '8', '.', '7'],		#['.', '8', '7', '3', '1', '6', '.', '5', '9']]        #################################################### 				for i in C2:		    if i is not in list(set(i))			    return False			else:			    return True						#檢測同一個3x3方塊中有沒有重複數字		        COL = [ ''.join(i) for i in C2]         #COL is like:        #['5618479..', '379..1684', '..89.317.', '61..8..4.', '794652318', '85..3..96', '..5.782.1', '1.6...8.7', '.87316.59']		        dim = [ ( i[:3],i[3:6],i[6:9] ) for i in COL ]         #dim is like:		#########################		#[('561', '847', '9..'), 		#('379', '..1', '684'), 		#('..8', '9.3', '17.'), 		#('61.', '.8.', '.4.'), 		#('794', '652', '318'), 		#('85.', '.3.', '.96'), 		#('..5', '.78', '2.1'), 		#('1.6', '...', '8.7'), 		#('.87', '316', '.59')] 		##########################	    SQ = [''.join(i) for i in ( list(zip(*dim[:3]))+ list(zip(*dim[3:6])) + list(zip(*dim[6:9])) ) ]         #SQ is like:		#['561379..8', '847..19.3', '9..68417.', '61.79485.', '.8.652.3.', '.4.318.96', '..51.6.87', '.78...316', '2.18.7.59'] 		#剛好每一項都是3x3方塊中的9個數字						for i in SQ:		    if i is not in list(set(i))			    return False			else:			    return True			    				def HasDoubleDigit(x):
            """This recieves a list of 9 strings, and returns true if any of
            them have more than one copy of any digit.""" >> ???????????????????????????????????????????????
            # I leave it up to you to write this function.
            (self.C1,self.C2,SQ) = self.__ThreeLists() # This assigns to three variables at once >> ????????????????????????????????????
            for i,j,k in aelf.C1, self.C2, SQ:		    			    if i is not in list(set(i)) and if j is not in list(set(j)) and if k is not in list(set(k)):							    return True          #This tests if any of the three variables HasDoubleDigit()

    def __could_be__(self,x,y):
        """This returns a list of numbers which the given column,row position
        could be. For example, suppose: the given row already has 1,4, and 7;
        the given column already has 1,2, and 3; the given 3x3 square already 
        has 9. Then, in that case, this function would return [5,6,8]."""
        (a,b,c) = self.__ThreeLists() # This assigns to three variables at once		        num = list(set(self.C1[a])) + list(set(self.C2[b])) + list(set(self.SQ))				num_lst = list(set(num))				could_be =[]				for i in [1,2,3,4,5,6,7,8,9]:		    if i is not in num_lst:			   could_be.append(i)			   		return could_be 				# This is a list comprehension. The elements of the list
        # will be all of the digits that are not in any of the
        # three lists assigned on the previous line.
        # Hint: those lists contain strings (eg, '1' not 1).
        # Hint: the 3x3 index is 3*(y//3)+x//3

    def issolved(self):
        """This function returns true if the board is solved (ie, the mutable
        copy has no "." symbols left)."""
        for i in self.board: # Loop through the 9 rows of the board
            if i.find(".") != -1: # Tests to see if you can find a '.'
                return False # If you can then the board isn't solved.
        return True

B = Sudoku()
def solve(B):
    """This function uses trial and error to obtain a solution to the remaining
    positions on the board. If the user has already made a mistake, however, 
    then the board is not solvable. In that case, the function will return the
    value False, and will leave the board unchanged."""
    for p in B:
        for c in B.__could_be__(*p):
            try:
                B[p[0],p[1]]=str(c)
                if B.issolved(): return True
                if solve(B): return True
            except: pass
        B[p[0],p[1]]='?'
        return False

if __name__ == "__main__":
    choice=input('\nValid inputs look like: "Aa=2". \nOther options: "test", "solve", "restart", "quit".\n\nHit enter to begin...')
    while (not B.issolved()) and (choice != "quit"):
        print(B)
        choice = input ("Enter your choice: ")
        if choice in [ "solve", "test" ]:
            v=B.getcount()
            C=[s for s in B.board]
            if(not solve(B)): print ("\n\nSorry, but your board has an error.")
            elif choice == "test": print ("\n\nThe board is solvable.")
            if choice == "test":
                for i in range(9):
                    B.board[i]=C[i]
                    B._Sudoku__cnt=v
        elif choice == "restart":
            B.__restart()        # This calls __restart(), which is private and hard to call
        elif choice != "quit":
            try:
                assert len(choice)==4 and choice[2]=='=',"Badly formatted choice."
                B[LETTER.lower().find(choice[1]),LETTER.find(choice[0])]=choice[3]
            except Exception as e:
                input (str(e)+"  Hit enter to try again...")
    print(B)
    if choice == "quit":
        print("Bye")
    else:
        print("Congratulations! You solved it with",B.getcount(),"corrections")
else:
    print((0,0) in B, [2,0] in B, "8" in B) # Should print: True, False, False
