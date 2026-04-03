"""
Data Structures in Python

Data structures are ways to organize and store data efficiently for different purposes.
Python provides several built-in data structures, and you can also create your own custom ones.
"""

print("--Data Structures in Python--\n")

# List example
print("List example:")
fruits = ['apple', 'banana', 'cherry']
print(f"fruits(list): {fruits}")
input("Press Enter to continue...")

# Tuple example
print("Tuple example:")
coordinates = (10, 20)
print(f"coordinates(tuple): {coordinates}")
input("Press Enter to continue...")

# Dictionary example
print("Dictionary example:")
student = {'name': 'Alice', 'age': 21, 'grade': 'A'}
print(f"student(dictionary): {student}")
input("Press Enter to continue...")

# Set example
print("Set example:")
unique_numbers = {1, 2, 3, 2, 1}
print(f"unique_numbers(set): {unique_numbers}")  # Duplicates are removed
input("Press Enter to continue...")

"""
Custom Data Structures
You can build your own data structures using classes or lists.
Common examples: Stack, Queue, Linked List, etc.
"""

# Stack example (using list)
print("Stack example (LIFO):")
stack = []
stack.append(1)
stack.append(2)
stack.append(3)
print(f"Stack after pushes: {stack}")
print(f"Pop: {stack.pop()}")  # Removes 3
print(f"Stack now: {stack}")
input("Press Enter to continue...")

# Queue example (using list)
print("Queue example (FIFO):")
queue = []
queue.append('a')
queue.append('b')
queue.append('c')
print(f"Queue after enqueues: {queue}")
print(f"Dequeue: {queue.pop(0)}")  # Removes 'a'
print(f"Queue now: {queue}")

"""
Note: Common Data Structure Terms (in depth)
- Mutable: Objects whose contents can be changed after creation. For example, lists can have 
elements added, removed, or modified. Dictionaries and sets are also mutable.
- Immutable: Objects whose contents cannot be changed after creation. Tuples and strings are 
immutable; once created, their values cannot be altered.
- Duplicates: Some structures allow repeated values (lists, tuples), while others (sets) 
automatically remove duplicates. Dictionaries allow duplicate values but not duplicate keys.
- Ordered: Elements are stored in a specific sequence and retain their order (lists, tuples, 
dictionaries in Python 3.7+). You can access elements by their position.
- Unordered: Elements are not stored in any particular sequence (sets). You cannot access elements 
by position.
- Heterogeneous: Structures can store elements of different types (e.g., a list can contain 
integers, strings, and floats together).
- Homogeneous: Structures are intended to store elements of the same type (not enforced in Python, 
but some languages require this).
- Key-value pairs: Data is stored as pairs of keys and values (dictionaries). Keys must be unique 
and immutable; values can be any type.
- LIFO (Last-In, First-Out): The last element added is the first one removed. Used in stacks 
(e.g., undo operations).
- FIFO (First-In, First-Out): The first element added is the first one removed. Used in queues 
(e.g., print jobs, task scheduling).
- Indexing: Accessing elements by their position (lists, tuples, strings). Not possible in sets 
or unordered structures.
- Hashing: Sets and dictionaries use hash functions to store and retrieve elements efficiently. 
Keys in dictionaries and elements in sets must be hashable (immutable).
- Nested: Data structures can contain other data structures (e.g., a list of dictionaries, a 
dictionary of lists).
"""

"""
Summary:
- List: ordered, mutable, allows duplicates.
- Tuple: ordered, immutable, allows duplicates.
- Dictionary: key-value pairs, unordered (Python 3.7+ keeps insertion order), mutable.
- Set: unordered, unique elements.
- Custom structures (like stack, queue) can be built using lists or classes.
- input("Press Enter to continue...") is used for step-by-step review.
"""
