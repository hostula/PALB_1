
#Among the positive natural numbers other than 1, a number that is not prime is called a composite number. Print the 
prime and composite numbers from 2 to 12 as follows.
# Print prime and composite numbers from 2 to 12

for num in range(2, 13):
    is_prime = True
    
    # Check if number is prime
    for i in range(2, num):
        if num % i == 0:   # compound condition check happens here logically
            is_prime = False
            break
    
    # Using if statement
    if is_prime and num != 1:
        print(num, "is a Prime number")
    else:
        print(num, "is a Composite number")
