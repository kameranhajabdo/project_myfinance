import random

class Pokerdeck:
    def __init__(self):
        numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, "j","q", "k","a"]
        self.cards = {
            "trefla": numbers,
            "inima rosie": numbers,
            "romb": numbers,
            "inima neagra": numbers,
        }
    def get_cards(self, number_of_cards: int):
        cards = []
        for i in range(0, number_of_cards):
            random_colour = random.choice(["trefla", "inima rosie", "romb", "inima neagra"])
            random_number = random.choice(self.cards[random_colour])
            cards.append((random_colour, random_number))
            self.cards[random_colour].remove(random_number)
        return cards

if __name__ = "__main__" :
    deck = Pokerdeck()
    cards = deck.get_cards()