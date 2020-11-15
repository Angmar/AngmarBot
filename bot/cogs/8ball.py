import discord
import random
import datetime as dt
from discord.ext import commands
from typing import Optional
from discord.ext.commands import Cog
from discord.ext.commands import command
from discord.utils import get
from discord.ext import menus

class _8ball(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['8ball'], brief="Eight Ball")
    async def _8ball(self, ctx, *, question):
        """Ask a Question and the bot will automatically respond with a random answer."""
        responses = ["It is certain.",
                    "It is decidedly so.",
                    "Without a doubt.",
                    "Yes - definitely.",
                    "You may rely on it.",
                    "As I see it, yes.",
                    "Most likely.",
                    "Outlook good.",
                    "Yes.",
                    "Signs point to yes.",
                    "Reply hazy, try again.",
                    "Ask again later.",
                    "Better not tell you now.",
                    "Cannot predict now.",
                    "Concentrate and ask again.",
                    "Don't count on it.",
                    "My reply is no.",
                    "My sources say no.",
                    "Outlook not so good.",
                    "Very doubtful."]

        embed = discord.Embed(
            title="8 Ball",
            description=(f'Question: {question}\nAnswer: {random.choice(responses)}')
            ,
            color=ctx.author.color,
            timestamp=dt.datetime.utcnow()
        )
        embed.set_footer(text=f"Invoked by {ctx.author.display_name}", icon_url=ctx.author.avatar_url)  
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(_8ball(bot))

