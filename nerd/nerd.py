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



def setup(bot):
    n = Hosting(bot)
    bot.add_cog(n)     
