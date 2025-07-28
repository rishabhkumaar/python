# 📘 Chapter 8: Functions & Recursions

A **function** is a group of statements performing a specific task.

When a program gets bigger and more complex, it becomes hard to keep track of what each part does. Functions help by organizing code into reusable blocks.

---

## ✅ What is a Function?

A function is a block of code that can be **called** (used) multiple times anywhere in your program.

### Example Syntax:

```python
def func1():
    print("Hello")
```

Calling the function:

```python
func1()
```

This will print:

```
Hello
```

---

## 🧩 Function Definition vs Function Call

| Term                    | Description                           | Example            |
| ----------------------- | ------------------------------------- | ------------------ |
| **Function definition** | The code block that performs the task | `def func1(): ...` |
| **Function call**       | Using the function in the program     | `func1()`          |

---

## ✍️ Quick Quiz

Write a program that greets a user with `"Good day"` using a function.

---

## 📚 Types of Functions in Python

1. **Built-in Functions**: Already present in Python
   Examples: `len()`, `print()`, `range()`

2. **User-defined Functions**: Defined by you!
   Example: `func1()` in the example above

---

## 🧰 Functions with Arguments

Functions can accept inputs called **arguments** and optionally **return** values.

### Example:

```python
def greet(name):
    greeting = "Hello " + name
    return greeting

a = greet("Rishabh")
print(a)
```

Output:

```
Hello Rishabh
```

---

## 🎯 Default Parameter Values

You can specify default values for function parameters. If no argument is provided, the default is used.

```python
def greet(name="stranger"):
    print("Hello " + name)

greet()            # Outputs: Hello stranger
greet("Rishabh")   # Outputs: Hello Rishabh
```

---

## 🔄 Recursion

**Recursion** is when a function calls itself to solve smaller instances of the same problem.

### Example: Factorial function

Mathematical definition:

$$
factorial(n) = n \times factorial(n-1)
$$

Python code:

```python
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
```

---

### ⚠️ Important Notes about Recursion

* Make sure there is a **base case** to stop recursion (like `if n == 0 or n == 1` above).
* Without a base case, the function would call itself **infinitely**, causing errors.
* Recursion is often the simplest way to implement some algorithms.

---