from bot.main import MusicBot

import discord
from discord.ext import commands


def main(): 
    bot = MusicBot()

    bot.run()


if __name__ == "__main__":
    main()