
def largest_num(a, b, c):


   if a > b and a > c:
       return "A", a
   elif b > a and b > c:
       return "B", b
   else:
       return "C", c


a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

    

letter, largest = largest_num(a, b, c)
print("Letter", letter, "is the largest number with a value of", largest)

