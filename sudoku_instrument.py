#########################################################
# YOUR JOB IS TO FILL IN ALL OF THE "..." PARTS, BELOW: #
#########################################################

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

#######################################################################
# The board I give you is partially solved. The original board was:   #
# start=("53..7..1.","6..195...",".98....6.","8...6...3","4..8.3..1", #
#         "7...2...6",".6....28.","...419..5","....8..79")            #
#######################################################################

#######################################
# Here is the partially-solved board: #
start=("53.678.1.",
       "67.195..8",
       "198.4.567",
       "8.9.6...3",
       "4..8537.1",
       "713.2.8.6",
       "961.3.28.",
       ".87419..5",
       ".4..86179")

#####################################################
# The following two strings will be useful for you: #
LETTER="ABCDEFGHI"
letter="abcdefghi"

# Add a line here to make a mutable copy of "start" (but rows remain strings):
...

def solved():
    """This function returns true if the board is solved (ie, the mutable copy
    has no "." symbols left). It uses the find() method of strings."""
    ...
    
def display():
    """This function displays the original and current boards, side-by-side.
    It involves concatenating strings. I've done some of it for you."""
    print("\n\n%24s%18sabc def ghi"%("original:","")) #Achieves correct spacing
    for i in range(9):
       print(...)
       if (i==2)or(i==5):
           print("             ---+---+---                  ---+---+---")
    print("\n")

def choiceFormatIsGood(choice,chc):
    """This function looks at the provided string parameter, "choice", to test
    if it has the required format. The required format is that it must:
      - Have exactly 4 characters.
      - The 1st character must be an upper-case letter between 'A' and 'I'.
      - The 2nd character must be a lower-case letter between 'a' and 'i'.
      - The 3rd character must be '='.
      - The 4th character must be either a '?' or a digit between '1' and '9'.
        And you must use the isdigit() method as part of this test.
    The second parameter, "chc", is a list:
      - When this function is called, the list is passed in as an empty list.
      - When this function finishes (assuming that the format tests passed) the
        "chc" list will have three elements:
         - The 1st element is a number between 0 and 8, which corresponds to
           the value of the first letter (the one that is between 'A' and 'I').
         - The 2nd element is a number between 0 and 8, which corresponds to
           the value of the second letter (the one that is between 'a' and 'i')
         - The 3rd element is a string. Its value is choice[3].""" 
    ...

def choiceIsEmpty(...):
    """This function return true if the chosen position currently holds a '.'
    character.
    One special aspect of this function is that it receives either 1 or 2 
    parameters. The optional parameter is the board that you will check for
    the empty spot. When the parameter is not provided, then your mutable
    object is assumed. (The other possibility, as described below, is that
    "start" is passed in.)"""
    ...

def choiceDoesNotViolateRules(chc):
    """This function returns false if the choice would violate one of the 
    three Sudoku rules: the same digit cannot appear twice in the same 1)row, 
    2)column, or 3) 3x3 square.
    Note: The choice might actually be correct, but still return false -- if
          the player has earlier made an incorrect move."""
    def rowHasItAlready(chc):
        """This function returns true if the choice violates the rule that
        the same digit cannot appear twice in the same row."""
        ...

    def columnHasItAlready(chc):
        """This function returns true if the choice violates the rule that
        the same digit cannot appear twice in the same column."""
        ...

    def squareHasItAlready(chc):
        """This function returns true if the choice violates the rule that
        the same digit cannot appear twice in the same 3x3 square."""
        ...
        
    ...

def updateBoard(chc):
    """This function adds the chosen value to the chosen position of the
    mutable sudoku board object. 
    At the point where this function is called, you know that the position
    is empty and the chosen value is allowed.
    But the challenge is that each row is a string, but strings are imutable;
    so you have to replace it with a newly created string."""
    ...

input('Valid inputs look like: "Aa=2". Hit enter to begin...')
while not solved():
    #This loop plays the game.
    ...
    
