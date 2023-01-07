import discord
import fortnite_api
from discord.ext import commands
import random
import datetime
from datetime import datetime


intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

#FortniteApi
api = fortnite_api.FortniteAPI()

mapimage = api.map.fetch().poi_image




client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Logged into {client.user}')
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="Gingerbread"))

@client.event
async def on_message(message):
    if message.content.startswith('$map'):
        embedVar = discord.Embed(title="Current Map", description=f"Hey {message.author.mention}, Here is the current fortnite map", color=0xc27c0e, timestamp=datetime.now())
        embedVar.set_image(url="https://fortnite-api.com/images/map_en.png")
        embedVar.set_footer(text='Gingerbread Open Source Discord Bot\u200b')
        await message.channel.send(embed=embedVar)
    elif message.content.startswith('$help') or message.content.startswith('$helplist'):
        embedVar2 = discord.Embed(title="All commands", color=0xc27c0e, timestamp=datetime.now())
        embedVar2.add_field(name="$Map", value="Shows Fortnite Map", inline=False)
        embedVar2.add_field(name="$1or2", value="Flips a coin", inline=False)
        embedVar2.set_footer(text='Gingerbread Open Source Discord Bot\u200b')
        await message.channel.send(embed=embedVar2)
    elif message.content.startswith('$1or2') or message.content.startswith('$flipacoin'):
        embedVar4 = discord.Embed(title="Current Map", description=f"The coinflips looking like a {random.randint(1,2)} {message.author.mention}", color=0xc27c0e, timestamp=datetime.now())
        embedVar4.set_image(url="https://cdn.dribbble.com/users/58530/screenshots/2323771/media/28389aa04539d4579db7b6eb56be35df.gif")
        embedVar4.set_footer(text='Gingerbread Open Source Discord Bot\u200b')
        await message.channel.send(embed=embedVar4)
    elif message.content.startswith('/dice') or message.content.startswith('$roll'):
        embedVar3 = discord.Embed(title="Current Map", description=f"The Dice has rolled a {random.randint(1,6)} {message.author.mention}", color=0xc27c0e, timestamp=datetime.now())
        embedVar3.set_image(url="https://64.media.tumblr.com/e1252f36ddaf27c01050befdab8b5a8b/b7053f0faf4e4e47-2c/s540x810/1e4dbb7ede433adf2cd0eeecf5f980150c4cd3a3.gif")
        embedVar3.set_footer(text='Gingerbread Open Source Discord Bot\u200b')
        await message.channel.send(embed=embedVar3)












client.run("YourTokenHere")






