"""
Set Comprehension in Python

Set comprehensions provide a concise way to create sets from iterables, similar to list and dictionary comprehensions. They are useful for generating sets with unique values in a single line.

Key Concepts:
- Set comprehensions allow you to generate a new set by applying an expression to each item in an iterable.
- The syntax is: {expression for item in iterable}
- Sets automatically remove duplicate values.
- Comprehensions can make your code shorter and more Pythonic.

Example Explained:
"""

# Traditional for loop to build a set of squares from 1 to 10
MySet = set()
for i in range(1, 11):
    MySet.add(i * i)
print(MySet)  # Output: {1, 4, 36, 9, 16, 49, 64, 100, 81, 25}

print(input("Press Enter to continue..."))

# Using set comprehension
print("Using set comprehension:")
s = {x * x for x in range(1, 11)}
print(s)  # Output: {1, 4, 36, 9, 16, 49, 64, 100, 81, 25}

"""
Explanation:
- The first part uses a traditional for loop to build a set of squares from 1 to 10.
- The second part uses a set comprehension to do the same thing in a single line.
- {x * x for x in range(1, 11)} means: for each x from 1 to 10, include x squared in the set.
- Set comprehensions are concise and automatically remove duplicates.
- You can use similar syntax for list and dictionary comprehensions as well.
"""