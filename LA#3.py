class Tank():
    def __init__(self, name, role):
        self.hero = name
        self.role = role
    
    def role_type(self):
        return f"{roamer.hero} is a {roamer.role}"

roamer = Tank("Atlas", "Tank/Roamer")
print(roamer.role_type())   

