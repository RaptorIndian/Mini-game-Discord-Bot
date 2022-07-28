def check_matches(hand):
    match = 0
    state = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    for i in hand:
        state[i["value"] - 1] += 1

    # Only detects the lowest value match-
    # Function must be run multiple times in the rare instance
    # of a multi-matching hand
    for i in range(13):
        if state[i] == 4:
            match = i + 1
            break

    return match

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

    # Test function to verify integrity of hands
    # TODO - delete me
    def hand_test(self):
        print("Hand Test for go Fish Player: " + self.id)
        print(self.hand)
        pass

    # Examine current hand and check if there are any matches
    def process_matches(self):

        # Initiate card match checking loop
        match_indicies = []
        loop = True
        match = 0
        while loop:

            # Return a value for matching cards, if any
            match = check_matches(self.hand)

            # Handle Match if there is a valid value
            if match != 0:

                # Iterate through hand and grab indicies of matching values
                for i in range(len(self.hand)):
                    if self.hand[i]["value"] == match:
                        match_indicies.append(i)

                print(match_indicies)
                # Check for a fatal error- detected match with not enough cards
                if len(match_indicies) != 4:
                    print("uh oh, big problem owo, fatal crash!!!")
                    print("WE DID A FUCKY WUCKY UWU ABORT MISSION!!!")
                    print("boom")
                    # die
                    exit()

                print("Match found! Removing " + str(match) + "s from hand.")

                # Update Match array and remove matched cards from hand
                self.matched_cards.append(match)
                for i in match_indicies[::-1]:
                    del self.hand[i]

                # Continue loop before exiting scope to check for additional matches
                # There are rare edge cases where this matters
                continue

            # No Match found- fallthrough kills the loop
            loop = False

    # TODO optimize this mess
    def ask_card(self, card):
        matches = []
        output = []

        # Find cards in hand matching value
        for i in range(len(self.hand)):
            if self.hand[i]["value"] == card:
                matches.append(i)

        # Update hand and get cards if matched
        if len(matches) > 0:
            for i in matches:
                output.append(self.hand[i])
            for i in matches[::-1]:
                del self.hand[i]

        return output

    def draw(self, card):
        self.hand.append(card)

    def empty_hand(self):
        return len(self.hand) == 0

    def total_matches(self):
        return len(self.matched_cards)