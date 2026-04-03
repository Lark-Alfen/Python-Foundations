"""
String Slicing in Python

Slicing allows you to extract a part (substring) of a string using the syntax: 
string[start:stop:step]
- start: index to begin the slice (inclusive, default is 0)
- stop: index to end the slice (exclusive, default is end of string)
- step: how many characters to skip (default is 1)
"""

text = "Programming"

# Basic slicing
print("Basic Slicing:")
print("text[0:6]:", text[0:6])      # 'Progra' (from index 0 to 5)
print("text[3:8]:", text[3:8])      # 'gramm' (from index 3 to 7)

input("Press Enter to continue...")

# Omitting start or stop
print("\nOmitting start or stop:")
print("text[:5]:", text[:5])        # 'Progr' (from start to index 4)
print("text[4:]:", text[4:])        # 'ramming' (from index 4 to end)

input("Press Enter to continue...")

# Using step
print("\nUsing step:")
print("text[::2]:", text[::2])      # 'Pormig' (every 2nd character)
print("text[1:8:2]:", text[1:8:2])  # 'rgam' (from index 1 to 7, every 2nd character)

input("Press Enter to continue...")

# Negative indices
print("\nNegative Indices:")
print("text[-7:-2]:", text[-7:-2])  # 'rammi' (from 4th to 9th character from end)

input("Press Enter to continue...")

# Negative step (reversing)
print("\nNegative Step (Reversing):")
print("text[::-1]:", text[::-1])    # 'gnimmargorP' (reversed string)
print("text[8:2:-1]:", text[8:2:-1]) # 'immarg' (from index 8 down to 3, backwards; excludes index 2)

"""
Summary:
- Slicing extracts substrings using [start:stop:step].
- Omitting start/stop uses defaults (start=0, stop=end).
- Step can skip or reverse characters.
- Negative indices and steps allow flexible slicing from the end or in reverse.
"""
