"""
The filter() Function in Python

The filter() function is used to filter elements from an iterable (like a list) based on a condition. It returns an iterator containing only the elements for which the function returns True.

Key Concepts:
- filter(function, iterable) applies 'function' to each item in 'iterable'.
- Only items for which the function returns True are included in the result.
- The result is a filter object (an iterator), which can be converted to a list, set, etc.
- filter() is often used with lambda functions for concise, one-line filtering.

Example Explained:
"""

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

# Traditional for loop to filter even numbers
filt_a = []
def filter_func(*args):
    for i in args:
        if i % 2 == 0:
            filt_a.append(i)
filter_func(*a)
print(filt_a)  # Output: [2, 4, 6, 8, 10, 12, 14]

print(input("Press Enter to continue..."))

# Using filter with a lambda function
Filtered_a = filter(lambda x: True if x % 2 == 0 else False, a)
print(list(Filtered_a))  # Output: [2, 4, 6, 8, 10, 12, 14]

"""
Explanation:
- The first part uses a traditional for loop and a function to filter even numbers from the list.
- The second part uses filter() with a lambda function to do the same thing in a single line.
- filter(lambda x: True if x % 2 == 0 else False, a) means: for each x in a, include x if x is even.
- filter() returns an iterator, so you usually convert it to a list to see the results.
- filter() is a powerful tool for extracting elements from iterables based on a condition, making your code more concise and readable.
"""

