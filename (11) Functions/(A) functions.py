"""
Functions in Python

A function is a reusable block of code that performs a specific task. Functions help organize code, 
avoid repetition, and make programs easier to read and maintain.

You define a function using the 'def' keyword, followed by the function name and parentheses 
(with optional arguments).
"""

print("--Functions in Python--\n")

# Function without arguments
print("Function without arguments:")
def greet():
    print("Hello! This is a function without arguments.")

greet()
input("Press Enter to continue...")

"""
Explanation:
- 'greet' is a function that takes no arguments.
- You call it by writing greet().
- Useful for actions that don't need input.
"""

input("Press Enter to continue...")

# Function with arguments
print("\nFunction with arguments:")
def add(a, b):
    print(f"Sum of {a} and {b} is {a + b}")

add(5, 7)
input("Press Enter to continue...")

"""
Explanation:
- 'add' is a function that takes two arguments (a and b).
- You call it by writing add(5, 7).
- Arguments allow you to pass values to the function for processing.
"""

# Types of arguments
print("\nTypes of function arguments:")

# Positional arguments
print("Positional arguments:")
def show_positional(x, y):
    print(f"x = {x}, y = {y}")

show_positional(10, 20)  # x=10, y=20
input("Press Enter to continue...")

# Keyword arguments
print("Keyword arguments:")
def show_keyword(x, y):
    print(f"x = {x}, y = {y}")

show_keyword(y=30, x=40)  # x=40, y=30
input("Press Enter to continue...")

# Default arguments
print("Default arguments:")
def show_default(x, y=50):
    print(f"x = {x}, y = {y}")

show_default(60)  # x=60, y=50 (default)
show_default(70, 80)  # x=70, y=80
input("Press Enter to continue...")

"""
Explanation:
- Positional arguments: Values are assigned to parameters in the order they are passed.
- Keyword arguments: Values are assigned by parameter name, not order.
- Default arguments: Parameters can have default values, used if no value is provided.
- You can mix these types for flexible function calls.
"""

"""
Summary:
- Functions are reusable blocks of code.
- Arguments let you pass values to functions.
- Types of arguments: positional, keyword, default.
- Use input("Press Enter to continue...") for step-by-step review.
"""
