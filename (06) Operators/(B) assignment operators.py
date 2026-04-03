"""
Assignment Operators in Python

Assignment operators are used to assign values to variables and update them. Here are the main assignment operators:
- =   : Assigns the value on the right to the variable on the left
- +=  : Adds the right value to the variable and assigns the result
- -=  : Subtracts the right value from the variable and assigns the result
- *=  : Multiplies the variable by the right value and assigns the result
- /=  : Divides the variable by the right value and assigns the result (result is float)
- //= : Floor divides the variable by the right value and assigns the result
- %=  : Takes the modulus with the right value and assigns the result
- **= : Raises the variable to the power of the right value and assigns the result
"""

print("Assignment Operators in Python\n")
x = 5
print("x =", x)            # Simple assignment: x is now 5
input("Press Enter to continue...")
x += 2
print("x += 2:", x)        # x = x + 2 -> x is now 7 (5 + 2 is 7)
input("Press Enter to continue...")
x -= 1
print("x -= 1:", x)        # x = x - 1 -> x is now 6 (7 - 1 is 6)
input("Press Enter to continue...")
x *= 3
print("x *= 3:", x)        # x = x * 3 -> x is now 18 (6 * 3 is 18)
input("Press Enter to continue...")
x /= 2
print("x /= 2:", x)        # x = x / 2 -> x is now 9.0 (18 / 2 is 9.0)
input("Press Enter to continue...")
x //= 2
print("x //= 2:", x)       # x = x // 2 -> x is now 4.0 (9.0 // 2 is 4.0)
input("Press Enter to continue...")
x **= 3
print("x **= 3:", x)       # x = x ** 3 -> x is now 64.0 (4.0 to the power of 3 is 64.0)
input("Press Enter to continue...")
x %= 2
print("x %= 2:", x)        # x = x % 2 -> x is now 0.0 (64.0 divided by 2 leaves a remainder of 0.0)
