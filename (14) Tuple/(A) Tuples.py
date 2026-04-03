"""
Tuples in Python

A tuple is a built-in data structure that stores an ordered collection of items. Tuples are immutable, can contain duplicates, and are heterogeneous (can store different types).
"""

print("--Tuples in Python--\n")
input("Press Enter to continue...")

# Basic tuple creation
print("Basic tuple creation:")
my_tuple = (1, 2, 3, 4, 5)
print(f"my_tuple: {my_tuple}")
input("Press Enter to continue...")

"""
Tuple Properties:
- Immutable: Cannot be changed after creation.
- Ordered: Elements retain their order; you can access by index.
- Allows duplicates: Same value can appear multiple times.
- Heterogeneous: Can store different types (int, str, float, etc.).
"""

# Demonstrating immutability
print("Immutability demonstration:")
try:
    my_tuple[0] = 10  # Attempt to change first element
except TypeError as e:
    print(f"Error: {e}")
input("Press Enter to continue...")

# Duplicates
print("Duplicates demonstration:")
dup_tuple = (1, 2, 2, 3)
print(f"Tuple with duplicates: {dup_tuple}")
input("Press Enter to continue...")

# Heterogeneous elements
print("Heterogeneous demonstration:")
mixed_tuple = (1, "hello", 3.14, print()) # Contains an int, string, float, and function (prints None)
print(f"Tuple with mixed types: {mixed_tuple}")
input("Press Enter to continue...")

# Ordered and indexing
print("Ordered and indexing demonstration:")
print(f"First element: {my_tuple[0]}")
print(f"Last element: {my_tuple[-1]}")
input("Press Enter to continue...")

# Tuple methods
print("Tuple methods:")
print(f"Count of 2: {dup_tuple.count(2)}")  # Counts occurrences of 2
print(f"Index of 3: {my_tuple.index(3)}")   # Finds index of 3
input("Press Enter to continue...")

# Tuple methods demonstration
print("Tuple methods demonstration:")
test_tuple = (1, 2, 2, 3, 4)
print(f"test_tuple: {test_tuple}")
print(f"Count of 2: {test_tuple.count(2)}")  # Returns number of times 2 appears
print(f"Index of 3: {test_tuple.index(3)}")  # Returns first index of 3
input("Press Enter to continue...")

"""
Line-by-line explanation:
- count(x): Returns the number of times x appears in the tuple.
- index(x): Returns the first index of x.
- These are the only two methods available for tuples.
"""

# Difference between lists and tuples
print("Difference between lists and tuples:")
print("Lists are mutable, tuples are immutable.")
print("Lists use [ ], tuples use ( ).")
print("Lists have many methods for modification, tuples have only count and index.")
input("Press Enter to continue...")

# Tuple unpacking
print("Tuple unpacking demonstration:")
coords = (10, 20)
x, y = coords  # Unpacks tuple into variables
print(f"x = {x}, y = {y}")
input("Press Enter to continue...")

# Tricky logic: a = (1) is not a tuple
print("Tricky logic demonstration:")
a = (1) # This is just an integer, not a tuple
b = (1,) # Comma is needed to create a single-element tuple
print(f"a = (1) type: {type(a)}")  # int
print(f"b = (1,) type: {type(b)}")  # tuple
input("Press Enter to continue...")

"""
Explanation:
- a = (1): Parentheses alone do not create a tuple; it's just an integer.
- b = (1,): The comma makes it a tuple.
"""

# Small programs and use cases
print("Small programs and use cases:")
# Swapping values
x, y = 5, 10
print(f"Before swap: x={x}, y={y}")
x, y = y, x
print(f"After swap: x={x}, y={y}")
input("Press Enter to continue...")

# Returning multiple values from a function
print("Returning multiple values from a function:")
def min_max(numbers):
    return min(numbers), max(numbers)
result = min_max([2, 8, 1, 5])
print(f"Min and Max: {result}")
input("Press Enter to continue...")

# Using tuples as dictionary keys
print("Using tuples as dictionary keys:")
location = {}
location[(10, 20)] = "Point A"
location[(30, 40)] = "Point B"
print(f"Dictionary with tuple keys: {location}")

"""
Summary:
- Tuples are immutable, ordered, allow duplicates, and can store any type.
- Only count and index methods are available.
- Use tuple unpacking for assigning multiple values.
- Parentheses alone do not create a tuple; a comma is needed for single-element tuples.
- Tuples are useful for fixed collections, swapping, returning multiple values, and as dictionary keys.
- input("Press Enter to continue...") is used for step-by-step review.
"""
