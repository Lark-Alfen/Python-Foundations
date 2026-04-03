"""
If-Else Statement in Python

The if-else statement lets you execute one block if a condition is True, and another if it is False.
"""

x = 3
if x % 2 == 0:
    print("x is even")  # Runs if x is divisible by 2
else:
    print("x is odd")   # Runs if x is not divisible by 2 which is the case here

"""
You can use if-else for binary decisions.
- The condition (x % 2 == 0) checks if x is even.
- If True, the first block runs; if False, the else block runs.
"""

# Trick: Ternary (one-line) if-else
result = "even" if x % 2 == 0 else "odd"
print("Ternary result:", result)  # This is a compact way to assign a value based on a condition

'''
The above code essentially works as a compact version of:
if x % 2 == 0:
    result = "even"
else:
    result = "odd"
This is useful for simple conditions where you want to assign a value based on a condition without 
writing multiple lines of code.
'''

# Trick: if-else with multiple conditions
name = "Alice"
if name:
    print(f"Hello, {name}")  # Runs if name is not empty (non-empty strings are True)
else:
    print("No name provided.")  # Runs if name is empty (empty strings are False)

"""
Explanation:
- The ternary if-else (also called conditional expression) allows you to write simple if-else logic in one line.
- Using if with variables like 'if name:' checks if the variable is non-empty or non-zero (truthy).
- This is useful for input validation or default messages.
"""

# Example: Nested if-else
age = 20
has_id = True
if age >= 18:
    if has_id:
        print("Allowed entry.")
    else:
        print("ID required.")
else:
    print("Not allowed, underage.")

"""
Nested if-else explanation:
- You can place an if-else inside another if or else block.
- This is useful for checking multiple related conditions.
- Example above: First checks age, then checks for ID if age is sufficient.
"""
