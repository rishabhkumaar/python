# Problem 1:
# Displaying a user-entered name with "Good Afternoon"
name = input("Enter your name: ")
print("Good Afternoon,", name)


# Problem 2:
# Filling in a letter template with actual name and date
letter = '''Dear <|NAME|>,
You are selected!
<|DATE|>'''

name = input("Enter your name: ")
date = input("Enter the date (DD/MM/YYYY): ")

letter = letter.replace("<|NAME|>", name)
letter = letter.replace("<|DATE|>", date)

print("\nFormatted Letter:\n")
print(letter)


# Problem 3:
# Detecting double spaces in a string
text = "This is a string  with some  double spaces."
double_space_index = text.find("  ")
print("\nFirst occurrence of double spaces is at index:", double_space_index)


# Problem 4:
# Replacing double spaces with single spaces
fixed_text = text.replace("  ", " ")
print("\nString after replacing double spaces:\n", fixed_text)


# Problem 5:
# Formatting a letter using escape sequence characters
formatted_letter = "Dear Rishabh,\n\tYou are selected!\n\tThanks and regards,\n\tAdmin"
print("\nFormatted letter with escape sequences:\n")
print(formatted_letter)
