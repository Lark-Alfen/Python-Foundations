"""
Input and Output in Python

This program demonstrates different ways to take input from the user and display output in Python.
"""

# --- Output in Python ---
print("--- Output Examples ---")

# Simple output
print("Simple output:")
print("Hello, World!")  # Prints a simple string

input("Press Enter to continue...")

# Output with multiple values
print("\nOutput with multiple values:")
name = "Alice"
age = 25
print("Name:", name, "Age:", age)  # Prints multiple values separated by spaces

input("Press Enter to continue...")

# Formatted output using f-strings (recommended)
print("\nFormatted output using f-strings:")
print(f"My name is {name} and I am {age} years old.")

input("Press Enter to continue...")

# Formatted output using format()
print("\nFormatted output using format():")
print("My name is {} and I am {} years old.".format(name, age))

input("Press Enter to continue...")

# Raw output (shows escape characters as-is)
print("\nRaw output using r-string:")
print(r"This is a raw string: C:\\Users\\Alice")

input("Press Enter to continue...")

# Output with custom separator and end
print("\nOutput with custom separator and end:")
print("A", "B", "C", sep="-", end=" END\n")  # Custom separator and end

input("Press Enter to continue...")

# --- Raw String Explanation ---
print("\n--- Raw String Explanation ---")

# Without raw string: backslashes are treated as escape characters
print("Normal string (with single backslashes) without r-string:")
path_normal = "C:\\Users\\Alice\\Documents"
print("Normal string (with double backslashes):", path_normal)  # Prints: C:\Users\Alice\Documents

# If you forget to double the backslashes, you may get an error or unexpected result
# The following line would cause a SyntaxError if uncommented:
# path_problem = "C:\Users\Alice\Documents"  # This will cause a unicodeescape error
# If you use a normal string with single backslashes, e.g. 'C:\Users\Alice\Documents', Python may 
# interpret \U as a Unicode escape and raise a SyntaxError.

print("Always use double backslashes or a raw string for Windows paths.")

input("Press Enter to continue...")

# With raw string: backslashes are preserved as-is
print("\nUsing r-string (r'...'):")
path_raw = r"C:\Users\Alice\Documents"
print("Raw string:", path_raw)  # Prints: C:\Users\Alice\Documents

"""
Raw strings are useful when:
- Writing Windows file paths (to avoid accidental escape sequences)
- Writing regular expressions (where backslashes are common)
- Any situation where you want backslashes to be treated literally

In a raw string, backslashes are not treated as escape characters, so r"C:\path" is exactly C:\path.
"""

"""
Summary of Output:
- print() is used for output.
- You can print multiple values, use custom separators, and change the end character.
- f-strings and format() allow formatted output.
- r"..." creates a raw string, useful for file paths.
"""

# --- Input in Python ---
print("\n--- Input Examples ---")

# Taking input and storing in a variable
user_name = input("Enter your name: ")  # Stores the input in user_name
print("Hello,", user_name)

# Taking input without storing (not an error, but value is lost)
input("Press Enter to continue...")  # No variable, just pauses for user

# Input is always a string by default
user_age = input("Enter your age: ")
print("Type of user_age:", type(user_age))  # Shows <class 'str'>

# Type conversion while taking input
user_age_int = int(input("Enter your age as a number: "))  # Converts input to int
print(f"Next year, you will be {user_age_int + 1} years old.")

# Taking multiple inputs in one line (split)
nums = input("Enter two numbers separated by space: ").split()  # Splits the input string into a list
num1 = int(nums[0])  # Converts the first input to integer
num2 = int(nums[1])  # Converts the second input to integer
print(f"Sum: {num1 + num2}")  # Prints the sum of the two numbers

"""
Explanation:
- input() takes the whole line as a string, e.g. '5 7'.
- .split() breaks the string into a list of substrings, e.g. ['5', '7'].
- nums[0] and nums[1] access the first and second values.
- int() converts them from string to integer for calculation.
This is a common way to take multiple values from the user in one line and process them.
"""

# --- .split() Explanation ---
print("\n--- .split() Explanation ---")
input_line = input("Enter several words separated by spaces: ")
words = input_line.split()  # Splits the input string into a list of words
print("List of words:", words)

"""
The .split() method is used to break a string into a list, using a separator (default is space).
For example, 'a b c'.split() gives ['a', 'b', 'c'].
You can use .split(',') to split by commas, or .split('-') to split by hyphens.
This is useful for taking multiple inputs in one line and processing them as separate values.
"""

"""
Summary of Input:
- input() is used to take user input (always returns a string).
- You can use input() without storing the value, but the input is lost.
- Use type conversion (int(), float(), etc.) to work with numbers.
- Use split() to take multiple inputs in one line.
"""
