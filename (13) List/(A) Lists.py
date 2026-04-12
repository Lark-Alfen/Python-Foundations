"""
Lists in Python

A list is a built-in data structure that stores an ordered collection of items. Lists are mutable, can contain 
duplicates, and are heterogeneous (can store different types).
"""

print("--Lists in Python--\n")
input("Press Enter to continue...")

# Basic list creation
print("Basic list creation:")
my_list = [1, 2, 3, 4, 5]  # Creates a list with 5 integers
print(f"my_list: {my_list}")  # Prints the list
input("Press Enter to continue...")

"""
Line-by-line explanation:
- my_list = [1, 2, 3, 4, 5]: Creates a new list with elements 1, 2, 3, 4, 5.
- print(f"my_list: {my_list}"): Displays the list.
"""

# Demonstrating mutability
print("Mutability demonstration:")
my_list[0] = 10  # Changes the first element to 10
print(f"After changing first element: {my_list}")  # Shows updated list
my_list.append(6)  # Adds 6 to the end
print(f"After appending 6: {my_list}")  # Shows updated list
my_list.remove(3)  # Removes the first occurrence of 3
print(f"After removing 3: {my_list}")  # Shows updated list
input("Press Enter to continue...")

"""
Line-by-line explanation:
- my_list[0] = 10: Changes the value at index 0 to 10.
- my_list.append(6): Adds 6 to the end of the list.
- my_list.remove(3): Removes the first occurrence of 3 from the list.
"""

# Duplicates
print("Duplicates demonstration:")
my_list.append(10)  # Adds another 10
print(f"After appending duplicate 10: {my_list}")  # Shows list with duplicate
input("Press Enter to continue...")

"""
Line-by-line explanation:
- my_list.append(10): Adds another 10, showing lists can have duplicates.
"""

# Heterogeneous elements
print("Heterogeneous demonstration:")
my_list.append(print())  # Adds a function (prints None)
my_list.append(3.14)     # Adds a float
print(f"After adding string and float: {my_list}")
input("Press Enter to continue...")

"""
Line-by-line explanation:
- my_list.append("hello"): Adds a string to the list.
- my_list.append(3.14): Adds a float to the list.
"""

# Ordered and indexing
print("Ordered and indexing demonstration:")
print(f"First element: {my_list[0]}")  # Accesses first element
print(f"Last element: {my_list[-1]}")  # Accesses last element
input("Press Enter to continue...")

"""
Line-by-line explanation:
- my_list[0]: Accesses the first element.
- my_list[-1]: Accesses the last element (negative index).
"""

# List functionalities
print("List functionalities:")
print(f"Length: {len(my_list)}")  # Number of elements
print(f"Index of 10: {my_list.index(10)}")  # First index of 10
print(f"Count of 10: {my_list.count(10)}")  # Number of times 10 appears
my_list.insert(2, 'inserted')  # Inserts 'inserted' at index 2
print(f"After insert at index 2: {my_list}")
my_list.pop()  # Removes last element
print(f"After pop (remove last): {my_list}")
my_list.sort(key=str)  # Sorts list by string representation
print(f"After sort (by string): {my_list}")
my_list.reverse()  # Reverses the list
print(f"After reverse: {my_list}")
input("Press Enter to continue...")

"""
Line-by-line explanation:
- len(my_list): Returns the number of elements.
- my_list.index(10): Finds the first index of 10.
- my_list.count(10): Counts how many times 10 appears.
- my_list.insert(2, 'inserted'): Inserts 'inserted' at index 2.
- my_list.pop(): Removes the last element.
- my_list.sort(key=str): Sorts the list by string value.
- my_list.reverse(): Reverses the order of the list.
"""

# Slicing
print("Slicing demonstration:")
slice_example = my_list[1:4]  # Gets elements from index 1 to 3
print(f"Slice from index 1 to 3: {slice_example}")
input("Press Enter to continue...")

"""
Line-by-line explanation:
- my_list[1:4]: Slices the list from index 1 up to (not including) 4.
"""

# List slicing using loops
print("List slicing using loops:")
start = 2
end = 5
sliced = []
for i in range(start, end):
    sliced.append(my_list[i])  # Adds elements from index 2 to 4
print(f"Elements from index {start} to {end-1}: {sliced}")
input("Press Enter to continue...")

"""
Line-by-line explanation:
- for i in range(start, end): Loops from start to end-1.
- sliced.append(my_list[i]): Adds each element in the range to the new list.
- This manually slices the list using a loop.
"""

# Nested lists
print("Nested lists demonstration:")
nested = [[1, 2], [3, 4]]
print(f"Nested list: {nested}")
print(f"Accessing element: {nested[1][0]}")
input("Press Enter to continue...")

# More list functionalities and methods
print("\nMore list functionalities and methods:")

# append()
my_list.append('new')  # Adds 'new' to the end
print(f"After append('new'): {my_list}")

# insert()
my_list.insert(1, 'inserted at 1')  # Inserts at index 1
print(f"After insert(1, 'inserted at 1'): {my_list}")

