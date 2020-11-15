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

    @commands.command(brief="Original Commands")
    async def Midnight(self, ctx):
        await ctx.send("Did someone mention Midnight? Oh god, here we go again...")

    @commands.command(brief="Original Commands")
    async def music(self, ctx):
        await ctx.send("https://www.youtube.com/watch?v=cpGqFko9veQ&list=PLDm6rOZCtmHkT8DUdUzGOZYB4VCRWIcQB")

    @commands.command(brief="Original Commands")
    async def Ryan(self, ctx):
        await ctx.send("Ryan is big gay")

    @commands.command(brief="Original Commands")
    async def JD(self, ctx):
        await ctx.send(":cake: :cake:")

    @commands.command(brief="Original Commands")
    async def Grant(self, ctx):
        await ctx.send("Grant is big thiccqq")

    @commands.command(brief="Original Commands")
    async def Evan(self, ctx):
        await ctx.send("Evan is big sexy")

    @commands.command(brief="Original Commands")
    async def Evanmeme(self, ctx):
        await ctx.send("https://imgur.com/6U8QqjD")

    @commands.command(brief="Original Commands")
    async def Nate(self, ctx):
        await ctx.send("Fine, I added in a command for you. Happy?")

    @commands.command(brief="Original Commands")
    async def Yesinia(self, ctx):
        await ctx.send("https://cdn.discordapp.com/attachments/739057929642311712/764533940915535942/Screenshot_20201009-135347_Google.jpg")

    @commands.command(brief="Original Commands")
    async def Hershel(self, ctx):
        await ctx.send("https://cdn.discordapp.com/attachments/722805149235413023/764538512241590282/image0.jpg")

    @commands.command()
    async def T(self, ctx):
        await ctx.send("<@!401351573462188034>")

        

def setup(bot):
    bot.add_cog(OGCommands(bot))