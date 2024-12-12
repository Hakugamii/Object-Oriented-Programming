class Tank():
    def __init__(self, name, role):
        self.name = name
        self.role = role

roamer = Tank("Atlas", "Tank/Roamer")
print(f"{roamer.name} is a {roamer.role}")