import deck, interface

card_dict = {'2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10,
            'J':10, 'Q':10, 'K':10, 'A':(1,11)}

WIN = 0
LOSE = 1
TIE = 2

WIN_VALUE = 21
DEALER_CONDITION = 16   #If equal or lower to condition, dealer draws

class Player():
    """ Player object containing name and hand (list of cards)
        Draw function adds another card to the hand
    """
    def __init__(self, name:str, initial_hand:list):
        self.name = name
        self.hand = initial_hand

    def draw(self, deck:list):
        self.hand.append(deck.pop())

def hand_value(hand:list, ace_value:int = 0) -> int:
    """ Returns int value of a player's hand """
    total = 0
    for cards in hand:
        card = cards[1:]     #Not looking at the suit, only card value
        if card == 'A':
            total += card_dict[card][ace_value]
        else:
            total += card_dict[card]
    return total

def hand_isBust(hand:list) -> bool:
    """ Returns true if hand value is over 21, else false """
    return hand_value(hand) > WIN_VALUE

def best_hand(hand:list) -> int:
    """ Returns the better hand value if player contains an Ace card
        If there is no ace card, basically hand value is returned
    """
    ACE_VALUE_1 = 0
    ACE_VALUE_11 = 1
    hand1 =  hand_value(hand, ACE_VALUE_1)
    hand2 = hand_value(hand, ACE_VALUE_11)
    if hand1 == WIN_VALUE:
        return hand1
    elif hand2 <= WIN_VALUE:
        return hand2
    else:
        return hand1

def user_actions(user, deck:list):
    """ Asks what kind of action the user wants. If the user wants to hit, a card is drawn
        from the deck. If the user BUSTS, turn ends automatically and user loses game.
        Function repeats or recursively calls itself until user stays and returns nothing
    """
    action = interface.userInput_move()
    if action.upper() == 'H':
        user.draw(deck)
        print("Updating hand...")
        interface.print_player_hand(user.name, user.hand)
        if hand_isBust(user.hand):
            interface.print_bust_message(user.name)
            return None
        user_actions(user, deck)

def should_draw(dealer) -> bool:
    """ Checks if dealer should draw a card. True to draw, else false
        Checks if either hand has 21, returning False
        Simply base the AI off of the smallest hand value (Ace value of 1)
    """
    hand = best_hand(dealer.hand)
    if hand == WIN_VALUE:
        return False
    return hand <= DEALER_CONDITION

def dealer_actions(dealer, deck:list):
    """ This function will have the dealer AI keep drawing until above
        the DEALER CONDITION
    """
    while should_draw(dealer):
        print("{} is drawing...".format(dealer.name))
        dealer.draw(deck)
        interface.print_dealer_hand(dealer.name, dealer.hand)
    print("{} is ending turn.".format(dealer.name))

def determine_winner(user, dealer) -> int:
    """ If User wins, return WIN value. If User loses, return Lose value.
        If a tie, return TIE value
    """
    user_best_hand = best_hand(user.hand)
    dealer_best_hand = best_hand(dealer.hand)
    if user_best_hand > dealer_best_hand and user_best_hand <= WIN_VALUE:
        return WIN
    if user_best_hand < dealer_best_hand and dealer_best_hand > WIN_VALUE:
        return WIN
    if user_best_hand > dealer_best_hand and dealer_best_hand <= WIN_VALUE:
        return LOSE
    if user_best_hand < dealer_best_hand and dealer_best_hand <= WIN_VALUE:
        return LOSE
    else:
        return TIE

def print_game_result(result:int):
    """ Prints and end game message depending on the game result """
    if result == WIN:
        print("YOU WIN!!")
    elif result == LOSE:
        print("You Lose... =(")
    else:
        print("TIE GAME!!")

def determine_continue_game() -> bool:
    return interface.userInput_new_game() == 'Y'

def new_game():
    card_deck = deck.create_randomDeck()
    dealer = Player("Dealer", [card_deck.pop(), card_deck.pop()])
    user = Player("You", [card_deck.pop(), card_deck.pop()])
    interface.print_beginning_hands(user.name, user.hand, dealer.name, dealer.hand)
    user_actions(user, card_deck)
    if hand_isBust(user.hand) == False:
        dealer_actions(dealer, card_deck)
    interface.print_reveal_dealer_hand(dealer.name, dealer.hand)
    if hand_isBust(dealer.hand):
        interface.print_bust_message(dealer.name)
    print_game_result(determine_winner(user, dealer))

def main():
    interface.print_welcome_message()
    CONTINUE_PLAYING = True
    while CONTINUE_PLAYING:
        print("Starting new game!")
        new_game()
        CONTINUE_PLAYING = determine_continue_game()
    interface.print_end_message()
    
if __name__ == "__main__":
    main()
