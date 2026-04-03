"""
Comparison Operators in Python

Comparison operators are used to compare values and return True or False. Here are the main comparison operators:
- ==  : Equal to (checks if two values are the same)
- !=  : Not equal to (checks if two values are different)
- >   : Greater than (checks if the left value is larger)
- <   : Less than (checks if the left value is smaller)
- >=  : Greater than or equal to (checks if the left value is larger or equal)
- <=  : Less than or equal to (checks if the left value is smaller or equal)
"""
print("Comparison Operators in Python\n")
p = 7
q = 10
print("p == q:", p == q)   # Checks if 7 is equal to 10 (False)
input("Press Enter to continue...")
print("p != q:", p != q)   # Checks if 7 is not equal to 10 (True)
input("Press Enter to continue...")
print("p > q:", p > q)     # Checks if 7 is greater than 10 (False)
input("Press Enter to continue...")
print("p < q:", p < q)     # Checks if 7 is less than 10 (True)
input("Press Enter to continue...")
print("p >= q:", p >= q)   # Checks if 7 is greater than or equal to 10 (False)
input("Press Enter to continue...")
print("p <= q:", p <= q)   # Checks if 7 is less than or equal to 10 (True)
input("Press Enter to continue...")

# Note: 10.0 is considered equal to 10 when using ==, but they are different types (int vs float)

# Comparison of strings

'''
String comparison is done lexicographically (based on Unicode values of characters). The 
comparison is done character by character from left to right and it compares the Unicode values 
of said characters.
'''
print("\nString Comparison Examples:")

# Example of string comparison
s3 = "aA"
s4 = "A"
s5 = "AB"
s6 = "AC"
print("aA > A:", s3 > s4)     # 'aA' > 'A' because 'a' (lowercase) has higher Unicode value than 'A' (uppercase)
input("Press Enter to continue...")
print("AB > AC:", s5 > s6)     # 'AB' > 'AC' because 'A' = 'A', but 'B' (Unicode 66) > 'C' (Unicode 67) is False
input("Press Enter to continue...")
print("AB < AC:", s5 < s6)     # 'AB' < 'AC' because after 'A', 'B' < 'C'
input("Press Enter to continue...")

# Example of comparison stops at first difference
print("\nComparison stops at first difference:")
s7 = "ACa"
s8 = "ABA"
print("s7 > s8:", s7 > s8)     # 'ACa' > 'ABA' is True because 'C' > 'B', comparison stops here
input("Press Enter to continue...")

# Example of comparing strings of different lengths
print("\nComparing strings of different lengths:") 
s1 = "apple"
s2 = "banana"
print("s1 == s2:", s1 == s2)   # Checks if s1 is equal to s2 (False)
input("Press Enter to continue...")
print("s1 != s2:", s1 != s2)   # Checks if s1 is not equal to s2 (True)
input("Press Enter to continue...")
print("s1 > s2:", s1 > s2)     # Checks if s1 is greater than s2 (False, 'apple' comes before 'banana')
input("Press Enter to continue...")
print("s1 < s2:", s1 < s2)     # Checks if s1 is less than s2 (True)

# Note: Strings cannot be compared with numbers using comparison operators. Doing so will raise a TypeError.

"""
In string comparison, Python checks each character in order:
- If characters are equal, it moves to the next character.
- As soon as a difference is found, the comparison result is decided.
For example, 'ACa' > 'ABA' is True because after 'A', 'C' > 'B'. The rest ('a' vs 'A') is not checked.
"""

"""
String comparison is based on the Unicode (ASCII) values of characters.
- If the first character is the same, Python compares the next character, and so on.
- Lowercase letters have higher Unicode values than uppercase letters ('a' > 'A').
- For example, 'aA' > 'A' because 'a' (Unicode 97) > 'A' (Unicode 65).
- 'AB' < 'AC' because after 'A', 'B' (Unicode 66) < 'C' (Unicode 67).
- If all characters are equal, the shorter string is considered less.
"""

