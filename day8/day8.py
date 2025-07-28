# Problem 1:
# Write a program using function to find greatest of three numbers.
def greatest_number(*numbers):
    number = list(numbers)
    number.sort()
    print(number[-1])

# Test
greatest_number(10, 25, 7)  # Output: 25

# Problem 2:
# Write a python program using function to convert celsius to fahrenheit.
def convert_temperature(value, from_unit, to_unit):
    # Convert input to lowercase for consistency
    from_unit = from_unit.lower()
    to_unit = to_unit.lower()

    # First convert the input to Celsius
    if from_unit == "celsius":
        celsius = value
    elif from_unit == "fahrenheit":
        celsius = (value - 32) * 5 / 9
    elif from_unit == "kelvin":
        celsius = value - 273.15
    else:
        return "Invalid input unit."

    # Then convert Celsius to desired unit
    if to_unit == "celsius":
        return celsius
    elif to_unit == "fahrenheit":
        return (celsius * 9 / 5) + 32
    elif to_unit == "kelvin":
        return celsius + 273.15
    else:
        return "Invalid output unit."


# Test
from_unit = input("Enter input unit (Celsius/Fahrenheit/Kelvin): ")
to_unit = input("Enter output unit (Celsius/Fahrenheit/Kelvin): ")
value = float(input(f"Enter temperature in {from_unit}: "))

converted = convert_temperature(value, from_unit, to_unit)
print(f"{value}° {from_unit.capitalize()} = {converted:.2f}° {to_unit.capitalize()}")

# Problem 3:
# How do you prevent a python print() function to print a new line at the end.
print('Test Case Line 1',end='')
print('Test Case Line 2',end='')
print('\n',end='')

# Problem 4:
# Write a recersive function to calculate the sum of first n natural numbers.
def natural_sum(num):
    if num <= 0:
        return 0
    else:
        return num + natural_sum(num - 1)

# Test
print(natural_sum(10))  # Output: 55
print(natural_sum(7))  # Output: 28

# Problem 5:
# Write a python function which converts inches to cms.
def length_converter(value, unit):
    if unit == "in":
        return value * 2.54  # inches to cm
    elif unit == "cm":
        return value / 2.54  # cm to inches
    else:
        return "Invalid unit"

# Test
print(length_converter(10, "in"))   # Output: 25.4
print(length_converter(25.4, "cm")) # Output: 10.0

# Problem 6:
# Write a python function to print first n lines of the following pattern:
'''
for n = 3
***
**
*
'''
def pattern(n):
    for a in range(n):
        print('*'*(n-a))

# Test
pattern(3)

# Problem 7:
# Write a python function to remove a given word from a list and strip it at the same time.
def remove_and_strip(word_list, target_word):
    stripped_list = [word.strip() for word in word_list]
    while target_word in stripped_list:
        stripped_list.remove(target_word)

    return stripped_list

# Test
words = ["  apple  ", "banana", " apple", "cherry ", "apple "]
result = remove_and_strip(words, "apple")
print(result)

# Problem 8
# Write a python function to print multiplication table of a givem number.
def print_table(number):
    print(f"Table of {number} : ")
    print("*" * 10)
    for i in range(1, 11):
        print(f"{number} x {i} = {number * i}")
    print("*" * 10)
    print()  # extra line break

def number_table(*numbers):
    for number in sorted(numbers):
        print_table(number)

# Test
number_table(7,11)