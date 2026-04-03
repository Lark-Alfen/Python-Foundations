"""
Hierarchical Inheritance in Python

Hierarchical inheritance is when multiple child classes inherit from the same parent class. Each child class can have its own attributes and methods, but they all share the parent class's features.

Key Concepts:
- One parent class, multiple child classes.
- Each child inherits attributes and methods from the parent.
- Each child can also have its own unique features.

Example:
"""

class Animal:
    def __init__(self, name):
        self.name = name  # Attribute for the animal's name
    def speak(self):
        print(f"{self.name} makes a sound.")

class Dog(Animal):  # Dog inherits from Animal
    def bark(self):
        print(f"{self.name} barks!")

class Cat(Animal):  # Cat also inherits from Animal
    def meow(self):
        print(f"{self.name} meows!")

# Creating objects of both child classes
d = Dog("Buddy")
c = Cat("Whiskers")

# Both can use the parent method
print("Dog:")
d.speak()  # Inherited from Animal
d.bark()   # Unique to Dog
print(input("Press Enter to continue..."))
print("Cat:")
c.speak()  # Inherited from Animal
c.meow()   # Unique to Cat
print(input("Press Enter to continue..."))

"""
Explanation:
- Animal is the parent class.
- Dog and Cat are child classes that both inherit from Animal.
- Both Dog and Cat can use the speak() method from Animal.
- Dog has its own bark() method, and Cat has its own meow() method.
- This is hierarchical inheritance: one parent, multiple children.
"""
