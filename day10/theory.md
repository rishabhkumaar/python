## 🧾 **Chapter 10 – Object Oriented Programming**

---

### ✅ **Main Concept:**

* Solving problems by creating **objects** is called **Object-Oriented Programming (OOP)**.
* It promotes **code reusability** and follows the **DRY (Don't Repeat Yourself)** principle.

---

### 🧱 **Core Components:**

#### **1. Class**

* A **blueprint** or template to create objects.
* Written using **PascalCase**.
* Example:

  ```python
  class Employee:
      # attributes and methods
  ```

#### **2. Object**

* A **real-world instance** of a class.
* Memory is allocated only when an object is created.
* Example:

  ```python
  rishabh = Employee()
  ```

---

### 📦 **Modeling a Real-World Problem**

| Type | Meaning    | Example                      |
| ---- | ---------- | ---------------------------- |
| Noun | Class      | `Employee`                   |
| Adj. | Attributes | `name`, `age`, `salary`      |
| Verb | Methods    | `getSalary()`, `increment()` |

---

### 🧮 **Types of Attributes**

#### **a. Class Attribute**

* Shared across all instances of a class.
* Modified using `ClassName.attribute`.
* Example:

  ```python
  class Employee:
      company = "Google" # Specific to each class
    rishabh = Employee() # Object instantiation
    rishabh.company 
    Employee.company = "Google" # Changing class attribute
  ```

#### **b. Instance Attribute**

* Unique to each object.
* Added via the object itself.
* Example:

  ```python
  rishabh.name = "Rishabh"
  ```

> 🔎 **Priority Rule**:
> If an attribute is found in both the object and class, **object attribute takes priority**.

---

### 🔁 **The `self` Parameter**

* Refers to the **current object**.
* Automatically passed in method calls.
* Example:

  ```python
  class Employee:
      def getSalary(self):
          print("Salary")
  ```

---

### 🚫 **Static Method**

* Does **not** use the `self` parameter.
* Use `@staticmethod` decorator.
* Example:

  ```python
  @staticmethod
  def greet():
      print("Hello User")
  ```

---

### 🚪 **Constructor: `__init__()`**

* Called **automatically** when an object is created.
* Used to **initialize object attributes**.
* Example:

  ```python
  class Employee:
      def __init__(self, name):
          self.name = name
      def getSalary(self):
        # ...
  rishabh=Employee("Rishabh") # Object can be instantiated using constructor like this
  ```

---