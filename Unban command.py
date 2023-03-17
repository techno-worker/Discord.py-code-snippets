

@client.command()
async def unban(ctx,user:discord.User=None):
	if ctx.author.guild_permissions.ban_members:
		if ctx.guild.me.guild_permissions.ban_members:
			if user == None:
				await ctx.send("Enter ID of member to be unbanned.")
				ctx.command.reset_cooldown(ctx)
			else:
				try:
					user = await client.fetch_user(user.id)
					await ctx.guild.unban(user)
					await ctx.send(f"Successfully unbanned {user.name}#{user.discriminator}")
				except discord.NotFound:
					await ctx.send(f"{user.name}#{user.discriminator} is not banned.")
		else:
			await ctx.send("I dont have `BAN MEMBERS` permission to unban members.")
	else:
		await ctx.send("You dont have `BAN MEMBERS` permission to unban members.")
	










