## ✅ Problem Statement Recap

> Create a class `Programmer` for storing information about a few programmers working at Microsoft.

So we need:

* A **class** to represent programmers
* A **shared workplace**: Microsoft
* Programmer-specific details like name, language, experience
* A way to **display the information**

---

## ✅ Code Breakdown

```python
class Programmer:
    workplace = "Microsoft"
```

### 🟢 What this does:

* `Programmer` is the **class**.
* `workplace` is a **class variable**, meaning it's the same for all objects created from this class. All programmers work at **Microsoft**.

---

```python
    def __init__(self, name, language, experience):
        self.name = name
        self.language = language
        self.experience = experience
```

### 🟢 What this does:

* `__init__` is the **constructor method**, automatically called when a new object is created.
* `self.name`, `self.language`, `self.experience` are **instance variables** — they store data unique to each programmer.
* Example: `Programmer("Alice", "Python", 3)` will store `name="Alice"`, etc.

---

```python
    def get_info(self):
        return f"{self.name} works at {Programmer.workplace}, codes in {self.language}, and has {self.experience} years of experience."
```

### 🟢 What this does:

* `get_info()` is a method (function inside a class) that **returns a formatted string** with all the programmer's details.
* We use `Programmer.workplace` to access the **class variable**.
* `self.name`, `self.language`, and `self.experience` refer to that particular programmer.

---

```python
p1 = Programmer("Alice", "Python", 3)
p2 = Programmer("Bob", "C++", 5)
```

### 🟢 What this does:

* Creates **two programmer objects**, `p1` and `p2`, with different data.

---

```python
print(p1.get_info())
print(p2.get_info())
```

### 🟢 What this does:

* Calls the `get_info()` method for each programmer to print their information.

---

## 🧠 Summary

| Concept                | Purpose                                      |
| ---------------------- | -------------------------------------------- |
| `class Programmer`     | Defines the blueprint for programmers        |
| `workplace`            | Class variable (same for all)                |
| `__init__`             | Initializes name, language, and experience   |
| `self`                 | Refers to the current object                 |
| `get_info()`           | Returns a readable summary of the programmer |
| `p1 = Programmer(...)` | Creates a new programmer object              |

---