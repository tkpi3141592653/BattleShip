from getpass import getpass
from random import choice

board = []

for x in range(0,3):
  board.append(["O"] * 3)

def print_board(board):
  print("")
  for row in board:
    print (" ".join(row))
  print("")
  
print("Let's play BATTLESHIP!")

def getRow():
    x = int(getpass("Which row do you want to hide your ship? (0-2) "))
    return x

def getColumn():
    x = int(getpass("Which column do you want to hide your ship? (0-2) "))
    return x

def getName():
    name = input("What is your name? ")
    return name

shipNameList = []
nameList = []

def playPreparation():
    while (input("Entered all?") != "yes"):
        n = getName()
        a = getRow()
        b = getColumn()
        shipNameList.append([n,[a,b]])
        nameList.append(n)
        masterNameList.append(n)
    
    return shipNameList, nameList, masterNameList 




#print(shipList)



def guessRow():
    x = int(input("Guess Row(0-2): "))
    return x

def guessColumn():
    x = int(input("Guess Column(0-2): "))
    return x

def whoGuess(nameList):
    return choice(nameList)

masterNameList = []
nameList2 = []
lostThisTime =[]
lostPlayers = []
#---------------------------Game Start--------------------------------------


def play():
    numberOfPlayers = len(nameList)
    while (numberOfPlayers > 1):
        print_board(board)
        who = whoGuess(nameList)
        
        nameList2.append(who)

        print(who, "please make the guess")
        guess_row = guessRow()
        guess_col = guessColumn()
        for entry in shipNameList:
            if (entry[1][0] == guess_row and entry[1][1] == guess_col):
                
                lostPlayers.append(entry[0])
                lostThisTime.append(entry[0])
                for ppl in nameList:
                    if ppl in lostPlayers:
                        del(nameList[nameList.index(ppl)])
        
        for ppls in nameList2:
            if ppls in lostPlayers:
                del(nameList2[nameList2.index(ppls)])
        
        del(nameList[nameList.index(who)])
        if (len(nameList) == 0):
            for names in nameList2:
                nameList.append(nameList2[nameList2.index(names)])
            nameList2.clear()

        if (lostThisTime != []):
            board[guess_row][guess_col] = "*"
            print("You guessed correctly!")
            print("You found:")
            print(lostThisTime)
            numberOfPlayers -= len(lostThisTime)
            while len(lostThisTime) != 0:
                del(lostThisTime[0])
        else:
            board[guess_row][guess_col] = "X"
            print("You haven't found anyone this time.")
        
        print("Number of players remaining: ", numberOfPlayers)

    if numberOfPlayers == 1:
        print("The winner is ", nameList[0], "! Congratulation!")
    elif numberOfPlayers < 1:
        print("You have got a draw!")    

    

playPreparation()
play()


