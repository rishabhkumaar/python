Chapter 11 - Inheritance & More on OOPs

Inheritance is a way of creating a new class from an existing class.

```python
# Syntax

class Employee:             # Base Class
    # code ...
class Programmer(Employee): # Derived or Child Class
    # code ...
```

We can use the methods and attributes of Employee in Programmer object.

Also, we can overwrite or add new attributes and methods in Programmer class.

### Types of Inheritance
* 1. Single Inheritance
* 2. Multiple Inheritance
* 3. Multilevel Inheritance

## Single Inheritance
Single inheritance occurs when child class inherits only a single parent class.

Base => Derived

## Multiple Inheritance 
Multiple inheritance occurs when the child class inherits from more than one parent class.

[Parent 1]      [Parent 2]
    |               |
    └───────────────┘
            |
            Child       

## Multilevel Inheritance

When a child class becomes a parent for another child class.

Parent
   |
Child 1
   |
Child 2

## super() method

super method is used to access the methofs of a superclass in the derived class.

```python
super().__init__()
                 └─> Calls constructor of the base class.
```

## class methods
A class method is a method which is bounded to the class and not the object of the class.
@classmethod decorator is used to create a class method