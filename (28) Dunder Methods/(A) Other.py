"""
Dunder Methods: Using 'other' in Operator Overloading (Simple Example)

Dunder methods like __add__ allow you to define how objects of your class interact with operators such as +.
The __add__ method takes two arguments: self (the left object) and other (the right object).

This lets you add two objects together in a natural way, using their internal values.

Example:
"""

class TwoValues:
    def __init__(self, value):
        self.value = value  # Store the value in self

    def __add__(self, other):
        # other is another TwoValues object
        return self.value + other.value  # Add the values inside self and other

n1 = TwoValues(10)
n2 = TwoValues(20)
print(n1 + n2)  # Output: 30

"""
Explanation:
- The __add__ method lets you use + to add two TwoValues objects.
- self refers to the left object (n1), other refers to the right object (n2).
- self.value and other.value are added together and returned.
- Dunder methods make it easy to define custom behavior for operators in your own classes.
"""

"""
Dunder Methods: Using 'other' as a Tuple of Objects with a For Loop

You can design your __add__ method to accept a tuple of objects as 'other' and use a for loop to add all their values together with self's value.
This is a flexible way to support adding multiple objects at once.

Example:
"""

class Adder:
    def __init__(self, num):
        self.num = num  # Store the value in self

    def __add__(self, other):
        # other is expected to be a tuple of Adder objects
        total = 0
        for v in other:
            total += v.num  # Access the num attribute of each object in the tuple
        return f"{total + self.num}"  # Add self.num to the total of other values

x1 = Adder(5)
x2 = Adder(10)
x3 = Adder(20)

print(x1 + (x2, x3))  # Output: 35 (5 + 10 + 20)

"""
Explanation:
- The __add__ method is defined to accept a tuple of Adder objects as 'other'.
- self.num is the value in the left object, and the rest come from the tuple.
- A for loop adds the num attribute of each object in the tuple to self.num.
- This shows how you can use 'other' flexibly in dunder methods to support adding multiple objects at once.
- Dunder methods make operator overloading powerful and customizable for your own classes.
"""
