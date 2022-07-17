import discord
import random
import os

# Initialize the bot
client = discord.Client()


@client.event
async def on_ready():
    """ Prints when the bot is ready. """

    print("Logged into Discord successfully!")

# A Go-Fish game.

deck = ["Ace of Hearts", "Ace of Diamonds", "Ace of Clubs", "Ace of Spades", "2 of Hearts", "2 of Diamonds", "2 of Clubs", "2 of Spades", "3 of Hearts", "3 of Diamonds", "3 of Clubs", "3 of Spades", "4 of Hearts", "4 of Diamonds", "4 of Clubs", "4 of Spades", "5 of Hearts", "5 of Diamonds", "5 of Clubs", "5 of Spades", "6 of Hearts", "6 of Diamonds", "6 of Clubs", "6 of Spades", "7 of Hearts", "7 of Diamonds", "7 of Clubs",
        "7 of Spades", "8 of Hearts", "8 of Diamonds", "8 of Clubs", "8 of Spades", "9 of Hearts", "9 of Diamonds", "9 of Clubs", "9 of Spades", "10 of Hearts", "10 of Diamonds", "10 of Clubs", "10 of Spades", "Jack of Hearts", "Jack of Diamonds", "Jack of Clubs", "Jack of Spades", "Queen of Hearts", "Queen of Diamonds", "Queen of Clubs", "Queen of Spades", "King of Hearts", "King of Diamonds", "King of Clubs", "King of Spades"]

# Shuffles the deck.
random.shuffle(deck)


class Discord_User:
    """
    The user on Discord interacting with the bot.
    """

    def __init__(self, hand, matched_cards, play_turn, ask_card, matches):
        self.hand = hand
        self.matched_cards = matched_cards
        self.play_turn = play_turn
        self.ask_card = ask_card
        self.matches = matches

    def play_turn(self):
        """
        The user's turn.
        """

        pass

    def ask_card(self, card):
        """
        The user's decision during their turn.
        """

        pass


def deal_cards(deck):
    """
    Deals cards to the players.
    """

    pass


# Run the bot with the hidden token
client.run(os.environ['token'])
