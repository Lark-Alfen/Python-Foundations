"""
**kwargs in Python Functions and Decorators

**kwargs allows you to pass a variable number of keyword (named) arguments to a function. The arguments are collected into a dictionary named 'kwargs' (or any name you choose, but the ** is required).

Decorators can also use **kwargs to accept and forward any number of keyword arguments to the wrapped function.

Key Concepts:
- **kwargs collects extra keyword arguments into a dictionary.
- You can loop through **kwargs to process all key-value pairs.
- Decorators using **kwargs can wrap functions with any number of keyword arguments.

Example Explained:
"""

def decorate(func):
    def wrapper(**kwargs):
        print("kargs will be passed to the function as a dictionary:", kwargs)
        print(input("Press Enter to continue..."))
        print("welcome to before the function")     # Code before the original function
        func(**kwargs)           # Call the original function with keyword arguments
        print("thank you for using the decorator")  # Code after the original function
    return wrapper

@decorate
def information(**kwargs):   # **kwargs can also be written as **k or **kw (any name) but ** is important
    for i in kwargs:
        print(f"{i} : {kwargs[i]}")

information(name="Alice", age=30, city="New York")

"""
Explanation:
- The decorate function wraps another function and uses **kwargs to accept any number of keyword arguments.
- When information(name="Alice", age=30, city="New York") is called, all arguments are collected into a dictionary: {'name': 'Alice', 'age': 30, 'city': 'New York'}.
- The wrapper prints the dictionary, then calls the original information function with all keyword arguments using func(**kwargs).
- The information function loops through **kwargs and prints each key-value pair.
- The decorator prints messages before and after the function call.
- **kwargs is a powerful feature for writing flexible functions and decorators that can handle any number of keyword arguments.
"""