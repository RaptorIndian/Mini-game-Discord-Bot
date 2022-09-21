import sys

# import our class
sys.path.append('classes')

from classes import game
Game = game.Game

# Spawn a new Game object
instance = Game(("Bot 1", "Bot 2"), (0, 0), 1, True)

# Start the game instance- can be deferred until the discord bot is ready.
instance.start()
