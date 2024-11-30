from src.projects.hanafuda.Deck import Deck


def calculate_score(cards):
    score = 0
    for card in cards:
        if card.type == "Bright":
            score += 20
        elif card.type == "Animal":
            score += 10
        elif card.type == "Ribbon":
            score += 5
        elif card.type == "Chaff":
            score += 1
    return score


class HanafudaGame:
    def __init__(self):
        self.deck = Deck()
        self.players = [[], []]  # Two players
        self.scores = [0, 0]

    def deal_cards(self):
        for _ in range(8):  # Deal 8 cards to each player
            for player in self.players:
                player.append(self.deck.draw_card())

    def play_game(self):
        self.deal_cards()
        for i, player_cards in enumerate(self.players):
            print(f"Player {i + 1}'s hand: {player_cards}")
            score = calculate_score(player_cards)
            self.scores[i] = score
            print(f"Player {i + 1}'s score: {score}")