# extend()
extension = [100, 200]
my_list.extend(extension)  # Adds all elements from extension
print(f"After extend([100, 200]): {my_list}")

# remove()
my_list.remove('new')  # Removes first occurrence of 'new'
print(f"After remove('new'): {my_list}")

# pop()
popped = my_list.pop()  # Removes and returns last element
print(f"After pop(): {my_list}, popped value: {popped}")

# index()
first_10_index = my_list.index(10)  # Finds first index of 10
print(f"Index of 10: {first_10_index}")

# count()
ten_count = my_list.count(10)  # Counts occurrences of 10
print(f"Count of 10: {ten_count}")

# sort()
# To avoid errors with mixed types, sort only numbers
numbers_only = [x for x in my_list if isinstance(x, (int, float))]
numbers_only.sort()
print(f"Sorted numbers only: {numbers_only}")

# reverse()
my_list.reverse()  # Reverses the list in place
print(f"After reverse(): {my_list}")

# copy()
copy_list = my_list.copy()  # Shallow copy
print(f"Copy of list: {copy_list}")

# clear()
copy_list.clear()  # Removes all elements
print(f"After clear(): {copy_list}")

input("Press Enter to continue...")

"""
Line-by-line explanation:
- append(x): Adds x to the end of the list.
- insert(i, x): Inserts x at index i.
- extend(iterable): Adds all elements from another iterable.
- remove(x): Removes the first occurrence of x.
- pop(): Removes and returns the last element.
- index(x): Returns the first index of x.
- count(x): Counts how many times x appears.
- sort(): Sorts the list in place (only works if all elements are comparable).
- reverse(): Reverses the list in place.
- copy(): Returns a shallow copy of the list.
- clear(): Removes all elements from the list.
"""

# Summary:
# - Lists are powerful, flexible, and widely used in Python.
# - They are mutable, ordered, allow duplicates, and can store any type.
# - Common functionalities: append, remove, insert, pop, sort, reverse, count, index, slicing, nesting.
# - input("Press Enter to continue...") is used for step-by-step review.

# Demonstration: Print positive and negative values separately from a mixed list
print("\n--- Demonstration: Print positive and negative values separately ---")
mixed_list = [10, -5, 7, -2, 0, 15, -8]

# Using for loop and if statement to print positive values
print("Positive values (using for loop and if):")
for value in mixed_list:
    if value > 0:
        print(value)
input("Press Enter to continue...")

# Using while loop and continue to print negative values
print("Negative values (using while loop and continue):")
i = 0
while i < len(mixed_list):
    if mixed_list[i] >= 0:
        i += 1
        continue  # Skip non-negative values
    print(mixed_list[i])
    i += 1
input("Press Enter to continue...")

"""
Line-by-line explanation:
- mixed_list: Contains both positive and negative values.
- for value in mixed_list: Loops through each value.
- if value > 0: Checks if value is positive; prints it if so.
- while i < len(mixed_list): Loops through list by index.
- if mixed_list[i] >= 0: Skips non-negative values using continue.
- print(mixed_list[i]): Prints negative values only.
- len(mixed_list): Returns the number of elements in the list.
"""

# Demonstrating copy: assignment vs .copy()
print("\nCopying lists: assignment vs shallow copy vs deep copy demonstration:")

# ==============================
# Assignment (NOT a copy)
# ==============================
print("Using assignment (NOT a copy):")
input("Press Enter to continue...")

original = [1, 2, 3, 4, 5]
assigned = original  # Assignment: both variables point to the SAME list

assigned[0] = 99  # Modify assigned list

print("After modifying assigned:")
print(f"original (shows change): {original}")
print(f"assigned: {assigned}")

input("Press Enter to continue...")


# ==============================
# Shallow Copy
# ==============================
print("\nUsing .copy() for shallow copy:")
input("Press Enter to continue...")

original = [1, 2, 3, 4, 5]
shallow_copy = original.copy()  # New list created

shallow_copy[0] = 77

print("After modifying shallow_copy:")
print(f"original (remains unchanged): {original}")
print(f"shallow_copy: {shallow_copy}")

input("Press Enter to continue...")


# ==============================
# Deep Copy (with nested list)
# ==============================
import copy

print("\nUsing deepcopy() for deep copy:")
input("Press Enter to continue...")

original = [[1, 2], [3, 4]]
deep_copy = copy.deepcopy(original)

deep_copy[0][0] = 111

print("After modifying deep_copy:")
print(f"original (remains unchanged): {original}")
print(f"deep_copy: {deep_copy}")

input("Press Enter to continue...")


"""
Explanation:

1. assigned = original
   - This is NOT a copy.
   - Both variables reference the SAME list.
   - Changing one changes the other.

2. shallow_copy = original.copy()
   - Creates a new outer list.
   - Works independently for simple (non-nested) lists.
   - Nested objects are still shared.

3. deep_copy = copy.deepcopy(original)
   - Creates a completely independent copy.
   - Even nested objects are duplicated.
"""

