"""
Logical Operators in Python

Logical operators are used to combine conditions and return True or False. Here are the main logical operators:
- and : Returns True if all conditions are True
- or  : Returns True if at least one condition is True
- not : Returns True if the condition is False (reverses the boolean value)
"""

print("Logical Operators in Python\n")
A = True
B = False
print("A and B:", A and B) # Logical AND: True and False is False
input("Press Enter to continue...")
print("A or B:", A or B)   # Logical OR: True or False is True
input("Press Enter to continue...")
print("not A:", not A)     # Logical NOT: not True is False
input("Press Enter to continue...")

# More examples
print("\nMore Logical Operator Examples:")
x = 5
y = 10
print("x > 0 and y > 0:", x > 0 and y > 0)  # Both conditions True, so result is True
input("Press Enter to continue...")
print("x > 0 and y > 0:", x > 0 and y < 0)  # One condition False, so result is False
input("Press Enter to continue...")
print("x > 0 or y < 0:", x > 0 or y < 0)    # One condition True, so result is True
input("Press Enter to continue...")
print("not (x < 0):", not (x < 0))          # x < 0 is False, so not False is True
input("Press Enter to continue...")

# We can also combine multiple logical operators in one expression:
print("\nCombining multiple logical operators:")
print("10 < 11 and 12 < 14 and 10 == 10 or 5 < 3:", 10 < 11 and 12 < 14 and 10 == 10 or 5 < 3) 
# Evaluates to True and True and True or False -> True or False -> True

"""
Logical operators are often used in if statements and loops to combine multiple conditions.
- 'and' requires all conditions to be True.
- 'or' requires at least one condition to be True.
- 'not' reverses the result.
"""
