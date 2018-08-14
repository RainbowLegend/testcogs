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
    @commands.has_any_role("Senior Moderator", "Moderator", "Administrator", "Game Night Moderator")
    async def togglehost(self, ctx):
        author = ctx.message.author
        localRoleAdmin = discord.Role(id='414196360321957888', server='288455332173316106')
        localRoleSeniorMod = discord.Role(id='414189641890267157', server='288455332173316106')
        localRoleMod = discord.Role(id='414196360321957888', server='288455332173316106')
        administrator = discord.Role(id='288457272663867392', server='288455332173316106')
        seniorModerator = discord.Role(id='288464565791096838', server='288455332173316106')
        moderator = discord.Role(id='288682024515141634', server='288455332173316106')

        # Checks to find which role in the hierarchy they need

        if moderator in author.roles:  #  If they are a Moderator...
            localRole = localRoleMod
        elif seniorModerator in author.roles: #  If they are a Senior Mod...
            localRole = localRoleSeniorMod
        elif administrator in author.roles:
            localRole = localRoleAdmin
        else:
            return

        if localRole in author.roles:  #  If the hosting role is in the author
            await self.bot.remove_roles(author, localRole)  # Remove the role
            await self.bot.say('Successfully removed the Hosting role.')
        else:  # If the hosting role not in the author
            await self.bot.add_roles(author, localRole)  # Add the role
            await self.bot.say('Successfully added the Hosting role.')
        



def setup(bot):
    n = Nerd(bot)
    bot.add_cog(n)     
