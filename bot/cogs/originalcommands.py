import discord
import random
from discord.ext import commands
from discord.ext.commands import command, cooldown, BucketType, Cog

class OGCommands(Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @command(brief="Original Commands")
    @cooldown(1, 20, BucketType.guild)
    async def ping(self, ctx):
        await ctx.send(f'Pong! {round(self.bot.latency * 1000)}ms')

   
    @command(brief="Original Commands")
    @cooldown(1, 20, BucketType.guild)
    async def Reading(self, ctx):
        await ctx.send("Reading is a skill you need to maintain even after leaving school. A lot of information is available to those that read. If you read, you don't have to ask questions that have been answered a thousand times, and you can be more self-sufficient. It's a great way to enrich your life.")

    @command(aliases=['ban'], brief="Original Commands")
    @cooldown(1, 20, BucketType.guild)
    async def banhammer(self, ctx):
        await ctx.send("https://tenor.com/view/banhammer-bongocat-gif-12967526")

    @command(brief="Original Commands")
    @cooldown(1, 20, BucketType.guild)
    async def deleted(self, ctx):
        await ctx.send("https://gfycat.com/magnificenthiddenafricanpiedkingfisher")

    @command(brief="Original Commands")
    @cooldown(1, 20, BucketType.guild)
    async def Midnight(self, ctx):
        await ctx.send("Did someone mention Midnight? Oh god, here we go again...")

    @command(brief="Original Commands")
    @cooldown(1, 20, BucketType.guild)
    async def music(self, ctx):
        await ctx.send("https://www.youtube.com/watch?v=cpGqFko9veQ&list=PLDm6rOZCtmHkT8DUdUzGOZYB4VCRWIcQB")

    @command(brief="Original Commands")
    async def Ryan(self, ctx):
        await ctx.send("Ryan is big gay")

    @command(brief="Original Commands")
    @cooldown(1, 20, BucketType.guild)
    async def JD(self, ctx):
        await ctx.send(":cake: :cake:")

    @command(brief="Original Commands")
    @cooldown(1, 20, BucketType.guild)
    async def Grant(self, ctx):
        await ctx.send("Grant is big thiccqq")

    @command(brief="Original Commands")
    @cooldown(1, 20, BucketType.guild)
    async def Evan(self, ctx):
        await ctx.send("Evan is big sexy")

    @command(brief="Original Commands")
    @cooldown(1, 20, BucketType.guild)
    async def Evanmeme(self, ctx):
        await ctx.send("https://imgur.com/6U8QqjD")

    @command(brief="Original Commands")
    @cooldown(1, 20, BucketType.guild)
    async def Nate(self, ctx):
        await ctx.send("Fine, I added in a command for you. Happy?")

    @command(brief="Original Commands")
    @cooldown(1, 20, BucketType.guild)
    async def Yesinia(self, ctx):
        await ctx.send("https://cdn.discordapp.com/attachments/739057929642311712/764533940915535942/Screenshot_20201009-135347_Google.jpg")

    @command(brief="Original Commands")
    @cooldown(1, 20, BucketType.guild)
    async def Hershel(self, ctx):
        await ctx.send("https://cdn.discordapp.com/attachments/722805149235413023/764538512241590282/image0.jpg")
    
    @command(brief = "Soup")
    @cooldown(1, 20, BucketType.guild)
    async def Soup(self, ctx):
        await ctx.send("https://cdn.discordapp.com/attachments/739057929642311712/788500402252808192/Screenshot_37.png")

        

def setup(bot):
    bot.add_cog(OGCommands(bot))