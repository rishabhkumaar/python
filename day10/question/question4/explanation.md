## 🧾 Updated Code Recap:

```python
class Calculator:
    @staticmethod
    def square(number):
        return number * number

    @staticmethod
    def cube(number):
        return number * number * number

    @staticmethod
    def square_root(number):
        return number ** 0.5

    @staticmethod
    def greet():
        print("Hello")
```

---

## 🔍 What Is a Static Method?

* A **static method** is a function **inside a class**, but it does **not use `self` or `cls`**.
* It belongs to the class **but doesn’t need any object or class info to work**.
* It’s useful when you want a method that:

  * **Logically belongs to the class**
  * But **doesn’t depend** on class or object data

---

## 🔹 The `greet()` Method

```python
@staticmethod
def greet():
    print("Hello")
```

### 🧠 What it does:

* It simply prints `"Hello"` to the screen.
* It doesn't use any data from the class or object.
* You can call it **directly using the class**.

---

## 🧪 How to Use:

```python
Calculator.greet()
```

### 🔄 Output:

```
Hello
```

You don't need to create an object:

```python
# This is unnecessary:
calc = Calculator()
calc.greet()  # works, but not needed
```

---

## ✅ Summary Table:

| Feature      | Type          | Access method              | Needs object? |
| ------------ | ------------- | -------------------------- | ------------- |
| `square()`   | Static Method | `Calculator.square(4)`     | ❌ No          |
| `greet()`    | Static Method | `Calculator.greet()`       | ❌ No          |
| `__init__()` | Constructor   | Called when object created | ✅ Yes         |

---

## 🧩 Why Use `@staticmethod`?

✅ Use it when:

* The method doesn’t use `self` or class variables
* But still belongs **logically** to the class

---