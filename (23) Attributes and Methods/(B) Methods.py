# Instance Method, Class Method, and Static Method Example
"""
There are three main types of methods in Python classes:
- Instance Method: Works with object (instance) data. Needs 'self'.
- Class Method: Works with class data. Needs 'cls' and uses @classmethod decorator.
- Static Method: Doesn't need object or class data. Uses @staticmethod decorator.
"""

class Demo:
	school = "ABC High School"  # Class attribute

	def __init__(self, name):
		self.name = name  # Instance attribute

	# Instance method
	def show_name(self):
		print(f"Instance method: My name is {self.name}")

	# Class method
	@classmethod
	def show_school(cls):
		print(f"Class method: School is {cls.school}")

	# Static method
	@staticmethod
	def greet():
		print("Static method: Hello!")

# Create an object
obj = Demo("Alice")

# Call instance method
obj.show_name()
print(input("Press Enter to continue..."))
# Call class method (can use class or object)
Demo.show_school()
obj.show_school()
print(input("Press Enter to continue..."))
# Call static method (can use class or object)
Demo.greet()
obj.greet()

"""
Explanation:
- Instance method (show_name): Needs 'self', works with object data.
- Class method (show_school): Needs 'cls', works with class data, uses @classmethod.
- Static method (greet): No self/cls, general utility, uses @staticmethod.
"""
