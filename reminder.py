
# You will need a function to convert time to run this command without problems

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


# Command

import asyncio

@client.command(aliases=['rm','reminder'])
async def remindme(ctx, seconds=None, *, query=None):
	unit = convert(seconds)
 
	if seconds==None:
		await ctx.send("Set the reminder timer.")

	else:
		if query == None:
			await ctx.send("Provide A Topic For Your Reminder")

		else:
			await ctx.send(f"{ctx.author.mention} Your Reminder Has Been Set For `{seconds}` For **{query}** ")
			await asyncio.sleep(unit)
			await ctx.send(f"{ctx.author.mention} \nYour reminder was over :-  {query}")

            # You can ignore this part if you dont want to send a DM to the user
			try:
				await ctx.author.send(f"Your reminder was over :- {query}")
			except:
				pass