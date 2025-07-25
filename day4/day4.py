# Problem 1:
# Storing seven fruits in a list entered by the user
f1 = input("Enter fruit 1: ")
f2 = input("Enter fruit 2: ")
f3 = input("Enter fruit 3: ")
f4 = input("Enter fruit 4: ")
f5 = input("Enter fruit 5: ")
f6 = input("Enter fruit 6: ")
f7 = input("Enter fruit 7: ")

fruit_list = [f1, f2, f3, f4, f5, f6, f7]
print("List of fruits:", fruit_list)

# Problem 2:
# Accepting marks of 6 students and displaying them sorted
m1 = int(input("Enter marks for student 1: "))
m2 = int(input("Enter marks for student 2: "))
m3 = int(input("Enter marks for student 3: "))
m4 = int(input("Enter marks for student 4: "))
m5 = int(input("Enter marks for student 5: "))
m6 = int(input("Enter marks for student 6: "))

marks = [m1, m2, m3, m4, m5, m6]
marks.sort()
print("Sorted marks:", marks)

# Problem 3:
# Demonstrating that a tuple is immutable in Python
t = (1, 2, 3, 4)
# t[0] = 10  # ❌ This line would raise a TypeError

print("Original tuple:", t)
print("Tuples are immutable. You cannot change their values.")

# Problem 4:
# Summing a list with 4 numbers
numbers = [5, 10, 15, 20]
total = sum(numbers)

print("List of numbers:", numbers)
print("Sum of numbers:", total)

# Problem 5:
# Counting the number of zeros in the tuple
a = (7, 0, 8, 0, 0, 9)
zero_count = a.count(0)

print("Tuple:", a)
print("Number of zeros:", zero_count)