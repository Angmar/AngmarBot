import discord
from discord.ext import commands
from discord.ext.commands import Cog
from discord.ext.commands import command


class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @Cog.listener()
    async def on_member_join(self, member):
        guild = member.guild
        if guild.system_channel is not None:
            to_send = 'Welcome to **{1.name}**  {0.mention}! We hope you enjoy your time here!'.format(member, guild)
            await guild.system_channel.send(to_send)

    @Cog.listener()
    async def on_member_leave(self, member):
        pass



def setup(bot):
    bot.add_cog(Help(bot))