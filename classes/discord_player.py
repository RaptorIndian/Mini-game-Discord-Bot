from util import stringify
from classes import player, turn
Player = player.Player
Turn = turn.Turn

# Take an input and verify that its a valid move


def validate_input(card, hand):
    valid = False
    if card != 0:
        for i in hand:
            if i["value"] == card:
                valid = True
                break
    return valid

# Use discord API to register an input for the game
# TODO


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

        card = 0
        while validate_input(card, self.hand) == False:
            #card = get_input()
            card = get_input_test(self.hand)

        returned_cards = other.ask_card(card)

        print(self.id + " selected: " + str(card))

        if len(returned_cards) > 0:
            for i in returned_cards:
                print(other.id + " gives a " + i["text"] + " to " + self.id)
                self.hand.append(i)
        else:
            print("go fish...")

        return Turn(count, 1, card, returned_cards)
