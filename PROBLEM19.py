#Write a code to print the following decorative output. In the first line, use only one '*' character with the operator * and 
number. In the second line, use only one '#' character and one space with the operator * and number.
Coding guideline: In the case of the first line, print in the same way as '*' * number n. The second line also uses the * 
operator
# Program to print decorative pattern using string multiplication

# Take input from user
n = int(input("Enter the number of repetitions: "))

# First line: print '*' using * operator
print('*' * n)

# Second line: print '# ' using * operator
print('# ' * n)
