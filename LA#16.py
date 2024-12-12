class Appliance():
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def operate(self):
        print("Operating!")

    def info(self):
        print(f"Brand: {self.brand}\nModel: {self.model}")

class WashingMachine(Appliance):
    def __init__(self, brand, model):
        super().__init__(brand, model)

    def operate(self):
        self.info()
        print("Washing clothes!")

class Refrigerator(Appliance):
    def __init__(self, brand, model):
        super().__init__(brand, model)

    def operate(self):
        self.info()
        print("Keeping food cold!")

class Microwave(Appliance):
    def __init__(self, brand, model):
        super().__init__(brand, model)

    def operate(self):
        self.info()
        print("Heating food!")

washy = WashingMachine("Toshiba", "AW-DUK1300K-PH")
coldy = Refrigerator("Samsung", "RF32CG5400SR")
heaty = Microwave("Fujidenzo", "MM22BL")

for appliances in [washy,coldy,heaty]:
    appliances.operate()