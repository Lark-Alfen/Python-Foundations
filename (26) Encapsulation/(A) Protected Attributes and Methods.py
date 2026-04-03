"""
Protected Attributes in Python (Encapsulation)

Encapsulation is the concept of restricting direct access to some of an object's attributes and methods, usually to protect the internal state of the object.

In many languages (like Java, C++), you can use access modifiers (public, protected, private) to control access:
- public: accessible from anywhere
- protected: accessible only within the class and its subclasses
- private: accessible only within the class

In Python:
- There is no strict enforcement of protected or private attributes.
- By convention, a single underscore _a is used to indicate that an attribute is protected (should not be accessed outside the class or its subclasses).
- This is just a convention and not enforced by the language. It serves as a hint to other developers.
- A normal attribute (a) is considered public and can be accessed from anywhere.

Example:
"""

class Example:
    def __init__(self):
        self.a = "public attribute"      # Public attribute
        self._a = "protected attribute"  # Protected attribute (by convention)

    def show(self):
        print(f"a: {self.a}")
        print(f"_a: {self._a}")

obj = Example()
obj.show()
print(input("Press Enter to continue..."))

# Accessing attributes from outside the class
print(obj.a)   # Allowed (public)
print(obj._a)  # Allowed, but not recommended (protected by convention)

"""
Explanation:
- self.a is a public attribute and can be accessed from anywhere.
- self._a is a protected attribute by convention. Python does not prevent access, but the single underscore tells other developers it should not be accessed directly outside the class or its subclasses.
- This convention helps communicate which attributes are meant for internal use and which are safe to use from outside.
- In subclasses, _a can be accessed and modified as needed.
- Python relies on developer discipline rather than strict enforcement for encapsulation.
"""
