
# This command can calculate all of your baisc operations like ( +,-,*,/ )

@client.command(aliases=['calculator'])
async def calc(ctx,calc=None):
	if calc==None:
		await ctx.send("Enter your numbers and operations to calculate.")
	else:
		cal=calc
		ans=("Answer: " + str(eval(cal)))
		await ctx.reply(f"```{ans}```")
  
  
# Example: >calc 100+100*2

# NOTE: Operations will be ignored if spaces are given in between
  
  
  