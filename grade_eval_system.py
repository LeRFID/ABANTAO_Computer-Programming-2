grade1 = float(input("Enter your first grade: "))
grade2 = float(input("Enter your second grade: "))

final_grade = (grade1 + grade2) / 2
print("Average grade:", final_grade)

if final_grade >= 76:
    print("Passed")
else:
    print("Failed")