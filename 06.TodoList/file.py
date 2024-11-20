#Simple To-Do List: Create a basic to-do list where you can add, remove, mark tasks as completed and exit.

def todo():
    myList = []  

    while True:
        print("\nWelcome to our Todo-list🔥")
        print("1. Add a task")
        print("2. Remove a task")
        print("3. View the list")
        print("4. Mark task as completed")
        print("5. Exit")

        try:
            user_input = int(input("Choose an option (1-5): "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if user_input == 1: 
            task_name = input("\nWhat task do you want to add? ")
            myList.append({"task": task_name, "status": "Pending"})
            print(f"'{task_name}' has been added to your list.")



        elif user_input == 2:  # Remove a task
            if not myList:
                print("\nYour list is empty!")
            else:
                print("\nTasks in the list:")
                for idx, task in enumerate(myList, start=1):
                    print(f"{idx}. {task['task']} - {task['status']}")
                task_to_remove = input("\nEnter the task name to remove: ")
                
                found = False
                for task in myList:
                    if task["task"] == task_to_remove:
                        myList.remove(task)
                        print(f"Task '{task_to_remove}' has been removed.")
                        found = True
                        break
                if not found:
                    print(f"Task '{task_to_remove}' not found in the list.")


        elif user_input == 3:  
            if not myList:
                print("\nYour list is empty!")
            else:
                print("\n🌟 Your To-Do List:")
                for idx, task in enumerate(myList, start=1):
                    print(f"{idx}. {task['task']} - {task['status']}")



        elif user_input == 4:  
            if not myList:
                print("\nYour list is empty!")
            else:
                print("\nTasks you can mark as completed:")
                for idx, task in enumerate(myList, start=1):
                    print(f"{idx}. {task['task']} - {task['status']}")
                try:
                    task_num = int(input("\nEnter the task number to mark as completed: "))
                    if 1 <= task_num <= len(myList):
                        myList[task_num - 1]["status"] = "Completed"
                        print(f"Task '{myList[task_num - 1]['task']}' marked as completed!")
                    else:
                        print("Invalid task number.")
                except ValueError:
                    print("Please enter a valid number.")



        elif user_input == 5:  
            print("Goodbye 🤗")
            break

        else:
            print("Invalid option. Please choose between 1 and 5.")

# Run the program
todo()
