"""
Duck Typing in Python (Polymorphism)

Duck typing is a concept in dynamic languages like Python where the type or class of an object is less important than the methods it defines or the behavior it exhibits. 

The phrase "If it looks like a duck and quacks like a duck, it's a duck" means that if an object implements the methods you need, you can use it, regardless of its actual type.

Key Concepts:
- Python cares about what an object can do, not what it is.
- If two unrelated classes have the same method name, you can use them interchangeably in code that expects that method.
- This is a form of polymorphism: different objects can be used in the same way if they provide the same interface.

Example:
"""

class Dad:
    def talk(self):
        return "dad is talking"
    
class Mom:
    def talk(self):
        return "mom is talking"
    
speak1 = Dad()
print(speak1.talk())  # Output: dad is talking
print(input("Press Enter to continue..."))
speak2 = Mom()
print(speak2.talk())  # Output: mom is talking

"""
Explanation:
- Both Dad and Mom classes have a talk() method, but they are unrelated by inheritance.
- You can use any object with a talk() method in the same way, regardless of its class.
- This is duck typing: Python only cares that the object has the method you want to use.
- This allows for flexible and generic code, as long as the required methods are present.
- Duck typing is a key part of Python's dynamic and flexible approach to polymorphism.
"""