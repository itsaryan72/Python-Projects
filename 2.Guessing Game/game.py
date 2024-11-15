# This is my second project where I will be making a guessing number
# steps to built this project are as follows:
# 1. ask the user to think of any number
# 2. randomly generate the number from 0 to 100
# 3. compare the user's guess with the generated number
# 4. provide feedback to user 
#     - too low
#     - too high
#     - correct

import random

def guessingGame():
    print("Welcome to guessing game")

    while True:
        x = random.randint(1,100)
        print("I have a picked a number between 1 to 100")

        y = 10

        for i in range(y):
            try:

                user = int(input("Enter your guess:"))
                
                if user>x:
                    print("too high")
                
                elif user<x:
                    print("too low")

                elif user == x:
                    print("Correct")
                    print("You've guessed it right!")
                    break

                else:
                    print("please input valid numbers")
            except ValueError:
                print("Invalid input! please enter valid input")

        playAgain = input("Do you want to continue playing (y/n)").lower()
        if playAgain != 'y':
            print("Thanks for playing")
            break
    

guessingGame()