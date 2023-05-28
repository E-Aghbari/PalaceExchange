class Player:
    def __init__(self, name, cards):
        self.name = name
        self.cards = cards
        self.spells = []
        self.health = 20
        self.armor = 0
    
    def choose_cards(self):
        pass

    def draw_card(self):
        pass

    def gain_armor(self):
        pass

    def gain_health(self):
        pass

    def use_potion(self):
        pass

    def __repr__(self):
        pass

class Card:
    def __init__(self, name, type, health):
        pass

    def attack(self):
        pass

    def use_potion(self):
        pass

    def __repr__(self):
        pass

class Spell:
    spells = ["Holy", "Natural", "Fire", "Frost"]

    def __repr__(self):
        pass