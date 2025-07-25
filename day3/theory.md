## 📘 Chapter 3: Strings

In this chapter, you'll learn about:

* What strings are
* String slicing and indexing
* String functions
* Escape sequence characters

---

## 🧵 What is a String?

A **string** is a **sequence of characters** enclosed in quotes. It's one of the most common data types in Python.

You can create strings in three ways:

```python
a = 'Rishabh'       # Single-quoted string
b = "Rishabh"       # Double-quoted string
c = '''Rishabh'''   # Triple-quoted string
```

Triple quotes can also be used to write **multi-line strings**.

---

## ✂️ String Slicing

Slicing allows you to extract a portion of a string.

```python
name = "RISHABH"   # Length = 7
        0123456    # Positive indices
       -7654321    # Negative indices
```

### 🔹 Basic Syntax:

```python
slice = name[start:end:step]
```

* `start` → index to begin (inclusive)
* `end` → index to stop (exclusive)
* `step` → how many characters to skip (default is 1)

### 🧪 Examples:

```python
name = "RISHABH"

print(name[0:3])   # 'RIS'  → index 0 to 2
print(name[1:3])   # 'IS'   → index 1 to 2
print(name[-3:])   # 'ABH'  → last 3 characters
```

---

## ⏭️ Slicing with Skip Value

```python
word = "amazing"
print(word[1:6:2])  # 'mzn'
```

This skips every second character between indices 1 and 5.

---

## 🔁 More Slicing Patterns

```python
word = "amazing"

print(word[:7])   # 'amazing' → from start to index 6
print(word[0:])   # 'amazing' → from index 0 to end
```

---

## 🧰 Common String Functions

Below are some commonly used string methods:

| Function                  | Description                       | Example                                         |
| ------------------------- | --------------------------------- | ----------------------------------------------- |
| `len()`                   | Returns the length of the string  | `len("Rishabh") → 7`                            |
| `endswith("bh")`          | Checks if string ends with `"bh"` | `"Rishabh".endswith("bh") → True`               |
| `count('h')`              | Counts occurrences of a character | `"Rishabh".count('h') → 2`                      |
| `capitalize()`            | Capitalizes the first character   | `"rishabh".capitalize() → "Rishabh"`            |
| `find("sha")`             | Finds first index of substring    | `"Rishabh".find("sha") → 2`                     |
| `replace("Rish", "Dish")` | Replaces substring                | `"Rishabh".replace("Rish", "Dish") → "Dishabh"` |

---

## 🔡 Escape Sequence Characters

Escape sequences start with a backslash (`\`) and allow special formatting inside strings.

| Escape Sequence | Description  |
| --------------- | ------------ |
| `\n`            | New line     |
| `\t`            | Tab space    |
| `\'`            | Single quote |
| `\\`            | Backslash    |

### 🧪 Example:

```python
print("Line1\nLine2")   # Prints in two lines
print("Name:\tRishabh") # Adds a tab space
```

---

## 📌 Summary

* ✅ Strings are sequences of characters enclosed in quotes.
* ✅ You can slice strings using `[start:end:step]` syntax.
* ✅ Negative indices allow counting from the end of the string.
* ✅ Python offers many built-in functions for working with strings.
* ✅ Escape sequences help insert special formatting into strings.

---