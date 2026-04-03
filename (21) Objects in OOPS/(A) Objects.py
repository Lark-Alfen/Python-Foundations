"""
Objects in Python OOPs

A class is like a blueprint, while an object is an actual instance created from that blueprint.
Each object can use the class's attributes and methods.
"""

# Provided Dog class
class Dog:
	species = "Pug" # Class attribute
	print("This line runs once during initialization of the class. It won't run again in one session")
	def bark(self): # Method that belongs to the Dog class
		print("says woof!")

# Creating objects (instances) of Dog
dog1 = Dog()
dog2 = Dog()

# Accessing class attribute
print(f"dog1's species: {dog1.species}")
print(f"dog2's species: {dog2.species}")

print(input("Press Enter to continue..."))

# Calling method on objects
print("dog1 barks:")
dog1.bark()

print(input("Press Enter to continue..."))

print("dog2 barks:")
dog2.bark()

"""
Explanation:
- The Dog class defines a class attribute (species) and a method (bark).
- When you create dog1 and dog2, they are objects (instances) of the Dog class.
- The print statement inside the class runs only once when the class is first loaded.
- Both dog1 and dog2 share the class attribute and can use the bark() method.
"""
