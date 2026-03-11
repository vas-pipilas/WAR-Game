"""
WAR Card Game Engine
An automated simulation of the classic 'War' card game, 
demonstrating logic flow and object-oriented deck management.
"""

import random

# Global Constants
SUITS = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
RANKS = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
VALUES = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':14}

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = VALUES[rank]

    def __str__(self):
        return f"{self.rank} of {self.suit}"

class Deck:
    def __init__(self):
        self.all_cards = [Card(suit, rank) for suit in SUITS for rank in RANKS]

    def shuffle(self):
        random.shuffle(self.all_cards)

    def deal_one(self):
        return self.all_cards.pop()

class Player:
    def __init__(self, name):
        self.name = name
        self.all_cards = []

    def remove_one(self):
        """Removes the top card from the player's hand."""
        return self.all_cards.pop(0)

    def add_cards(self, new_cards):
        """Adds won cards to the bottom of the player's deck."""
        if isinstance(new_cards, list):
            self.all_cards.extend(new_cards)
        else:
            self.all_cards.append(new_cards)

    def __str__(self):
        return f'Player {self.name} has {len(self.all_cards)} cards.'

# --- Game Simulation Logic ---

def play_war():
    # Setup
    player_one = Player("One")
    player_two = Player("Two")
    
    deck = Deck()
    deck.shuffle()

    # Split the deck
    for x in range(26):
        player_one.add_cards(deck.deal_one())
        player_two.add_cards(deck.deal_one())

    game_on = True
    round_num = 0
    
    while game_on:
        round_num += 1
        
        # Win Condition Check
        if len(player_one.all_cards) == 0:
            print(f"Player One out of cards! Player Two Wins in {round_num} rounds.")
            game_on = False
            break
        if len(player_two.all_cards) == 0:
            print(f"Player Two out of cards! Player One Wins in {round_num} rounds.")
            game_on = False
            break

        # Start a new round
        p1_cards = [player_one.remove_one()]
        p2_cards = [player_two.remove_one()]

        at_war = True
        while at_war:
            if p1_cards[-1].value > p2_cards[-1].value:
                player_one.add_cards(p1_cards)
                player_one.add_cards(p2_cards)
                at_war = False
            elif p2_cards[-1].value > p1_cards[-1].value:
                player_two.add_cards(p1_cards)
                player_two.add_cards(p2_cards)
                at_war = False
            else:
                print(f"WAR! Round {round_num}")
                # Tie condition: Check if players have enough cards to wage war
                if len(player_one.all_cards) < 5:
                    print("Player One unable to play war! Player Two wins.")
                    game_on = False
                    break
                elif len(player_two.all_cards) < 5:
                    print("Player Two unable to play war! Player One wins.")
                    game_on = False
                    break
                else:
                    # Draw 5 cards for the war sacrifice
                    for num in range(5):
                        p1_cards.append(player_one.remove_one())
                        p2_cards.append(player_two.remove_one())

if __name__ == "__main__":
    play_war()
