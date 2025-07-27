## 📘 Chapter 4: Conditional Statements in Python

In this chapter, you'll learn about:

* What conditionals are and why we use them
* Syntax of `if`, `elif`, and `else`
* How to use **relational** and **logical** operators
* Writing decision-making programs
* Common mistakes and important tips

---

## 🤔 Conditional Experience

Sometimes we make decisions based on conditions:

* We play games **if the day is Sunday**
* We order ice cream **if the day is sunny**
* We go hiking **if our parents allow**

These are real-life examples of **conditional thinking** — we do something **only when** a condition is true.

🧠 In Python, we use **conditional statements** (`if`, `elif`, `else`) to make similar decisions in our code.

---

## 🧪 `if`, `elif`, and `else` in Python

Conditional statements are used to **control the flow** of the program based on conditions.

### 🔹 Syntax:

```python
class DecisionMaker:
    def make_decision(self, condition1, condition2):
        if condition1:
            print("Yes")
        elif condition2:
            print("No")
        else:
            print("Maybe")
```

---

## 🧑‍💻 Example: Odd or Even Checker

```python
class NumberAnalyzer:
    def odd_even(self, *args):
        for arg in args:
            if arg % 2 == 0:
                print(f"{arg} is Even")
            else:
                print(f"{arg} is Odd")
```

---

## 🧩 Quick Quiz

✍️ **Write a program that prints "Yes" when the user's age is 18 or more.**

```python
class AgeChecker:
    def check_age(self):
        age = int(input("Enter Age: "))
        if age >= 18:
            print("Yes")
        else:
            print("No")
```

---

## ⚖️ Relational Operators

These compare two values and return `True` or `False`.

| Operator | Meaning                  | Example         |
| -------- | ------------------------ | --------------- |
| `==`     | Equals                   | `5 == 5 → True` |
| `!=`     | Not equals               | `5 != 3 → True` |
| `>`      | Greater than             | `5 > 3 → True`  |
| `<`      | Less than                | `5 < 3 → False` |
| `>=`     | Greater than or equal to | `5 >= 5 → True` |
| `<=`     | Less than or equal to    | `3 <= 5 → True` |

---

## 🔗 Logical Operators

These are used to combine multiple conditions.

| Operator | Meaning                              | Example                         |
| -------- | ------------------------------------ | ------------------------------- |
| `and`    | True if **both** conditions are true | `x > 5 and x < 10`              |
| `or`     | True if **at least one** is true     | `x > 5 or x < 2`                |
| `not`    | Inverts the boolean value            | `not(x > 5)` → True if `x <= 5` |

---

## 🧱 The `elif` Ladder

You can chain multiple conditions using `elif` (short for *else if*):

```python
if condition1:
    # code
elif condition2:
    # code
elif condition3:
    # code
else:
    # fallback code
```

🧠 **Only one block** of this ladder is executed — the **first condition that is true**.

---

## ⚠️ Important Notes

1. ✅ You can use **as many `elif`** statements as needed.
2. ✅ The final `else` is **optional**, but is used as a **fallback** if none of the conditions are met.
3. ❌ Avoid using `break` or `continue` outside loops.
4. ✅ Always use proper indentation in Python (4 spaces or a tab).

---

## 📌 Summary

* ✅ **Conditional statements** let you execute code based on conditions.
* ✅ Use `if`, `elif`, and `else` to handle multiple scenarios.
* ✅ **Relational** and **logical** operators help in writing complex conditions.
* ✅ The `elif` ladder runs from top to bottom and stops when a condition is true.
* ✅ Clean indentation and syntax are crucial for conditionals to work properly.

---