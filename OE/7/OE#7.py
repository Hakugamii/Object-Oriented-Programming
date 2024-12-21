class TekkenCharacter():
    def __init__(self, name, ability):
        self.name = name
        self.ability = ability

    def introduce(self, func_name):
        def introducer(*args, **kwargs):
            print("Introducing...")
            func_name(*args, **kwargs)
            print("This character is amazing!")
        return 
        
lee = TekkenCharacter("Lee Chaolan", "Acid Rain Cardinal")
@lee.introduce
def character_intro():
    print(f"I am {lee.name} and I can use {lee.ability}")
character_intro()