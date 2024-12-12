class party:
    def __init__(self, foods, special, secretDish):
        self.foods = foods
        self.special = special
        self.secretDish = secretDish

    def dishes(self):
        print(f"The main course of the party are {self.foods} and the specialty of the cook is {self.special}.")
        self.__secretDishGetter()

    def __secretDishGetter(self):
        print(f"The secret dish is {self.secretDish}.")

backyardParty = party("Barbeque, Smores, Hotdogs, Corns", "Brisket", "Grilled Salmon")
birthday = party("Spaghetti, Coffee Jelly, Lechon Kawali, Mashed Potatoes, Chocolate Cake", "Roasted Turkey", "Hamonado")
pajamaParty = party("Pizza, Popcorn, Onion Rings, Hot Cocoa", "French Fries and Chips", "Shawarma")

backyardParty.dishes()
birthday.dishes()
pajamaParty.dishes()