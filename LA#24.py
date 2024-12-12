from abc import ABC, abstractmethod

class GameCharacter(ABC):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def attack(self):
        pass

class Warrior(GameCharacter):
    def attack(self):
        print("Swings Sword!")

class Mage(GameCharacter):
    def attack(self):
        print("Casts a fireball!")

class Archer(GameCharacter):
    def attack(self):
        print("Shoots an arrow!")

class Healer(GameCharacter):
    def attack(self):
        print("Casts Healing spell on ally!")

kata = Warrior()
kishin = Mage()
toka = Archer()
kyouka = Healer()

kata.attack()
kishin.attack()
toka.attack()
kyouka.attack()
