"""
While Loops in Python

A while loop repeatedly executes a block of code as long as a condition remains True.
It is useful for situations where you don't know in advance how many times you need to repeat.
"""

print("--While Loops in Python--\n")
# Basic while loop
print("Basic while loop:")
count = 1
while count <= 5:
    print(f"Count: {count}")
    count += 1
input("Press Enter to continue...")

"""
Explanation:
- The loop runs as long as the condition (count <= 5) is True.
- The variable 'count' is initialized to 1 and is updated in each iteratio using count += 1.
- Without updating the loop variable, the loop would run infinitely.
- The loop variable is updated inside the loop.
- When the condition becomes False, the loop stops.
"""

# While loop with user input
print("While loop with user input:")
user_input = ''
while user_input != 'exit':
    user_input = input("Type 'exit' to stop: ")
    print(f"You typed: {user_input}")
input("Press Enter to continue...")

"""
Explanation:
- The loop continues until the user types 'exit'.
- Useful for interactive programs or repeated prompts.
"""

# Infinite loop (with break)
print("Infinite loop with break:")
while True:
    answer = input("Enter 'q' to quit: ")
    if answer == 'q':
        print("Quitting loop.")
        break
    print(f"You entered: {answer}")
input("Press Enter to continue...")

"""
Explanation:
- while True creates an infinite loop.
- break is used to exit the loop when a condition is met.
- Useful for menu-driven programs or waiting for a specific input.
"""

# Note:
# While both examples use a loop that waits for a specific user input to exit,
# the first uses a condition in the while statement (user_input != 'exit'),
# so the loop checks the exit condition before each iteration.
# The second uses 'while True' (an infinite loop) and exits using 'break' when the condition is met inside the loop.
# The 'while True' + break pattern is more flexible for complex exit logic or multiple exit points.
# Both are common, but 'while True' is preferred for input validation and menu-driven programs.

# continue statement in while loop
print("Continue statement in while loop:")
i = 0
while i < 5:
    i += 1
    if i % 2 == 0:
        print(f"Skipping even number: {i}")
        continue
    print(f"Odd number: {i}")
input("Press Enter to continue...")

"""
Explanation:
- continue skips the rest of the current iteration and moves to the next.
- In the example, even numbers are skipped.
"""

# else statement in while loop
print("Else statement in while loop:")
i = 1
while i <= 3:
    print(f"i = {i}")
    i += 1
else:
    print("Loop completed without break.")
input("Press Enter to continue...")

"""
Explanation:
- else runs after the loop finishes normally (not interrupted by break).
- Useful for post-loop actions.
"""

# else with break in while loop
print("Else with break in while loop:")
i = 1
while i <= 5:
    print(f"i = {i}")
    if i == 3:
        print("Breaking loop at i == 3")
        break
    i += 1
else:
    print("This will not print because break was used.")
input("Press Enter to continue...")

"""
Explanation:
- If break is used, the else block does not run.
- This helps distinguish between loops that finish normally and those interrupted by break.
"""

# Using while loop for input validation
print("While loop for input validation:")
while True:
    num = input("Enter a positive number: ")
    if num.isdigit() and int(num) > 0:
        print(f"You entered: {num}")
        break
    print("Invalid input. Try again.")

"""
Explanation:
- The loop keeps asking for input until a valid positive number is entered.
- Useful for robust user input handling.
"""

"""
Summary:
- while loops repeat as long as a condition is True.
- Use break to exit early, continue to skip iterations, else for post-loop actions.
- Infinite loops (while True) are useful for repeated prompts or menu-driven programs.
- Input validation is a common use case.
- input("Press Enter to continue...") is used for step-by-step review and better learning experience.
"""
