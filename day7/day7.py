# Problem 1:
# Write a program to print multiplication table of a given number using for loop.
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

# Problem 2:
# Write a program to greet all the person names stored in a list which starts with S or R.
def greet_selected(names):
    for name in names:
        if name.startswith('S') or name.startswith('R'):
            print(f"Hello, {name}!")

# Test
l1 = ["Rishabh", "Suchi","Ankit", "Prince","Sanya", "Priya", "Ravi", "Swati", "Neha"]
greet_selected(l1)

# Problem 3:
# Attempt problem 1 using while loop.
def while_print_table(number):
    print(f"Table of {number} : ")
    print("*" * 10)
    i = 1
    while i <= 10:
        print(f"{number} x {i} = {number * i}")
        i += 1
    print("*" * 10)
    print()  # extra line break

def while_number_table(*numbers):
    sorted_numbers = sorted(numbers)
    index = 0
    while index < len(sorted_numbers):
        while_print_table(sorted_numbers[index])
        index += 1

# Test
number_table(7, 11)

# Problem 4:
# Write a program to find whether a given number is prime or not.
def is_prime(number):
    if number < 2:
        print(f"{number} is not a prime number.")
        return

    count = 0
    for i in range(1, number + 1):
        if number % i == 0:
            count += 1

    if count == 2:
        print(f"{number} is a prime number.")
    else:
        print(f"{number} is not a prime number.")

# Test
is_prime(7)   # 7 is a prime number.
is_prime(9)   # 9 is not a prime number.
is_prime(1)   # 1 is not a prime number.

# Problem 5:
# Write a program to find the sum of first n natural numbers using while loop.
def sum_natural(n):
    total = 0
    i = n
    while n > 0:
        total += n
        n -= 1
    print(f"Sum of first {i} natural numbers is {total}.")

# Test
sum_natural(5)
# Output: Sum of first 5 natural numbers is 15.

# Problem 6:
# Write a program to calculate the factorial of a given number using for loop.
def factorial(number):
    if number < 0:
        print("Factorial is not defined for negative numbers.")
        return

    fac = 1
    for a in range(1, number + 1):
        fac *= a
    print(f"Factorial of {number} is {fac}")

# Test
factorial(6)  # Output: Factorial of 6 is 720
factorial(-3) # Output: Factorial is not defined for negative numbers.

# Problem 7:
# Write a program to print the follwoing star pattern:
'''
for n = 3
  *
 ***
*****
'''
def pattern_7(n):
    for i in range(1, n + 1):
        spaces = n - i
        stars = 2 * i - 1
        print(" " * spaces + "*" * stars)

# Test
pattern_7(3)

# Problem 8:
# Write a program to print the follwoing star pattern:
'''
for n = 3
*
**
***
'''
def pattern_8(n):
    for i in range(1, n + 1):
        print("*" * i)

# Test
pattern_8(3)

# Problem 9:
# Write a program to print the follwoing star pattern:
'''
for n = 3
***
* *
***
'''
def pattern_9(n):
    for i in range(1, n + 1):
        if i == 1 or i == n:
            print("*" * n)
        else:
            print("*" + " " * (n - 2) + "*")

# Test
pattern_9(3)

# Problem 10:
# Write a program to print multiplication table of n using for loop in reversed order.
def rev_print_table(number):
    print(f"Table of {number} : ")
    print("*" * 10)
    for i in range(10, 0,-1):
        print(f"{number} x {i} = {number * i}")
    print("*" * 10)
    print()  # extra line break

def rev_number_table(*numbers):
    for number in sorted(numbers):
        rev_print_table(number)

# Test
rev_number_table(7,5)