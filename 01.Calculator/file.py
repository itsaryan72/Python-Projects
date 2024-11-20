# Make a calculator
# perform all operations
# use switch case and if else condition
# ask to perform calculation again if yes repeat else exit




def addition(a,b):
    return a+b

def subtraction(a,b):
    return a-b

def multiplication(a,b):
    return a*b

def division(a,b):
    return a//b



def calculator():
    while True:
        try:
            a = int(input("Enter your first number :"))
            b = int(input("Enter your second number :"))
        except ValueError:
            print("Invalid input")
            continue

        print("Operations:")
        print("1.Addition")
        print("2.Subtraction")
        print("3.Multiplication")
        print("4.Division")
        print("5.Exit")

        ch = input("Enter your choice :")
        
        if ch == '1':
            result = addition(a,b)
            print(f"The addition of both numbers is:{result}")
        
        elif ch == '2':
            result = subtraction(a,b)
            print(f"The addition of both numbers is:{result}")
        
        elif ch == '3':
            result = multiplication(a,b)
            print(f"The addition of both numbers is:{result}")
        
        elif ch == '4':
            result = division(a,b)
            print(f"The addition of both numbers is:{result}")

        elif ch == '5':
            exit()

        else:
            print("Invalid input")

        repeat = input("Do you want to perform another calculation? (y/n): ")
        if repeat!= 'y':
            print("Exiting the calculator. Goodbye!")
            break


calculator()
