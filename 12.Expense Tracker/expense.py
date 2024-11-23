#Expense Tracker:Build an app that helps users track their daily expenses and calculate total expenses.

def track_expense():

    expenses = []

    def createNewAcc(amount,category,date,description):
        expense = {
        "amount": amount,
        "category": category,
        "date": date,
        "description": description
        }
        expenses.append(expense)


    def viewExpenses():
        print("\n")
        for expense in expenses:
                print(f'{expense}')
        print("\n")
            

    def calculateSum():
        total = sum(expense["amount"] for expense in expenses)
        print(f"\nTotal: {total}\n")


    def filteredExpense():
        category = input("\nEnter the category you want to filter=").lower()
        found = False
        for expense in expenses:
            if expense['category'] == category:
                print(f"\n{expense}\n")
                found = True
        if not found:
                print("Category doesn't exists!!\n")

        

    print("Welcome to Expense Tracker")
    while True:
        print("1. Add new expense")
        print("2. View all expenses")
        print("3. Calculate sum of total expenses")
        print("4. Filter expenses by category")
        print("5. Exit")

        try:
            user_input = int(input("Enter your choice="))
        except ValueError:
            print("Enter a valid choice!")

        if user_input == 1:
            #amount category date description
            amount = int(input("\nEnter the amount="))
            category = input("Enter the category=")
            date = input("Enter date (YYYY-MM-DD):")
            description = input("Enter description for it=")
            createNewAcc(amount,category,date,description)
            print("Your expense has been stored successfully!\n")

        elif user_input == 2:
            viewExpenses()

        elif user_input == 3:
            calculateSum()

        elif user_input == 4:
            filteredExpense()
        
        elif user_input == 5:
            print("Welcome Again🤗!")
            exit()
        
        else:
            print("Welcome🤗")
            break
            

track_expense()