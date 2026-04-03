"""
Exception Handling in Python

Errors are problems in a program that cause it to stop running. There are two main types:
- Syntax Errors: Mistakes in the code structure (e.g., missing colon, misspelled keyword). These cannot be handled by exception handling and must be fixed in the code.
- Exceptions: Errors that occur during execution (e.g., dividing by zero, accessing a missing file). These can be handled using exception handling.

Some errors that cannot be handled by exception handling:
- SyntaxError
- IndentationError
- SystemExit
- KeyboardInterrupt

Exceptions vs Errors:
- Errors (like SyntaxError) are detected before the program runs and stop execution immediately.
- Exceptions are detected while the program is running and can be handled to prevent the program from crashing.
"""

print("--Exception Handling in Python--\n")
input("Press Enter to continue...")

# Exception handling keywords
print("Exception handling keywords:")
print("- try: Block of code to test for errors.")
print("- except: Block to handle the error if it occurs.")
print("- else: Block to run if no error occurs in try.")
print("- finally: Block that always runs, error or not.")
print("- raise: Used to raise a custom exception.")
input("Press Enter to continue...")

# Simple try-except example
print("Simple try-except example:")
try:
    x = 10 / 0
except ZeroDivisionError:
    print("You can't divide by zero!")
print("This line runs after handling the exception so the flow continues.")
input("Press Enter to continue...")

"""
Explanation:
- The code in try block may cause an exception.
- If ZeroDivisionError occurs, the except block runs.
"""

# try-except with Exception as err
print("try-except with 'except Exception as err':")
try:
    y = int('abc')
except Exception as err:
    print(f"An error occurred which was: {err}")
print("This line runs after handling the exception so the flow continues.")
print("You can use 'except Exception as err' to catch any exception and get its message.")
input("Press Enter to continue...")

"""
Explanation:
- 'except Exception as err' catches any exception and stores it in 'err'.
- Useful for debugging or logging errors.
"""

# try-except-else
print("try-except-else example:")
try:
    num = int(input("Enter a number: "))
except ValueError:
    print("That's not a valid number!")
else:
    print(f"You entered: {num}")
print("This line runs after handling the exception so the flow continues.")
input("Press Enter to continue...")

"""
Explanation:
- The else block runs only if no exception occurs in try.
- Useful for code that should only run if try succeeds.
"""

# try-except-finally
print("try-except-finally example:")
try:
    print("Inside try block.")
    num = int(input("Enter a number(If you enter 0, it will raise an error): "))
    result = 10 / num
    print(f"Result: {result}")
except Exception as err:
    print(f"Error: {err}")
finally:
    print("This always runs (finally block runs always)")
input("Press Enter to continue...")

"""
Explanation:
- The finally block always runs, whether or not an exception occurred.
- Useful for cleanup actions (like closing files, releasing resources, or printing final messages).
"""

# raise example
print("raise example:")
def check_positive(n):
    if n < 0:
        raise ValueError("Number must be positive!")
    return n
try:
    n = int(input("Enter a positive number: "))
    check_positive(n)
    print(f"You entered: {n}")
except ValueError as err:
    print(f"Custom error: {err}")
input("Press Enter to continue...")

"""
Explanation:
- raise is used to trigger an exception manually.
- Useful for enforcing rules or validating input.
"""

"""
Summary:
- Errors stop the program; exceptions can be handled.
- Use try, except, else, finally, and raise for robust error handling.
- Always use finally for cleanup, and raise for custom exceptions.
- input("Press Enter to continue...") is used for step-by-step review.
"""
