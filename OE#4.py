import random

class Character:
    def __init__(self, name, health, power):
        self.name = name
        self.health = health
        self.power = power
        self.normal = power
        self.defending = None

    def attack(self, target):
        if target.defending == self:
            self.power *= 0.75
        target.health = target.health - self.power
        print(f"{self.name} attacked {target.name}'s remaining health is {target.health}.\nThe Damage dealt was {self.power}.\n")
        if target.defending == self:
            self.power = self.normal
            target.defending = None

    def defend(self, attacker):
        self.defending = attacker

    def special_move(self):
        pass

class Warrior(Character):
    def __init__(self, name, health, power):
        super().__init__(name, health, power)
        self.empower = False

    def special_move(self):
        print("Warrior uses Shield Bash!\n")
        self.empower = True

    def attack(self, target):
        if self.empower:
            self.power += self.power
        super().attack(target)
        if self.empower:
            self.empower = False
            self.power = self.normal

class Mage(Character):
    def __init__(self, name, health, power):
        super().__init__(name, health, power)

    def special_move(self, target):
        target.health -= 500
        print(f"{self.name} Casts Fireball! on {target.name}.\n{target.name}'s remaining health is {target.health}.\nThe Damage dealt was 500.\n")

        #reduce targets health by a large fixed amount

class Archer(Character):
    def __init__(self, name, health, power):
        super().__init__(name, health, power)

    def special_move(self, target):
        target.health = target.health - self.power
        print(f"{self.name} shoots Piercing Arrow! on {target.name}.\n{target.name}'s remaining health is {target.health}.\nThe Damage dealt was {self.power}.\n")
        #ignores target's defense causing damage behave differently across various classes.

class Monster(Character):
    def __init__(self, name, health, power):
        super().__init__(name, health, power)

    def special_move(self):
        print("Monster roars and increases its health by 80!\n")
        self.health = self.health + 80

kata = Warrior("Kata", 3491, 203)
kishin = Mage("Kishin", 2841, 276)
toka = Archer("Toka", 2978, 262)
roshan = Monster("Roshan", 14320, 563)

kata.attack(roshan)
kata.special_move()
kata.attack(roshan)
kata.attack(roshan)
roshan.defend(kata)
kata.attack(roshan)
kata.attack(roshan)

kishin.attack(roshan)
kishin.special_move(roshan)
kishin.attack(roshan)
roshan.defend(toka)
kishin.attack(roshan)

toka.attack(roshan)
toka.special_move(roshan)
toka.attack(roshan)

roshan.attack(kishin)
roshan.special_move()
roshan.attack(kata)
roshan.attack(toka)
roshan.special_move()

selection = [kata, kishin, toka, roshan]
def randomizer():
    removed = []
    for each in selection:
        if each.health <= 0:
            selection.remove(each)
            removed.append(each)
    max = len(selection)
    selector = random.randrange(0,max)
    selected = selection[selector]
    for each in removed:
        selection.append(each)
    return selected
    
def target_randomizer(selected):
    removed = []
    for each in selection:
        if each == selected:
            selection.remove(each)
            removed.append(each)
        elif each.health <= 0:
            selection.remove(each)
            removed.append(each)
    max = len(selection)
    selector = random.randrange(0, max)
    target = selection[selector]
    for each in removed:
        selection.append(each)
    return target

def attack():
    attacker = randomizer()
    target = target_randomizer(attacker)
    attacker.attack(target)

def defend():
    defender = randomizer()
    attacker = target_randomizer(defender)
    defender.defend(attacker)

def special():
    caster = randomizer()
    target = target_randomizer(caster)
    if caster == kata or caster == roshan:
        caster.special_move()
    else:
        caster.special_move(target)
    
alive = [character for character in selection if character.health > 0]
print("Battle Starts!")
while len(alive) > 1:
    defend()
    attack()
    special()
    alive = [character for character in selection if character.health > 0]
print(alive)
print("Battle has ended")
