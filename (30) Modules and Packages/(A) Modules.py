"""
Modules in Python

A module is a file containing Python code (functions, variables, classes, etc.).
Modules help organize code into separate files, making it easier to manage and reuse.
You can import code from one module into another using the 'import' statement.
"""

print("--Modules in Python--\n")
input("Press Enter to continue...")

# Importing functions from another module (FirstHello.py)
from FirstHello import hello, greet  # Imports hello() and greet() from FirstHello.py

# Calling the imported functions
print(hello())  # Calls the hello() function from FirstHello.py
print(greet("Alice"))  # Calls the greet() function from FirstHello.py with argument "Alice"
input("Press Enter to continue...")

"""
Line-by-line explanation:
- from FirstHello import hello, greet: Imports the functions hello and greet from the module FirstHello.
- print(hello()): Calls and prints the result of hello().
- print(greet("Alice")): Calls and prints the result of greet() with argument "Alice".
"""
from FirstHello import hello, greet

print(hello())
print(greet("Alice"))