class Phone():
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def describePhone(self):
        print(f"Phone Brand: {self.brand}\nPhone Model: {self.model}")
        
class Android(Phone):
    def __init__(self, brand, model):
        Phone.__init__(self, brand, model)

linuxphone = Android("Realme","GT Neo 5 SE")
linuxphone.describePhone()
