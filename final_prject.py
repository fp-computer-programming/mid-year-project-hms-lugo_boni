# Ryan Lugo, Mat

# print("    1    2    3    4    5    6    7    8   9   10","\n1  [ ]  [ ]  [ ]  [ ]  [ ]  [ ]  [ ]  [ ] [ ]  [ ]")

# Long list of empty arrays to store for each part of a ship that's in it
# First number is top, second is side

import time
import random

# Row 1
one_one = []
one_two = []
one_three = []
one_four = []
one_five = []
one_six = []
one_seven = []
one_eight = []
one_nine = []
one_ten = []

# Row 2
two_one = []
two_two = []
two_three = []
two_four = []
two_five = []
two_six = []
two_seven = []
two_eight = []
two_nine = []
two_ten = []

# Row 3
three_one = []
three_two = []
three_three = []
three_four = []
three_five = []
three_six = []
three_seven = []
three_eight = []
three_nine = []
three_ten = []

# Row 4
four_one = []
four_two = []
four_three = []
four_four = []
four_five = []
four_six = []
four_seven = []
four_eight = []
four_nine = []
four_ten = []

# Row 5
five_one = []
five_two = []
five_three = []
five_four = []
five_five = []
five_six = []
five_seven = []
five_eight = []
five_nine = []
five_ten = []

# Row 6
six_one = []
six_two = []
six_three = []
six_four = []
six_five = []
six_six = []
six_seven = []
six_eight = []
six_nine = []
six_ten = []

# Row 7
seven_one = []
seven_two = []
seven_three = []
seven_four = []
seven_five = []
seven_six = []
seven_seven = []
seven_eight = []
seven_nine = []
seven_ten = []

# Row 8
eight_one = []
eight_two = []
eight_three = []
eight_four = []
eight_five = []
eight_six = []
eight_seven = []
eight_eight = []
eight_nine = []
eight_ten = []

# Row 9
nine_one = []
nine_two = []
nine_three = []
nine_four = []
nine_five = []
nine_six = []
nine_seven = []
nine_eight = []
nine_nine = []
nine_ten = []

# Row 10
ten_one = []
ten_two = []
ten_three = []
ten_four = []
ten_five = []
ten_six = []
ten_seven = []
ten_eight = []
ten_nine = []
ten_ten = []

# Ships and how many rows they take
Carter = 5
Battleship = 4
Cruiser = 3
Submarine = 3
Destroyer = 2

# Ships table so we can compare choice
ships = ["carter","battleship","cruiser","submarine","destroyer"]

print("Hello user, and welcome to battleships!\n If you want to play enter 1, if you want to see the credits enter 2, if you want to quit enter 3.")

def clearConsole():
    print('\n'*150)

def coin_flip():
    number = random.randint(1,2)
    if number == 1:
        return "Heads"
    else:
        return "Tails"

def shipSelect(ship,top,side,rotation):
     
     for i,v in enumerate(ships):
         if str.lower(ship) == v:
             
             list.remove(v)

def start_game(startingPosition):
    if startingPosition == 1:
        clearConsole()
        print("So since you are first, you get to select your ships positions first.")
        print("\nNow you are going to select your ship, and then put in which Top row, then bottom row you want it in. (Rotate it type R as the last one, if you don't leave it blank)")
        
        shipSelection = input("Ship: ")
        topRow = input("Top Row: ")
        sideRow = input("Side Row: ")
        rotation = input("Rotate?(Y = yes, N = no): ")
        shipSelect()
    elif startingPosition == 2:
        clearConsole()
        print("So since you are second, you get to select your ships positions after the AI.")

def user_choice(choice):
    clearConsole()
    if choice == "1":

        print("Flip a coin and if land heads you go first, if you land tails you go second. (PRESS ENTER TO CONTINUE)")
        input("")
        clearConsole()

        print("Flipping....")
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

user_choice(input(""))