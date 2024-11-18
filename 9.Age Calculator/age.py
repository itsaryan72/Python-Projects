#9. Age Calculator:Write a program that calculates your age based on your birthdate.

from datetime import datetime

def calculate_age():
    birthday_input = input("Enter your birthdate (dd-mm-yyyy):")
    birthdate = datetime.strptime(birthday_input,"%d-%m-%Y")

    today = datetime.today()

    age = today.year - birthdate.year

    if today.month < birthdate.month or (today.month == birthdate.month and today.day < birthdate.day):
        age -= 1

    print(f"You are {age} years old.")

calculate_age()