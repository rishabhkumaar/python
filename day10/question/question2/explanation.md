## 🔍 Step-by-Step Explanation

### 🧱 1. `class Calculator:`

This defines a **class** named `Calculator`. It groups related functions (`square`, `cube`, `square_root`) together — like a toolbox for math operations.

---

### 🔧 2. `@staticmethod`

This means the method:

* **Doesn't need `self`** (no access to instance-specific data)
* Can be called directly using the class like:

  ```python
  Calculator.square(4)
  ```

You use `@staticmethod` when the function just needs **inputs**, and not anything about the class or object.

---

### ➗ 3. `square(number)`

```python
return number * number
```

This simply multiplies the number with itself.
Example: `Calculator.square(5)` → `25`

---

### 🧊 4. `cube(number)`

```python
return number * number * number
```

This calculates the cube of a number.
Example: `Calculator.cube(3)` → `3 * 3 * 3 = 27`

---

### 📐 5. `square_root(number)`

```python
return number ** 0.5
```

This raises the number to the power of 0.5, which is the same as square root.
Example: `Calculator.square_root(16)` → `16 ** 0.5 = 4.0`

---

## 💡 How to Use It

```python
print(Calculator.square(6))       # ➝ 36
print(Calculator.cube(2))         # ➝ 8
print(Calculator.square_root(25)) # ➝ 5.0
```

Notice — we are **not** doing:

```python
calc = Calculator()
calc.square(5)
```

Because the methods are static, we **don’t need to create an object**.

---

## 🤔 Why Use a Class Here?

Even though we could write these as normal functions, grouping them in a class:

* Organizes them logically
* Makes the code reusable and cleaner
* Is good practice for OOP (Object-Oriented Programming)

---