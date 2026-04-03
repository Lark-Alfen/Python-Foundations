"""
Dictionaries in Python

A dictionary is a built-in data structure that stores key-value pairs. Dictionaries are mutable, unordered 
(insertion order preserved in Python 3.7+), and keys must be unique and hashable (immutable).
"""

print("--Dictionaries in Python--\n")
input("Press Enter to continue...")

# Basic dictionary creation
print("Basic dictionary creation:")
my_dict = {'name': 'Alice', 'age': 25, 'grade': 'A'}
print(f"my_dict: {my_dict}")
input("Press Enter to continue...")

"""
Dictionary Properties:
- Mutable: You can add, change, or remove key-value pairs after creation.
- Unordered: No guaranteed order (insertion order preserved in Python 3.7+).
- Keys must be unique and hashable (immutable types like int, str, tuple).
- Values can be any type and can be duplicated.
"""

# Demonstrating mutability
print("Mutability demonstration:")
# These operations can also be done using methods like update(), pop(), setdefault(), etc.
my_dict['age'] = 26  # Change value
print(f"After changing age: {my_dict}")
my_dict['city'] = 'New York'  # Add new key-value pair
print(f"After adding city: {my_dict}")
del my_dict['grade']  # Remove key-value pair
print(f"After deleting grade: {my_dict}")
input("Press Enter to continue...")

# Keys and values
print("Keys and values demonstration:")
print(f"Keys: {list(my_dict.keys())}") # Get list of keys
print(f"Values: {list(my_dict.values())}") # Get list of values
print(f"Items: {list(my_dict.items())}") # Get list of key-value pairs as tuples
input("Press Enter to continue...")

# Dictionary methods
print("Dictionary methods demonstration:")
my_dict.update({'country': 'USA'})  # Add/update key-value pairs
print(f"After update: {my_dict}")
value = my_dict.get('name')  # Get value for key
print(f"Value for 'name': {value}")
removed = my_dict.pop('city')  # This removes 'city' which is a key and returns the value associated with it
print(f"After pop('city'): {my_dict}, removed value: {removed}")
my_dict.setdefault('email', 'alice@example.com')  # Set default value if key not present
print(f"After setdefault('email'): {my_dict}")
my_dict.clear()  # Remove all items
print(f"After clear(): {my_dict}")
input("Press Enter to continue...")

# popitem()
popped_item = my_dict.popitem()  # Removes and returns the last inserted key-value pair (as of Python 3.7+)
print(f"After popitem(): {my_dict}, popped item: {popped_item}")

# items()
all_items = my_dict.items()  # Returns a view of all key-value pairs as tuples
print(f"All items (using items()): {list(all_items)}")

"""
Line-by-line explanation:
- update(dict): Adds or updates key-value pairs.
- get(key): Returns value for key, or None if not found.
- pop(key): Removes key and returns its value.
- setdefault(key, default): Sets value if key not present.
- clear(): Removes all items.
- popitem(): Removes and returns the last inserted key-value pair as a tuple (key, value).
- items(): Returns a view of all key-value pairs as tuples (useful for iteration).
"""

# Keys must be hashable
print("Keys must be hashable demonstration:")
try:
    bad_dict = {[1, 2]: 'value'}  # List is not hashable
except TypeError as e:
    print(f"Error: {e}")
good_dict = {(1, 2): 'value'}  # Tuple is hashable
print(f"Dictionary with tuple key: {good_dict}")
input("Press Enter to continue...")

# Difference between dictionaries, lists, sets, and tuples
print("Difference between dictionaries, lists, sets, and tuples:")
print("Dictionaries store key-value pairs, lists and tuples store values by index, sets store unique values.")
print("Dictionaries require unique, hashable keys; lists and tuples allow duplicates and any type.")
input("Press Enter to continue...")

# Dictionary iteration
print("Dictionary iteration demonstration:")
my_dict = {'a': 1, 'b': 2, 'c': 3}
for key in my_dict:
    print(f"Key: {key}, Value: {my_dict[key]}")
input("Press Enter to continue...")

