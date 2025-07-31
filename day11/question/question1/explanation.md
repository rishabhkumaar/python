## ✅ **Objective Recap**

We are asked to:

* Create a 2D vector class.
* Extend it to a 3D vector class.
* Include features like constructor, magnitude calculation, addition, and string representation.

---

## 🧱 Step 1: Define the `Vector2D` class

```python
class Vector2D:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
```

* This is a constructor that initializes `x` and `y` components.
* Default values (`0`) are provided so that you can create a vector without arguments.

---

### 🧮 Add magnitude method

```python
    def magnitude(self):
        return (self.x**2 + self.y**2) ** 0.5
```

* This uses the Pythagorean theorem to calculate the **length** (magnitude) of a 2D vector.

---

### ➕ Add vector addition method

```python
    def add(self, other):
        return Vector2D(self.x + other.x, self.y + other.y)
```

* This method adds the components of two vectors and returns a new `Vector2D` object.

---

### 📄 Add string representation

```python
    def __str__(self):
        return f"Vector2D({self.x}, {self.y})"
```

* This method makes it easy to print the vector in a human-readable form.

---

## 🧱 Step 2: Define the `Vector3D` class (inherits from `Vector2D`)

```python
class Vector3D(Vector2D):
    def __init__(self, x=0, y=0, z=0):
        super().__init__(x, y)
        self.z = z
```

* `Vector3D` **inherits** `x` and `y` from `Vector2D` using `super()`.
* Adds a new attribute `z` for 3D functionality.

---

### 🧮 Override magnitude method for 3D

```python
    def magnitude(self):
        return (self.x**2 + self.y**2 + self.z**2) ** 0.5
```

* This calculates the magnitude in 3D space.

---

### ➕ Override add method

```python
    def add(self, other):
        return Vector3D(self.x + other.x, self.y + other.y, self.z + other.z)
```

* Adds two 3D vectors and returns a new `Vector3D` object.

---

### 📄 Override `__str__` for better 3D display

```python
    def __str__(self):
        return f"Vector3D({self.x}, {self.y}, {self.z})"
```

---

## 🚀 Example Usage

```python
v2 = Vector2D(3, 4)
v3 = Vector3D(1, 2, 2)

print(v2)                      # → Vector2D(3, 4)
print(v2.magnitude())          # → 5.0

print(v3)                      # → Vector3D(1, 2, 2)
print(v3.magnitude())          # → 3.0
```

* These lines create and use both classes.
* They show how inheritance works and how methods behave differently in 2D and 3D vectors.

---

## ✅ Summary

| Feature     | Vector2D         | Vector3D                      |
| ----------- | ---------------- | ----------------------------- |
| Attributes  | `x`, `y`         | Inherits `x`, `y`, adds `z`   |
| Magnitude   | √(x² + y²)       | √(x² + y² + z²)               |
| Addition    | Adds `x` and `y` | Adds `x`, `y`, and `z`        |
| Inheritance | Base class       | Derived class from `Vector2D` |

---
