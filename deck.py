import random
"""
GLOBAL VARIABLES CREATED THAT CAN BE USABLE
-----------------------------------------------
SUIT_TYPES = tuple of char of suit types in order


FUNCTIONS THAT CAN BE USUABLE
-----------------------------
create_orderedDeck(): return tuple of str representing cards
create_randomDeck(): returns tuple of str representing cards
print_deck(): Prints out a deck tuple in a readable format
"""

#CREATING SUIT_TYPES
SUIT_TYPES = ('D', 'C', 'H', 'S')

#CREATING CARD_TYPES
def create_CARD_TYPES():
    result = []
    for int in range(2,11):
        result.append(str(int))
    for letter in ('J', 'Q', 'K', 'A'):
        result.append(letter)
    return tuple(result)

def create_orderedDeck():
    deck = []
    for suit in SUIT_TYPES:
        for card in create_CARD_TYPES():
            deck.append(suit + card)
    return deck

def create_randomDeck():
    deck = create_orderedDeck()
    random.shuffle(deck)
    return deck

def print_deck(deck:tuple):
    row = 0
    while row < 4:
        string = ""
        index = row * 13
        for i in range(13):
            string += str(deck[index + i]) + ' '
        print(string)
        row += 1

if __name__ == "__main__":
    print("SUIT_TYPES: {}".format(SUIT_TYPES))
    print("CARD_TYPES: {}".format(create_CARD_TYPES()))
    print("create_orderedDeck():")
    print_deck(create_orderedDeck())
    print("create_randomDeck():")
    print_deck(create_randomDeck())
