#Basic Countdown Timer:Implement a countdown timer that takes an input (number of seconds) and counts down.

import time

def basicTimer(seconds):
    while seconds > 0:
        print(f"Time left: {seconds} seconds")
        time.sleep(1)
        seconds -= 1
    print("Time's up!")

try:
    print("Welcome to our time machine 😎")
    user_input = int(input("Enter the countdown time in seconds:"))
    basicTimer(user_input)
except ValueError:
    print("Please enter valid input!")