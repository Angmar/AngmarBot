import discord
from discord.ext import commands
from datetime import datetime
from typing import Optional
from discord.ext.commands import Cog
from discord.ext.commands import command
from discord import Embed, Member
from discord.ext.commands import when_mentioned_or, command, has_permissions
from psutil import Process, virtual_memory
from discord import __version__ as discord_version
from platform import python_version
from datetime import datetime, timedelta
from time import time


class Info(Cog):
    def __init__(self, bot):
        self.bot = bot

    @command(name="userinfo", brief="Info")
    async def user_def(self, ctx, target: Optional[Member]):
        """Gives information on a particular user, type the name of a user afterwards to get their information."""
        target = target or ctx.author
        hours = (int(target.created_at.strftime ("%H")))-17

        if hours == 0:
            hours = 12
            
        else:
            pass
        
        if hours == -16:
            hours = 1
        
        else:
            pass

        if hours == -15:
            hours = 2
        
        else:
            pass

        if hours == -14:
            hours = 3
        
        else:
            pass

        if hours == -13:
            hours = 4
        
        else:
            pass

        if hours == -12:
            hours = 5
        
        else:
            pass


        if hours == -11:
            hours = 6
        
        else:
            pass

        if hours == -10:
            hours = 7
        
        else:
            pass

        if hours == -9:
            hours = 8
        
        else:
            pass
        
        if hours == -8:
            hours = 9

        else:
            pass

        if hours == -7:
            hours = 10

        else:
            pass


        if hours == -6:
            hours = 11

        else:
            pass
        if hours == -5:
            hours = 12
        
        else:
            pass

        if hours == -4:
            hours = 1
        
        else:
            pass

        if hours == -3:
            hours = 2
        
        else:
            pass

        if hours == -2:
            hours = 3
        
        else:
            pass

        if hours == -1:
            hours = 4
        
        else:
            pass

        foo = (int(target.joined_at.strftime ("%H")))-17
            
        if foo == 0:
            foo = 12
            
        else:
            pass

        if foo == -16:
            foo = 1
        
        else:
            pass

        if foo == -15:
            foo = 2
        
        else:
            pass

        if foo == -14:
            foo = 3
        
        else:
            pass

        if foo == -13:
            foo = 4
        
        else:
            pass

        if foo == -12:
            foo = 5
        
        else:
            pass


        if foo == -11:
            foo = 6
        
        else:
            pass

        if foo == -10:
            foo = 7
        
        else:
            pass

        if foo == -9:
            foo = 8
        
        else:
            pass
        
        if foo == -8:
            foo = 9

        else:
            pass

        if foo == -7:
            foo = 10

        else:
            pass


        if foo == -6:
            foo = 11

        else:
            pass
        if foo == -5:
            foo = 12
        
        else:
            pass

        if foo == -4:
            foo = 1
        
        else:
            pass

        if foo == -3:
            foo = 2
        
        else:
            pass

        if foo == -2:
            foo = 3
        
        else:
            pass

        if foo == -1:
            foo = 4
        
        else:
            pass


        embed = Embed(title="User information",
                        color=target.color,
                        timestamp=datetime.utcnow())

        embed.set_thumbnail(url=target.avatar_url)
        


        fields = [("Name", str(target), True),
                    ("ID", target.id, False),
                    ("Bot?", target.bot, True),
                    ("Status", str(target.status).title(), True),
                    ("Created at", target.created_at.strftime(f"%m/%d/%Y {hours}:%M:%S %p"), True),
                    ("Joined at", target.joined_at.strftime(f"%m/%d/%Y {foo}:%M:%S %p"), True)]
        
        for name, value, inline in fields:
            embed.add_field(name=name, value=value, inline=inline)

        await ctx.send(embed=embed)
        
        
    @command(name="serverinfo", brief="Info")
    async def server_info(self, ctx, cmd: Optional[str]):
        """Displays server information"""
        embed = Embed(title="Server information",
                      color=ctx.guild.owner.color,
                      timestamp=datetime.utcnow())
                      
        
        embed.set_thumbnail(url=ctx.guild.icon_url)
        
        statuses = [len(list(filter(lambda m: str(m.status) == "online", ctx.guild.members))),
                    len(list(filter(lambda m: str(m.status) == "idle", ctx.guild.members))),
                    len(list(filter(lambda m: str(m.status) == "dnd", ctx.guild.members))),
                    len(list(filter(lambda m: str(m.status) == "offline", ctx.guild.members)))]

        pong = (int(ctx.guild.created_at.strftime ("%H")))-17

        if pong == 0:
             pong = 12
            
        else:
            pass

        if pong == -16:
            pong= 1
        
        else:
            pass

        if pong == -15:
            pong = 2
        
        else:
            pass

        if pong == -14:
            pong = 3
        
        else:
            pass

        if pong == -13:
            pong = 4
        
        else:
            pass

        if pong == -12:
            pong = 5
        
        else:
            pass


        if pong == -11:
            pong = 6
        
        else:
            pass

        if pong == -10:
            pong = 7
        
        else:
            pass

        if pong == -9:
            pong = 8
        
        else:
            pass
        
        if pong == -8:
            pong = 9

        else:
            pass

        if pong == -7:
            pong = 10

        else:
            pass


        if pong == -6:
            pong = 11

        else:
            pass
        
        if pong == -5:
            pong = 12
        
        else:
            pass

        if pong == -4:
            pong = 1
        
        else:
            pass

        if pong == -3:
            pong = 2
        
        else:
            pass

        if pong == -2:
            pong = 3
        
        else:
            pass

        if pong == -1:
            pong = 4
        
        else:
            pass

                    
        fields = [("ID", ctx.guild.id, True),
                  ("Owner", ctx.guild.owner, True),
                  ("Created at", ctx.guild.created_at.strftime(f"%m/%d/%Y {pong}:%M:%S %p"), True),
                  ("Members", len(ctx.guild.members), True),
                  ("Humans", len(list(filter(lambda m: not m.bot, ctx.guild.members))), True),
                  ("Bots", len(list(filter(lambda m: m.bot, ctx.guild.members))), True),
                  ("Statuses", f"🟢 {statuses[0]} 🟠 {statuses[1]} 🔴 {statuses[2]} ⚪ {statuses[3]}", True),
                  ("Text channels", len(ctx.guild.text_channels), True),
                  ("Voice channels", len(ctx.guild.voice_channels), True)]
                  
        for name, value, inline in fields:
            embed.add_field(name=name, value=value, inline=inline)
            
        await ctx.send(embed=embed)
        
    
    @command(name="botinfo")
    async def show_bot_stats(self, ctx):
        embed = Embed(title="Bot Info",
                      color=ctx.author.color,
                      thumbnail=self.bot.user.avatar_url,
                      timestamp=datetime.utcnow())
                      
        proc = Process()
        with proc.oneshot():
            uptime = timedelta(seconds=time()-proc.create_time())
            cpu_time = timedelta(seconds=(cpu := proc.cpu_times()).system + cpu.user)
            mem_total = virtual_memory().total / (1024**2)
            mem_of_total = proc.memory_percent()
            mem_usage = mem_total * (mem_of_total / 100)
            
        fields = [
            ("Bot version", "0.7.3", True),
            ("Python version", python_version(), True),
            ("discord.py version", discord_version, True),
            ("Uptime", uptime, True),
            ("CPU time", cpu_time, True),
            ("Memory usage", f"{mem_usage:,.3f} MiB/ {mem_total:,.0f} MiB ({mem_of_total:.0f}%)", True),
            ]
            
        for name, value, inline in fields:
            embed.add_field(name=name, value=value, inline=inline)
            
        await ctx.send(embed=embed)
def setup(bot):
    bot.add_cog(Info(bot))