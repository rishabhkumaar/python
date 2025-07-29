## ✅ What is this code doing?

The `Train` class is designed to simulate a simple **Indian Railways train booking system**. It includes:

| Functionality     | Purpose                       |
| ----------------- | ----------------------------- |
| `book_ticket()`   | Books a seat if available     |
| `get_status()`    | Shows how many seats are left |
| `get_fare_info()` | Tells the fare of the train   |

---

## 📦 Full Code First (for reference):

```python
class Train:
    def __init__(self, name, fare, seats):
        self.name = name
        self.fare = fare
        self.seats = seats

    def get_status(self):
        print(f"Train '{self.name}' has {self.seats} seat(s) available.")

    def get_fare_info(self):
        print(f"The fare for '{self.name}' is ₹{self.fare}.")

    def book_ticket(self):
        if self.seats > 0:
            print(f"Ticket booked successfully in '{self.name}'!")
            self.seats -= 1
        else:
            print("Sorry, no seats available!")
```

---

## 🧠 Let's Understand Each Part

### 1. **Constructor: `__init__()`**

This sets up the train with:

* `name` → Name of the train (e.g. "Rajdhani Express")
* `fare` → How much the ticket costs (e.g. ₹1500)
* `seats` → How many tickets are available

📌 Example:

```python
Train("Rajdhani Express", 1500, 5)
```

This means:

* Train name = "Rajdhani Express"
* Ticket price = ₹1500
* Seats available = 5

---

### 2. **Method: `get_status()`**

Shows how many seats are still available.

```python
def get_status(self):
    print(f"Train '{self.name}' has {self.seats} seat(s) available.")
```

📌 Output:

```
Train 'Rajdhani Express' has 5 seat(s) available.
```

---

### 3. **Method: `get_fare_info()`**

Tells you the price of a single ticket.

```python
def get_fare_info(self):
    print(f"The fare for '{self.name}' is ₹{self.fare}.")
```

📌 Output:

```
The fare for 'Rajdhani Express' is ₹1500.
```

---

### 4. **Method: `book_ticket()`**

Tries to book 1 ticket:

* If `seats > 0`: it books the ticket and decreases the count.
* If no seats left: it shows an error message.

```python
def book_ticket(self):
    if self.seats > 0:
        print(f"Ticket booked successfully in '{self.name}'!")
        self.seats -= 1
    else:
        print("Sorry, no seats available!")
```

📌 Output:

```
Ticket booked successfully in 'Rajdhani Express'!
```

Or if seats = 0:

```
Sorry, no seats available!
```

---

## 🔁 Sample Run:

```python
train1 = Train("Rajdhani Express", 1500, 2)

train1.get_status()        # Train 'Rajdhani Express' has 2 seat(s) available.
train1.book_ticket()       # Ticket booked...
train1.book_ticket()       # Ticket booked...
train1.book_ticket()       # Sorry, no seats...
train1.get_status()        # Train 'Rajdhani Express' has 0 seat(s) available.
```

---

## ✅ Summary

| Component         | Meaning                               |
| ----------------- | ------------------------------------- |
| `__init__()`      | Sets up train details                 |
| `book_ticket()`   | Books 1 ticket if seats are available |
| `get_status()`    | Shows remaining seats                 |
| `get_fare_info()` | Shows ticket price                    |

---