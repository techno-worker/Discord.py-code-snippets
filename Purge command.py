
# This is a very simple purge command which can be used by anyone

@client.command(aliases=['clear'])
async def purge(ctx):
	def check(m):
		return m.pinned == False
	llimit = ctx.message.content[7:].strip()			
	await ctx.channel.purge(limit=int(llimit) + 1, check=check)
	

# Modified purge command with permission checks

@client.command(aliases=['clear'])
async def purge(ctx):
	
	#checking author's permissions
	if ctx.author.guild_permissions.manage_messages:
		
		#checking bot's permissions
		if ctx.guild.me.guild_permissions.manage_messages:
			
			def check(m):
				return m.pinned == False
			llimit = ctx.message.content[7:].strip()
			await ctx.channel.purge(limit=int(llimit) + 1, check=check)
		
		else:
			await ctx.send("I am missing the `MANAGGE MESSAGES` permission.")
			
	else:
		await ctx.send("You dont have the `MANAGE MESSAGES` permission")
