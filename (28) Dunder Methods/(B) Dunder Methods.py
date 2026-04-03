"""
Dunder (Double Underscore) Methods in Python

Dunder methods (short for "double underscore" methods, also called magic methods or special methods) are special methods with names that start and end with double underscores (e.g., __init__, __str__).

They allow you to define how your objects behave with built-in Python operations (like printing, arithmetic, comparisons, iteration, etc.).

You don't call dunder methods directly; instead, Python calls them automatically in response to certain operations.

Below is a categorized list of important dunder methods you should know. This is for reference only—no code implementations here.

LEVEL 1 — MUST KNOW (Daily Use)
Object Creation
    __new__
    __init__
    __del__
Representation
    __str__
    __repr__
Comparisons
    __eq__
    __ne__
    __lt__
    __le__
    __gt__
    __ge__
Arithmetic Operators
    __add__
    __sub__
    __mul__
    __truediv__
    __floordiv__
    __mod__
    __pow__
Container Behavior
    __len__
    __getitem__
    __setitem__
    __delitem__
    __contains__
Iteration
    __iter__
    __next__
Callable Objects
    __call__
Context Managers
    __enter__
    __exit__
Boolean Conversion
    __bool__

LEVEL 2 — COMMON (Used Often in Real Projects)
Reverse + In-Place Operators
    __radd__     __iadd__
    __rsub__     __isub__
    __rmul__     __imul__
    __rtruediv__ __itruediv__
    # Used when supporting: 5 + obj, obj += 5
Formatting & Display
    __format__
    __bytes__
Attribute Access Control
    __getattr__
    __getattribute__
    __setattr__
    __delattr__
    __dir__
    # Very powerful → used in frameworks.
Hashing / Dictionaries
    __hash__
    # Needed for: set(), dict keys
Type Conversion
    __int__
    __float__
    __complex__
    __index__
Iteration Extras
    __reversed__

LEVEL 3 — OCCASIONALLY USEFUL
These appear when writing libraries, advanced utilities, or frameworks.
Class & Subclass Hooks
    __init_subclass__
    __class_getitem__
    # Used in: generics, typing, advanced class customization
Descriptor Protocol
    __get__
    __set__
    __delete__
    __set_name__
    # Used behind: @property, ORM models, Django fields, dataclasses internals
Copy / Pickling Support
    __copy__
    __deepcopy__
    __reduce__
    __reduce_ex__
    # Serialization & multiprocessing.
Numeric Unary Operations
    __neg__
    __pos__
    __abs__
    __invert__
Memory / Size
    __sizeof__
Awaitable / Async Support (Occasional)
    __await__
    __aiter__
    __anext__
    __aenter__
    __aexit__
    # Used in async frameworks.
"""
