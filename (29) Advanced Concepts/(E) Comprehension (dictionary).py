"""
Dictionary Comprehension in Python

Dictionary comprehensions provide a concise way to create dictionaries from iterables, similar to list comprehensions. They are useful for transforming or filtering key-value pairs in a single line.

Key Concepts:
- Dictionary comprehensions allow you to generate a new dictionary by applying an expression to each item in an iterable, optionally filtering with a condition.
- The syntax is: {key_expr: value_expr for item in iterable if condition}
- Comprehensions can make your code shorter and more Pythonic.

Example Explained:
"""

# Traditional for loop to build a dictionary labeling numbers as 'even' or 'odd'
my_dict = {}
for i in range(1, 11):
    if i % 2 == 0:
        my_dict[i] = "even"
    else:
        my_dict[i] = "odd"
print(my_dict)  # Output: {1: 'odd', 2: 'even', 3: 'odd', 4: 'even', 5: 'odd', 6: 'even', 7: 'odd', 8: 'even', 9: 'odd', 10: 'even'}

print(input("Press Enter to continue..."))

# Using dictionary comprehension
print("Using dictionary comprehension:")
d = {i : "even" if i % 2 == 0 else "odd" for i in range(1, 11)}
print(d)  # Output: {1: 'odd', 2: 'even', 3: 'odd', 4: 'even', 5: 'odd', 6: 'even', 7: 'odd', 8: 'even', 9: 'odd', 10: 'even'}

"""
Explanation:
- The first part uses a traditional for loop to build a dictionary labeling numbers from 1 to 10 as 'even' or 'odd'.
- The second part uses a dictionary comprehension to do the same thing in a single line.
- {i : "even" if i % 2 == 0 else "odd" for i in range(1, 11)} means: for each i from 1 to 10, include i as a key and label it 'even' or 'odd' depending on its value.
- Dictionary comprehensions are more concise and often easier to read for simple transformations and filters.
- You can use similar syntax for list and set comprehensions as well.
"""