import discord
import random
import datetime as dt
from discord.ext import commands, tasks
from typing import Optional
from discord.ext.commands import Cog
from discord.ext.commands import command
from discord.utils import get
from discord.ext import menus
import os
import asyncio
from asyncio import gather


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

        
    @command(brief="fun")
    async def conversation(self, ctx):
        embed = discord.Embed(
            title="How To Mute A Discord Server",
            description=("**On Mobile**: \n1) Click the three dots at the top \n2) Click Notifications \n3) Click Mute Servername \n4) Click until I turn it back on \n**On PC** \n1) Right Click the Server Icon and Hover over Mute Server \n2) Click Until I Turn it back on"),
            color=ctx.author.color
        )
        await ctx.send(embed=embed)

    @command(aliases=["rps"], brief="fun")
    async def bored(self, ctx, user_choice):
        rpsGame = ['rock', 'paper', 'scissors']
        if user_choice in rpsGame: 
            embed=discord.Embed(
                title = "Rock, Paper, Scissors",
                description = f"Your Choice: **{user_choice}**\nMy Choice: **{random.choice(rpsGame)}**",
                color=ctx.author.color,
                timestamp=dt.datetime.utcnow()
            )
            embed.set_footer(text=f'Invoked by {ctx.author.display_name}', icon_url=ctx.author.avatar_url)
            await ctx.send(embed=embed)
        elif user_choice not in rpsGame:
            await ctx.send("Please use either rock, paper or scissors") 
def setup(bot):
    bot.add_cog(_8ball(bot))

