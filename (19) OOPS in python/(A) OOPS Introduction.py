"""
OOPs (Object-Oriented Programming) in Python

What is OOPs?
Object-Oriented Programming (OOPs) is a programming paradigm based on the concept of objects, which contain data (attributes) and code (methods).

Why OOPs over Imperative Approach?
- Imperative (procedural) programming organizes code as functions and variables. As programs grow, managing data and functions separately becomes hard.
- OOPs groups data and functions together as objects, making code more organized, reusable, and easier to maintain.
- OOPs supports concepts like encapsulation, inheritance, and polymorphism, which help manage complexity in large programs.

Simple Example:
"""

# Imperative approach
def car_description(color, brand):
    print(f"This car is a {color} {brand}.")
car_description("red", "Toyota")

# OOPs approach
class Car:
    def __init__(self, color, brand):
        self.color = color
        self.brand = brand
    def description(self):
        print(f"This car is a {self.color} {self.brand}.")

my_car = Car("blue", "Honda")
my_car.description()

"""
Explanation:
- In the imperative approach, data and function are separate.
- In OOPs, data (color, brand) and behavior (description) are bundled in the Car object.
- OOPs makes code more modular and easier to extend.
"""
