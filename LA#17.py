import random

class Player:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power
    
    def attack(self, target):
        target.health = target.health - self.attack_power
        print(f"{self.name} attacked {target.name}'s remaining health is {target.health}\nThe Damage dealt was {self.attack_power}.\n")

    def heal(self, amount):
        self.health = self.health + amount
zetsu = Player("Zetsuzen", 2134, 219)
shinra = Player("Shinra", 2234, 209)

while (zetsu.health > 1) and (shinra.health > 1):
    if zetsu.health > 1:
        zetsu.attack(shinra)
    if shinra.health > 1:
        shinra.attack(zetsu)
    healfactor = random.randint(775, 780)
    if healfactor == 777:
        healamount = random.randint(1,50)
        shinra_luck = random.randint(1,10)
        zetsu_luck = random.randint(1,10)
        if (zetsu_luck > shinra_luck) and (zetsu.health > 1):
            zetsu.heal(healamount)
            print(f"Zetsuzen's luck was higher. Zetsuzen Healed {healamount} Health")
        elif (shinra_luck > zetsu_luck) and (shinra.health > 1):
            shinra.heal(healamount)
            print(f"Shinra's luck was higher. Shinra Healed {healamount} Health")
        else:
            print("You are both lucky no one gets a heal")
    if shinra.health < 1:
        print("Zetsu Wins!")
    elif zetsu.health < 1:
        print("Shinra Wins!")