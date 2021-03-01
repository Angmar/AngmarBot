import discord
from discord.ext import commands 
from aiohttp import request
from discord import Member, Embed
from discord.ext.commands import Cog, BucketType
from discord.ext.commands import BadArgument
from discord.ext.commands import command, cooldown

class Api(commands.Cog):
    def __init__(self, bot):
        self.bot = bot 
        
    @command(name="fact")
    @cooldown(3, 15, BucketType.guild)
    async def animal_fact(self, ctx, animal: str):
        if (animal := animal.lower()) in ("dog", "cat", "panda", "fox", "bird", "koala"):
            fact_url = f"https://some-random-api.ml/facts/{animal}"
            image_url = f"https://some-random-api.ml/img/{'birb' if animal == 'bird' else animal}"
            
            async with request("GET", image_url, headers={}) as response:
                if response.status == 200:
                    data = await response.json()
                    image_link = data["link"]
                    
                else:
                    image_link = None
                    
                async with request("GET", fact_url, headers={}) as response:
                    if response.status == 200:
                        data = await response.json()
                        
                        embed = Embed(title=f"{animal.title()} fact",
                                      description=data["fact"],
                                      color=ctx.author.color)
                    if image_link is not None:
                        embed.set_image(url=image_link)
                        await ctx.send(embed=embed)
                        
                    else:
                        await ctx.send(f"API returned a {response.status} status.")
                        
        else:
            await ctx.send("No facts are available for that animal.")


    
    @command(name="meme")
    @cooldown(3, 15, BucketType.guild)
    async def meme(self, ctx):
            image_url = "https://some-random-api.ml/meme"

            async with request("GET", image_url, headers={}) as response:
                data = await response.json()
                image_link = data["image"]
                    
               
                        
            embed = Embed(title=data["caption"],
                                      color=ctx.author.color)
            embed.set_image(url=image_link)
            await ctx.send(embed=embed)
                        
   
                
    

    
    

    

def setup(bot):
    bot.add_cog(Api(bot))
