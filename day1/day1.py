# Problem 1: Print "Twinkle Twinkle Little Star" poem
print("Twinkle, twinkle, little star,")
print("How I wonder what you are!")
print("Up above the world so high,")
print("Like a diamond in the sky.")
print("Twinkle, twinkle, little star,")
print("How I wonder what you are!")



# Problem 2: Use REPL (manually)

# Open your terminal and type:
# >>> python
# Then in the Python shell (REPL), type:

print("Multiplication Table of 5:")
for i in range(1, 11):
    print(f"5 x {i} = {5 * i}")

# Exit REPL using Ctrl+Z (Windows) or Ctrl+D (Linux/macOS)



# Problem 3: Install external module and use it

# Let's use the `emoji` module (a fun example)

# Step 1: Install the module
# In terminal: pip install emoji

# Step 2: Use it in Python
import emoji

print(emoji.emojize("I love Python :snake:"))



# Problem 4: Print contents of a directory using `os` module

import os

# Get list of files and folders in the current directory
contents = os.listdir()

print("Contents of current directory:")
for item in contents:
    print("-", item)



# Problem 5: Add comments to the above program

# Importing the built-in os module for interacting with the operating system
import os

# Getting a list of all files and folders in the current working directory
contents = os.listdir()

# Printing each item in the directory one by one
print("Contents of current directory:")
for item in contents:
    print("-", item)