"""
Type Conversion in Python

Type conversion means converting a value from one data type to another. There are two types:
1. Explicit Type Conversion (done by the programmer)
2. Implicit Type Conversion (done automatically by Python)
"""

# --- Explicit Type Conversion ---
print("--- Explicit Type Conversion ---")
# str(): Convert to string
print("Explicit Type Conversion to String using str():")
num = 123
flt = 4.56
boolean = True
print("str(num):", str(num), type(str(num)))      # Converts integer 123 to string '123'
input("Press Enter to continue...")
print("str(flt):", str(flt), type(str(flt)))      # Converts float 4.56 to string '4.56'
input("Press Enter to continue...")
print("str(boolean):", str(boolean), type(str(boolean)))  # Converts boolean True to string 'True'

input("Press Enter to continue...")

# int(): Convert to integer
print("\nExplicit Type Conversion to Integer using int():")
s_num = "789"
s_flt = "12.34"
f = 7.89
b = False
print("int(s_num):", int(s_num), type(int(s_num)))    # Converts string '789' to integer 789
input("Press Enter to continue...")
print("int(f):", int(f), type(int(f)))                # Converts float 7.89 to integer 7 (decimal part is removed)
input("Press Enter to continue...")
print("int(b):", int(b), type(int(b)))                # Converts boolean False to integer 0
# print(int(s_flt))  # This will cause ValueError because '12.34' is not a valid integer string

input("Press Enter to continue...")

# float(): Convert to float
print("\nExplicit Type Conversion to Float using float():")
s_flt2 = "56.78"
i = 42
b2 = True
print("float(s_flt2):", float(s_flt2), type(float(s_flt2)))  # Converts string '56.78' to float 56.78
input("Press Enter to continue...")
print("float(i):", float(i), type(float(i)))                # Converts integer 42 to float 42.0
input("Press Enter to continue...")
print("float(b2):", float(b2), type(float(b2)))             # Converts boolean True to float 1.0

input("Press Enter to continue...")

# bool(): Convert to boolean
print("\nExplicit Type Conversion to Boolean using bool():")
zero = 0
empty_str = ""
nonzero = -5
nonempty_str = "hello"
print("bool(zero):", bool(zero))                # 0 is considered False
input("Press Enter to continue...")
print("bool(empty_str):", bool(empty_str))      # Empty string is considered False
input("Press Enter to continue...")
print("bool(nonzero):", bool(nonzero))          # Any nonzero number is considered True
input("Press Enter to continue...")
print("bool(nonempty_str):", bool(nonempty_str))# Any non-empty string is considered True
input("Press Enter to continue...")
print("bool([]):", bool([]))                    # Empty list is considered False
input("Press Enter to continue...")
print("bool([1,2,3]):", bool([1,2,3]))          # Non-empty list is considered True

"""
Note on bool():
There are exactly 7 values in Python that bool() converts to False:
1. 0 (zero, any numeric zero: 0, 0.0, 0j)
2. False
3. None
4. "" (empty string)
5. [] (empty list)
6. {} (empty dictionary)
7. () (empty tuple)

All other values are considered True.
"""

# --- Implicit Type Conversion ---
print("\n--- Implicit Type Conversion ---")
# Python automatically converts int to float during arithmetic
x = 5
y = 2.0
result = x + y
print("x:", x, type(x))  # x is integer
print("y:", y, type(y))  # y is float
print("result = x + y:", result, type(result))  # Result is float because Python converts int to float automatically

# Mixing bool and int
flag = True
num2 = 10
sum_result = flag + num2  # True is treated as 1, so result is 11
print("flag:", flag, type(flag))  # flag is boolean
print("num2:", num2, type(num2))  # num2 is integer
print("sum_result = flag + num2:", sum_result, type(sum_result))  # Result is integer

# Mixing int and complex
c = 3 + 4j
z = 7
complex_sum = c + z
print("c:", c, type(c))  # c is complex number
print("z:", z, type(z))  # z is integer
print("complex_sum = c + z:", complex_sum, type(complex_sum))  # Result is complex because int is converted to complex

"""
Summary:
- Explicit type conversion is done by the programmer using functions like str(), int(), float(), bool().
- Implicit type conversion is done automatically by Python when mixing types in expressions.
- Not all conversions are possible (e.g., int("12.34") gives an error).
"""
