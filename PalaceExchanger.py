class Player:
    def __init__(self, name, cards, spells = 0):
        self.name = name
        self.cards = cards
        self.spells = spells
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

    def lose_armor(self, amount):
        self.armor -= amount

    def lose_health(self, amount):
        self.health -= amount
        if self.health <= 0:
            self.knocked_out = True

    def __repr__(self):
        return f"{self.name} has {self.health} health and {self.armor} armor. His cards are {self.cards} and his spells are {self.spells}."

class Card:
    warriors = {"Knight": [2, 2], "Paladin": [3, 1], "Berserker": [1, 3], "Archer": [2, 2], "Assassin": [1, 3], "Wizard": [3, 1]}
    
    def __init__(self, name, level = 1):
        if name in Card.warriors.keys():
            self.name = name
            self.level = level
            self.health = Card.warriors[name][1] + level
            self.damage = Card.warriors[name][0] + level
            self.player = None

    def assign_player(self, player_):
        if type(player_) is Player:
            self.player = (player_)


    def attack(self, other_card):
        if other_card.player.armor > 0:
            other_card.player.lose_armor(self.damage)
        else:    
            other_card.health -= self.damage

        if other_card.health == 0:
            self.player.cards.remove(other_card)
            print(f"{other_card.name} got defeated.")
        if self.damage > other_card.health:
            if self.player.knocked_out:
                print(f"{self.player.name} got knocked out!")
                return
            other_card.player.lose_health(self.damage - other_card.health)

    def use_potion(self):
        pass

    def __repr__(self):
        return f"This level {self.level} warrior named {self.name} has {self.damage} worth of damage and {self.health} HP"

class Spell:
    spells = ["Holy", "Natural", "Fire", "Frost"]

    def __repr__(self):
        return f"This spell does this and thatz"

player1 = Player("Ebrahim")
player2 = Player("Abdullah")

print(f"Before :{player1}")
print(f"Before :{player2}")
print()


card1 = Card("Knight")
card2 = Card("Archer", 9)
card1.assign_player(player1)
card2.assign_player(player2)

card1.assign_cards()
card2.assign_cards()


card2.attack(card1)
print(card1.player.name)
print(card2.player.name)
print()

print(player1)
print(player2)