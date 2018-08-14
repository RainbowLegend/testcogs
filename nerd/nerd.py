import discord
from discord.ext import commands
from cogs.utils import checks
from cogs.utils.dataIO import dataIO
from cogs.utils.chat_formatting import box, pagify
from copy import deepcopy
from collections import defaultdict
import asyncio
import logging
import logging.handlers
import random
import os
import datetime
import re
from datetime import datetime

class Nerd:
    """Host commands"""

    default = {}

    def __init__(self, bot):
        db = dataIO.load_json("data/selftosroles/roles.json")
        self.bot = bot
        self.db = defaultdict(lambda: default.copy(), db)
        
    @commands.command()
    async def newCommand(self):
        await self.bot.say("Hello World!")
        
    @commands.command(pass_context=True)
    @commands.has_any_role()
    async def commandTwo(self, ctx, nume: int):
        if nume == 69:
            await self.bot.say("lol gay")
            elif nume == 54
            await self.bot.say("dan likes dick lol")
        
        



def setup(bot):
    n = Nerd(bot)
    bot.add_cog(n)     
