"""
String Indexing in Python

Indexing allows you to access individual characters in a string using their position (index). 
Indexing starts from 0 for the first character (positive indexing). You can also use negative 
indexing, where -1 refers to the last character, -2 to the second last, and so on.
"""

text = "Programming"


# Positive indexing
print("Positive Indexing:")
print("text[0]:", text[0])   # First character 'P'
print("text[6]:", text[6])   # Seventh character 'm'

input("Press Enter to continue...")

# Negative indexing
print("\nNegative Indexing:")
print("text[-1]:", text[-1])   # Last character 'g'
print("text[-5]:", text[-5])   # Fifth last character 'm'

input("Press Enter to continue...")

# Out of index example
print("\nOut of Index Example:")
try:
    print(text[20])  # This will cause an IndexError
except IndexError as e:
    print("Error:", e)
    print(f"Explanation: This error occurs when you try to access a position that does not exist in the string. The valid indices for this string are from 0 to {len(text)-1} (or -1 to -{len(text)}).")

input("Press Enter to continue...")

# Multiple indexing: printing multiple characters using different indices
print("\nMultiple Indexing (Accessing multiple characters):")
print("text[1], text[2], text[3]:", text[1], text[2], text[3])  # 2nd, 3rd, 4th characters
print("text[-2], text[-3], text[-4]:", text[-2], text[-3], text[-4])  # 2nd, 3rd, 4th from end

"""
You can print multiple characters from a string by accessing each index separately.
For example, text[1], text[2], text[3] prints the 2nd, 3rd, and 4th characters.
Similarly, text[-2], text[-3], text[-4] prints characters from the end using negative indices.
"""

"""
Summary:
- Positive indexing starts from 0 (left to right).
- Negative indexing starts from -1 (right to left).
- Accessing an index outside the valid range causes an IndexError.
"""
