from pathlib import Path

import discord
from discord import Intents
import asyncio
from discord.ext import commands
from asyncio import sleep
from datetime import datetime
from glob import glob
import wavelink
from ..db import db


from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger
from discord import Embed, File, DMChannel
from discord.errors import HTTPException, Forbidden
from discord.ext.commands import Bot as BotBase
from discord.ext.commands import Context
from discord.ext.commands import (CommandNotFound, BadArgument, MissingRequiredArgument,
								  CommandOnCooldown)


COGS = [p.stem for p in Path(".").glob("./bot/cogs/*.py")]
OWNER_ID = 656994493463003136
def get_prefix(bot, message):
        prefix= db.field("SELECT Prefix FROM guilds WHERE GuildID =?", message.guild.id)
        return commands.when_mentioned_or(prefix)(bot, message)

class Ready(object):
    def __init__(self):
        for cog in COGS:
            setattr(self, cog, False)
            
    def all_ready(self):
        return all([getattr(self, cog) for cog in COGS])


class AngmarBot(commands.Bot):
    def __init__(self):
        self._cogs = [p.stem for p in Path(".").glob("./bot/cogs/*.py")]
        self.scheduler = AsyncIOScheduler()
        self.ready = False
        self.cogs_ready = Ready()
        db.autosave(self.scheduler)

        super().__init__(command_prefix=get_prefix, 
                         case_insensitive=True, 
                         intents = discord.Intents.all(),
                         owner_id= OWNER_ID,)

    def update_db(self):
        db.multiexec("INSERT OR IGNORE INTO guilds (GuildID) VALUES (?)",
                     ((guild.id,) for guild in self.guilds))


        db.commit()
    
    def update_starboard(self):
        db.multiexec("INSERT OR IGNORE INTO channels (GuildID) VALUES (?)",
                     ((guild.id,) for guild in self.guilds))

        db.commit()


    def setup(self):
        print("Running setup...")

        for cog in self._cogs:
            self.load_extension(f"bot.cogs.{cog}")
            print(f" Loaded `{cog}` cog.")

        print("Setup complete.")

    def run(self):
        self.setup()

        with open("data/token.0", "r", encoding="utf-8") as f:
            TOKEN = f.read()

        print("Running bot...")
        super().run(TOKEN, reconnect=True)
        
    async def rules_reminder(self):
        await self.stdout.send("Remember to adhere to the rules!")

    async def shutdown(self):
        print("Closing connection to Discord...")
        await super().close()

    async def close(self):
        print("Closing on keyboard interrupt...")
        await self.shutdown()

    async def on_connect(self):
        print(f" Connected to Discord (latency: {self.latency*1000:,.0f} ms).")

    async def on_resumed(self):
        print("Bot resumed.")

    async def on_disconnect(self):
        print("Bot disconnected.")
        
    

    # async def on_error(self, err, *args, **kwargs):
    #     raise

    # async def on_command_error(self, ctx, exc):
    #     raise getattr(exc, "original", exc)

    async def on_ready(self):
                self.client_id = (await self.application_info()).id
                print("Bot ready.")
                    
                await self.change_presence(activity=discord.Game(name="Type .help for help"))\

                if not self.ready:
                    self.scheduler.add_job(self.rules_reminder, CronTrigger(day_of_week=0, hour=12, minute=0, second=0))
                    self.scheduler.start()
                    self.stdout = self.get_channel(739057929642311712)

                    self.update_db()
                    self.update_starboard()



    async def process_commands(self, message):
        ctx = await self.get_context(message, cls=commands.Context)

        if ctx.command is not None:
            await self.invoke(ctx)

    async def on_message(self, message):
        if not message.author.bot:
            await self.process_commands(message)
