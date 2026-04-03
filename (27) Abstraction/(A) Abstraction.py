"""
Abstraction in Python (using abc and abstractmethod)

Abstraction is the concept of hiding the complex implementation details and showing only the essential features of an object. It helps in reducing programming complexity and effort.

In many languages (like Java, C++), you can create abstract classes and methods directly. Python does not have built-in abstract classes, but you can simulate abstraction using the abc module and the @abstractmethod decorator.

Key Concepts:
- An abstract class cannot be instantiated directly.
- An abstract class can have abstract methods (methods with no implementation) and concrete methods (with implementation).
- Any subclass of an abstract class must implement all its abstract methods, or it will also be considered abstract.
- This enforces a contract for subclasses, ensuring certain methods are always defined.

Example: Vehicle abstraction
"""

from abc import ABC, abstractmethod

class Vehicle(ABC):  # Abstract base class
    @abstractmethod
    def start(self):
        pass  # Abstract method (no implementation)

    @abstractmethod
    def fuel_type(self):
        print("Most vehicles use petrol, diesel, or electricity.") # Abstract method with implementation (concrete method)

class Car(Vehicle):
    def start(self):
        print("Car engine started with a key or button.")  # Implementation of abstract method

    def fuel_type(self):
        print("Cars can use petrol, diesel, or electricity.")  # Implementation of abstract method while overriding (optional to override but mandatory to implement abstract method)

class Bike(Vehicle):
    def start(self):
        print("Bike engine started with a kick or button.")  # Implementation of abstract method without overriding fuel_type() (optional to override but mandatory to implement abstract method)

    def fuel_type(self):
        super().fuel_type() # Implementation of abstract method 

# v = Vehicle()  # This will raise an error: Can't instantiate abstract class

my_car = Car()
my_bike = Bike()

my_car.start()      # Car engine started with a key or button.
print(input("Press Enter to continue..."))
my_bike.start()     # Bike engine started with a kick or button.
print(input("Press Enter to continue..."))
my_car.fuel_type()  # Cars can use petrol, diesel, or electricity.
print(input("Press Enter to continue..."))
my_bike.fuel_type() # Most vehicles use petrol, diesel, or electricity.


"""
Explanation:
- Vehicle is an abstract class (inherits from ABC) and has an abstract method start().
- Car and Bike are subclasses that implement the start() method.
- You cannot create an object of Vehicle directly.
- You can create objects of Car and Bike, and they must provide their own start() method.
- The fuel_type() method is a regular method and can be used by all subclasses.
- This is how abstraction is simulated in Python using abc and abstractmethod.
"""
