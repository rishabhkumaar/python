# Problem 1:
# Write a program to find the greatest of four numbers entered by the user.
def greatest_number():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    c = int(input("Enter third number: "))
    d = int(input("Enter fourth number: "))

    if a > b and a > c and a > d:
        print(f"{a} is the greatest")
    elif b > c and b > d:
        print(f"{b} is the greatest")
    elif c > d:
        print(f"{c} is the greatest")
    else:
        print(f"{d} is the greatest")

# Call the function
greatest_number()

# Problem 2:
# Write a program to find out whether a student is pass or fail, if it requires total 40% and at least 33% in each subject to pass. Assume 3 subjects and take marks as an input from the user.
def examination_tool(*marks):
    subject_count = len(marks)
    total_marks = sum(marks)
    percentage = (total_marks / (subject_count))  # Assuming each subject is out of 100

    # Check if any subject is less than 33
    if any(mark < 33 for mark in marks):
        print("Student Failed due to insufficient marks in a subject.")
    elif percentage < 40:
        print("Student Failed due to low total percentage.")
    else:
        print("Congratulations! You are promoted to the next academic session.")

# Call the function
examination_tool()

# Problem 3:
'''
A spam comment is defined as a text that contains any of the following keywords:
make a lot of money, buy now, subscribe this, click this
✍️ Write a program to detect whether a given text/comment is a spam based on these phrases.
'''
def spam_detector(message):
    spam_trigger = ["make a lot of money", "buy now", "subscribe this", "click this"]
    flag = 0
    for spam in spam_trigger:
        if spam.lower() in message.lower():
            print("🚨 This could be a SPAM Message! BE ALERT!")
            flag = 1
            break  # Stop checking after finding spam
    if flag == 0:
        print("✅ Looks Fine for Now!")

# Test
spam_detector("Click this link to make a lot of money!")  # spam ✅
spam_detector("Just saying hello, have a good day!")      # clean ✅


# Problem 4
# Write a program to find whether a given username contains less than 10 characters or not.
def char_counter(user_id):
    if len(user_id) < 10:
        print(f"The user ID '{user_id}' is shorter than 10 characters.")
    else:
        print(f"The user ID '{user_id}' is 10 or more characters long.")

# Test 
char_counter("rishabh")       # Shorter than 10
char_counter("rishabh12345")  # 10 or more characters

# Problem 5
# Write a program which finde out whether a given name is present in a list or not.
def name_searcher(name, name_list):
    if name in name_list:
        print(f"✅ Yes, '{name}' is present in the list.")
    else:
        print(f"❌ No, '{name}' is not present in the list.")

# Test
friends = ["Rishabh", "Suchi", "Aryan", "Neha"]
name_searcher("Rishabh", friends)
name_searcher("Vikram", friends)

# Problem 6
# Write a program to calculate the grade of a student from his marks from the following scheme: 
'''
90 - 100 -> O
80 -  90 -> A
70 -  80 -> B
60 -  70 -> C
50 -  60 -> D
   <  50 -> F
'''
def grading_system(name, marks):
    if 90 <= marks <= 100:
        grade = 'O'
    elif 80 <= marks < 90:
        grade = 'A'
    elif 70 <= marks < 80:
        grade = 'B'
    elif 60 <= marks < 70:
        grade = 'C'
    elif 50 <= marks < 60:
        grade = 'D'
    elif 0 <= marks < 50:
        grade = 'F'
    else:
        print(f"Invalid marks for {name}: {marks}")
        return

    print(f"Student: {name}, Marks: {marks}, Grade: {grade}")

# Test
grading_system("Rishabh", 92)   # Grade O
grading_system("Anjali", 78)    # Grade B
grading_system("Aryan", 47)     # Grade F
grading_system("Neha", 105)     # Invalid

# Problem 7
# Write a program to find out whether a given post is talking about "Rishabh" or not.
def post_checker(post):
    if "rishabh" in post.lower():
        print("✅ This post is talking about Rishabh.")
    else:
        print("❌ This post does not mention Rishabh.")
# Test
post_checker("Rishabh is an amazing coder.")        # ✅ Match
post_checker("This post is about someone else.")    # ❌ No match
post_checker("rIsHaBh is working on a new project") # ✅ Match (case-insensitive)