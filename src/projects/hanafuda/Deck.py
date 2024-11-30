import random

from src.projects.hanafuda.Card import Card


class Deck:
    def __init__(self):
        self.cards = self.create_deck()
        random.shuffle(self.cards)

    def create_deck(self):
        suits = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
                 "November", "December"]
        types = ["Bright", "Animal", "Ribbon", "Chaff"]
        emojis = ["🌕", "🐦", "🎀", "🍂"]
        deck = []
        for suit in suits:
            for i in range(4):
                deck.append(Card(suit, types[i % 4], emojis[i % 4]))
        return deck

    def draw_card(self):
        return self.cards.pop() if self.cards else None
