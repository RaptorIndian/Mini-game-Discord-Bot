from classes import player, turn
Player = player.Player
Turn = turn.Turn
import random

# Easy Turn AI
def easy_turn(other, hand):
    options = []

    # Create an unweighted option space
    for i in hand:
        if i["value"] in options:
            continue
        options.append(i["value"])
    
    # Randomly select card from options
    card = random.choice(options)
    
    # Ask for the card and get the returned cards if any
    returned_cards = other.ask_card(card)
    
    # return the guess and the result to calling context
    return (card, returned_cards)

# TODO
def normal_turn(other, hand, history):
    options = {}

    # Created a weighted option space
    for i in hand:
        if options[str(i["value"])]:
            options[str(i["value"])] += float(1)
            continue
        options[str(i["value"])] = float(1)

    # Look through 8 most recent turns


# TODO
def hard_turn(other, hand, history):
    pass

class Computer_Player(Player):

    def __init__(self, playerid, hand, difficulty):
        super().__init__(playerid, hand)

        # Controller for the difficulty level of the AI
        # 1 = Easy
        # 2 = Normal
        # 3 = Hard
        # See AI.md for a detailed breakdown on difficulty
        self.difficulty = difficulty

    def play_turn(self, other, history, count, diff_override = 0):
        difficulty = diff_override or self.difficulty

        print("It is " + self.id + "'s turn")

        # Tuple containing the resulting data from AI turn
        result = (0, [])

        # Run the proper choice logic
        if difficulty == 1:
            result = easy_turn(other, self.hand)
        elif difficulty == 2:
            result = normal_turn(other, self.hand, history)
        elif difficulty == 3:
            result = hard_turn(other, self.hand, history)

        print(self.id + " selected: " + str(result[0]))

        # Update hand if a guess successfully returned cards
        if len(result[1]) > 0:
            for i in result[1]:
                print(other.id + " gives a " + i["text"] + " to " + self.id)
                self.hand.append(i)
        else:
            print("go fish...")

        # Generate a Turn object based on the results of this turn
        return Turn(count, 0, result[0], result[1])

