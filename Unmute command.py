
@client.command()
async def unmute(ctx, member: discord.Member = None):
	mrole = discord.utils.get(ctx.guild.roles, name="Muted")
 
	if ctx.author.guild_permissions.manage_messages:
     
		if ctx.guild.me.guild_permissions.manage_roles:
      
			if member == None:
				await ctx.send("Mention a member or use their ID")

    
			else:
				if mrole in member.roles:
					await member.remove_roles(mrole)
					await ctx.send(f"Unmuted {member.name}")
     
				else:
					await (f"{member.name}#{member.discriminator} is not muted.")

    
		else:
			await ctx.send("I dont have `MANAGE ROLES` permission to unmute members.")
   
	else:

		await ctx.send("You dont have `MANAGE MESSAGES` permission to unmute members.")





























