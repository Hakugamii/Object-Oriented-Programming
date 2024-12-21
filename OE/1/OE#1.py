class Hero():
    def __init__(self, name, role, dmg_type, health, dmg):
        self.name = name
        self.role = role
        self.dmg_type = dmg_type
        self.health = health
        self.dmg = dmg

    def __str__(self):
        return "This is a Mobile Legends Meta Team"
    
    def describe(self):
        return f"{self.name} is a {self.role} with a {self.dmg_type} power, {self.health} Health and {self.dmg} Basic Attack Damage"
    
hero_mm1 = Hero("Claude", "Marksman", "Physical Damage", 1023, 46)
hero_roam1 = Hero("Natalia", "Roaming/Assasin", "Physical Damage", 952, 56)
hero_jungle1 = Hero("Sun", "Fighter/Assasin", "Physical Damage", 1142, 57)
hero_exp1 = Hero("Terizla", "Fighter/Tank", "Physical Damage", 1342, 53)
hero_mage1 = Hero("Lylia", "Mage", "Magic Damage", 983, 49)

print(f"{hero_mm1.describe()}\n{hero_roam1.describe()}\n{hero_jungle1.describe()}\n{hero_exp1.describe()}\n{hero_mage1.describe()}")
print(f"\n{hero_mm1}")