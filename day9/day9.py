# Problem 1:
# Write a program to read the text from a given file 'poems.txt' and find out whether it contains the word 'twinkle'.
with open("poems.txt", "r") as f:
    content = f.read()
    if "twinkle" in content.lower():
        print("Twinkle is present")
    else:
        print("Twinkle is not present")

# Problem 2:
# The game() function in a program lets a user play game and returns the score as an integer.
# You need to read a file 'history.txt' which is either blank or contains the previous Hi-score.
# You need to write a program to update the Hi-score whenever game() breaks the Hi-Score.
def game():
    return int(input("Enter your score: "))

score = game()

try:
    with open("history.txt", "r") as f:
        hiscore = f.read()
        hiscore = int(hiscore) if hiscore else 0
except FileNotFoundError:
    hiscore = 0

if score > hiscore:
    with open("history.txt", "w") as f:
        f.write(str(score))
    print("New High Score!")
else:
    print("Try Again!")

# Problem 3:
# Write a program to generate multiplication tables from 2 to 20 and write it to the different files.
# Place these files in a folder for a 13 - year old.
import os

os.makedirs("tables", exist_ok=True)

for i in range(2, 21):
    with open(f"tables/table_of_{i}.txt", "w") as f:
        for j in range(1, 11):
            f.write(f"{i} x {j} = {i*j}\n")

# Problem 4:
# A file contains a word "Donkey" multiple times.
# You need to write a program which replaces this word with ###### by updating the same file.
with open("offensive.txt", "r") as f:
    content = f.read()

content = content.replace("Donkey", "######")

with open("offensive.txt", "w") as f:
    f.write(content)

# Problem 5:
# Repeat program 4 for a list of such words to be censored.
words = ["donkey", "idiot", "mango"]

with open("censored.txt", "r") as f:
    content = f.read()

for word in words:
    content = content.replace(word, "######")

with open("censored.txt", "w") as f:
    f.write(content)

# Problem 6:
# Write a program to open a log file and find out whether it contains 'python'
with open("log.txt", "r") as f:
    content = f.read()
    if "python" in content.lower():
        print("Yes, 'python' is present")
    else:
        print("No, 'python' is not present")

# Problem 7:
# Write a program to find out the line number where python is present from Ques 6
with open("log.txt", "r") as f:
    for index, line in enumerate(f, 1):
        if "python" in line.lower():
            print(f"'python' found at line number {index}")

# Problem 8:
# Write a program to make a copy of a text file "this.txt"
with open("this.txt", "r") as f:
    content = f.read()

with open("copy_this.txt", "w") as f:
    f.write(content)

# Problem 9:
# Write a program to find out whether a file is identical & matches the content of another file.
with open("file1.txt", "r") as f1, open("file2.txt", "r") as f2:
    if f1.read() == f2.read():
        print("Files are identical")
    else:
        print("Files are not identical")

# Problem 10:
# Write a program to wipe out the contents of a file using python.
with open("wipe_me.txt", "w") as f:
    f.write("")

# Problem 11:
# Write a program to rename a file to "renamed_by_python.txt"
import os

os.rename("to_be_renamed.txt", "renamed_by_python.txt")