import discord
from discord.ext import commands

TOKEN="token_here"
client=commands.Bot(command_prefix=['your_prefix'],intents=discord.Intents.all())

@client.event
async def on_ready():
  	await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening,name="to your commands"))
  

client.run(TOKEN)
