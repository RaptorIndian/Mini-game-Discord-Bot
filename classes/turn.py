class Turn:
    def __init__(self, turnid, player, asked, cards):

        # Number of Unique Turns so far
        self.id = turnid # Number of Unique Turns so far
        
        # Integer determining which player performed this turn
        # 0 = CPU
        # 1 = User
        self.player = player

        # The value asked for by the player
        self.asked = asked

        # The cards exchanged on this turn
        self.cards = cards