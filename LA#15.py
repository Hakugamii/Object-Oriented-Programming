class Dog():
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name}: Barks!")

class Cat():
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name}: Meows!")

class Bird():
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name}: Tweeets!")

class Fish():
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name}: ...")

aso = Dog("Zetsu")
pusa = Cat("Retsu")
ibon = Bird("Tweety")
isda = Fish("Nemo")

def animal_sounds(animal):
    animal.speak()
    
for animal in [aso,pusa,ibon,isda]:
    animal_sounds(animal)

