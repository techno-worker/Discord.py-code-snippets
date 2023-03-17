@client.command()
@commands.cooldown(1, 5, commands.BucketType.user)
async def mute(ctx,member: discord.Member = None,*,reason=none):
	mrole = discord.utils.get(member.guild.roles, name="Muted")
	owner = await ctx.guild.fetch_member(ctx.guild.owner_id)
	abc = await ctx.guild.fetch_member(client.user.id)
	
	if ctx.author.guild_permissions.manage_messages:
		
		if ctx.guild.me.guild_permissions.manage_roles:
			
			if member == None:
				await ctx.send("Member not specified. Mention them or use their ID")
				ctx.command.reset_cooldown(ctx)
			else:
				if member.top_role >= abc.top_role or member == owner:
					
					await ctx.send( f"You cant mute {member.name}#{member.discriminator} as their role is above you.")
					ctx.command.reset_cooldown(ctx)
					
				else:
						if mrole not in member.roles:
							await member.add_roles(mrole,reason=reason)
							e=discord.Embed(description=f"Muted {member.name}#{member.discriminator} for Reason: {reason}",color=0x00ff35)
							await ctx.send(embed=e)
						else:
							await ctx.send("That member is already muted.")

						
		else:
					await ctx.send("I dont have `MANAGE ROLES` permission to mute members.")
				
	else:
		await ctx.send("You dont have `MANAGE ROLES` permission to mute members.")
