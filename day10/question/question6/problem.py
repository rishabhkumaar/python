# Can you choose the self parameter inside a class to something else (say "rishabh"). Try changing self to slf or rishabh and see the effects.

class Example1:
    def show(self, name):
        print("Hello", name)

class Example2:
    def show(rishabh, name):
        print("Hello", name)

obj = Example1()
obj.show("Rishabh")

obj = Example2()
obj.show("Rishabh")

# Output 
# Hello Rishabh
# Hello Rishabh

# For Better Understanding
class Train:
    def __init__(rishabh, name, seats):
        rishabh.name = name
        rishabh.seats = seats

    def book_ticket(rishabh):
        if rishabh.seats > 0:
            print(f"Ticket booked on {rishabh.name}")
            rishabh.seats -= 1
        else:
            print("No seats available")

    def get_status(rishabh):
        print(f"{rishabh.name} has {rishabh.seats} seat(s) left")

train = Train("Rajdhani Express", 3)
train.get_status()
train.book_ticket()
train.get_status()

# Output
'''
Rajdhani Express has 3 seat(s) left
Ticket booked on Rajdhani Express
Rajdhani Express has 2 seat(s) left
'''