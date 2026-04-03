"""
Sets in Python

A set is a built-in data structure that stores an unordered collection of unique items. Sets are mutable, do not allow duplicates, and are heterogeneous (can store different types, but only hashable/immutable types).
"""

print("--Sets in Python--\n")
input("Press Enter to continue...")

# Basic set creation
print("Basic set creation:")
my_set = {1, 2, 3, 4, 5}
print(f"my_set: {my_set}")
input("Press Enter to continue...")

"""
Set Properties:
- Mutable: You can add or remove elements after creation.
- Unordered: Elements do not retain any order.
- Unique: No duplicate values allowed.
- Heterogeneous: Can store different types, but only hashable/immutable types.
"""

# Demonstrating mutability
print("Mutability demonstration:")
my_set.add(6)  # Adds 6 to the set
print(f"After add(6): {my_set}")
my_set.remove(3)  # Removes 3 from the set
print(f"After remove(3): {my_set}")
input("Press Enter to continue...")

# Duplicates
print("Duplicates demonstration:")
dup_set = {1, 2, 2, 3}
print(f"Set with duplicates (duplicates removed automatically): {dup_set}")
input("Press Enter to continue...")

# Heterogeneous elements
print("Heterogeneous demonstration:")
mixed_set = {1, "hello", 3.14}
print(f"Set with mixed types: {mixed_set}")
input("Press Enter to continue...")

# Unordered and indexing
print("Unordered demonstration:")
print("Sets do not support indexing or order.")
input("Press Enter to continue...")

# Set methods demonstration
print("\nSet methods demonstration:")
method_set = {1, 2, 3}
method_set.add(4)  # Adds 4 to the set
print(f"After add(4): {method_set}")
method_set.update([5, 6])  # Adds multiple elements
print(f"After update([5, 6]): {method_set}")
method_set.remove(2)  # Removes 2 from the set but raises an error if not found
print(f"After remove(2): {method_set}")
method_set.discard(10)  # Works like remove but does not raise an error if the element is not found
print(f"After discard(10): {method_set}")
popped = method_set.pop()  # Removes and returns an arbitrary element based on hash values (since sets are unordered)
print(f"After pop(): {method_set}, popped value: {popped}")
method_set.clear()  # Removes all elements
print(f"After clear(): {method_set}")
input("Press Enter to continue...")

"""
Line-by-line explanation:
- add(x): Adds x to the set (if not already present).
- update(iterable): Adds all elements from another iterable.
- remove(x): Removes x from the set (raises error if not found).
- discard(x): Removes x if present, does nothing if not (no error).
- pop(): Removes and returns an arbitrary element (since sets are unordered).
- clear(): Removes all elements from the set.

Note:
- discard() is safer than remove() if you are not sure the element exists.
- Set methods do not use indices because sets are unordered.
- Instead, sets use hash values to store and access elements efficiently.
- This is why you cannot access or remove elements by index, but you can add or remove by value.
- Sets are mutable: you can add or remove elements, but only if they are hashable (immutable types).
"""

# Hash values and immutability
print("Hash values and immutability:")
immutable_set = {1, 2, (3, 4)}  # Tuples are hashable
print(f"Set with tuple: {immutable_set}")
try:
    my_set = {1, [2, 3]}  # Lists are not hashable
except TypeError as e:
    print(f"Error: {e}")
input("Press Enter to continue...")

# Hash values and immutability in sets
print("\nHash values and immutability in sets:")
# Demonstrate hashing on individual values
values = [10, "hello", (1, 2), 3.14]
for val in values:
    print(f"Value: {val}, Type: {type(val)}, Hash: {hash(val)}")
input("Press Enter to continue...")

"""
Explanation:
- The hash() function returns a unique integer for each immutable value.
- Sets use these hash values to store and quickly retrieve elements.
- Only immutable types (int, float, str, tuple) can be hashed and used in sets.
- Mutable types (like lists, dicts) cannot be hashed and will cause an error if added to a set.
- Hashing allows sets to check membership and uniqueness efficiently.
- Example: hash(10), hash("hello"), hash((1, 2)), hash(3.14) all produce unique hash values.
- The hash value may differ between runs and Python versions, but is consistent for the same value in a session.
"""

# Difference between sets, lists, and tuples
print("Difference between sets, lists, and tuples:")
print("Sets are unordered and unique, lists are ordered and allow duplicates, tuples are ordered and immutable.")
print("Sets do not support indexing, lists and tuples do.")
input("Press Enter to continue...")

