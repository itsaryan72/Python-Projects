# Unit Converter:Create a program that converts between different units (length, weight, temperature, etc.).

def lengthConverter():
    print("\nLength Conversion:")
    print("1.Meters to Kilometers")
    print("2.Kilometers to Miles")
    print("3.Miles to Yards\n")

    x = float(input("Enter your choice="))
    y = int(input("Enter the value to convert="))

    if x == 1:
        res = y/1000
        print(f"The {y} Meters is equal to {res} Kilometers.")
    
    elif x == 2:
        res = y*0.621
        print(f"The {y} Kilometers is equal to {res} Miles.")

    elif x == 3:
        res = y * 1760
        print(f"The {y} Miles is equal to {res} Yards.")

    else:
        print("Please enter a valid choice!!")

def weightConverter():
    print("\nWeight Conversion:")
    print("1. Kilograms to Pounds")
    print("2. Pounds to Ounces")
    print("3. Grams to Kilograms\n")

    x = int(input("Enter your choice="))
    y = int(input("Enter the value to convert="))

    if x == 1:
        res = y*2.20
        rounded_value = round(res,2)
        print(f"The {y} kilogram is equal to {rounded_value} Pounds.")
    
    elif x == 2:
        res = y*16
        print(f"The {y} Pounds is equal to {res} Ounces.")

    elif x == 3:
        res = y/1000
        print(f"The {y} Grams is equal to {res} Kilograms.")

    else:
        print("Please enter a valid choice!!")

def tempConverter():
    print("\nTemperature Conversion:")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Celsius to Kelvin\n")

    x = int(input("Enter your choice="))
    y = int(input("Enter the temperature value="))

    if x == 1:
        res = (y* 9/5) + 32
        print(f"The {y} celsius is equal to {res} Fahrenheit.")

    elif x == 2:
        res = (y - 32) * 5/9
        print(f"The {res} Fahrenheit is equal to {res} Celsius.")
    
    elif x == 3:
        res = y + 273.15
        print(f"The {y} celsius is equal to {res} Kelvin.")

    else:
        print("Please enter a valid choice!!")


def main():
    print("Welcome to Converter System😃")

    while True:
        print("\n1.Length Converter")
        print("2. Weight Converter")
        print("3. Temperature Converter\n")
        
        try:
            user_input = int(input("Enter your choice="))
        except ValueError:
            print("No string or special character is allowed to enter here.")

        if user_input == 1:
            lengthConverter()

        elif user_input == 2:
            weightConverter()

        elif user_input == 3:
            tempConverter()
        
        else:
            print("Please enter a valid choice!!")

main()