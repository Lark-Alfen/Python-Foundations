"""
Method Resolution Order (MRO) in Python

When a class inherits from multiple parent classes, Python needs to know which parent to search first when you call a method or access an attribute. This order is called the Method Resolution Order (MRO).

Key Concepts Demonstrated:
- The order in which you list parent classes in the child class definition determines the MRO.
- Python searches for methods/attributes from left to right in the parent class list.
- If a method is not found in the child, Python looks for it in the first parent, then the next, and so on.
- You can view the MRO of a class using ClassName.__mro__ or help(ClassName).

Code Walkthrough:
"""

class mom:
    def speak(self):
        return "I am the mother"
    
class dad:
    def speak(self):
        return "I am the father"
    
class FirstChild(dad, mom):  # Inherits from dad first, then mom
    def speak(self):
        return super().speak()  # Uses MRO to find the first 'speak' method

c1 = FirstChild()
print(c1.speak())  # This will print "I am the father" because dad is first in MRO

class SecondChild(mom, dad):  # Inherits from mom first, then dad
    def speak(self):
        return super().speak()  # Uses MRO to find the first 'speak' method

c2 = SecondChild()
print(c2.speak())  # This will print "I am the mother" because mom is first in MRO

# You can see the MRO for any class:
print(FirstChild.__mro__)
print(input("Press Enter to continue..."))
print(SecondChild.__mro__)

"""
Explanation:
- In FirstChild, dad is listed first, so Python finds dad's speak() method first.
- In SecondChild, mom is listed first, so Python finds mom's speak() method first.
- The super() function in the child class uses the MRO to determine which parent method to call.
- The MRO can be checked using the __mro__ attribute, which shows the order Python will search for methods.
- This is important in multiple inheritance to avoid ambiguity and understand which method will be called.
"""