class AnimeCharacter():
    def __init__(self, name, ability):
        self.name = name
        self.ability = ability

    def introduce(self, func_name):
        def introducer(*args, **kwargs):
            print("Introducing...")
            func_name(*args, **kwargs)
            print("This character is amazing!")
        return introducer
    
dbz = AnimeCharacter("Goku", "Ultra-Instinct")

@dbz.introduce
def character_intro():
    print(f"I am {dbz.name} and I can use {dbz.ability}")
character_intro()