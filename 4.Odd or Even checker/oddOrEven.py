#Odd or Even Checker - Write a program that checks whether a number is odd or even.

def checkNumber():
    while True:
        print("Welcome to odd even checker!!")
        x = int(input("Enter any number="))

        if x == 0:
            print("It's a zero")
        elif x % 2 == 0:
            print("It is an even number")
        else:
            print("It is an odd number")

        repeat = input("Do you want to continue(y/n):")
        if(repeat!='y'):
            print("Welcome!")
            break

checkNumber()