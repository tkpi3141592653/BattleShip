namelist = []

while input("exit?")!= "yes":
    namelist.append(input("What is the player name? "))

from random import choice

numberOfPlayerSelected = 0
playerList = []

def playerSelection(namelist):
    return choice(namelist)

while numberOfPlayerSelected < 5:
    playerList.append(playerSelection(namelist))
    del(namelist[namelist.index(playerList[numberOfPlayerSelected])])
    numberOfPlayerSelected += 1

print(playerList)