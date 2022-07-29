from secrets import choice
import discord
from discord.ext import commands


class test(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @discord.app_commands.describe(name="Your name", description="Your age")
    @discord.app_commands.choices(age=[Choice(name="Age", value=1), Choice(name="Age", value=2), Choice(name="Age", value=3)])
    @discord.app_commands.command(name='introduce', description='Introduce yourself!')
    async def introduce(self, interaction: discord.Interaction, name: str, age: int):
        await interaction.send(f'Hello, {name}! I am {self.bot.user} and I am {age} years old.')

    async def setup(bot: commands.Bot) -> None:
        await bot.add_cog(test(bot), guilds=[discord.Object(id=931002849628930048)])
