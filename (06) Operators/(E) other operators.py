"""
Other Operators in Python

Identity and membership operators are used for object comparison and checking membership.
"""

print("Other Operators in Python\n")

# Identity operators
print("Identity Operators in Python\n")
A = True
B = False
print("A is B:", A is B)       # Checks if A and B are the same object
print("A is not B:", A is not B)

input("Press Enter to continue...")

# Membership operators
print("Membership Operators in Python\n")
my_list = [1, 2, 3]
print("2 in my_list:", 2 in my_list)   # Checks if 2 is in the list
print("4 not in my_list:", 4 not in my_list)

input("Press Enter to continue...")

"""
Explanation:
- Identity operators: 'is' checks if two variables point to the same object in memory. 'is not' checks if they do not.
- Membership operators: 'in' checks if a value exists in a sequence (like a list, string, tuple, etc.), 'not in' checks if it does not.
- These operators are useful for comparisons beyond just values, such as object identity and sequence membership.
- Use input("Press Enter to continue...") to pause and let the user review each concept.
"""