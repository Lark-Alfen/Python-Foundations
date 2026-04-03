"""
File Handling in Python

This file demonstrates all major file handling modes and functions using file.txt.
A new file 'created.txt' will be used for write and append demonstrations.
Each section explains what the code does.
"""

print("--File Handling in Python--\n")
input("Press Enter to continue...")

# 1. Reading a file (r mode)
print("1. Reading file.txt in 'r' (read) mode:")
with open("file.txt", "r") as f:
    content = f.read()
    print(content)
print("\nExplanation: 'r' mode opens the file for reading. File must exist.")
input("Press Enter to continue...")

# 2. Reading line by line
print("2. Reading file.txt line by line:")
with open("file.txt", "r") as f:
    for line in f:
        print(line.strip())
print("\nExplanation: Reading line by line is memory efficient for large files.")
input("Press Enter to continue...")

# 3. Writing to a file (w mode)
print("3. Writing to created.txt in 'w' (write) mode:")
with open("created.txt", "w") as f:
    f.write("This file was created using 'w' mode.\n")
    f.write("All previous content is erased.\n")
print("Content written to created.txt.")
print("\nExplanation: 'w' mode creates a new file or overwrites if it exists.")
input("Press Enter to continue...")

# 4. Appending to a file (a mode)
print("4. Appending to created.txt in 'a' (append) mode:")
with open("created.txt", "a") as f:
    f.write("This line is appended using 'a' mode.\n")
print("Line appended to created.txt.")
print("\nExplanation: 'a' mode adds content to the end of the file, creating it if needed.")
input("Press Enter to continue...")

# 5. Reading and writing (r+ mode)
print("5. Reading and writing created.txt in 'r+' mode:")
with open("created.txt", "r+") as f:
    print("Current content:")
    print(f.read())
    f.seek(0, 2)  # Move to end
    f.write("Added with r+ mode.\n")
print("\nExplanation: 'r+' mode allows reading and writing. File must exist.")
input("Press Enter to continue...")

# 6. Writing and reading (w+ mode)
print("6. Writing and reading created.txt in 'w+' mode:")
with open("created.txt", "w+") as f:
    f.write("This content replaces everything.\n")
    f.seek(0)
    print("After writing, reading content:")
    print(f.read())
print("\nExplanation: 'w+' mode allows writing and reading, but erases file first.")
input("Press Enter to continue...")

# 7. Appending and reading (a+ mode)
print("7. Appending and reading created.txt in 'a+' mode:")
with open("created.txt", "a+") as f:
    f.write("Appended with a+ mode.\n")
    f.seek(0)
    print("Reading all content after appending:")
    print(f.read())
print("\nExplanation: 'a+' mode allows appending and reading. File is created if not exists.")
input("Press Enter to continue...")

# 8. Using file methods
print("8. Demonstrating file methods:")
with open("file.txt", "r") as f:
    print("readline():", f.readline().strip())
    f.seek(0)
    print("readlines():", f.readlines())
print("\nExplanation: readline() reads one line, readlines() returns a list of all lines.")
input("Press Enter to continue...")

# 9. Closing files
print("9. Demonstrating file closing:")
f = open("file.txt", "r")
print(f.read(10))  # Read first 10 characters
f.close()
print("File closed using close() method.")
print("\nExplanation: Always close files when not using 'with' statement.")
input("Press Enter to continue...")

print("\nSummary:")
print("- 'r': Read, file must exist.")
print("- 'w': Write, creates/overwrites file.")
print("- 'a': Append, creates if not exists.")
print("- 'r+': Read and write, file must exist.")
print("- 'w+': Write and read, erases file.")
print("- 'a+': Append and read, creates if not exists.")
print("- Use with statement for auto-closing files.")
print("- Use file methods: read(), readline(), readlines(), write(), seek(), close().")
