"""
Input and Output in Python

This program demonstrates different ways to take input from the user and display output in Python.
"""

# --- Output in Python ---
print("--- Output Examples ---")

# Basic output
print("Hello, World!")  # Prints a simple string

# Output with multiple values
name = "Alice"
age = 25
print("Name:", name, "Age:", age)  # Prints multiple values separated by spaces

# Formatted output using f-strings (recommended)
print(f"My name is {name} and I am {age} years old.")  # f-string formatting

# Formatted output using format()
print("My name is {} and I am {} years old.".format(name, age))  # .format() method

# Raw output (shows escape characters as-is)
print(r"This is a raw string: C:\\Users\\Alice")  # r before string makes it raw

# Output with custom separator and end
print("A", "B", "C", sep="-")  # Prints: A-B-C
print("This is the first line.", end=" ")  # Changes end character from newline to space
print("This is on the same line.")

"""
Summary of Output:
- print() is used for output.
- You can print multiple values, use custom separators, and change the end character.
- f-strings and .format() allow formatted output.
- Raw strings (r"...") display escape characters as-is.
"""

# --- Input in Python ---
print("\n--- Input Examples ---")

# Taking input and storing in a variable
user_name = input("Enter your name: ")  # Stores the input in user_name
print("Hello,", user_name)

# Taking input without storing (not an error, but value is lost)
input("Press Enter to continue...")  # No variable, input is taken but not used

# Input is always a string by default
user_age = input("Enter your age: ")
print("Type of user_age:", type(user_age))  # Shows <class 'str'>

# Type conversion while taking input
user_age_int = int(input("Enter your age as a number: "))  # Converts input to integer
print(f"Next year, you will be {user_age_int + 1} years old.")

# Taking multiple inputs in one line (split)
nums = input("Enter two numbers separated by space: ").split()
num1 = int(nums[0])
num2 = int(nums[1])
print(f"Sum: {num1 + num2}")

"""
Summary of Input:
- input() is used to take user input (always returns a string).
- You can take input without storing it, but the value is lost.
- Use type conversion (int(), float(), etc.) to work with numbers.
- Use split() to take multiple inputs in one line.
"""
