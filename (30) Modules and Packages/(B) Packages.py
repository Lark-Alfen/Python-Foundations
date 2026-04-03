"""
Packages in Python

A package is a way of organizing related modules into a single directory hierarchy.
A package is simply a directory containing a special __init__.py file (can be empty) and other modules or sub-packages.
Packages help structure large projects and avoid name conflicts.
You can import modules from packages using dot notation.
"""

print("--Packages in Python--\n")
input("Press Enter to continue...")

# Importing a module from a package (Mod1/SecHello.py)
from Mod1 import SecHello  # Imports SecHello module from Mod1 package

# Calling functions from the imported module
print(SecHello.Hi())  # Calls Hi() function from SecHello.py
print(SecHello.welcome("Bob"))  # Calls welcome() function from SecHello.py with argument "Bob"
input("Press Enter to continue...")

# Importing a module from a subpackage (Mod1/Mod2/ThirdHello.py)
from Mod1.Mod2 import ThirdHello  # Imports ThirdHello module from Mod1.Mod2 subpackage

# Calling functions from the imported submodule
print(ThirdHello.yo())  # Calls yo() function from ThirdHello.py
print(ThirdHello.wassup("Charlie"))  # Calls wassup() function from ThirdHello.py with argument "Charlie"
input("Press Enter to continue...")

"""
Line-by-line explanation:
- from Mod1 import SecHello: Imports the SecHello module from the Mod1 package.
- print(SecHello.Hi()): Calls and prints the result of Hi() from SecHello.
- print(SecHello.welcome("Bob")): Calls and prints the result of welcome() from SecHello with argument "Bob".
- from Mod1.Mod2 import ThirdHello: Imports the ThirdHello module from the Mod1.Mod2 subpackage.
- print(ThirdHello.yo()): Calls and prints the result of yo() from ThirdHello.
- print(ThirdHello.wassup("Charlie")): Calls and prints the result of wassup() from ThirdHello with argument "Charlie".
"""
from Mod1 import SecHello

print(SecHello.Hi())
print(SecHello.welcome("Bob"))

from Mod1.Mod2 import ThirdHello

print(ThirdHello.yo())
print(ThirdHello.wassup("Charlie"))