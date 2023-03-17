
# This one is for setting cooldown for the particular user
# Replace 5 with any number you want your cooldown to be

@client.command()
@commands.cooldown(1,5,commands.BucketType.user):
    #code here
    

# This one is for setting cooldown for the complete server
# Starts when anyone in the server uses this command

@client.command()
@commands.cooldown(1,5,commands.BucketType.guild):
    #code here


# To reset cooldown
# You can reset the cooldown in case of command incompletion or error by the user
# You can use this under (if) and (else) statements

ctx.command.reset_cooldown(ctx)











