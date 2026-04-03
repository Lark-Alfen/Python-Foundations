"""
If Statement in Python

The if statement is used to execute a block of code only if a condition is True.
"""

x = 10
if x > 5:
    print("x is greater than 5")  # This line runs because the condition is True

"""
You can use any expression that evaluates to True or False.
"""

# Trick: Using if with non-boolean values
if "hello":
    print("Non-empty strings are True!")
if 0:
    print("This will not print, because 0 is False.")
if [1, 2, 3]:
    print("Non-empty lists are also True!")

"""
Trick: You can use if to check for existence or emptiness:
if not []:
    print("Empty list is False so not False will be True, so this prints.")

Explanation:
- In Python, empty containers like [], '', {}, set(), and 0 are considered False in a boolean context.
- 'not []' means 'not False', which is True, so the code block runs.
- This is a common way to check if a list (or other container) is empty before performing actions.
"""
