import discord
import random
import os

# Initialize the bot
client = discord.Client()


@client.event
async def on_ready():
    """ Prints when the bot is ready. """

    print("Logged into Discord successfully!")


# More code goes here!


# Run the bot with the hidden token
client.run(os.environ['token'])
