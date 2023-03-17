# You can change the permissions for a particular role or for the guild's default role i.e. @everyone

# Here I will show you how to make a channel lock/unlock and private/unprivate command

# Here the permissions will be changed for the @everyone role

# Lock/Unlock command will take the permission to send message in the particular channel

# Private/Unprivate command will take the permission to view the particular channel



@client.command()
async def lock(ctx, channel: discord.TextChannel = None):
    
	if ctx.author.guild_permissions.manage_channels:
     
		if ctx.guild.me.guild_permissions.manage_channels:
      
			if channel == None:
				channel = ctx.channel
			overwrite = channel.overwrites_for(ctx.guild.default_role)
			overwrite.send_messages = False
			await channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)
   
			await ctx.send(f"Successfully locked {ctx.channel.mention}")
		else:
			await ctx.send("I dont have `MANAGE CHANNELS` permission to lock channel.")
	else:

		await ctx.send("You dont have `MANAGE ROLES` permission to lock channel.")


@client.command()
async def unlock(ctx, channel: discord.TextChannel = None):
	if ctx.author.guild_permissions.manage_channels:
		if ctx.guild.me.guild_permissions.manage_channels:
			if channel == None:
				channel = ctx.channel
			overwrite = channel.overwrites_for(ctx.guild.default_role)
			overwrite.send_messages = None
			await channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)
			e = discord.Embed(description=f"Successfully unlocked {channel.mention}",color=0x00ff35)
			await ctx.send(embed=e)
   
		else:
			await ctx.send("I dont have `MANAGE CHANNELS` permission to unlock channel.")
   
	else:
		await ctx.send("You dont have the `MANAGE ROLES` permission to unlock  channel.")


@client.command()
async def private(ctx, channel: discord.TextChannel = None):
	
	if ctx.author.guild_permissions.manage_channels:
	 
		if ctx.guild.me.guild_permissions.manage_channels:
	  
			if channel == None:
				channel = ctx.channel
			overwrite = channel.overwrites_for(ctx.guild.default_role)
			overwrite.view_channel = False
			await channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)
   
			await ctx.send(f"{channel.mention} Is Now A Private Channel")
   
		else:

			await ctx.send("I dont have `MANAGE CHANNELS` permission to private channel.")
	else:
		await ctx.send("You dont have  `MANAGE CHANNELS` permission to private channel.")


@client.command()
async def unprivate(ctx, channel: discord.TextChannel = None):
	
	if ctx.author.guild_permissions.manage_channels:
	 
		if ctx.guild.me.guild_permissions.manage_channels:
	  
			if channel == None:
				channel = ctx.channel
			overwrite = channel.overwrites_for(ctx.guild.default_role)
			overwrite.view_channel = None
			await channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)
   
			await ctx.send(f"{channel.mention} is now a public channel")
   
		else:
			await ctx.send("I dont have `MANAGE CHANNELS` permission to unprivate channels.")

	else:
		await ctx.send("You dont have `MANAGE CHANNELS` permission to unprivate channels.")