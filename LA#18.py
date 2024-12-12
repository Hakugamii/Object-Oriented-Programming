class Itlog:
    def __init__(self, luto, itlog, asin, magic_sarap):
        self.luto = luto
        self.itlog = itlog
        self.asin = asin
        self.magic_sarap = magic_sarap
    
    def __str__(self):
        return f"My {self.luto} has {self.itlog}, {self.asin}, {self.magic_sarap}"
    
scrambbledEgg = Itlog("Scrambled Egg","Egg", "Salt", "Magic Sarap Fuyioh")
sunnySideUp = Itlog("Sunny Side Up","Egg", "Salt", "Ajinomoto MSG Fuyioh")
boildEgg = Itlog("Boiled Egg","Egg", None, None)

print(scrambbledEgg)
print(sunnySideUp)
print(boildEgg)