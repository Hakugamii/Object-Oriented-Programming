class Car:
    def __init__(self, brand):
        car_brand = brand
    def __str__(self):
        return f"Car Object"
vehicle = Car("Lamborghini")
print(vehicle)
del vehicle
print(vehicle)