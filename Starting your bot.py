import discord
from discord.ext import commands


client=commands.Bot(command_prefix=['your_prefix'],intents=discord.Intents.all())


#All your other codes will be here


@client.event
async def on_ready():
	print(f"Connect To Bot: {client.user.name}")

client.run("token_here")


#You can also put the token in a variable 

#TOKEN = 'token_here'

#client.run(TOKEN)
