# Create a class Vector2D to represent a 2-dimensional vector with attributes x and y. Then, create a subclass Vector3D that represents a 3-dimensional vector by extending the Vector2D class and adding a z attribute.

# Class representing a 2D vector
class Vector2D:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Vector2D({self.x}, {self.y})"

    def magnitude(self):
        return (self.x**2 + self.y**2) ** 0.5

    def add(self, other):
        return Vector2D(self.x + other.x, self.y + other.y)

# Class representing a 3D vector, inheriting from 2D vector
class Vector3D(Vector2D):
    def __init__(self, x=0, y=0, z=0):
        super().__init__(x, y)  # Call Vector2D constructor
        self.z = z

    def __str__(self):
        return f"Vector3D({self.x}, {self.y}, {self.z})"

    def magnitude(self):
        return (self.x**2 + self.y**2 + self.z**2) ** 0.5

    def add(self, other):
        return Vector3D(self.x + other.x, self.y + other.y, self.z + other.z)

# Example usage:
v2 = Vector2D(3, 4)
v3 = Vector3D(1, 2, 2)

print(v2)                      # Vector2D(3, 4)
print(f"2D Magnitude: {v2.magnitude()}")  # 5.0

print(v3)                      # Vector3D(1, 2, 2)
print(f"3D Magnitude: {v3.magnitude()}")  # 3.0
