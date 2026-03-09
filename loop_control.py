
while True:
    password = input("Enter your password: ")
    
    has_letter = False
    has_number = False

    for char in password:
        if char.isalpha():
            has_letter = True
        if char.isdigit():
            has_number = True


    if has_letter and has_number:
       print("Logged in successfully.")
       break
    else:
       print("Invalid password, try again.")