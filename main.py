from classes import game
from dotenv import load_dotenv
import discord
import os
from discord.ext import commands

Game = game.Game
load_dotenv()


class MyBot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix='!',
                         intents=discord.Intents.all(), application_id=os.getenv('app_id'))

    async def setup_hook(self):
        await self.load_extension(f'cogs.test')
        # TODO: get guild id from the bot's guilds list.
        await bot.tree.sync(guild=discord.Object(id=931002849628930048))

    async def on_ready(self):
        print(f'{self.user} has connected to Discord!')


bot = MyBot()


# Creates a new instance of the Game class
instance = Game(("Bot 1", "Bot 2"), (0, 0), 1, True)

# Call the start method on the instance
instance.start()


bot.run(os.getenv("token"))
