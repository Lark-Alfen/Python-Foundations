"""
The map() Function in Python

The map() function applies a given function to every item of an iterable (like a list) and returns a map object (an iterator). It's useful for transforming data without writing explicit loops.

Key Concepts:
- map(function, iterable) applies 'function' to each item in 'iterable'.
- The result is a map object, which can be converted to a list, set, or other collection.
- map() is often used with lambda functions for concise, one-line transformations.

Example Explained:
"""

List = [1, 2, 3, 4, 5]

def square(x):
    return x * x

# Using map with a named function
result = map(square, List)
print(result)           # Output: <map object at ...> (an iterator)
print(list(result))     # Output: [1, 4, 9, 16, 25]

print(input("Press Enter to continue..."))

# Using map with a lambda function
result = map(lambda x: x * x, List)
print(result)           # Output: <map object at ...>
print(list(result))     # Output: [1, 4, 9, 16, 25]

print(input("Press Enter to continue..."))

# Using map to create a dictionary labeling numbers as even or odd
result = dict(map(lambda x: (x, "even" if x % 2 == 0 else "odd"), List))
print(result)           # Output: {1: 'odd', 2: 'even', 3: 'odd', 4: 'even', 5: 'odd'}

"""
Core Logic Breakdown: Using map and lambda to build a dictionary

result = dict(map(lambda x: (x, "even" if x % 2 == 0 else "odd"), List))

How it works:
- map applies the lambda function to each element x in List.
- The lambda function returns a tuple: (x, "even") if x is even, or (x, "odd") if x is odd.
- map produces an iterator of tuples: (1, 'odd'), (2, 'even'), (3, 'odd'), etc.
- dict() converts this sequence of tuples into a dictionary, where each number is a key and its value is 'even' or 'odd'.

Step-by-step for List = [1, 2, 3, 4, 5]:
1. For x = 1: lambda returns (1, 'odd')
2. For x = 2: lambda returns (2, 'even')
3. For x = 3: lambda returns (3, 'odd')
4. For x = 4: lambda returns (4, 'even')
5. For x = 5: lambda returns (5, 'odd')

- dict() collects these pairs into: {1: 'odd', 2: 'even', 3: 'odd', 4: 'even', 5: 'odd'}

Why is this useful?
- This pattern is a compact way to build a dictionary from a list, assigning values based on a condition.
- It combines transformation (lambda) and collection (dict + map) in a single line.
- You can use this approach for any logic that produces (key, value) pairs from a sequence.
"""

"""
Explanation:
- The first part uses map() with a named function (square) to square each number in the list.
- The second part uses map() with a lambda function for the same purpose, showing how you can use anonymous functions for quick operations.
- The third part uses map() with a lambda to create (key, value) pairs for a dictionary, labeling each number as 'even' or 'odd'.
- map() returns an iterator, so you usually convert it to a list or dict to see the results.
- map() is a powerful tool for applying transformations to iterables in a concise and readable way.
"""