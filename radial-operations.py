import math

pi = math.pi


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def perimeter(self):
        return 2 * 3.14 * self.radius

    def area(self):
        return pi * self.radius * self.radius


class Sphere:
    def __init__(self, radius):
        self.radius = radius


radi1 = Circle(float(input("Enter Radius here: ")))

print(radi1.perimeter())
print(radi1.area())
