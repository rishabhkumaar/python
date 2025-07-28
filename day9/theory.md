# 📘 Chapter 9: File I/O in Python

---

## Why File I/O?

RAM is **volatile**, which means all its content is lost when the program ends.
To **store data permanently**, we use **files**.

📁 A file is data stored on a **storage device**, and Python can:

* ✅ Read data from files
* ✅ Write data to files

```
RAM (Volatile)    ↔️    File (Non-Volatile)
        ^                    ^
        |---- Python Code ---|
```

---

## 🗂️ Types of Files

1. **Text Files** – `.txt`, `.c`, `.py`, etc.
2. **Binary Files** – `.jpg`, `.png`, `.mp3`, `.dat`, etc.

Python provides built-in functions to handle both types efficiently.

---

## 🔓 Opening a File

```python
file = open("file.txt", "r")
```

* `"r"` stands for **read mode**
* Other common modes include:

  * `"w"` – write
  * `"a"` – append
  * `"r+"` – read and write
  * `"rb"` – read in binary mode
  * `"rt"` – read in text mode

---

## 📖 Reading a File

```python
f = open("this.txt", "r")
text = f.read()
print(text)
f.close()
```

* You can also read a **specific number of characters**:

  ```python
  text = f.read(2)  # Reads the first 2 characters
  ```

### 📌 `readline()` Method

```python
line = f.readline()
```

* Reads **one line at a time**
* Successive calls to `f.readline()` read the next lines

---

## 📝 Writing to a File

To **write** content, use the `"w"` or `"a"` mode:

```python
f = open("this.txt", "w")
f.write("This is nice.\n")
f.write("This will overwrite any existing content.")
f.close()
```

* `"w"` will **overwrite** the file
* `"a"` will **append** to the file

---

## ✅ Best Practice: `with` Statement

Automatically handles file closing:

```python
with open("this.txt", "r") as f:
    content = f.read()
    print(content)
# No need to call f.close()
```

---

## 🧩 Quick Quiz Idea

✍️ **Write a program that creates a file and writes your name to it using Python. Then, read the file and display its content.**

---

## 🧠 Summary

✅ Files are used to **store data permanently** (unlike RAM)
✅ Use `open()` to read or write files
✅ File Modes:

* `"r"` → read
* `"w"` → write (overwrites)
* `"a"` → append
* `"r+"` → read + write

✅ Use `read()`, `readline()`, or `readlines()` to read from files
✅ Use `write()` to write content
✅ Prefer using the `with` statement for **auto-closing** and better file management

---