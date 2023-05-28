class Player:
    def __init__(self, name):
        self.name = name
        self.cards = []
        self.spells = []
        self.health = 20
        self.armor = 0
        self.knocked_out = False
    
    def choose_cards(self, card):
        card = input("Choose a card: ")
        if card not in self.cards:
            self.cards.append(card)
        else:
            print("You already have that card.")

    def choose_spells(self, spell):
        spell = input("Choose a spell: ")
        if spell not in self.spells:
            self.spells.append(spell)

    def gain_armor(self):
        self.armor += 5

    def gain_health(self):
        if self.knocked_out:
            print("You can't gain health while knocked out.")
        else:
            self.health += 5

    def lose_armor(self):
        pass

    def lose_health(self):
        pass

    def __repr__(self):
        return f"{self.name} has {self.health} health and {self.armor} armor. His cards are {self.cards} and his spells are {self.spells}."

class Card:
    warriors = {"Knight": [2, 2], "Paladin": [3, 1], "Berserker": [1, 3], "Archer": [2, 2], "Assassin": [1, 3], "Wizard": [3, 1]}
    def __init__(self, name, level = 1):
        if name in Card.warriors.keys():
            self.name = [name]
            self.level = level
            self.health = Card.warriors[name][1] + level
            self.damage = Card.warriors[name][0] + level


    def attack(self, other_card):
        pass

    def use_potion(self):
        pass

    def __repr__(self):
        return f"This level {self.level} warrior named {self.name} has {self.damage} worth of damage and {self.health} HP"

class Spell:
    spells = ["Holy", "Natural", "Fire", "Frost"]

    def __repr__(self):
        pass



print(Card("Paladin", 3))