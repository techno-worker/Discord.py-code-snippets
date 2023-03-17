
# We will need a function to convert time to use cooldown commands

def convert(time):
	pos = [
	 "s", "m", "h", "d", "hr", "hour", "hours", "min", "minute", "minutes", "day",
	 "days"
	]

	time_dict = {
	 "s": 1,
	 "m": 60,
	 "h": 3600,
	 "d": 3600 * 24,
	 "day": 3600 * 24,
	 "min": 60,
	 "minute": 60,
	 "hour": 3600,
	 "hours": 3600,
	 "minutes": 60,
	 "days": 3600 * 24,
	 "hr": 3600
	}
	unit = time[-1]
	if unit not in pos:
		return -1
	try:
		val = int(time[:-1])
	except:
		return -2
	return val * time_dict[unit]


# Cooldown command

import asyncio

@client.command()
@commands.cooldown(1, 5, commands.BucketType.user)
async def slowmode(ctx, seconds):
    
	if ctx.author.guild_permissions.manage_channels:
     
		if ctx.guild.me.guild_permissions.manage_channels:
      
			unit = convert(seconds)
   
			if unit == -1:
				await ctx.send("Please Enter A Proper Unit [s | m | h]")
				ctx.command.reset_cooldown(ctx)
    
			elif unit == -2:
				await ctx.send("Please Use A Proper Unit Reference [s | m | h]")
				ctx.command.reset_cooldown(ctx)
    
			else:
				channel = ctx.channel
				await channel.edit(slowmode_delay=unit)
				await ctx.send(F"Set the slowmode for {seconds}")
    
		else:
			await ctx.send("I dont have `MANAGE CHANNELS` permission to set slowmode.")
   
	else:
		await ctx.send("You dont have  `MANAGE CHANNELS` permission to set slowmode.")