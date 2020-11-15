import discord
from typing import Optional
from discord.ext import commands
from discord.ext.commands import Cog
from discord.ext.commands import command
from discord.utils import get
from discord.ext import menus


def syntax(command):
    cmd_and_aliases = "|".join([str(command), *command.aliases])
    params = []
    
    for key, value in command.params.items():
        if key not in ("self", "ctx"):
            params.append(f"[{key}]" if "NoneType" in str(value) else f"<{key}>")

    params = " ".join(params)
    
    return f"```{cmd_and_aliases}```"

class HelpMenu(menus.ListPageSource):
    def __init__(self, ctx, data):
        self.ctx = ctx

        super().__init__(data, per_page=5)
    
    async def write_page(self, menu, fields=[]):
        offset = (menu.current_page*self.per_page) + 1
        len_data = len(self.entries)

        embed = discord.Embed(title="Help",
                              description="Command Help Dialog, Type .help then a particual command to get more information.",
                              color=self.ctx.author.color)
        embed.set_thumbnail(url=self.ctx.guild.me.avatar_url)
        embed.set_footer(text=f"{offset:,} - {min(len_data, offset+self.per_page-1):,} of {len_data:,} commands.")

        for name, value in fields: 
            embed.add_field(name=name, value=value, inline=False)

        return embed

    async def format_page(self, menu, entries):
        fields = []

        for entry in entries:
            fields.append((entry.brief or "No description", syntax (entry)))

        return await self.write_page(menu, fields)
            
class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.bot.remove_command("help")

    async def cmd_help(self, ctx, command):
        embed = discord.Embed(title=f"Help with {command}",
                description=syntax(command),
                color=ctx.author.color)
        embed.add_field(name="Command description", value=command.help)
        await ctx.send(embed=embed)

    @command(name = "help", brief="Help")
    async def show_help(self, ctx, cmd: Optional[str]):
        """Type .help then a particular command to get more information on specified command."""
        if cmd is None:
            menu = menus.MenuPages(source=HelpMenu(ctx, list(self.bot.commands)),
                             delete_message_after=True,
                             timeout=60.0)
            await menu.start(ctx)

        else:
            if (command := get(self.bot.commands, name=cmd)):
                await self.cmd_help(ctx, command)

    


def setup(bot):
    bot.add_cog(Help(bot))
    