# Set operations
print("Set operations:")
a = {1, 2, 3}
b = {3, 4, 5}
print(f"a: {a}, b: {b}")
print(f"Union: {a | b}")
print(f"Union using union(): {a.union(b)}")
input("Press Enter to continue...")
print(f"Intersection: {a & b}")
print(f"Intersection using intersection(): {a.intersection(b)}")
input("Press Enter to continue...")
print(f"Difference: {a - b}")
print(f"Difference a - b using difference(): {a.difference(b)}")
print("\nAnd")
print(f"Difference b - a using difference(): {b.difference(a)}")
input("Press Enter to continue...")
print(f"Symmetric Difference: {a ^ b}")
print(f"Symmetric Difference using symmetric_difference(): {a.symmetric_difference(b)}")
input("Press Enter to continue...")

# Compound set operations demonstration
print("\nCompound set operations demonstration:")
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}
print(f"set_a: {set_a}")
print(f"set_b: {set_b}")
input("Press Enter to continue...")

# Union (|=)
print("Union demonstration (|=):")
set_a_copy = set_a.copy() # Create a copy to demonstrate in-place modification
# set_a_copy |= set_b is equivalent to: set_a_copy = set_a_copy | set_b
set_a_copy |= set_b  # Updates set_a_copy with all unique elements from both sets
print(f"After set_a |= set_b (union): {set_a_copy}")
input("Press Enter to continue...")

# Intersection (&=)
print("Intersection demonstration (&=):")
set_a_copy = set_a.copy() # Create a copy to demonstrate in-place modification
# set_a_copy &= set_b is equivalent to: set_a_copy = set_a_copy & set_b
set_a_copy &= set_b  # Updates set_a_copy with only the elements found in both sets
print(f"After set_a &= set_b (intersection): {set_a_copy}")
input("Press Enter to continue...")

# Difference (-=)
print("Difference demonstration (-=):")
set_a_copy = set_a.copy() # Create a copy to demonstrate in-place modification
# set_a_copy -= set_b is equivalent to: set_a_copy = set_a_copy - set_b
set_a_copy -= set_b  # Updates set_a_copy by removing elements found in set_b (keeps only elements unique to set_a)
print(f"After set_a -= set_b (difference): {set_a_copy}")
input("Press Enter to continue...")

# Symmetric difference (^=)
print("Symmetric difference demonstration (^=):")
set_a_copy = set_a.copy() # Create a copy to demonstrate in-place modification
# set_a_copy ^= set_b is equivalent to: set_a_copy = (set_a_copy | set_b) - (set_a_copy & set_b)
set_a_copy ^= set_b  # Updates set_a_copy with elements in either set, but not both
print(f"After set_a ^= set_b (symmetric difference): {set_a_copy}")
input("Press Enter to continue...")

"""
Line-by-line explanation:
- set_a |= set_b: Updates set_a with the union of set_a and set_b (all unique elements from both). Equivalent to set_a = set_a | set_b.
- set_a &= set_b: Updates set_a with the intersection of set_a and set_b (only elements in both). Equivalent to set_a = set_a & set_b.
- set_a -= set_b: Updates set_a by removing elements found in set_b (only elements unique to set_a remain). Equivalent to set_a = set_a - set_b.
- set_a ^= set_b: Updates set_a with the symmetric difference (elements in either set, but not both). Equivalent to set_a = (set_a | set_b) - (set_a & set_b).
- These compound operators modify the set in place.
"""

# Set membership and iteration
print("Set membership and iteration:")
if 2 in a:
    print("2 is in set a")
for value in b:
    print(f"Value in set b: {value}")
input("Press Enter to continue...")

# Small programs and use cases
print("Small programs and use cases:")
# Remove duplicates from a list
nums = [1, 2, 2, 3, 4, 4, 5]
unique_nums = set(nums)
print(f"Unique numbers from list: {unique_nums}")
input("Press Enter to continue...")

# Find common elements
set1 = {1, 2, 3}
set2 = {2, 3, 4}
common = set1 & set2
print(f"Common elements: {common}")
input("Press Enter to continue...")

'''
Note: lets say we run a loop for the set s = {1, 2, 3}

for x in s:
    print(x)

The output will be:
1
2
3

now if we wmodify the same set s during that code session, s = {1 , 2, 4, 3}
and we run the same loop again, the output will be:
1
2
3
4
This is because sets are unordered, so the order of elements is not guaranteed. When we modify the set, the order 
can change, and the new element (4) may appear in a different position when we iterate over it again.
'''

"""
Summary:
- Sets are mutable, unordered, unique, and require hashable elements.
- Only immutable types can be set elements.
- Sets are useful for membership tests, removing duplicates, and mathematical operations.
- input("Press Enter to continue...") is used for step-by-step review.
"""
