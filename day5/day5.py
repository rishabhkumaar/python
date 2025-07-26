# Problem 1:
# Creating a dictionary of Hindi words and providing lookup feature
hindi_dict = {
    "pankha": "fan",
    "dabba": "box",
    "vastu": "item",
    "pustak": "book"
}

word = input("Enter a Hindi word to translate: ")
print("Meaning:", hindi_dict.get(word, "Word not found in dictionary."))

# Problem 2:
# Taking 8 inputs from user and showing unique numbers
nums = []

for i in range(8):
    num = int(input(f"Enter number {i+1}: "))
    nums.append(num)

unique_nums = set(nums)
print("Unique numbers:", unique_nums)

# Problem 3:
# Checking if int 18 and str "18" can coexist in a set
s = {18, "18"}
print(s)

# Problem 4:
# Checking set length after adding similar-looking values
s = set()
s.add(20)      # int
s.add(20.0)    # float, same as 20.0 == 20
s.add("20")    # string

print("Set:", s)
print("Length of set:", len(s))
# Output
'''
Set: {20, '20'}
Length of set: 2

'''

# Problem 5:
# Identifying type of empty curly braces
s = {}
print("Type of s:", type(s))
# Output
'''
Type of s: <class 'dict'>
'''

# Problem 6:
# Creating a dictionary to store favorite languages
fav_lang = {}

name1 = input("Enter your name: ")
lang1 = input("Enter your favorite language: ")

name2 = input("Enter your name: ")
lang2 = input("Enter your favorite language: ")

name3 = input("Enter your name: ")
lang3 = input("Enter your favorite language: ")

name4 = input("Enter your name: ")
lang4 = input("Enter your favorite language: ")

fav_lang[name1] = lang1
fav_lang[name2] = lang2
fav_lang[name3] = lang3
fav_lang[name4] = lang4

print("Favorite languages dictionary:", fav_lang)

# Problem 7:
# If two keys (names) are same, the last value will overwrite the previous one
# The dictionary will only keep one entry for that name — the latest one entered will replace the previous.

# Problem 8:
# Same values (languages) are allowed in dictionaries
# Dictionaries allow duplicate values — so same languages can be stored for different friends without issue.

# Problem 9:
# Attempting to put a list inside a set
s = {8, 7, 12, "Rishabh", [7, 7, 6]}  # ❌ This will raise an error
# No, because lists are mutable and unhashable, so they cannot be added to a set.
# Error: TypeError: unhashable type: 'list'