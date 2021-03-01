import discord
from discord.ext.commands import command, Cog
import typing as t
from ..db import db

class Channel(Cog):
    def __init__(self, bot):
        self.bot = bot
    

    @command()
    async def Starboard(self, ctx):
        guild = ctx.message.guild
        sb = await guild.create_text_channel("Starboard")
        db.execute("UPDATE channels SET DefaultStarboardChannelID = ?, StarboardChannelID = ? WHERE GuildID =?", sb.id, sb.id, guild.id)
        
        await ctx.send(f"Starboard Channel set to {sb.mention}")
    
def setup(bot):
    bot.add_cog(Channel(bot))

