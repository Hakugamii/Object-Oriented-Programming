class Vehicle():
    def __init__(self, brand, model, fuel_type):
        self.brand = brand
        self.model = model
        self.fuel_type = fuel_type

    def describeVehicle(self):
        print(f"Brand: {self.brand}\nModel: {self.model}\nFuel Type: {self.fuel_type}")

class Car(Vehicle):
    pass
class Motorcycle(Vehicle):
    pass

porsche = Car("Porsche", "Cayman", "Gasoline")
porsche.describeVehicle()

kawasaki = Motorcycle("Kawasaki", "Ninja H2R", "Gasoline")
kawasaki.describeVehicle()