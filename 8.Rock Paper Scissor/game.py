#Build a simple Rock, Paper, Scissors game in Python where a player competes against the computer. 
#Rock beats Scissors
#Scissors beats Paper
#Paper beats Rock

import random

options = ["Rock","Paper","Scissor"]


def play():

    while True:
        print("\nWelcome to Rock, Paper & Scissor game!\n")
        print("1.Rock")
        print("2.Paper")
        print("3.Scissor\n")


        try:
            user_input = input("Select your choice=")
        except ValueError:
            print("Select valid options!!")

        computer = random.choice(options)
        
        if (user_input == 'Rock' and computer=='Scissors') or (user_input == 'Scissors' and computer == 'Paper') or (user_input=='Paper' and computer=='Rock'):
            print(f"User: {user_input} & Computer: {computer}")
            print("You won! ✅")

        elif (user_input == computer):
            print(f"User: {user_input} & Computer: {computer}")
            print("It's a tie")
        
        else:
            print(f"User: {user_input} & Computer: {computer}")
            print("You Loose! ❌")

        replay = input("Do you want to play again(y/n):")
        if replay != 'y':
            print("Welcome!")
            break
        
            
play()