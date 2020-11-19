
from random import randint
import discord
import asyncio
from discord.ext import commands
from discord.ext.commands import Cog




def is_num(s):
	try:
		int(s)
		return True
	except ValueError:
		return False


def roll_hit(num_of_dice, dice_type, hit, modifier, threshold):
		results = ""
		total = 0
		for x in range(0, int(num_of_dice)):
			y = randint(1, int(dice_type))
			if (int(hit) > 0):
				if (y >= int(hit)):
					results += "**{}** ".format(y)
					total += 1
				else:
					results += "+{} ".format(y)
			else:
				results += "{} ".format(y)
				total += y
		total += int(modifier)
		if modifier != 0:
			if modifier > 0:
				results += "+{} = {}".format(modifier, total)
			else:
				results += "{} = {}".format(modifier, total)
		else:
			results += "= {}".format(total)
		if threshold != 0:
			if total >= threshold:
				results += " meets or beats the {} threshold. ***Success***".format(threshold)
			else:
				results += " does not meet the {} threshold. ***Failure***".format(threshold)
		return results

def roll_basic(a, b, modifier, threshold):
    results = ""
    base = randint(int(a), int(b))
    if (base + modifier) >= threshold:
        if modifier != 0:
            if modifier > 0:
                results += "***Success***: {}+{} [{}] meets or beats the {} threshold.".format(base, modifier, (base + modifier), threshold)
            else:
                results += "***Success***: {}{} [{}] does not meet the {} threshold.".format(base, modifier, (base + modifier), threshold)
        else:
            results += "***Success***: {}".format(base)
    else:
        if modifier != 0:
            if modifier > 0:
                results += "{}+{} [{}]".format(base, modifier, (base + modifier))
            else:
                results += "{}{} [{}]".format(base, modifier, (base + modifier))
        else:
            results += "{}".format(base)
    return results

class gab(Cog):
	def __init__(self, bot):
		self.bot = bot
	
	@commands.command(pass_context=True, brief="Dice")
	@asyncio.coroutine
	def roll(self, ctx, roll : str):
		a, b, modifier, hit, num_of_dice, threshold, dice_type = 0, 0, 0, 0, 0, 0, 0

	
		
		if (roll.find('>') != -1):
			roll, threshold = roll.split('>')
		if (roll.find('+') != -1):
			roll, modifier = roll.split('+')
		if (roll.find('!') != -1):
			roll, hit = roll.split('!')
		if (roll.find('d') != -1):
			num_of_dice, dice_type = roll.split('d')
		elif (roll.find('-') != -1):
			a, b = roll.split('-')
		else:
			a = 1
			b = roll

		try:
			if (modifier != 0):
				if (is_num(modifier) is False):
					raise ValueError("Modifier value format error. Proper usage 1d4+1")
					
				else:
					modifier = int(modifier)
			if (hit != 0):
				if (is_num(hit) is False):
					raise ValueError("Hit value format error. Proper usage 3d6!5")
					
				else:
					hit = int(hit)
			if (num_of_dice != 0):
				if (is_num(num_of_dice) is False):
					raise ValueError("Number of dice format error. Proper usage 3d6")
					
				else:
					num_of_dice = int(num_of_dice)
			if (num_of_dice > 200):
				raise ValueError("Too many dice. Please limit to 200 or less.")
				
			if (dice_type != 0):
				if (is_num(dice_type) is False):
					raise ValueError("Dice type format error. Proper usage 3d6")
					
				else:
					dice_type = int(dice_type)
			if (a != 0):
				if (is_num(a) is False):
					raise ValueError("Error: Minimum must be a number. Proper usage 1-50.")
					
				else:
					a = int(a)
			if (b != 0):
				if (is_num(b) is False):
					raise ValueError("Error: Maximum must be a number. Proper usage 1-50 or 50.")
					
				else:
					b = int(b)
			if (threshold != 0):
				if (is_num(threshold) is False):
					raise ValueError("Error: Threshold must be a number. Proper usage 1-100>30")
					
				else:
					threshold = int(threshold)
			if (dice_type != 0 and hit != 0):
				if (hit > dice_type):
					raise ValueError("Error: Hit value cannot be greater than dice type")
					
				elif (dice_type < 0):
					raise ValueError("Dice type cannot be a negative number.")
					
				elif (num_of_dice < 0):
					raise ValueError("Number of dice cannot be a negative number.")
					
			if a != 0 and b != 0:
				yield from ctx.send("{}-{}. Result: {}".format(a, b, roll_basic(a, b, modifier, threshold)))
			else:
				yield from ctx.send("{}d{} Rolled . Details: {}".format(num_of_dice, dice_type, roll_hit(num_of_dice, dice_type, hit, modifier, threshold)))
	
		except ValueError as err:
			yield from ctx.send(err)
			
		
def setup(bot):
	bot.add_cog(gab(bot))	 