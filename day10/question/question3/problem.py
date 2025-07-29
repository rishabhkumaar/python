# Create a class with a class attribute a; create an object from itand set a directly using object.a = 0. Does this change the class attribute?

class MyClass:
    a = 10  # class attribute

obj = MyClass()
obj.a = 0  # modifying a using the object

print("Class attribute:", MyClass.a)
print("Object attribute:", obj.a)

# Output
'''
Class attribute: 10
Object attribute: 0
'''