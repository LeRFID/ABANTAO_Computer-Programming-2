ako = []

while True:
    print("\nUSER MENU")
    print("A. Show Users")
    print("B. Add User")
    print("C. Update User")
    print("D. Delete User")
    print("E. Exit")

    choice = input("Enter your choice: ")

    if choice == 'A':
        if len(ako) == 0:
            print("No users found.")
        else:
            print("\nUsers List:")
            for index, user in enumerate(ako):
                print(f"{index + 1}. {user}")
     
    elif choice == 'B':
        new_ako = input("Enter the name of the user that you want to add: ")
        ako.append(new_ako)
        print(f"{new_ako} has been added successfully!")
    
    elif choice == 'C':
        if len(ako) == 0:
            print("No users to be updated")
        else:
            for index, user in enumerate(ako):
                print(f"{index + 1}. {user}")
            try:
                ako_index = int(input("Enter the user's number to update: ")) - 1
                if 0 <= ako_index < len(ako):
                    updated_ko = input("Enter a new name: ")
                    ako[ako_index] = updated_ko
                    print("User updated successfully!")
                else:
                    print("Invalid user number.")
            except ValueError:
                    print("Please enter a valid number.")

    elif choice == 'D':
        if len(ako) == 0:
            print("No users found that can be deleted")
        else:
            for index, user in enumerate(ako):
                print(f"{index + 1}. {user}")
            try:
                notAko_index = int(input("Enter the user's number to delete:")) - 1
                if 0 <= notAko_index < len(ako):
                    removed_ako = ako.pop(notAko_index)
                    print(f"{removed_ako} has been deleted.")
                else:
                    print("Invalid user number.")
            except ValueError:
                    print("Please enter a valid number.")

    elif choice == 'E':
        print("Exiting program...")
        break

    else:
        print("Invalid choices. Please try again.")



                   
 