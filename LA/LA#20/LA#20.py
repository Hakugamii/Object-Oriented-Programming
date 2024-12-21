class Itlog:
    def __init__(self, luto, itlog, asin, magic_sarap):
        self.luto = luto
        self._itlog = itlog
        self.__asin = asin
        self.magic_sarap = magic_sarap
    
    def __str__(self):
        return f"My {self.luto} has {self._itlog}, {self.__asin}, {self.magic_sarap}"
    
    def accessItlog(self):
        return self._itlog
    
    def accessAsin(self):
        return self.__asin
    
scrambbledEgg = Itlog("Scrambled Egg","Egg", "Salt", "Magic Sarap Fuyioh")
sunnySideUp = Itlog("Sunny Side Up","Egg", "Salt", "Ajinomoto MSG Fuyioh")
omellete = Itlog("Omelette","Egg", "Salt", "MSG Fuyioh")

print(scrambbledEgg.accessItlog())
print(sunnySideUp.accessAsin())
print(omellete)