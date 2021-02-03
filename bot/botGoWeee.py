import discord
client = discord.Client()
largest = ("",0)

@client.event 
async def on_ready():
    global largest
    
    print("look ma it's {0.user}".format(client))
    channel = await grab_channel("🧮-counting")
    messages =  await channel.history(limit=50).flatten()
    for message in messages:
        try:
            if int(message.content) >= largest[1]:
                largest = (message.author, int(message.content))
        except:
            pass
    print(largest)
    game = discord.Game("with numbers")
    await client.change_presence(activity=discord.CustomActivity("counting the things for you naughty children"))


@client.event
async def on_message(message):
    global largest

    if message.author == client.user:
        print("deleted becaust author matches client user")
        return
    if message.channel.name != "🧮-counting":
        print("deleted because it's in the wrong channel.")
        return 
    try:
        print("we got in the try")
        if message.author.id == largest[0].id or int(message.content) != largest[1]+1:
            await message.delete()
        else:
            largest = (message.author, int(message.content))
    except:
            await message.delete()
    print(largest)


async def grab_channel(channel_name):
    for channel in client.get_all_channels():
        if channel.name == channel_name:
            return channel

#needed perms: manage messages, read message history

client.run('NzQ4MzM5MTY2MjQ0NTAzNjMy.X0b_KA.R9OLxlUBHyw58hfkar2DUJ1GhvE')

