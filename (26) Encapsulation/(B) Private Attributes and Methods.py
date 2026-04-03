"""
Private Attributes and Methods in Python (Encapsulation)

Private attributes and methods are intended to be accessible only within the class where they are defined. In many languages (like Java, C++), the 'private' keyword enforces this restriction.

In Python:
- There is no true enforcement of private attributes, but a naming convention is used.
- Prefixing an attribute or method with double underscores (e.g., __a) makes it 'private' by name mangling.
- Python internally renames __a to _ClassName__a, making it harder (but not impossible) to access from outside the class.
- This is meant to discourage access, not prevent it.

Example:
"""

class Example:
    def __init__(self):
        self.__a = "private attribute"  # Private attribute

    def __private_method(self):         # Private method
        print("This is a private method.")

    def show(self):
        print(self.__a)                 # Accessing private attribute inside the class
        self.__private_method()         # Calling private method inside the class

obj = Example()
obj.show()
print(input("Press Enter to continue..."))
# The following lines will cause AttributeError:
# print(obj.__a)            # Not allowed: AttributeError
# obj.__private_method()    # Not allowed: AttributeError

# But you can still access them using name mangling (not recommended):
print(obj._Example__a)           # Accessing private attribute (not recommended)
print(input("Press Enter to continue..."))
obj._Example__private_method()   # Calling private method (not recommended)

"""
Explanation:
- __a and __private_method are private to the Example class due to name mangling.
- They cannot be accessed directly from outside the class using their original names.
- You can still access them using _ClassName__attribute, but this is discouraged.
- The double underscore is a convention to signal that these are private and should not be used outside the class.
- Python relies on developer discipline rather than strict enforcement for encapsulation.
"""
