"""
Method Overriding in Python (Polymorphism)

Method overriding is a feature in object-oriented programming where a child class provides its own implementation of a method that is already defined in its parent class. This allows the child class to change or extend the behavior of that method.

Key Concepts:
- The method in the child class must have the same name as in the parent class.
- When you call the method on a child object, the child class's version is used (not the parent's).
- This is a form of polymorphism: the same method name behaves differently depending on the object.


Example:
"""

class Parent:
    def talk(self):
        print("Hi, im dad")  # Parent's version of talk()

class Child(Parent):
    def talk(self):
        print("Hi, im son")  # Child's version of talk() overrides Parent's

call = Child()
call.talk()  # Output: Hi, im son

"""
Explanation:
- The Parent class defines a method talk().
- The Child class inherits from Parent and defines its own talk() method with the same name.
- When you create a Child object and call talk(), Python uses the Child's version, not the Parent's.
- This is called method overriding, and it's a key part of polymorphism in OOP.
- If you remove the talk() method from Child, calling talk() would use the Parent's version instead.

# Note: Python does not support method overloading by argument type or count. Use default values or *args/**kwargs for flexibility.
"""
# Note on Method Overloading:
# Method overloading means having multiple methods with the same name but different parameters in the same class.
# Python does not support true method overloading like some other languages (e.g., Java, C++).
# If you define multiple methods with the same name in a class, only the last one is kept (previous ones are overwritten).
# To achieve similar behavior, use default arguments or *args and **kwargs to handle different numbers/types of arguments in a single method.
