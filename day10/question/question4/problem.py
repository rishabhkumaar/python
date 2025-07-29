# Add a static method in problem 2 to greet the user with hello.

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

# Test

Calculator.greet()             # ➝ Hello
print(Calculator.square(4))    # ➝ 16
print(Calculator.cube(3))      # ➝ 27
print(Calculator.square_root(9))  # ➝ 3.0
