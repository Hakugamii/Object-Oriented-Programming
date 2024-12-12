class Toy():
    def __init__(self, name, price):
        self.name = name
        self.price = price
    
    def describeToy(self):
        print(f"Toy Name: {self.name}\nToy Price: {self.price}")

class Cube(Toy):
    def __init__(self, name, price):
        super().__init__(name, price)

rubix = Cube("Rubik's Cube", "499")
rubix.describeToy()