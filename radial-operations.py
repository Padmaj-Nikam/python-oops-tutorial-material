import math

pi = math.pi


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def perimeter(self):
        return 2 * 3.14 * self.radius

    def area(self):
        return pi * self.radius**2


class Sphere:
    def __init__(self, radius):
        self.radius = radius

    def surface_area(self):
        return 4 * pi * self.radius**2

    def volume(self):
        return 4 / 3 * pi * self.radius**3


radi1 = Circle(float(input("Enter Radius here: ")))

print(radi1.perimeter())
print(radi1.area())

sphere1 = Sphere(float(input("Enter radius here: ")))

print(sphere1.surface_area())
print(sphere1.volume())
