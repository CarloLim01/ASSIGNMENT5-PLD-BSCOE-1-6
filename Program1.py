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

grade = float (input("Enter your Grade: "))

if grade <= 100 and grade >= 97:
    print("Grade/Mark: 1.0")
    print("Description: Excellent")