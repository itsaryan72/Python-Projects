#Temperature Converter: Build a program that converts temperatures between Fahrenheit and Celsius.
# F = (9/5)*c + 32
# C = (F - 32) * (5/9)

def convertToCelsius(F):
    return ((F-32) * (5/9))

def convertToFahrenheit(C):
    return ((9/5)*C + 32)



def tempConverter():        

        while True:
            print("Welcome to temperature converter:")
            print("1. Fahrenheit to Celsius")
            print("2. Celsius to Fahernheit")
            x = int(input("Enter your choice="))
            if x>2 or x<=0:
                print("please select the correct option to use our Services!!!")


            try:
                if(x==1):
                    F=int(input("Enter temperature in Fahrenheit:"))
                    res = convertToCelsius(F)
                    print(f"{F}°C is equal to: {res:.2f}°C")

                elif (x==2):
                    C=int(input("Enter temperature in Celsius:"))
                    res = convertToFahrenheit(C)
                    print(f"{C}°C is equal to: {res:.2f}°F")


            except ValueError:
                print("Invalid input! Please enter valid number")
            
            playAgain = input("Do you want to convert again:(y/n)")
            if playAgain != 'y':
                print("Thanks for using temperature converter!")
                break


tempConverter()