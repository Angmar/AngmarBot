import discord
from discord.ext import commands
from datetime import datetime
from typing import Optional
from discord.ext.commands import Cog
from discord.ext.commands import command
from discord import Embed, Member
from discord.ext.commands import when_mentioned_or, command, has_permissions
from discord.ext.commands import CheckFailure


from ..db import db

class gamer(Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @command(name="prefix", brief="Adminstrative commands")
    @has_permissions(manage_guild=True)
    async def change_prefix(self, ctx, new: str):
        """Changes the prefix of the bot. must have Manage server permissions to change."""
        if len(new) > 5:
            await ctx.send("The prefix can not be more than 5 characters in length.")
            
        else:
            db.execute("UPDATE guilds SET Prefix = ? WHERE GuildID = ?", new, ctx.guild.id)
            await ctx.send(f"Prefix set to {new}")
            
    @change_prefix.error
    async def change_prefix_error(self, ctx, exc):
        if isinstance(exc, CheckFailure):
            await ctx.send("You need the Manage Server permission to do that.")


def setup(bot):
    bot.add_cog(gamer(bot))