for key, value in my_dict.items():
    print(f"Key: {key}, Value: {value}")
input("Press Enter to continue...")

# Dictionary unpacking
print("Dictionary unpacking demonstration:")
def print_info(name, age):
    print(f"Name: {name}, Age: {age}")
info = {'name': 'Bob', 'age': 30}
print_info(**info)  # Unpacks dictionary into function arguments
# The **info syntax unpacks the dictionary so that each key-value pair is passed as a named argument to the function.
# Equivalent to: print_info(name=info['name'], age=info['age'])
input("Press Enter to continue...")

"""
Note: The use of * and ** in Python

- * (single asterisk) is used to unpack sequences (like lists or tuples) into positional arguments in function calls.
  Example:
      def add(a, b):
          return a + b
      nums = [2, 3]
      add(*nums)  # Equivalent to add(2, 3)

- ** (double asterisk) is used to unpack dictionaries into keyword arguments in function calls.
  Example:
      def greet(name, age):
          print(f"Hello {name}, you are {age} years old.")
      info = {'name': 'Alice', 'age': 25}
      greet(**info)  # Equivalent to greet(name='Alice', age=25)

- * can also be used in function definitions to accept a variable number of positional arguments (as a tuple):
      def func(*args):
          print(args)
      func(1, 2, 3)  # args = (1, 2, 3)

- ** can be used in function definitions to accept a variable number of keyword arguments (as a dictionary):
      def func(**kwargs):
          print(kwargs)
      func(a=1, b=2)  # kwargs = {'a': 1, 'b': 2}

- These features make functions flexible and allow dynamic argument passing and collection.
"""

# Small programs and use cases
print("Small programs and use cases:")
# Counting occurrences
words = ['apple', 'banana', 'apple', 'cherry']
count_dict = {}
for word in words:
    count_dict[word] = count_dict.get(word, 0) + 1
print(f"Word counts: {count_dict}")
input("Press Enter to continue...")

# Grouping values
students = [('Alice', 'A'), ('Bob', 'B'), ('Alice', 'A+')]
group_dict = {}
for name, grade in students:
    group_dict.setdefault(name, []).append(grade)
print(f"Grouped grades: {group_dict}")
input("Press Enter to continue...")

# Demonstrating copy: assignment vs .copy() for dictionaries
print("\nCopying dictionaries: assignment vs .copy() demonstration:")
print("Using assignment (deep copy):")
input("Press Enter to continue...")
d1 = {'a': 1, 'b': 2, 'c': 3}
deep_copy = d1  # Assignment: both variables point to the same dictionary (deep copy)
deep_copy['a'] = 99  # Change value in deep_copy
print(f"After modifying deep_copy:")
print(f"d1: {d1}")  # Shows change in original
def print_dicts():
    print(f"deep_copy: {deep_copy}")
print_dicts()
input("Press Enter to continue...")

# Using .copy() for shallow copy
print("\nCopying dictionaries: .copy() demonstration:")
input("Press Enter to continue...") 
d1 = {'a': 1, 'b': 2, 'c': 3}
shallow_copy = d1.copy()  # Shallow copy: new dictionary, same key-value pairs
shallow_copy['a'] = 77  # Change value in shallow_copy
print(f"After modifying shallow_copy:")
print(f"d1: {d1}")  # Original remains unchanged
print(f"shallow_copy: {shallow_copy}")  # Only shallow_copy changes

"""
Explanation:
- deep_copy = d1: Both variables refer to the same dictionary in memory. Changing one changes the other.
- shallow_copy = d1.copy(): Creates a new dictionary with the same key-value pairs. Changing one does not affect the other.
- Use .copy() when you want a separate dictionary that won't affect the original.
"""

"""
Summary:
- Dictionaries are mutable, store key-value pairs, and require unique, hashable keys.
- Values can be any type and duplicated.
- Common methods: update, get, pop, setdefault, clear, keys, values, items.
- Useful for fast lookups, counting, grouping, and flexible data storage.
- input("Press Enter to continue...") is used for step-by-step review.
"""
