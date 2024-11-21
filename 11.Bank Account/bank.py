#11. Bank Account Management:Implement a program that allows users to create bank accounts, deposit and withdraw money, and check balances.


def Bank():
    print("Welcome to Our Bank Services!")
    data = [
            {'name':'aryan','age':21,'amt':23500},
            {'name':'mohit','age':25,'amt':14200}
        ]

    

    while True:
        print("\n1.Create a new bank account")
        print("2.Deposit money")
        print("3.Withdraw money")
        print("4.Check Balance")
        print("5.Exit\n")

        try:
            user_choice = int(input("Enter your choice="))
        except ValueError:
            print("Please enter number only from the given services.")

        

        if user_choice == 1:
            x = input("Enter your name:").lower()
            for person in data:
                if x == person['name']:
                    print('Your data has been found in our database!')
                    break
                    
                else:
                    age=input("Enter your age=")
                    amt=input("Enter the cash amount=")
                    data.append({'name':x,'age':age,'amt':amt})
                    print("Success! Your new account has been created.")
                    break
            
        elif user_choice == 2:
            x = input("Enter the name of your account:").lower()
            try:
                y = int(input("Enter the amount you want to insert?"))
                if y<=0:
                    print('Amount must be greater than 0.')
                    continue
            except ValueError:
                print("Please enter a valid amount.")
                continue

            account_found = False

            for person in data:
                if x == person['name'] :
                    person['amt'] = int(person['amt'])
                    person['amt'] += y
                    print(f"\nAmount:{y} has been deposited to account {x}")
                    print(f"Balance:{person['amt']}\n")
                    account_found = True
                    break

            if not account_found:
                print('please create your account first!')
                break

        elif user_choice == 3:
            x = input("Enter the name of your account:").lower().strip()
            try:
                y = int(input("Enter the amount you want to withdraw?"))
                if y<=0:
                    print('Amount must be a position number')
                    continue
            except ValueError:
                print('Invalid input! Please enter a valid number for the amount.')
                continue

            withdrawal_successful = False 

            for person in data:
                if x == person['name']:
                    person['amt'] = int(person['amt'])

                    if y>person['amt']:
                        print('Failure,Not sufficient funds in your bank account.')
                    else:
                        person['amt']-=y
                        print(f"The amount withdrawn is {y}.")
                        print(f"The remaining balance is={person['amt']}")
                        withdrawal_successful = True
                    break 
            if not withdrawal_successful:
                print('Account not found or withdrawal failed.')


        elif user_choice == 4:
            print("\n")
            for x in data:
                print(f'{x}')

        elif user_choice == 5:
            print("Welcome 🙏🏻")
            break
            
Bank()