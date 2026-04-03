"""
Loops in Python

Python provides two main types of loops: for loops and while loops. Both are used to execute a block of code multiple times, but they differ in how they control the repetition.

1. For Loop:
- Used to iterate over a sequence (like a list, tuple, string, or range).
- The loop variable takes each value from the sequence, one by one.
- Syntax:
    for variable in sequence:
        # code block

2. While Loop:
- Repeats as long as a condition is True.
- The condition is checked before each iteration.
- Syntax:
    while condition:
        # code block

Control Statements (work in both for and while loops):
- break: Exits the loop immediately, even if the condition or sequence is not finished.
- continue: Skips the rest of the current iteration and moves to the next one.
- else: An optional block that runs if the loop completes normally (not interrupted by break).

These statements help you control the flow of your loops for more complex logic.

"""

print("Loops in Python\n")
print("Python provides for and while loops, plus break, continue, and else statements for advanced control.\n")
input("Press Enter to continue...")

# For loop example
print("For loop example:")
for i in range(3):
    print(f"Iteration {i}")
input("Press Enter to continue...")

# While loop example
print("While loop example:")
count = 0
while count < 3:
    print(f"Count is {count}")
    count += 1
input("Press Enter to continue...")

# break example
print("Break statement example:")
for i in range(5):
    if i == 3:
        print("Breaking at i = 3")
        break
    print(i)
input("Press Enter to continue...")

# continue example
print("Continue statement example:")
for i in range(5):
    if i % 2 == 0:
        continue
    print(f"Odd number: {i}")
input("Press Enter to continue...")

# else with loop example
print("Else with loop example:")
for i in range(3):
    print(i)
else:
    print("Loop completed without break.")
input("Press Enter to continue...")

"""
Summary:
- for loops: iterate over sequences.
- while loops: repeat while a condition is True.
- break: exit loop early.
- continue: skip to next iteration.
- else: runs if loop finishes without break.
- Use input("Press Enter to continue...") to pause and review each concept.
"""
