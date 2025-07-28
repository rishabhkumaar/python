# 📘 Chapter 1: Modules, Comments & PIP

Welcome to your very first Python program! In this chapter, we'll cover:

- Writing your first Python script
- What modules are
- Using PIP (Python's package manager)
- Python as a calculator
- Understanding comments

---

## ✅ Your First Python Program

Create a file called `hello.py` and paste the following code:

```python
print("Hello, World!")
````

To execute it, open your terminal (or command prompt), navigate to the folder containing the file, and run:

```bash
python hello.py
```

You should see:

```
Hello, World!
```

---

## 📦 What Are Modules?

A **module** is simply a Python file (`.py`) that contains functions, classes, or variables that you can import and use in other Python programs.

### 🧩 Types of Modules in Python:

| Type         | Description                  | Examples                               |
| ------------ | ---------------------------- | -------------------------------------- |
| **Built-in** | Comes with Python by default | `math`, `os`, `random`, `datetime`     |
| **External** | Installed using `pip`        | `flask`, `numpy`, `pandas`, `requests` |

---

## 🧰 Using Python as a Calculator (REPL Mode)

You can use Python directly as a calculator by typing:

```bash
python
```

This opens the **REPL** — which stands for:

> 🧠 **Read-Evaluate-Print Loop**

It lets you enter Python code line-by-line, and see the output immediately:

```python
>>> 5 + 7
12
>>> 9 * 3
27
```

Press `Ctrl + Z` (Windows) or `Ctrl + D` (Linux/macOS) to exit.

---

## 📝 Comments in Python

**Comments** are lines in your code that are **not executed**. They're used to explain code, add notes, or mark authorship.

### ✍️ Types of Comments:

1. **Single-Line Comments**

   Written using the `#` symbol:

   ```python
   # This is a single-line comment
   print("Hello")  # This is also a comment
   ```

2. **Multi-Line Comments**

   In Python, multi-line comments can be written using triple quotes:

   ```python
   """
   This is a multi-line comment
   It spans multiple lines
   """
   ```

---

## 📦 What is PIP?

**PIP** is the package manager for Python. You use it to install external libraries (modules) that are **not built-in**.

### Example:

```bash
pip install flask
```

This installs the **Flask** web framework.

> Note: Built-in modules like `math` don’t need installation.

🔗 [math module documentation](https://docs.python.org/3/library/math.html)

---

## 🔍 Summary

* ✅ Python files end in `.py` and can be run from the terminal.
* ✅ Modules add powerful functionality to your code.
* ✅ Use `pip` to install external modules.
* ✅ REPL mode is great for quick calculations and testing.
* ✅ Comments make your code easier to understand and maintain.

---
