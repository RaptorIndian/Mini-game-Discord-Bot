import random
from classes import discord_player
from classes import computer_player
from classes import turn

Discord_Player = discord_player.Discord_Player
Computer_Player = computer_player.Computer_Player
Turn = turn.Turn


class Game:

    base_deck = [{'value': 1, 'suit': 'Hearts', 'text': 'Ace of Hearts'}, {'value': 1, 'suit': 'Diamonds', 'text': 'Ace of Diamonds'}, {'value': 1, 'suit': 'Clubs', 'text': 'Ace of Clubs'}, {'value': 1, 'suit': 'Spades', 'text': 'Ace of Spades'}, {'value': 2, 'suit': 'Hearts', 'text': '2 of Hearts'}, {'value': 2, 'suit': 'Diamonds', 'text': '2 of Diamonds'}, {'value': 2, 'suit': 'Clubs', 'text': '2 of Clubs'}, {'value': 2, 'suit': 'Spades', 'text': '2 of Spades'}, {'value': 3, 'suit': 'Hearts', 'text': '3 of Hearts'}, {'value': 3, 'suit': 'Diamonds', 'text': '3 of Diamonds'}, {'value': 3, 'suit': 'Clubs', 'text': '3 of Clubs'}, {'value': 3, 'suit': 'Spades', 'text': '3 of Spades'}, {'value': 4, 'suit': 'Hearts', 'text': '4 of Hearts'}, {'value': 4, 'suit': 'Diamonds', 'text': '4 of Diamonds'}, {'value': 4, 'suit': 'Clubs', 'text': '4 of Clubs'}, {'value': 4, 'suit': 'Spades', 'text': '4 of Spades'}, {'value': 5, 'suit': 'Hearts', 'text': '5 of Hearts'}, {'value': 5, 'suit': 'Diamonds', 'text': '5 of Diamonds'}, {'value': 5, 'suit': 'Clubs', 'text': '5 of Clubs'}, {'value': 5, 'suit': 'Spades', 'text': '5 of Spades'}, {'value': 6, 'suit': 'Hearts', 'text': '6 of Hearts'}, {'value': 6, 'suit': 'Diamonds', 'text': '6 of Diamonds'}, {'value': 6, 'suit': 'Clubs', 'text': '6 of Clubs'}, {'value': 6, 'suit': 'Spades', 'text': '6 of Spades'}, {'value': 7, 'suit': 'Hearts', 'text': '7 of Hearts'}, {'value': 7, 'suit': 'Diamonds', 'text': '7 of Diamonds'}, {'value': 7, 'suit': 'Clubs', 'text': '7 of Clubs'}, {'value': 7, 'suit': 'Spades', 'text': '7 of Spades'}, {'value': 8, 'suit': 'Hearts', 'text': '8 of Hearts'}, {'value': 8, 'suit': 'Diamonds', 'text': '8 of Diamonds'}, {'value': 8, 'suit': 'Clubs', 'text': '8 of Clubs'}, {'value': 8, 'suit': 'Spades', 'text': '8 of Spades'}, {'value': 9, 'suit': 'Hearts', 'text': '9 of Hearts'}, {'value': 9, 'suit': 'Diamonds', 'text': '9 of Diamonds'}, {'value': 9, 'suit': 'Clubs', 'text': '9 of Clubs'}, {'value': 9, 'suit': 'Spades', 'text': '9 of Spades'}, {'value': 10, 'suit': 'Hearts', 'text': '10 of Hearts'}, {'value': 10, 'suit': 'Diamonds', 'text': '10 of Diamonds'}, {'value': 10, 'suit': 'Clubs', 'text': '10 of Clubs'}, {'value': 10, 'suit': 'Spades', 'text': '10 of Spades'}, {'value': 11, 'suit': 'Hearts', 'text': 'Jack of Hearts'}, {'value': 11, 'suit': 'Diamonds', 'text': 'Jack of Diamonds'}, {'value': 11, 'suit': 'Clubs', 'text': 'Jack of Clubs'}, {'value': 11, 'suit': 'Spades', 'text': 'Jack of Spades'}, {'value': 12, 'suit': 'Hearts', 'text': 'Queen of Hearts'}, {'value': 12, 'suit': 'Diamonds', 'text': 'Queen of Diamonds'}, {'value': 12, 'suit': 'Clubs', 'text': 'Queen of Clubs'}, {'value': 12, 'suit': 'Spades', 'text': 'Queen of Spades'}, {'value': 13, 'suit': 'Hearts', 'text': 'King of Hearts'}, {'value': 13, 'suit': 'Diamonds', 'text': 'King of Diamonds'}, {'value': 13, 'suit': 'Clubs', 'text': 'King of Clubs'}, {'value': 13, 'suit': 'Spades', 'text': 'King of Spades'}]
    
    def __init__(self, names, controller = (1,0), difficulty = 1, debug = False):

        # Gameloop controller
        self.active = True

        # Which player is performing a turn
        self.active_player = 0 # Initialized at Game.start

        # Current Unique Turn ID
        self.counter = 0
        
        # Array of previously completed turns
        self.turns = []

        # Game Difficulty
        self.difficulty = difficulty

        # Debug log controller
        self.debug = debug

        # Initialize Deck for game Instance
        random.shuffle(Game.base_deck) # Consider replacing
        self.deck = Game.base_deck

        # Initialize starting hands
        hands = [[],[]]
        for i in range(2):
            hands[i] += self.deck[0:7]
            self.deck = self.deck[7:]

        # Spawn Player instances
        for i in range(2):
            self.__dict__["p" + str(i + 1)] = (Computer_Player(names[i], hands[i], self.difficulty), Discord_Player(names[i], hands[i])) [controller[i] == 1]

    def start(self):
        # Winner variable, to be updated in game loop
        winner = None

        # Determine who goes first
        self.active_player = (1,0) [random.random() * 2 > 1]

        # Initialize a turn buffer
        turn = None

        # Result of the guess
        draw = None

        # Player object performing this turn's actions
        target = None
        other = None

        # Start Gameloop
        while self.active:

            print("\n\nTurn " + str(self.counter))

            # Player 1 Turn
            if self.active_player == 1:
                target = self.p1
                other = self.p2

            # Player 2 Turn
            else:
                target = self.p2
                other = self.p1

            # Check hand of player and prompt a draw if no cards
            if target.empty_hand() and self.deck:
                print(target.id + " has no cards and draws a " + self.deck[0]["text"])
                target.draw(self.deck.pop(0))

            # Check winstate
            if target.empty_hand() and other.empty_hand() and len(self.deck) == 0:
                winner = (other, target) [target.total_matches() > other.total_matches()]
                print(winner.id + " Wins!!!")
                print("Score: " + target.id + ": " + str(target.total_matches()) + " to " + other.id + ": " + str(other.total_matches()))
                self.active = False
                break

            # Play turn
            if target.empty_hand() == False:
                turn = target.play_turn(other, self.turns, self.counter)
                draw = len(turn.cards) == 0

                # Draw if "Go Fish"
                if draw and self.deck:
                    print(target.id + " draws a " + self.deck[0]["text"])
                    target.draw(self.deck.pop(0))

                target.process_matches()
            else:
                turn = Turn(self.counter, target, 0, [])


            # Update Turn controls
            self.turns.append(turn)
            self.counter += 1

            # Flip the Active Player bit if theres no match
            if draw:
                self.active_player ^= 1

