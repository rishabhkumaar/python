## 📘 Chapter 5: Dictionaries and Sets

In this chapter, you'll learn about:

* What dictionaries and sets are
* Dictionary properties and methods
* Set properties and methods
* How to perform basic operations on sets

---

## 🗂️ What is a Dictionary?

A **dictionary** in Python is a collection of **key-value pairs**. It is used to store data values like a map.

### 🔹 Syntax:

```python
a = {
    "key": "value",
    "name": "Rishabh",
    "age": 19,
    "from": "India",
}
```

---

## 📌 Properties of Python Dictionaries

1. ✅ Dictionaries are **unordered**
2. ✅ Dictionaries are **mutable**
3. ✅ Dictionaries are **indexed** by keys
4. ✅ **Duplicate keys are not allowed**

---

## 🧰 Dictionary Methods

Consider the following dictionary:

```python
a = {
    "name": "Rishabh",
    "from": "India",
    "item_id": [92, 98, 96]
}
```

| Method            | Description                                     | Example                       |
| ----------------- | ----------------------------------------------- | ----------------------------- |
| `a.items()`       | Returns a list of all key-value pairs as tuples | `[("name", "Rishabh"), ...]`  |
| `a.keys()`        | Returns a list of all the keys                  | `["name", "from", "item_id"]` |
| `a.update({...})` | Updates dictionary with new key-value pairs     | `a.update({"friend": "Sam"})` |
| `a.get("name")`   | Returns value for the specified key             | `"Rishabh"`                   |

🔗 For more methods, visit [docs.python.org](https://docs.python.org)

---

## 🔢 What is a Set?

A **set** is a **collection of unique (non-repetitive) elements** in Python.

### 🔹 Example:

```python
s = set()
s.add(1)
s.add(2)
```

If you're a beginner, think of sets simply as data types that **store unique values**.

---

## 📌 Properties of Sets

1. ✅ Sets are **unordered**
2. ✅ Sets are **unindexed**
3. ✅ Sets are **immutable** (individual items can't be changed)
4. ✅ Sets **do not allow duplicate elements**

---

## 🛠️ Set Operations

Consider the set:

```python
s = {1, 8, 2, 3}
```

| Method                    | Description                                                     | Result             |
| ------------------------- | --------------------------------------------------------------- | ------------------ |
| `len(s)`                  | Returns number of elements in the set                           | `4`                |
| `s.remove(8)`             | Removes 8 from the set                                          | `{1, 2, 3}`        |
| `s.pop()`                 | Removes and returns an **arbitrary** element                    | (varies each time) |
| `s.clear()`               | Empties the entire set                                          | `set()`            |
| `s.union({8, 11})`        | Returns a new set containing all unique elements from both sets | `{1, 2, 3, 8, 11}` |
| `s.intersection({8, 11})` | Returns a set of common elements between both sets              | `{8}`              |

---

## 📌 Summary

* ✅ **Dictionaries** are mutable key-value pair collections.
* ✅ **Duplicate keys** are not allowed in dictionaries.
* ✅ **Sets** store unique items and are unordered.
* ✅ Use methods like `.add()`, `.remove()`, `.union()` and `.intersection()` with sets.
* ✅ Both types are useful for organizing and managing collections of data in Python.

---
