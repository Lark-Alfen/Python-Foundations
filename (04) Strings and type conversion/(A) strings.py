"""
Strings in Python: Unicode and Memory Usage

Strings use more space than other data types like int or float because each character in a string 
is stored using Unicode. Unicode assigns a unique number (code point) to every character, regardless 
of language or symbol. This allows Python to support text from all languages and many symbols, but 
it also means each character can take more memory compared to a simple number.
"""

# Display Unicode code points for all uppercase and lowercase English letters
print("Uppercase letters and their Unicode values:")
for c in range(ord('A'), ord('Z') + 1):
    print(chr(c), ":", c)

input("Press Enter to continue...")

print("\nLowercase letters and their Unicode values:")
for c in range(ord('a'), ord('z') + 1):
    print(chr(c), ":", c)

input("Press Enter to continue...")

"""
ord() and chr() functions:
- ord(character): Returns the Unicode code point (integer) for the given character.
- chr(code): Returns the character for the given Unicode code point (integer).

Examples:
"""

print("\nExamples of ord() and chr():")

input("Press Enter to continue...")

print("ord('A'):", ord('A'))  # 65

input("Press Enter to continue...")

print("ord('a'):", ord('a'))  # 97

input("Press Enter to continue...")

print("chr(65):", chr(65))    # 'A'

input("Press Enter to continue...")

print("chr(97):", chr(97))    # 'a'

input("Press Enter to continue...")

a = 70
b = "Z"

print("chr(a) where a = 70:", chr(a))  # 'F'

input("Press Enter to continue...")

print("ord(b) where b = 'Z':", ord(b))  # 90

"""
Summary:
- Strings use Unicode, so each character has a unique code point and may use more memory.
- Use ord() to get the Unicode value of a character.
- Use chr() to get the character from a Unicode value.
"""
