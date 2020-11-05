from random import randint
SUITS = ["Hearts","Spades","Clubs","Diamonds"]
RANKS = ["1","2","3","4","5","6","7","8","9","10", "Jack","Queen","King","Ace"]
cardpile = []
class Card:
    def __init__(self, value, kind):
        self.value = value
        self.kind = kind
    def __repr__(self):
        return "{} {}".format(self.value, self.kind)
    def addcard(self):
        randsuit = randint(0, 3)
        randrank = randint(0,13)
        cardpile.append(RANKS[randrank]+SUITS[randsuit])


print(cardpile)