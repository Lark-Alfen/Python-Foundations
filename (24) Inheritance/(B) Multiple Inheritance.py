"""
Multiple Inheritance in Python

Multiple inheritance allows a class to inherit from more than one parent class. This means the child class can access attributes and methods from all its parent classes.

Key Concepts Demonstrated:
- Each parent class (Dad, Mom) has its own attributes and methods.
- The child class (Child) inherits from both Dad and Mom.
- The child class can access class attributes and methods from both parents.
- The __init__ method of both parents is called in the child's __init__ to ensure all attributes are initialized.
- The child class can have its own attributes and methods as well.
- You can access class attributes (like mom_dna, dad_dna, child_dna) from the child object.

Code Walkthrough:
"""

class Dad:
    dad_dna = "010"  # Class attribute specific to Dad
    def __init__(self, name):
        self.name = name  # Instance attribute

    def Basketball(self):
        return "plays basketball"  # Dad's method

dad = Dad("John")
print(f"{dad.name} {dad.Basketball()}")  # John plays basketball
print(input("Press Enter to continue..."))

class Mom:
    mom_dna = "101"  # Class attribute specific to Mom
    def __init__(self, name):
        self.name = name  # Instance attribute

    def Badminton(self):
        return "plays badminton"  # Mom's method
mom = Mom("Jane")
print(f"{mom.name} {mom.Badminton()}")  # Jane plays badminton
print(input("Press Enter to continue..."))

class Child(Dad, Mom):  # Multiple inheritance
    child_dna = "111"  # Class attribute specific to Child
    def __init__(self, name):
        Dad.__init__(self, name)   # Initialize Dad part
        Mom.__init__(self, name)   # Initialize Mom part

    def sports(self):
        return f"{self.name} {self.Basketball()} and {self.Badminton()}"  # Uses both parents' methods

son = Child("Jack")
# Accessing class attributes from all classes
print(son.mom_dna)    # Inherited from Mom
print(son.dad_dna)    # Inherited from Dad
print(son.child_dna)  # Defined in Child
print(input("Press Enter to continue..."))
# Using the sports method to show Jack's activities
print(son.sports())   # Jack plays basketball and plays badminton

"""
Explanation:
- Dad and Mom are two separate classes, each with their own class attributes and methods.
- Child inherits from both Dad and Mom, so it can use methods and attributes from both.
- In Child's __init__, both Dad's and Mom's __init__ are called to ensure all initialization is done.
- The sports() method in Child combines the activities from both parents.
- You can access class attributes from any parent using the child object.
- This is a classic example of multiple inheritance in Python.
"""