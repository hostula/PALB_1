
An Armstrong number is a three-digit integer that is equal to the sum of the cubes of each digit. Find all Armstrong 
numbers among three-digit integers and print them as follows.
# Find Armstrong numbers among 3-digit integers

for num in range(100, 1000):
    # Extract digits
    hundreds = num // 100
    tens = (num // 10) % 10
    ones = num % 10

    # Check Armstrong condition using compound expression
    if num == (hundreds**3 + tens**3 + ones**3):
        print(num, "is an Armstrong number")
