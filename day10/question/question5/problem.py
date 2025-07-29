# Write a class Train which has methods to book a ticket, get status (no of seats) and get fare information of trains running under Indian Railways.

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

# Test

rajdhani = Train("Rajdhani Express", 1500, 5)

rajdhani.get_status()       # ➝ 5 seats
rajdhani.get_fare_info()    # ➝ ₹1500
rajdhani.book_ticket()      # ➝ Booking done
rajdhani.get_status()       # ➝ 4 seats