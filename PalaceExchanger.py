

class Player:
    def __init__(self, name ):
        self.name = name
        self.cards = []
        self.health = 5
        self.armor = 0
        self.knocked_out = False
    
    def choose_cards(self):
        while len(self.cards) != 3:
            card = input(f"Choose cards: {Card.warriors}\n")
            if card not in self.cards:
                card = Card(card, player = self)
                self.cards.append(card)
                print(self.cards)
            else:
                print("You already have that card.")
            
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
        return f"{self.name} has {self.health} health and {self.armor} armor. His cards are {[ elem.name for elem in self.cards]}.\n"

class Card:
    warriors = {"Knight": [2, 2], "Paladin": [3, 1], "Berserker": [1, 3], "Archer": [2, 2], "Assassin": [1, 3], "Wizard": [3, 1]}
    
    def __init__(self, name, player, level = 1):

            if name in Card.warriors.keys():
                self.name = name
                self.level = level
                self.damage = Card.warriors[name][0] + level
                self.health = Card.warriors[name][1] + level
                self.player = player
            else:
                print("This hero does not exist.")
                
            

    def removed(self):
        del self
    
    def set_player(self, player):
        self.player = player


    def attack(self, other_card):
        if self.damage > other_card.health:
            if other_card.player.armor > 0:
                other_card.player.lose_armor(self.damage - other_card.health)
            else:
                other_card.player.lose_health(self.damage - other_card.health)  
            other_card.health = 0
            other_card.player.cards.remove(other_card)
            print(f"{other_card.name} got defeated.")          
        else:
            other_card.health -= self.damage

        if other_card.player.knocked_out:
            print(f"{other_card.player.name} got knocked out!")
            
            
    def __repr__(self):
        return f"This level {self.level} warrior named {self.name} has {self.damage} worth of damage and {self.health} HP.\n"


class Game:
    def __init__(self):
        self.gameOver = False
        self.rounds = 0
    
    def newRound(self):
        self.rounds += 1
        print(f"Round {self.rounds} has started.")
    
    def checkWin(self, player1, player2):
        if player1.knocked_out:
            print(f"{player2.name} won!")
            self.gameOver = True
        elif player2.knocked_out:
            print(f"{player1.name} won!")
            self.gameOver = True

    def __repr__(self):
        return f"The game has lasted for {self.rounds} rounds."
    


current_game =  Game()
player1 = Player("John")
player2 = Player("Drake")



players = [player1, player2]


print("\nWelcome to Palace Exchanger!\n")

print("Player 1, choose 3 cards.")
for i in range(3):
    player1.choose_cards()

print("\nPlayer 2, choose your cards.")
for i in range(3):
    player2.choose_cards()

print(player1, player2)

input("Press Enter to start the game.\n")

while not current_game.gameOver:
    print(f"{len(player1.cards)}, and {len(player2.cards)}")   
    current_game.newRound()
    
    try:   
        card1 = int(input(f"{player1.name} choose the index number of the card from your deck to attack\n\nYour Deck:{[card.name for card in player1.cards]}\n"))
        card2 = int(input(f"{player2.name} choose the index number of the card from your deck to attack\n\nYour Deck:{[card.name for card in player2.cards]}\n"))
    except:
        print("You must enter a number.")
        continue

    try:
        player1.cards[card1].attack(player2.cards[card2]) 
        player2.cards[card2].attack(player1.cards[card1])
        print(player1.cards[card1], player2.cards[card2]) 
    except:
        if len(player1.cards) != 3:
            print("Player 1, choose 3 cardss.")
            for i in range(3):
                player1.choose_cards()
                

        if len(player2.cards) != 3:
            print("\nPlayer 2, choose your cards.")
            for i in range(3):
                player2.choose_cards() 
    print(player1, player2)
    print(player1.cards, player2.cards) 

    current_game.checkWin(player1, player2)

    

