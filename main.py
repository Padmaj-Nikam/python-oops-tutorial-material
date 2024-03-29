# Class: A class is a blueprint for creating objects. It defines a set of attributes (data members) and methods (functions) that the objects of the class will have.
class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def get_make(self):
        return self.make

    def get_model(self):
        return self.model


# Object: An object is an instance(you can say that it is an entity made using the class blueprint) of a class. It is a concrete entity created based on the class, and it can have its own unique attributes and behaviors.
car1 = Car("Tesla", "S")
car2 = Car("BMW", "7")

# Printing a particular attribute
print(car1.get_model(), car2.get_model())
