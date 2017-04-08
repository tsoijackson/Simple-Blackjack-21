"""
This file will contain all functions (basically printing functions) for user interface.
"""

def print_welcome_message():
    print("Welcome to Blackjack!!! May the odds be in your favor!")
    print()
    print("INSTRUCTIONS")
    print("------------")
    print("First character stands for the suit.")
    print("Second characters stands for the card.")
    print("Hit = H or h")
    print("Stand/Stay = S or s")
    print()

def print_new_round_message():
    print("New round starting!!!")
    print("Dealer is now dealing cards...")
    print()

def print_end_message():
    print("Game Ending...Goodbye!")

def print_bust_message(name: str):
    print("{} Busted!".format(name))

def print_border(message: str) -> str:
    border = ""
    for char in message:
        border += '-'
    print(border)

def print_player_hand(name:str, hand:list):
    heading = "{} Hand".format(name)
    top = ""; mid = ""; bot = ""
    for card in hand:
        top += "|----| "
        mid += "| {:3}| ".format(card)
        bot += "|----| "
    print(heading)
    print_border(heading)
    print(top + '\n' + mid + '\n' + bot + '\n')

def print_dealer_hand(name:str, hand:list):
    heading = "{} Hand".format(name)
    top = ""; mid = ""; bot = ""
    for card in hand:
        top += "|----| "
        bot += "|----| "
    for card in hand[:-1]:
        mid += "| {:3}| ".format(card)
    mid += "| ?? |"
    print(heading)
    print_border(heading)
    print(top + '\n' + mid + '\n' + bot + '\n')

def print_beginning_hands(user_name:str, user_hand: list,
                          dealer_name:str, dealer_hand: list):
    print("Revealing starting hands...")
    print()
    user_heading = heading = "{} Hand".format(user_name)
    dealer_heading = heading = "{} Hand".format(dealer_name)
    print_dealer_hand(dealer_name, dealer_hand)
    print_player_hand(user_name, user_hand)

def print_reveal_dealer_hand(name:str, hand:list):
    print("Revealing {} hand!!".format(name))
    print_player_hand(name, hand)

def userInput_move() -> str:
    answer = input("What is your move (Hit or Stay) ? ").strip().upper()
    if answer == 'H' or answer == 'S':
        print()
        return answer
    else:
        print("Incorrect input. Please enter only H, h, S, or s.")
        return userInput_move()

def userInput_new_game() -> str:
    answer = input("Would you like to play another round (Y/N)? ").strip().upper()
    if answer == 'Y' or answer == 'N':
        print()
        return answer
    else:
        print("Incorrect input. Pleae enter only Y, y, N, or n.")
        return userInput_new_game()

if __name__ == "__main__":
    print("TESTING FUNCTIONS")
    print("-----------------")
    sample_hand1 = ['D6', 'D10']
    sample_hand2 = ['D6', 'D10', 'D8']
    print_player_hand("Your", sample_hand1)
    print_player_hand("Your", sample_hand2)
    print_dealer_hand("Dealer", sample_hand1)
    print_dealer_hand("Dealer", sample_hand2)
    print_beginning_hands("Your", sample_hand1, "Dealer", sample_hand2)
