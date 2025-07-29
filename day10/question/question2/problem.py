# Write a class calculator capable of finding square, cube and square root of a number.

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

# Test
print("Square of 5:", Calculator.square(5))         # 25
print("Cube of 3:", Calculator.cube(3))             # 27
print("Square root of 16:", Calculator.square_root(16))  # 4.0