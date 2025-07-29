## 🧠 Key Concepts First:

### ✅ 1. **Class Attribute**

* Defined **inside the class**, but **outside any method**.
* Shared by **all objects**.
* Accessible as `ClassName.attribute` or `object.attribute` (until overridden).

```python
MyClass.a     # => 10
obj.a         # => 10 (initially)
```

---

### ✅ 2. **Object Attribute**

* Created **when you assign** to an attribute on an object.
* Overrides (or **shadows**) the class attribute **for that object only**.
* Does **not affect the class** or other objects.

---

## 🔍 Now, What Happens Line by Line:

```python
class MyClass:
    a = 10
```

* Class `MyClass` is created.
* It has a **class variable** `a = 10`.

```python
obj = MyClass()
```

* `obj` is an object of `MyClass`.
* Initially, `obj.a` gets the value **from the class**, so `obj.a == 10`.

```python
obj.a = 0
```

* Now you assign `a = 0` to the object.
* This **creates a new variable** called `a` inside `obj`.
* So now:

  * `obj.a = 0` (instance attribute)
  * `MyClass.a = 10` (class attribute — unchanged)

---

## 📊 Visual Diagram

```
MyClass
├── a = 10  ← class attribute

obj = MyClass()
├── a = 0   ← instance attribute (shadows class a)
```

---

## 🧪 Proof with Code:

```python
class MyClass:
    a = 10

obj = MyClass()
print(MyClass.a)   # 10
print(obj.a)       # 10 (gets it from the class)

obj.a = 0
print(obj.a)       # 0 (now it's the object's own variable)
print(MyClass.a)   # 10 (still unchanged)
```

---

## ✅ Summary

| Accessed As         | Value | Reason                             |
| ------------------- | ----- | ---------------------------------- |
| `MyClass.a`         | `10`  | Class attribute                    |
| `obj.a` (before)    | `10`  | Inherited from class               |
| `obj.a` (after)     | `0`   | Instance attribute overrides class |
| `MyClass.a` (after) | `10`  | Still class attribute, unchanged   |

---