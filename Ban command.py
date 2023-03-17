

@client.command()
@commands.cooldown(1, 5, commands.BucketType.user)
async def ban(ctx,member: discord.Member = None,*,reason="No reason specified"):
	
	if ctx.author.guild_permissions.ban_members:
		
		if ctx.guild.me.guild_permissions.ban_members:
			
			if member == None:
				await ctx.send('Give the member ID or mention them.')
				ctx.command.reset_cooldown(ctx)
			else:
				
				if member.top_role >= ctx.author.top_role or member.id == ctx.guild.owner_id:
					await ctx.send(f"You can not ban {member.name}#{member.discriminator} as your role is below them.")
				else:
					await member.ban(reason=f"{reason} By {ctx.author}")
					await ctx.send(f"Banned {member.name}#{member.discriminator} for Reason: {reason}")
					
		else:
			await ctx.send("I dont have `BAN MEMBERS` permission to ban members.")
			
	else:
		await ctx.send("You dont have `BAN MEMBERS` permission to ban members.")

