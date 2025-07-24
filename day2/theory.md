## 📘 Chapter 2: Variables and Data Types

In this chapter, we'll explore:

* What variables are
* Common data types in Python
* Rules for naming variables
* Python operators
* The `type()` function and typecasting
* Using `input()` to take user input

---

## 🧠 What is a Variable?

A **variable** is a name given to a memory location that stores a value.

```python
a = 30         # Variable 'a' holds an integer value
b = "Rishabh"  # Variable 'b' holds a string
c = 7122       # Variable 'c' holds another integer
```

### ⚙️ Terminology:

| Term           | Meaning                                                  |
| -------------- | -------------------------------------------------------- |
| **Variable**   | A container used to store a value                        |
| **Keyword**    | Reserved words in Python like `if`, `while`, `def`, etc. |
| **Identifier** | Names used for variables, functions, classes, etc.       |

---

## 🧪 Data Types in Python

Python automatically detects the data type when you assign a value.

### 🔢 Primary Data Types:

1. `int` – Integer numbers (e.g. `10`, `-5`)
2. `float` – Decimal numbers (e.g. `3.14`, `-7.6`)
3. `str` – Strings (text) (e.g. `"hello"`)
4. `bool` – Boolean values (`True` or `False`)
5. `NoneType` – Represents the absence of a value (`None`)

```python
a = 71              # int
b = 88.44           # float
name = "Rishabh"    # str
```

> Python is a dynamically typed language — no need to declare variable types explicitly!

---

## 🧾 Rules for Naming Variables

The same rules apply to **all identifiers** (variables, functions, classes).

✅ **Valid Variable Names:**

* Can contain **letters**, **digits**, and **underscores**
* **Must not** start with a digit
* Can start with a **letter** or an **underscore**
* **Cannot contain spaces**

```python
rishabh = "name"
one7 = 17
seven_ = 7
_seven = "underscore"
```

❌ **Invalid Examples:**

```python
7name = "invalid"     # Starts with a digit
my name = "nope"      # Contains a space
```

---

## ➕ Python Operators

Python provides a wide range of operators:

| Type           | Examples                            |
| -------------- | ----------------------------------- |
| **Arithmetic** | `+`, `-`, `*`, `/`, `//`, `%`, `**` |
| **Assignment** | `=`, `+=`, `-=`, `*=`, `/=`, etc.   |
| **Comparison** | `==`, `!=`, `>`, `<`, `>=`, `<=`    |
| **Logical**    | `and`, `or`, `not`                  |

---

## 🔍 `type()` Function

Use the `type()` function to check the data type of a variable:

```python
a = 31
print(type(a))   # <class 'int'>

b = "3"
print(type(b))   # <class 'str'>
```

---

## 🔁 Typecasting (Converting Data Types)

Python provides built-in functions to **convert between types**.

```python
str(31)      # "31" -> Integer to String
int("32")    # 32   -> String to Integer (if valid string)
```

---

## ⌨️ `input()` Function

`input()` is used to **take input from the user** (always returns a string):

```python
a = input("Enter your name: ")
print("You entered:", a)
```

Even if the user types a number like `34`, it is still stored as a string.

> Tip: Use `int()` or `float()` to convert input to numeric types if needed.

```python
age = int(input("Enter your age: "))
print("Next year, you will be", age + 1)
```

---

## 📌 Summary

* ✅ Variables store data and are identified by names (identifiers).
* ✅ Python has several built-in data types: `int`, `float`, `str`, `bool`, `NoneType`.
* ✅ Variable names must follow specific naming rules.
* ✅ Python includes arithmetic, assignment, comparison, and logical operators.
* ✅ `type()` tells you a variable's type; typecasting lets you convert between types.
* ✅ `input()` lets users type input from the keyboard (always as a string).

---