try:
    with open("new_text.txt", "x"):
        print("File created successfully!")

except FileExistsError:
    print("File already exists!")

while True:
    print("\nMESSAGING APP\n")
    print("a. Send a Message")
    print("b. View Messages")
    print("c. Exit")
    
    choice = input("\nEnter choice: ")
    
    if choice == 'a':
        message = input("\nEnter your text: ")
        
        if message.strip():
            try:
                with open("new_text.txt", "a") as f:
                    f.write(message + "\n")
                print("\Message sent successfully!")

            except Exception as e:
                print("\nError Sending the Message:", e)
        else:
            print("Message cannot be empty.")
    
    elif choice == 'b':
        try:
            with open("new_text.txt", "r") as f:
                messages = f.readlines()
                
                if messages:
                    print("\n--- Messages ---\n")
                    for msg in messages:
                        print(msg.strip())
                else:
                    print("No messages found.")

        except Exception as e:
            print("Error reading the message:", e)
    
    elif choice == 'c':
        print("Exiting the program....")
        break
    
    else:
        print("Invalid choice. Please enter again.")
