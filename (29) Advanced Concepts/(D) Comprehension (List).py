"""
Comprehensions in Python

Comprehensions provide a concise way to create lists, sets, or dictionaries from iterables. They are often used as a more readable and compact alternative to traditional for loops.

Key Concepts:
- List comprehensions allow you to generate a new list by applying an expression to each item in an iterable, optionally filtering with a condition.
- The syntax is: [expression for item in iterable if condition]
- Comprehensions can make your code shorter and more Pythonic.

Example Explained:
"""

l1 = []
for i in range(1, 21):
    if i % 2 == 0:
        l1.append(i)

print(l1)  # Output: [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

print(input("Press Enter to continue..."))

# Using list comprehension
print("Using list comprehension:")
l2 = [i for i in range(1, 21) if i % 2 == 0]
print(l2)  # Output: [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

"""
Explanation:
- The first part uses a traditional for loop to build a list of even numbers from 1 to 20.
- The second part uses a list comprehension to do the same thing in a single line.
- [i for i in range(1, 21) if i % 2 == 0] means: for each i from 1 to 20, include i in the list if i is even.
- List comprehensions are more concise and often easier to read for simple transformations and filters.
- You can use similar syntax for set and dictionary comprehensions as well.
"""
