# **Chapter 11 - Inheritance & More on OOPs**

---

## **What is Inheritance?**

Inheritance is a feature in Object-Oriented Programming that allows a new class (child/derived class) to inherit attributes and methods from an existing class (base/parent class).

```python
# Example

class Employee:             # Base Class
    pass

class Programmer(Employee): # Derived or Child Class
    pass
```

With inheritance, the `Programmer` class can reuse the code in `Employee`, and also add or override functionality.

---

## **Types of Inheritance**

1. **Single Inheritance**
   One child class inherits from one parent class.

   ```
   Base → Derived
   ```

2. **Multiple Inheritance**
   One child class inherits from multiple parent classes.

   ```
   [Parent1]     [Parent2]
       \           /
        \         /
         \       /
           Child
   ```

3. **Multilevel Inheritance**
   A chain of inheritance.

   ```
   Parent
     ↓
   Child1
     ↓
   Child2
   ```

---

## **The `super()` Method**

* `super()` is used to call methods of the parent class inside the child class.
* Commonly used to initialize parent class constructor.

```python
class A:
    def __init__(self):
        print("A's constructor")

class B(A):
    def __init__(self):
        super().__init__()  # Calls A's constructor
        print("B's constructor")
```

---

## **Class Methods**

* Bound to the **class**, not an instance.
* Created using the `@classmethod` decorator.
* First parameter is usually named `cls`.

```python
class MyClass:
    @classmethod
    def show(cls):
        print("This is a class method")
```

---

## **@property Decorator**

* Allows methods to be accessed like attributes.
* Often used to define **getters**, **setters**, and **deleters** for encapsulated attributes.

```python
class Employee:
    def __init__(self, name):
        self._ename = name

    @property
    def name(self):
        return self._ename

    @name.setter
    def name(self, value):
        self._ename = value
```

Usage:

```python
e = Employee("Ravi")
print(e.name)      # Getter
e.name = "Rohan"   # Setter
```

---

## **Operator Overloading**

Python lets you override operators for objects using **dunder (double underscore) methods**:

| Operator | Method           | Example    |
| -------- | ---------------- | ---------- |
| `+`      | `__add__()`      | `p1 + p2`  |
| `-`      | `__sub__()`      | `p1 - p2`  |
| `*`      | `__mul__()`      | `p1 * p2`  |
| `//`     | `__floordiv__()` | `p1 // p2` |

---

## **Other Magic Methods**

* `__str__()` → Defines behavior for `str(obj)`
* `__len__()` → Defines behavior for `len(obj)`

Example:

```python
class Book:
    def __init__(self, pages):
        self.pages = pages

    def __len__(self):
        return self.pages

    def __str__(self):
        return f"Book with {self.pages} pages"

b = Book(200)
print(len(b))      # 200
print(str(b))      # Book with 200 pages
```

---