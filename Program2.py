# Create a program that ask 3 numbers. 
# Find the lowest number using only if-else statement.
# Display the lowest number

first = int(input("Enter first number: "))
second = int(input("Enter second number: "))
third = int(input("Enter third number: "))

if first < second and first < third:
    print(f"The lowest number is {first}.")
elif second < first and second < third:
    print(f"The lowest number is {second}.")
else:
    print(f"The lowest number is {third}.")
    