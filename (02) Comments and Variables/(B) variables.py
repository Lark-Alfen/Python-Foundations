"""
This program demonstrates variables in Python.
Variables are used to store data values. You can assign different types of values to variables.

Variable Naming Rules:
- Variable names must start with a letter (a-z, A-Z) or underscore (_)
- Variable names cannot start with a number
- Variable names cannot contain spaces
- Variable names cannot contain special characters (like @, #, $, %, etc.) except underscore (_)
- Variable names are case-sensitive (age and Age are different)
- Variable names can contain letters, numbers, and underscores
"""

# Integer variable
age = 25  # Stores an integer value

# Float variable
height = 5.9  # Stores a floating-point number

# String variable
name = "Alice"  # Stores a string value

# Boolean variable
is_student = True  # Stores a boolean value (True or False)

# Multiple assignment
x, y, z = 1, 2.5, "hello"  # Assigns values to multiple variables at once

# Printing variables
print("Name:", name)
print("Age:", age)
print("Height:", height)
print("Is student:", is_student)
print("x:", x, "y:", y, "z:", z)

input("Press Enter to continue...")

"""
Variable names should start with a letter or underscore, and can contain letters, numbers, and underscores.
They are case-sensitive (age and Age are different variables).
Variables can change type by assigning a new value of a different type.
"""

# Changing variable type
age = "twenty-five"  # Now age is a string
print("Age (as string):", age)


# Naming Conventions

PythonCoding = "pacal case" # Words have capital first letters and no spaces
python_coding = "snake case" # Words are all lowercase and separated by underscores
pythonCoding = "camel case" # First word is lowercase, subsequent words have capital first letters