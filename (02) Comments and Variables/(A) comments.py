"""
Fibonacci sequence generator
This program prints the first n numbers in the Fibonacci sequence but we focus on the use of comments.
"""

n = 10  # Number of Fibonnacci umbers to print

a = 0  # First number in the sequence
b = 1  # Second number in the sequence

print(a)  # Print the first number
print(b)  # Print the second number

for i in range(n - 2):  # Loop to print the next numbers
    c = a + b  # Calculate the next number
    print(c)  # Print the next number
    a = b  # Update a to the previous b
    b = c  # Update b to the new c

'''
Comments in Python start with the hash symbol or can use triple quotes for docstrings.
They are ignored by the Python interpreter and are used to explain code.
'''