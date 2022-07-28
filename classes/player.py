class Player:
    """
    Player base class
    """

    def __init__(self, playerid, hand):
        # Player ID
        self.id = playerid

        # Cards in hand
        self.hand = hand

        # Sets of cards that have been matched from the hand
        self.matched_cards = []

    def hand_test(self):
        print("Hand Test for go Fish Player: " + self.id)
        print(self.hand)
        pass