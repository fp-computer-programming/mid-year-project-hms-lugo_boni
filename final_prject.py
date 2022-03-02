# Ryan Lugo, Mat

# print("    1    2    3    4    5    6    7    8   9   10","\n1  [ ]  [ ]  [ ]  [ ]  [ ]  [ ]  [ ]  [ ] [ ]  [ ]")

# Long list of empty arrays to store for each part of a ship that's in it
# First number is top, second is side

from re import S
import time
import random

# Tables for plr and ai to be accessed later for ships
# 0 = water , 1 = Ship, 2 = Hit, 3 = Miss
plrTable = [[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0]]
aiTable = [[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0]]
guessedTable = [[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0]]


# Visible plr Board
board = []

# Ships table so we can compare choice
ships = {"carrier":5,"battleship":4,"cruiser":3,"submarine":3,"destroyer":2}
aiShips = {"carrier":5,"battleship":4,"cruiser":3,"submarine":3,"destroyer":2}

def wait(wait):
    time.sleep(wait)

def clearConsole():
    print('\n'*150)

def printShips():
    for i,v in enumerate(plrTable):
        print(v)

def printAI(): #testing purposes only
    for i,v in enumerate(aiTable):
        print(v)

def printGuesses():
     for i,v in enumerate(guessedTable):
        print(v)

def coin_flip():
    number = random.randint(1,2)
    if number == 1:
        return "Heads"
    else:
        return "Tails"

# Loop var
loopSelection = True

def shipSelect():
    global loopSelection

    clearConsole()
    print("Now you are going to select your ship, and then put in which Top row, and bottom row that you want it in.")
     
    while loopSelection == True:
        if len(ships) > 0:
            wait(4)
            clearConsole()

            printShips()
            print("\nShips left:",ships)
            ship = input("Ship: ")
            try:
                top = int(input("Top Row: "))
                side = int(input("Side Row: "))

                counter = 0
                checkCounter = 0
                noSpace = False

                for (i,v) in ships.items():
                    if str.lower(ship) == i: # Checking if they find the ship in the list
                        if top > 0 and side > 0 and plrTable[side-1][top-1] == 0: # checking if the player met the conditionals
                            while counter <  v:
                                if plrTable[side-1+counter][top-1] == 0:
                                    counter += 1
                                else:
                                    noSpace = True
                            if noSpace == True:
                                break
                            else:
                                while checkCounter < v:
                                    plrTable[side-1+checkCounter][top-1] = 1
                                    checkCounter += 1
                                del ships[i]
                            printShips()
                        else:
                            print("Try inputting it again.")
                            break

                    else:
                        print("Hmm, something you inputted wasn't put in correctly. Try again.")
            except:
                continue
        else:
            return True
            
def aiShipSelection():
    aiLoop = True

    while aiLoop:
          top = random.randint(1,10)
          side = random.randint(1,10)
          if aiTable[side-1][top-1] == 0:
              try:
                Selectedship = random.choice(list(aiShips.keys()))
                counter = 0
                checkCounter = 0
                noSpace = False
                for (i,v) in aiShips.items():
                  if Selectedship == i:
                    while counter < v:
                            if aiTable[side-1+counter][top-1] == 0:
                                counter += 1
                            else:
                             noSpace = True
                    if not noSpace:
                         while checkCounter < v:
                             aiTable[side-1+checkCounter][top-1] = 1
                             checkCounter += 1
                         del aiShips[Selectedship]
              except:
                  continue
                  print("..")
          if len(aiShips) < 1:
             aiLoop = False

