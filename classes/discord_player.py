from classes import player, turn
Player = player.Player
Turn = turn.Turn
from util import stringify

# Take an input from the player and determine if this is a legal guess to make
def validate_input(card, hand):
    valid = False
    if card != 0:
        for i in hand:
            if i["value"] == card:
                valid = True
                break;
    return valid

# Use discord API to register an input for the game
# TODO - Waiting on Rapta's discord implementation
def get_input():
    return True

# Test method for getting input pre-discord integration
def get_input_test(hand):
    handarr = []
    for i in hand:
        handarr.append(i["text"])
    print("Current hand: " + stringify(", ", handarr))
    output = 0
    while output == 0:
        try:
            output = int(input("Select a Card: "))
        except:
            print("Invalid selection. Input must be a number.")
    return output
    

class Discord_Player(Player):
    """
    The user on Discord interacting with the bot.
    """

    def __init__(self, playerid, hand):
        super().__init__(playerid, hand)

    # Bad practice, but turns is unused and only included
    # to keep a consistent function signature
    def play_turn(self, other, turns, count):
        print("It is " + self.id + "'s turn")

        # Prompt the user to select a card to guess until they input a valid move
        # TODO - switch this over to using the discord-integrated get_input method
        card = 0
        while validate_input(card, self.hand) == False:
            #card = get_input()
            card = get_input_test(self.hand)

        # Ask the other player if they have this card and get the matched cards, if any
        returned_cards = other.ask_card(card)

        print(self.id + " selected: " + str(card))

        # If cards were given to us from the other player, add them to our hand
        if len(returned_cards) > 0:
            for i in returned_cards:
                print(other.id + " gives a " + i["text"] + " to " + self.id)
                self.hand.append(i)
        else:
            print("go fish...")

        # Generate a Turn object based on what happened this turn
        return Turn(count, 1, card, returned_cards)
