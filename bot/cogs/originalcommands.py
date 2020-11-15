import discord
import random
from discord.ext import commands

class OGCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command(brief="Original Commands")
    async def ping(self, ctx):
        await ctx.send(f'Pong! {round(self.bot.latency * 1000)}ms')

   
    @commands.command(brief="Original Commands")
    async def Reading(self, ctx):
        await ctx.send("Reading is a skill you need to maintain even after leaving school. A lot of information is available to those that read. If you read, you don't have to ask questions that have been answered a thousand times, and you can be more self-sufficient. It's a great way to enrich your life.")

    @commands.command(aliases=['ban'], brief="Original Commands")
    async def banhammer(self, ctx):
        await ctx.send("https://tenor.com/view/banhammer-bongocat-gif-12967526")

    @commands.command(brief="Original Commands")
    async def deleted(self, ctx):
        await ctx.send("https://gfycat.com/magnificenthiddenafricanpiedkingfisher")

        

def setup(bot):
    bot.add_cog(OGCommands(bot))
