# Ryan Lugo, Mat

# print("    1    2    3    4    5    6    7    8   9   10","\n1  [ ]  [ ]  [ ]  [ ]  [ ]  [ ]  [ ]  [ ] [ ]  [ ]")

# Long list of empty arrays to store for each part of a ship that's in it
# First number is top, second is side

import time
import random
from turtle import clear


# Loop var
loopSelection = True

# Ships and how many rows they take
Carter = 5
Battleship = 4
Cruiser = 3
Submarine = 3
Destroyer = 2

# Ships table so we can compare choice
ships = ["carter","battleship","cruiser","submarine","destroyer"]

def clearConsole():
    print('\n'*150)


def coin_flip():
    number = random.randint(1,2)
    if number == 1:
        return "Heads"
    else:
        return "Tails"

def shipSelect():

    clearConsole()
    print("Now you are going to select your ship, and then put in which Top row, and bottom row that you want it in.")
     
    while loopSelection == True:

        time.sleep(4)
        clearConsole()

        print("Ships left:",ships)
        ship = input("Ship: ")
        top = int(input("Top Row: "))
        side = int(input("Side Row: "))
        rotation = input("Rotate?(Y = yes, N = no): ")

        for i,v in enumerate(ships):
            if str.lower(ship) == v: # Checking if they find the ship in the list
                if top > 0 or side > 0 or str.lower(rotation) != "y" or str.lower(rotation) != "n": # checking if the player met the conditionals
                    print()
                    
                

                

def start_game(startingPosition):
    if startingPosition == 1:
        clearConsole()
        print("So since you are first, you get to select your ships positions first.")
    
        if shipSelect() == True:
            loopSelection = False

    elif startingPosition == 2:
        clearConsole()
        print("So since you are second, you get to select your ships positions after the AI.")
        time.sleep(4)
        clearConsole()
        print("Waiting for the AI to finish selecting....")
        time.sleep(10)
        clearConsole()
        print("The AI has finished selecting his ships positions, it's now your turn.")
        time.sleep(4)
        if shipSelect() == True:
            loopSelection = False
        

def user_choice(choice):
    clearConsole()
    if choice == "1":

        print("Flip a coin and if it lands heads you go first, if you land tails you go second. (PRESS ENTER TO CONTINUE)")
        input("")
        clearConsole()

        print("Flipping.")
        time.sleep(1)
        clearConsole()
        print("Flipping..")
        time.sleep(1)
        clearConsole()
        print("Flipping...")
        time.sleep(2)
        clearConsole()

        coinflip = coin_flip()
        if coinflip == "Heads":
            print("You got heads so you go first..")
            time.sleep(2)
            start_game(1)
        else:
            print("You got tails so you go second..")
            time.sleep(2)
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