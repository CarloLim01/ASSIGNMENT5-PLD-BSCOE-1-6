# Create a program that will ask for grade percentage. 
# Display the equivalent Grade/Mark and Description
# Example:
# Input grade: 87.6
# Grade/Mark: 1.75
# Description: Very Good
# grade/mark    percentage     description
# 1.0           100-97          Excellent
# 1.25          96-94           Excellent
# 1.5           93-91           Very Good
# 1.75          90-88           Very Good
# 2.0           87-65           Good
# 2.25          84-82           Good
# 2.50          81-79           Satisfactory
# 2.75          78-76           Satisfactory
# 3.0           75              Passing
# 5.0           74-65           Failure
# Inc.                          Incomplete
# W                             Withdrawn
# D                             Dropeed

status = input("Enter your grade: ")

if status == "Inc":
    print("Your status in is INCOMPLETE")
elif status == "W":
    print("Your status is WITHDRAWN")
elif status == "D":
    print("Your status is DROPPED")
else:
    grade = round(float(status))
    if grade <= 100 and grade >= 97:
        print("Grade/Mark: 1.0")
        print("Description: Excellent")
    elif grade <= 96 and grade >= 94:
        print("Grade/Mark: 1.25")
        print("Description: Excellent")
    elif grade <= 93 and grade >= 91:
        print("Grade/Mark: 1.5")
        print("Description: Very Good")
    elif grade <= 90 and grade >= 88:
        print("Grade/Mark: 1.75")
        print("Description: Very Good")
    elif grade <= 87 and grade >= 85:
        print("Grade/Mark: 2.0")
        print("Description: Good")
    elif grade <= 84 and grade >= 82:
        print("Grade/Mark: 2.25")
        print("Description: Good")
    elif grade <= 81 and grade >= 79:
        print("Grade/Mark: 2.5")
        print("Description: Satisfactory")
    elif grade <= 78 and grade >= 76:
        print("Grade/Mark: 2.75")
        print("Description: Satisfactory")
    elif grade == 75:
        print("Grade/Mark: 3.00")
        print("Description: Passing")
    else:
        print("Grade/Mark: 5.0")
        print("Description: Failure")

