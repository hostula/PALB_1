# Write a program that takes two random integers as input and lists them from smallest to largest.
# Program to list two different integers from smallest to largest

# Take two integer inputs from the user
a = int(input("Enter the first integer: "))
b = int(input("Enter the second integer: "))

# Check if the integers are not the same
if a == b:
    print("The integers must be different.")
else:
    # Sort and display them in ascending order
    if a < b:
        print(a, b)
    else:
        print(b, a)
