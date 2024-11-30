class Card:
    def __init__(self, suit, type, emoji):
        self.suit = suit
        self.type = type
        self.emoji = emoji

    def __repr__(self):
        return f"{self.emoji} ({self.suit}, {self.type})"