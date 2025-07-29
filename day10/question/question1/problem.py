# Create a class programmer for storing information of few programmers working at microsoft.

class Programmer:
    # Class variable shared by all instances
    workplace = "Microsoft"

    def __init__(self, name, language, experience):
        self.name = name
        self.language = language
        self.experience = experience  # in years

    def get_info(self):
        return f"{self.name} works at {Programmer.workplace}, codes in {self.language}, and has {self.experience} years of experience."


# Example usage:
p1 = Programmer("Alice", "Python", 3)
p2 = Programmer("Bob", "C++", 5)

print(p1.get_info())
print(p2.get_info())

# Output
'''
Alice works at Microsoft, codes in Python, and has 3 years of experience.
Bob works at Microsoft, codes in C++, and has 5 years of experience.
'''