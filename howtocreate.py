#How to create a bot

#1. Go to discord developer portal - https://discord.com/developers/applications and sign in.
#2. Next Create a project, and add a bot, give the bot the gateway intents, and create the URL generator on OAuth2 to invite the bot to your server
#3. Now for the fun (python) time, open a fresh project with a new file called bot.py

#Here is some of the code i used to make the bot

import discord
from discord.ext import commands

#Importing both of these will allow for the bot to work
#Next Specify the intents -

intents = discord.Intents.default()
intents.message_content = True

#Next allow for the bot commands and intents, and call the bot as client

bot = commands.Bot(command_prefix='$', intents=intents)
client = discord.Client(intents=intents)

#Here i used the on_ready function to create status, and what you see in the terminal upon connect

@client.event
async def on_ready():
    print(f'Logged into {client.user}')
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="CHANGE ME"))
 
#Now we can create a simple command

async def on_message(message):
    if message.content.startswith('$hi'):
      await message.channel.send(f"Hello {message.author.name}")
    
#Now we must run it using the token (found in dev portal)

client.run("Your Token Here")

