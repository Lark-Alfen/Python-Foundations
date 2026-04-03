# Inheritance and the super() keyword in Python
"""
Inheritance allows a class (child/derived class) to use the properties and methods of another class (parent/base class).
This helps in code reuse and building relationships between classes.

In this example:
- Animal is the parent class.
- Cat is the child class that inherits from Animal.

The super() keyword is used in the child class to call the parent class's __init__ method, so the 'name' attribute 
is set up properly.

Key concepts shown:
- Inheritance: Cat inherits from Animal, so it gets all its methods (Introduction, speak, move).
- Method overriding: Cat can override or extend methods from Animal if needed.
- super(): Used to call the parent class's __init__ so the base attributes are initialized.
- Attribute extension: Cat adds a new attribute 'sound' that Animal doesn't have.
- If you call speak() or move() on an Animal object, it will error if 'sound' is not set (as shown in the 
commented lines).
"""

class Animal:

    def __init__(self, name):
        self.name = name  # Instance attribute for the animal's name

    def Introduction(self):
        print(f"Name's {self.name}.")  # Introduce the animal
    
    def speak(self):
        print(f"{self.name} says {self.sound}")  # Uses 'sound' attribute (must be set in child)
    
    def move(self):
        print(f"{self.name} runs and says {self.sound} {self.sound}")  # Uses 'sound' attribute


class Cat(Animal):  # Cat inherits from Animal
    def __init__(self, name, sound):
        super().__init__(name)  # Call parent constructor to set name
        self.sound = sound      # Add/override sound attribute for Cat


person = Animal('John')  # Create an Animal object
animal1 = Cat("Whiskers", "Meow")  # Create a Cat object (inherits Animal)

person.Introduction()  # Calls Animal's Introduction
print(input("Press Enter to continue..."))
animal1.Introduction()  # Inherited method from Animal
print(input("Press Enter to continue..."))
animal1.speak()  # Uses Cat's sound attribute
print(input("Press Enter to continue..."))
animal1.move()   # Uses Cat's sound attribute
print(input("Press Enter to continue..."))

# person.speak() # This will raise an error because 'Animal' class doesn't have 'sound' attribute
# person.move()  # This will also raise an error for the same reason