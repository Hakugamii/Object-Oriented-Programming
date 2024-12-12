class Car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

vehicle = Car("Lotus", "Red")
print(f"Original : {vehicle.brand} {vehicle.color}")
vehicle.color = "Black"
print(f"Updated : {vehicle.brand} {vehicle.color}")

vehicle2nd = Car("Nissan","Silver")
print(f"Original : {vehicle2nd.brand} {vehicle2nd.color}")
print(f"Updated : {vehicle2nd.brand} {vehicle2nd.color}")