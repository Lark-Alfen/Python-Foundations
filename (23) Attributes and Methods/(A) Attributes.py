# Class and Instance Attributes Example
"""
Class attributes are shared by all objects of the class.
Instance attributes are unique to each object (instance).
"""

class Student:
	# Class attribute
	school = "ABC High School"

	def __init__(self, name, grade):
		# Instance attributes
		self.name = name
		self.grade = grade

# Creating objects
student1 = Student("Alice", 10)
student2 = Student("Bob", 12)

# Accessing class attribute
print(f"All students study at: {Student.school}")
print(input("Press Enter to continue..."))
print(f"student1's school: {student1.school}")
print(input("Press Enter to continue..."))
print(f"student2's school: {student2.school}")
print(input("Press Enter to continue..."))

# Accessing instance attributes
print(f"{student1.name} is in grade {student1.grade}")
print(input("Press Enter to continue..."))
print(f"{student2.name} is in grade {student2.grade}")
print(input("Press Enter to continue..."))

"""
Explanation:
- 'school' is a class attribute, so it's the same for all students.
- 'name' and 'grade' are instance attributes, so each student has their own values.
"""
