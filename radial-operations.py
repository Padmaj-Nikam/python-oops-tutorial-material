import math

pi = math.pi


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def perimeter(self):
        return 2 * (pi * self.radius)

    def area(self):
        return 3.14 * self.radius**2


radi1 = Circle(input("Enter Radius here: "))
print(radi1.perimeter)
