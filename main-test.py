from classes import game
import discord
from dotenv import load_dotenv

Game = game.Game

instance = Game(("Bot 1", "Bot 2"), (0, 0), 1, True)

instance.start()

# The above code can be explained as:
# 1. Create a new instance of the Game class
# 2. Pass in the names of the players and the number of cards each player should have
# 3. Call the start method on the instance
