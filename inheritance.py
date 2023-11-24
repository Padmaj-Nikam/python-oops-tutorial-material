# Super Class from which the lower classes take in the key attributes.
class Vehicle:
    def __init__(self, name, wheels):
        self.name = name
        self.wheels = wheels

    def show(self):
        print(f"Hey I am a {self.name} and I have {self.wheels} wheels.")


# Lower class for two wheelers. Using the super class just requires us to input the class name while declaring the lower classes.
class two_wheelers(Vehicle):
    def __init__(self, name, wheels, colour):
        super().__init__(name, wheels)
        self.colour = colour

    def col(self):
        return self.colour


# Lower class for four wheelers.
class four_wheelers(Vehicle):
    def __init__(self, name, wheels, colour, horse):
        super().__init__(name, wheels)
        self.colour = colour
        self.horse = horse

    def col(self):
        return self.colour

    def power(self):
        print(f"I have {self.horse} horsepower")


v1 = two_wheelers("bullet_350", 2, "black")
v2 = four_wheelers("tesla_s", 4, "white", "800")

print(v1.col(), v2.power(), v1.show(), v2.show())
