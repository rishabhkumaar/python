## 📘 Chapter 4: Lists and Tuples

In this chapter, you'll learn about:

* What lists and tuples are
* Indexing and slicing in lists
* List methods
* Tuples and their immutability
* Tuple methods

---

## 📦 What is a List?

A **list** is a **container that holds a collection of values** of any data type. Lists are mutable, meaning their contents can be changed.

```python
owner = ["Rishabh", "Student", 19, "07/07/2006", True]
#         str()      str()     int()     str()       bool()
```

You can store different data types in the same list.

---

## 🔢 List Indexing

Just like strings, **lists are indexed** starting from 0.

```python
l1 = ["Rishabh", "Student", 19, "07/07/2006", True]

print(l1[0])  # Rishabh
print(l1[1])  # Student
```

### ⚠️ Index Error:

```python
print(l1[10])  # IndexError: list index out of range
```

---

## ✂️ List Slicing

You can use slicing on lists just like strings.

```python
print(l1[0:2])   # ['Rishabh', 'Student']
print(l1[:3])    # ['Rishabh', 'Student', 19]
print(l1[2:])    # [19, '07/07/2006', True]
print(l1[0:5:2]) # ['Rishabh', 19, True]
```

---

## 🛠️ List Methods

Consider the list:

```python
l1 = [1, 8, 7, 2, 21, 15]
```

| Method            | Description                                      | Result                 |
| ----------------- | ------------------------------------------------ | ---------------------- |
| `l1.sort()`       | Sorts the list in ascending order                | `[1, 2, 7, 8, 15, 21]` |
| `l1.reverse()`    | Reverses the current list order                  | `[15, 21, 2, 7, 8, 1]` |
| `l1.append(8)`    | Adds 8 to the end of the list                    | `[..., 8]`             |
| `l1.insert(3, 8)` | Inserts 8 at index 3                             | `[..., 2, 8, ...]`     |
| `l1.pop(2)`       | Removes and returns the element at index 2       | `7`                    |
| `l1.remove(21)`   | Removes the first occurrence of 21 from the list | `[..., 15]`            |

---

## 🧊 What is a Tuple?

A **tuple** is an **immutable** collection of elements. Once created, its contents **cannot be changed**.

```python
a = ()           # Empty tuple
a = (1,)         # Tuple with one element (comma is necessary!)
a = (1, 7, 2)    # Tuple with multiple elements
```

---

## 🔐 Tuple Immutability

You **cannot modify** a tuple once it's defined.

```python
a = (1, 7, 2)
a[0] = 5  # ❌ Error: 'tuple' object does not support item assignment
```

---

## 🧰 Tuple Methods

Consider the tuple:

```python
a = (1, 7, 2, 1)
```

| Method       | Description                                        | Example      | Result |
| ------------ | -------------------------------------------------- | ------------ | ------ |
| `a.count(1)` | Returns the number of times 1 appears in the tuple | `a.count(1)` | `2`    |
| `a.index(1)` | Returns the index of the first occurrence of 1     | `a.index(1)` | `0`    |

---

## 📌 Summary

* ✅ **Lists** can store multiple data types and are mutable.
* ✅ You can access and slice lists just like strings.
* ✅ Python provides many useful **list methods** like `sort()`, `append()`, and `pop()`.
* ✅ **Tuples** are like lists, but **immutable** (unchangeable after creation).
* ✅ Use `count()` and `index()` to work with tuples.

---