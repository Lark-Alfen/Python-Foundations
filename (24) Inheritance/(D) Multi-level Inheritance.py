"""
Multi-level Inheritance in Python

Multi-level inheritance is when a class is derived from another derived class, forming a chain of inheritance. Each level can add its own attributes and methods, and the most derived class inherits everything from all its ancestors.

Key Concepts Demonstrated:
- Each class adds its own attributes.
- Each child class uses super() to call its parent constructor, ensuring all attributes are initialized.
- The most derived class (sedan) has access to all attributes from its parent and grandparent classes.

Code Walkthrough:
"""

class factory:
    def __init__(self, material):
        self.material = material  # Attribute for the material used in the factory

class car(factory):  # car inherits from factory
    def __init__(self, material, parts):
        super().__init__(material)  # Initialize material from factory
        self.parts = parts          # Attribute for car parts

class sedan(car):  # sedan inherits from car (which inherits from factory)
    def __init__(self, material, parts, model):
        super().__init__(material, parts)  # Initialize material and parts
        self.model = model                 # Attribute for sedan model

# Creating an object of the most derived class
automobile = sedan("steel", ["engine", "wheels", "doors"], "Model S")

# Accessing attributes from all levels
print(f"Material: {automobile.material}")  # From factory
print(input("Press Enter to continue..."))
print(f"Parts: {automobile.parts}")        # From car
print(input("Press Enter to continue..."))
print(f"Model: {automobile.model}")        # From sedan

"""
Explanation:
- factory is the base class, car inherits from factory, and sedan inherits from car.
- Each class adds its own attribute: material (factory), parts (car), model (sedan).
- When you create a sedan object, all constructors are called in order, so all attributes are set.
- The sedan object (automobile) can access attributes from all its parent classes.
- This is called multi-level inheritance because the inheritance chain has more than two levels.
"""