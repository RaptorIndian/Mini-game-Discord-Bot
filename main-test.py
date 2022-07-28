import sys

# import our class
sys.path.append('classes')

from classes import game
Game = game.Game

instance = Game(("Bot 1", "Bot 2"), (0, 0), 1, True)

instance.start()