import math

pi = math.pi


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def perimeter(self):
        return 2 * int(pi * self.radius)

    def area(self):
        return int(pi) * int(self.radius) * int(self.radius)


radi1 = Circle(input("Enter Radius here: "))

radi1.perimeter()
