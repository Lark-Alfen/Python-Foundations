"""
For Loops in Python

A for loop is used to iterate over a sequence (like a list, tuple, string) or other iterable objects.
It allows you to execute a block of code multiple times, once for each item in the sequence.
"""

# Basic for loop over a list
print("For loop over a list:")
numbers = [1, 2, 3, 4, 5]
for num in numbers:
    print(num)  # Prints each number in the list

"""
Explanation:
- The variable 'num' takes the value of each item in 'numbers' one by one.
- The loop body (indented block) runs for each item.
- After the last item, the loop ends.
"""

input("Press Enter to continue...")

# For loop over a string
print("\nFor loop over a string:")
word = "hello"
for char in word:
    print(char)  # Prints each character in the string

"""
You can use for loops with any iterable: lists, tuples, strings, dictionaries (keys), sets, etc.
"""

input("Press Enter to continue...")

# Using range() in a for loop
print("\nUsing range() in a for loop:")
print("Using range(5):")
for i in range(5):
    print(i)  # Prints 0, 1, 2, 3, 4

"""
Explanation of range():
- range(n) generates numbers from 0 up to (but not including) n.
- Commonly used to repeat an action a specific number of times.
- range is like: range(start(default 0), stop(user input), step(default 1))
"""

input("Press Enter to continue...")

# Storing a range in a variable
print("\nStoring a range in a variable:")
r = range(3, 8)
for i in r:
    print(i)  # Prints 3, 4, 5, 6, 7

"""
You can specify a start and stop: range(start, stop)
- The loop above prints numbers from 3 to 7.
"""

input("Press Enter to continue...")

# Taking range from user input
print("\nTaking range from user input:")
start = int(input("Enter start: "))
stop = int(input("Enter stop: "))
for i in range(start, stop):
    print(i)

"""
This lets the user control the range of the loop.
"""

input("Press Enter to continue...")

# Using steps in range
print("\nUsing range with step:")
for i in range(0, 10, 2):
    print(i)  # Prints 0, 2, 4, 6, 8

"""
range(start, stop, step) lets you specify the increment (step).
- The above prints even numbers from 0 to 8.
"""

input("Press Enter to continue...")

# Reversed range
print("Reversed range:")
for i in range(10, 0, -1):
    print(i)  # Prints 10 down to 1

"""
If step is negative, range counts down.
- Useful for countdowns or reverse iteration.
"""

input("Press Enter to continue...")

# More scenarios:
print("\nLooping over a list with index (using range):")
fruits = ['apple', 'banana', 'cherry']
for idx in range(len(fruits)):
    print(f"Index {idx}: {fruits[idx]}")

input("Press Enter to continue...")

print("\nLooping with enumerate (index and value):")
for idx, fruit in enumerate(fruits):
    print(f"Index {idx}: {fruit}")

"""
Note: The len() function
- len() returns the number of items in an object (such as a list, string, tuple, etc.).
- In the example above, len(fruits) gives the total number of elements in the 'fruits' list (which is 3).
- It's commonly used to determine the range for looping over all indices of a sequence.
- Example: range(len(fruits)) creates a sequence from 0 up to (but not including) the length of the list.
"""

input("Press Enter to continue...")

"""
Explanation:
- Using range(len(list)) lets you access both the index and the value by index. Useful if you need 
the index for calculations or assignments.
- enumerate(list) gives you both the index and the value directly in each loop iteration. It's more 
Pythonic and readable for most use cases.
- Both methods are common for looping with indices, but enumerate() is preferred for clarity and 
simplicity.
- input("Press Enter to continue...") is used after each concept to let the user review the output 
before moving on.
"""

print("\n--- break statement in for loop ---")
for i in range(1, 6):
    print(f"i = {i}")
    if i == 3:
        print("Breaks the loop when i == 3")
        break
input("Press Enter to continue...")

"""
Explanation:
- break: Exits the loop immediately. In the example, the loop stops when i == 3.
- Useful for stopping a loop early when a condition is met.
"""

print("\n--- continue statement in for loop ---")
for i in range(1, 6):
    if i % 2 == 0:
        print(f"Skipping even number: {i}")
        continue
    print(f"Odd number: {i}")
input("Press Enter to continue...")

"""
Explanation:
- continue: Skips the rest of the current iteration and moves to the next one.
- In the example, even numbers are skipped and only odd numbers are printed.
- Useful for ignoring certain cases in a loop.
"""

print("\n--- else statement in for loop ---")
for i in range(1, 4):
    print(f"i = {i}")
    if i == 10:
        print("Breaking loop at i == 3, but this will never happen")
        break
else:
    print("Loop completed without break.")
input("Press Enter to continue...")

"""
Explanation:
- else: Runs after the loop finishes normally (no break).
- In the example, the else block prints a message after the loop completes.
- Useful for post-loop actions if the loop wasn't interrupted.
"""

print("\n--- else with break in for loop ---")
for i in range(1, 6):
    print(f"i = {i}")
    if i == 3:
        print("Breaking loop at i == 3")
        break
else:
    print("This will not print because break was used.")


"""
Explanation:
- If break is used, the else block does not run.
- This is useful for distinguishing between loops that finish normally and those interrupted by break.
"""

# Summary:
# - for loops are versatile and work with any iterable (lists, strings, ranges, etc.).
# - range() is commonly used for numeric loops, with options for start, stop, step, and reverse.
# - Use enumerate() to get both index and value when looping over a sequence.
# - break: exits the loop immediately when a condition is met.
# - continue: skips the rest of the current iteration and moves to the next.
# - else: runs after the loop finishes normally (not interrupted by break).
# - else with break: else block does not run if break is used.