def battle(pos):

    trying = True
    foundCounter = 0

    for v in aiTable: # Checking if the player beat the  AI
        for value in v:
            if value == 1:
                foundCounter += 1

    if foundCounter < 1:
        print("You beat the AI! Congratulations!")
        exit()
    foundCounter = 0

    for v in plrTable: # Checking if the AI beat the player
        for value in v:
            if value == 1:
                foundCounter += 1
    
    if foundCounter < 1:
        print("You lost to the AI... Sadge")
        exit()
    foundCounter = 0

    while trying:
        if pos == 1:
            clearConsole()
            print("It's your turn to choose a spot to shoot!(Remember 1-10)")
            print("\nGuesses So far:")
            printGuesses()
            print("\nYour ships:")
            printShips()
            top = int(input("Top: "))
            side = int(input("Side: "))

            if side > 0 and top > 0 and side < 11 and top < 11:
                if aiTable[side-1][top-1] == 1:
                    print("BOOM! You've just hit the other AI's ship!")
                    wait(4)
                    clearConsole()
                    aiTable[side-1][top-1] = 2
                    guessedTable[side-1][top-1] = 2
                    battle(2)
                elif aiTable[side-1][top-1] == 0:
                    print("Dang! You missed the other AI's ship!")
                    wait(4)
                    clearConsole()
                    aiTable[side-1][top-1] = 3
                    guessedTable[side-1][top-1] = 3
                    battle(2)
                elif aiTable[side-1][top-1] == 2:
                    print("You've just shot there before! Try again!")
                    wait(4)
                    clearConsole()
                else:
                    print("You've just shot there before! Try again!")
                    wait(4)
                    clearConsole()
            else:
                print("Try inputting again!")
                wait(2)
                continue
        
        elif pos == 2:
            clearConsole()
            print("The AI is now choosing his spot to shoot!")
            print("\nYour ships:")
            printShips()

            wait(5)
            top = random.randint(1,10)
            side = random.randint(1,10)
            if plrTable[side-1][top-1] == 0:
                plrTable[side-1][top-1] = 3
                clearConsole()
                print("The AI shot and missed!")
                wait(4)
                battle(1)
            elif plrTable[side-1][top-1] == 1:
                plrTable[side-1][top-1] = 2
                clearConsole()
                print("The AI shot and hit your ship!")
                wait(4)
                battle(1)
            elif plrTable[side-1][top-1] == 2:
                wait(2)
                continue
            elif plrTable[side-1][top-1] == 3:
                wait(2)
                continue
        else:
            print("Huh??")          

def start_game(startingPosition):
    global loopSelection
    
    if startingPosition == 1:
        clearConsole()
        print("So since you are first, you get to select your ships positions first.")
    
        if shipSelect() == True:
            loopSelection = False
            print("So since you selected your ships, it's now the AI's time to do so.")
            wait(4)
            clearConsole()
            print("Waiting for the AI to finish selecting....")
            aiShipSelection()
            print("..")
            wait(10)
            clearConsole()
            print("The AI has finished selecting his ships positions, it's now time to start!")
            wait(4)
            battle(startingPosition)

    elif startingPosition == 2:
        clearConsole()
        print("So since you are second, you get to select your ships positions after the AI.")
        wait(4)
        clearConsole()
        print("Waiting for the AI to finish selecting....")
        aiShipSelection()
        

        wait(10)
        clearConsole()
        print("The AI has finished selecting his ships positions, it's now your turn.")
        wait(4)

        if shipSelect() == True:
            loopSelection = False
            battle(startingPosition)
        

def user_choice(choice):
    clearConsole()
    if choice == "1":

        print("Flip a coin and if it lands heads you go first, if you land tails you go second. (PRESS ENTER TO CONTINUE)")
        input("")
        clearConsole()

        print("Flipping.")
        wait(1)
        clearConsole()
        print("Flipping..")
        wait(1)
        clearConsole()
        print("Flipping...")
        wait(2)
        clearConsole()

        coinflip = coin_flip()
        if coinflip == "Heads":
            print("You got heads so you go first..")
            wait(2)
            start_game(1)
        else:
            print("You got tails so you go second..")
            wait(2)
            start_game(2)
    elif choice == "2":
        print("Credits moment...\nRyan Lugo: Scripter/Designer\nMateo Bonilla: Scripter/Designer\nTeacher: Project Lead")
    elif choice == "3":
        print("Goodbye User..")
        exit()
    else:
        print("That is not a number, try again.")
        user_choice(input(""))


# Starting code
clearConsole()
print("Hello user, and welcome to battleships!\n If you want to play enter 1, if you want to see the credits enter 2, if you want to quit enter 3.")
user_choice(input(""))