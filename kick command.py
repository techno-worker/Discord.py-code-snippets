# Easy version

@client.command()
async def kick(ctx,member:discord.Member,reason=None):
  	await member.kick(reason=reason) # None if no reason is given
 	await ctx.send(f"Kicked {member.name}")
	
	
	
# Modified Version

@client.command()
async def kick(ctx,member:discord.Member=None,reason=None):
	
	#checking author's permissions
	if ctx.author.guild_permission.kick_members:
		
		#checking bot's permissions
		if ctx.guild.me.guild_permissions.kick_members:
			
			if member==None:
				await ctx.send("Mention a member or use their ID")
				
			else:
				await member.kick(reason=reason)
				await ctx.send(f"Kicked {member.name} | Reason: {reason}") #shows None if no reason given
				
				#sending a message to the member
				
				#checks if bot can send message to the member
				try:
					await member.send(f"You have been kicked from {ctx.guild.name} for Reason: {reason}")
				except:
					return
			
		else:
			await ctx.send("I am missing the `KICK MEMBERS` permission")
			
	else:
		await ctx.send("You are missing the `KICK MEMBERS` permission")
