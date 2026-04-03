"""
*args in Python Functions and Decorators

*args allows you to pass a variable number of positional arguments to a function. The arguments are collected into a tuple named 'args' (or any name you choose, but the * is required).

Decorators can also use *args to accept and forward any number of arguments to the wrapped function.

Key Concepts:
- *args collects extra positional arguments into a tuple.
- You can loop through *args to process all arguments.
- Decorators using *args can wrap functions with any number of arguments.

Example Explained:
"""

def decorator(func):
    def wrapper(*args):
        print("args will be passed to the function as a tuple:", args)
        print(input("Press Enter to continue..."))
        print("welcome to before the function")     # Code before the original function
        print("your sum is:",func(*args))           # Call the original function and print its result
        print("thank you for using the decorator")  # Code after the original function
    return wrapper

@decorator
def sum(*args):     # *args can also be written as *a or *ag (any name, but * is important)
    temp = 0
    for i in args:
        temp += i
    return temp

sum(2, 34, 55, 12, 33)

"""
Explanation:
- The decorator function wraps another function and uses *args to accept any number of arguments.
- When sum(2, 34, 55, 12, 33) is called, all arguments are collected into a tuple (2, 34, 55, 12, 33).
- The wrapper prints the tuple, then calls the original sum function with all arguments using func(*args).
- The sum function loops through *args and adds all the numbers together.
- The decorator prints messages before and after the function call, and displays the result.
- *args is a powerful feature for writing flexible functions and decorators that can handle any number of arguments.
"""
