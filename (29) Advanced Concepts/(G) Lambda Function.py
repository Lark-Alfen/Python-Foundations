"""
Lambda Functions in Python

Lambda functions are small, anonymous functions defined with the lambda keyword. They are useful for creating simple, one-line functions without formally defining them using def.

Key Concepts:
- Lambda functions can take any number of arguments but only have one expression.
- The result of the expression is automatically returned.
- Lambda functions are often used for short, throwaway operations, especially as arguments to functions like map, filter, and sorted.
- For more complex logic, use regular def functions.

Example Explained:
"""

def add(a, b):
    return a + b

print(add(5, 10))  # Output: 15
print(input("Press Enter to continue..."))

# Simple lambda function for addition
LDadd = lambda a, b: a + b
print(LDadd(5, 10))  # Output: 15
print(input("Press Enter to continue..."))

"""
Explanation:
- The add function uses def to define a regular function for addition.
- LDadd is a lambda function that does the same thing in one line.
- Both can be called with two arguments and return their sum.
"""

# Complex use case: Filtering even numbers

e = {}
def odd_even(*args):
    for i in args:
        if i % 2 == 0:
            e[i] = "even"
        else:
            e[i] = "odd"
odd_even(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(e)  # Output: {1: 'odd', 2: 'even', 3: 'odd', 4: 'even', 5: 'odd', 6: 'even', 7: 'odd', 8: 'even', 9: 'odd', 10: 'even'}
print(input("Press Enter to continue..."))

# Lambda function for the same task
LDodd_even = lambda *args: {i : "even" if i % 2 == 0 else "odd" for i in args}
print(LDodd_even(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))  # Output: {1: 'odd', 2: 'even', 3: 'odd', 4: 'even', 5: 'odd', 6: 'even', 7: 'odd', 8: 'even', 9: 'odd', 10: 'even'}

"""
Explanation:
- The even function uses def and a for loop to collect even numbers from the arguments.
- LDeven is a lambda function that uses a list comprehension to do the same thing in one line.
- Both approaches return a list of even numbers from the input.
- Lambda functions are best for simple, short operations; use def for more complex logic or when you need a named function.
"""

"""
Lambda Function for Dictionary Comprehension: Odd/Even Labeling

This lambda function combines the power of lambda expressions and dictionary comprehensions to label numbers as 'even' or 'odd'.

Core Logic:
LDodd_even = lambda *args: {i : "even" if i % 2 == 0 else "odd" for i in args}

How it works:
- *args collects all positional arguments into a tuple (e.g., (1, 2, 3, 4, 5)).
- The dictionary comprehension iterates over each i in args.
- For each i, it checks if i % 2 == 0:
    - If True, the value is 'even'.
    - If False, the value is 'odd'.
- The result is a dictionary where each key is the input number and the value is either 'even' or 'odd'.

Example Usage:
LDodd_even = lambda *args: {i : "even" if i % 2 == 0 else "odd" for i in args}

print(LDodd_even(1, 2, 3, 4, 5))  # Output: {1: 'odd', 2: 'even', 3: 'odd', 4: 'even', 5: 'odd'}

"""



