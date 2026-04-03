"""
Constructors in Python

The __init__ method is called a constructor. It runs automatically when you create a new object from a class.

What does 'print(self)' show?
- Inside __init__, 'self' refers to the object being created.
- When you print(self), you see something like <__main__.BagFactory object at 0x...>.
- This shows the unique memory address of each object, proving that each object is a separate instance.

What does the 'show' method do?
- The show method prints the details of the object (its attributes).
- You call it on an object (like reebok.show()), and it uses self to access that object's data.

Summary:
- __init__ sets up the object's data when you create it.
- 'self' always refers to the current object (by referring to the object's location in memory).
- Each object has its own data, and you can use methods like show() to display it.
"""


class BagFactory:
    def __init__(self, material, zips, pockets):
        print(self)  # Shows the unique object being created
        self.material = material
        self.zips = zips
        self.pockets = pockets

    def show(self):
        print(f"Your object details are: {self.material}, {self.zips}, {self.pockets}")

reebok = BagFactory("leather", 2, 3)
campus = BagFactory("nylon", 1, 2)

reebok.show()
campus.show()

