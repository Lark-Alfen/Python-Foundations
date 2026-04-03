# Classes, Attributes, and Methods in Python
"""
A class is a blueprint for creating objects. It defines attributes (data) and methods (functions) that belong to the class.

- Attributes: Variables that belong to the class or objects.
- Methods: Functions defined inside a class that operate on its attributes.
"""

# Simple class example
class Dog:
    species = "Pug" # Class attribute
    print("This line runs once during initialization of the class. It won't run again in one session")
    def bark(self): # Method that belongs to the Dog class
        print("says woof!")
	


# Accessing class attribute
print(f"Species: {Dog().species}") # Accessing attribute
Dog().bark() # Accessing method
"""
Explanation:
- The class attribute 'species' is shared by all Dog objects.
- The __init__ method runs once when each object is created (see the print statement).
- Instance attributes (name, age) are unique to each object.
- Methods (like bark) use self to access attributes.
"""
