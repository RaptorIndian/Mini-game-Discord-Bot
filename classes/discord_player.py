from classes import player
Player = player.Player

class Discord_Player(Player):
    """
    The user on Discord interacting with the bot.
    """

    def __init__(self, hand):
        super().__init__("User", hand)

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