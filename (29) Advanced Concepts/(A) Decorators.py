"""
Decorators in Python

A decorator is a function that takes another function as input and extends or alters its behavior without modifying its code. Decorators are widely used for logging, access control, timing, memoization, and more.

Key Concepts:
- Decorators allow you to add functionality to existing functions in a clean and readable way.
- The @decorate syntax is a shortcut for hello = decorate(hello).
- The inner function (wrapper) usually calls the original function and can do something before and/or after it.
- Decorators can accept arguments if the wrapped function does.

Example Explained:
"""

def decorate(func):
    def wrapper(a):
        print("welcome to before the function")  # Code before the original function
        print(func(a))                           # Call the original function and print its result
        print("thank you for using the decorator")  # Code after the original function
    return wrapper

@decorate
def hello(a):
    return f"Hello, {a}!"  # The function to be decorated

a = "world"
hello(a)  # Calls wrapper(a) instead of hello(a)

"""
Explanation:
- decorate is a decorator function. It takes a function (func) as input and returns a new function (wrapper).
- The @decorate syntax applies the decorator to hello, so hello now refers to wrapper.
- When you call hello(a), it actually calls wrapper(a):
    1. Prints a message before the function.
    2. Calls the original hello(a) and prints its return value.
    3. Prints a message after the function.
- This allows you to add extra behavior before and after the original function runs, without changing its code.
- Decorators are a powerful feature for code reuse and separation of concerns.
"""