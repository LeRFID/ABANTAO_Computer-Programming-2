def abantao_function():
    w = int(input("Enter first number: "))
    y = int(input("Enter second number: "))
    z = int(input("Enter third number: "))
    
    x = 300
    letters = [w, y, z]
    
    if w == y == z:
        closest = w
        print(f"w is {w}, y is {y}, and z with the value of {z} are all equal, therefore all numbers are closest to {x}")
    else:
        closest = min(letters, key=lambda n: abs(n - x))
        print(f"The closest number to {x} is {closest}")

abantao_function()