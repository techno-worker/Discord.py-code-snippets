
# This command has two parts:

# 1. Lock the entire server by changing the permissions of the default guild role i.e. @everyone
# 2. Unlock the entire server

# The time depends upon the number of channels the server has

# Channels for which bot doesnt have permissions will be ignored


# Here the cooldown is set for the guild for 120 seconds i.e. 2 minutes

# The user needs ADMINISTRATOR permission to run the command.
# You can change it for any permission you want

import asyncio

@client.command()
@commands.cooldown(1,120,BucketType.guild)
async def serverlock(ctx):
    
	if ctx.author.guild_permissions.administrator:
     
		if ctx.guild.me.guild_permissions.manage_channels:
      
			sure = await ctx.reply("Are you sure you want to **LOCK** the server ?")
			await asyncio.sleep(3)
   
			def check(reaction,user):
				return user ==ctx.author and str(reaction.emoji) in ("✅","❎")
			list=["✅","❎"]
   
			for i in list:
				await sure.add_reaction(i)
			try:
				reaction,user=await client.wait_for('reaction_add',check=check,timeout=20.0)
    
			except asyncio.TimeoutError:
				await ctx.send("Time's up")
				ctx.command.reset_cooldown(ctx)
    
			else:
				if str(reaction.emoji) == "✅":							
					msg = await ctx.send("Server Lock Process Initiated")
					await asyncio.sleep(2)
					await msg.edit(
					 content="Server Lock Process Initiated \nLocking All Channels")
     
					for bruh in ctx.guild.text_channels:
						overwrite = bruh.overwrites_for(ctx.guild.default_role)
						overwrite.send_messages = False
						await bruh.set_permissions(ctx.guild.default_role, overwrite=overwrite)
      
					for bruh in ctx.guild.voice_channels:
						overwrite = bruh.overwrites_for(ctx.guild.default_role)
						overwrite.send_messages = None
						await bruh.set_permissions(ctx.guild.default_role, overwrite=overwrite)
      
					await msg.edit(content="Server Lock Process Initiated \nLocking All Channels \n\n Server Locked")
     
				elif str(reaction.emoji)== "❎":
					await ctx.send("Server lock Aborted.")
					ctx.command.reset_cooldown(ctx)
				else:
					pass
 
		else:
			await ctx.send("I dont have `MANAGE CHANNELS` permission lock the server.")
   
	else:
		await ctx.send("You dont have `ADMINISTRATOR` permission to lock the server.")


@client.command()
@blacklist()
@commands.cooldown(1, 120, commands.BucketType.guild)
async def serverunlock(ctx):
    
	if ctx.author.guild_permissions.administrator:
     
		if ctx.guild.me.guild_permissions.manage_channels:
      
			sure = await ctx.reply("Are you sure you want to **UNLOCK** the server ?")
			await asyncio.sleep(3)
   
			def check(reaction,user):
				return user ==ctx.author and str(reaction.emoji) in ("✅","❎")
			list=["✅","❎"]
   
			for i in list:
				await sure.add_reaction(i)
			try:
				reaction,user=await client.wait_for('reaction_add',check=check,timeout=20.0)
    
			except asyncio.TimeoutError:
				await ctx.send("Time's up")
				ctx.command.reset_cooldown(ctx)
    
			else:
				if str(reaction.emoji) == "✅":
					msg = await ctx.send(f"Server Unlock Process Initiated")
					for bruh in ctx.guild.text_channels:
						overwrite = bruh.overwrites_for(ctx.guild.default_role)
						overwrite.send_messages = None
						await bruh.set_permissions(ctx.guild.default_role, overwrite=overwrite)
      
					for bruh in ctx.guild.voice_channels:
						overwrite = bruh.overwrites_for(ctx.guild.default_role)
						overwrite.send_messages = None
						await bruh.set_permissions(ctx.guild.default_role, overwrite=overwrite)
      
					await msg.edit(content=F"Server Unlock Process Initiated \nOverwrites Removed From All Channels \n\nServer Unlocked")
     
				elif str(reaction.emoji) == "❎":
					await ctx.send("Server unlock Aborted.")
					ctx.command.reset_cooldown(ctx)
     
		else:
			await ctx.send("I dont have `MANAGE CHANNELS` permission to unlock the server.")
   
	else:
		await ctx.send("You dont have `ADMINISTRATOR` permission to unlock the server.")