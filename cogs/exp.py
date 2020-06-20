import os
import r
from discord.ext import commands
import discord
import random
import asyncio

class jgame(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

def setup(bot):
    bot.add_cog(jgame(bot))
