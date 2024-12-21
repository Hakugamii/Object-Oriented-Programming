class Dog():
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name}: Bark!")

class Cat():
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name}: Meow!")

class Bird():
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name}: Chirp!")

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

