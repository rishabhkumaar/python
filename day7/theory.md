# 📘 **Chapter 7: Loops in Python**

In this chapter, you'll learn about:

* 🔁 Why we use loops
* 🔄 Types of loops in Python
* ⚙️ `while` and `for` loops
* ⛔ `break`, `continue`, `pass`

---

## 💡 Why Loops?

Loops allow us to **repeat code** efficiently.

Example: Printing numbers from 1 to 1000 manually would take forever!
With loops, we can write logic once and execute it multiple times.

---

## 🔁 Types of Loops in Python

There are two main types:

1. `while` loop
2. `for` loop

Let’s explore them one by one.

---

## 🔄 `while` Loop

### ✅ Syntax:

```python
while condition:
    # code block (loop body)
```

* The **condition is checked first**
* If it's `True`, the loop body runs
* It **repeats until** the condition becomes `False`

---

## 🧩 Quick Quiz

✍️ **Print numbers from 1 to 50 using a while loop**

```python
num = 1
while num <= 50:
    print(num)
    num += 1   # ✅ Fix: was "i += 1"
```

---

## ⚠️ Infinite Loop Alert

If the condition **never becomes false**, the loop will run forever!

```python
while True:
    print("This will run forever!")
```

---

## 🧩 Quick Quiz

✍️ **Print the contents of a list using a while loop**

```python
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
index = 0

while index < len(data):
    print(data[index])
    index += 1
```

---

## 🔁 `for` Loop

Used to iterate over **sequences** like:

* list
* tuple
* string

### ✅ Syntax:

```python
l = [1, 7, 8]
for item in l:
    print(item)
```

---

## 🎯 `range()` Function

`range(start, stop, step)` generates a sequence of numbers.

### Example:

```python
for i in range(0, 7):
    print(i)
```

---

## 🧩 `for` loop with `else`

The `else` block runs when the loop **finishes without break**.

### Example:

```python
l = [1, 7, 8]
for item in l:
    print(item)
else:
    print("Done")  # Will print after the loop ends normally
```

---

## ⛔ `break` Statement

Used to **exit** the loop early.

### Example:

```python
for i in range(10):
    print(i)
    if i == 3:
        break  # Loop exits when i == 3
```

---

## 🔄 `continue` Statement

Skips the **current iteration** and moves to the next one.

### Example:

```python
for i in range(4):
    print("Painting")
    if i == 2:
        continue  # Skips printing i when i == 2
    print(i)
```

---

## 🚫 `pass` Statement

`pass` is a **null statement** — it does nothing.

### Example:

```python
l = [1, 7, 8]
for item in l:
    pass  # Required when a loop or function is syntactically needed but you don’t want to run any code yet
```

---

## 📌 Summary – Chapter 7: Loops in Python

* 🔁 **Loops** allow you to repeat a block of code multiple times.
* 🌀 Python supports two main types of loops:

  * **`while` loop**: Repeats as long as a condition is `True`.
  * **`for` loop**: Iterates over items in a sequence (like list, string, range, etc.).
* ✅ **`while` loops** are great when the number of iterations isn't known in advance.
* ✅ **`for` loops** are perfect when you're working with collections or know how many times to repeat.
* 🧠 Use the **`range()` function** to generate sequences of numbers (with optional start, stop, step).
* 🚫 The **`break`** statement is used to **exit** a loop prematurely.
* ➡️ The **`continue`** statement **skips** the current iteration and moves to the next.
* 🪄 The **`pass`** statement acts as a **placeholder** where code is syntactically required but not needed yet.
* ✅ You can combine `else` with a `for` loop — the `else` block runs **only if the loop completes normally** (not stopped by `break`).

---