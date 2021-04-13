from model import *
import os
import discord
#from scoretable import scoreboard
#from dotenv import load_dotenv

#load_dotenv()
#TOKEN = os.getenv('DISCORD_TOKEN')
image_types = ["png", "jpeg", "gif", "jpg"]
TOKEN =""
GUILD="testing"
from discord.ext import commands

#bot = commands.Bot(command_prefix='$')

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
    for guild in client.guilds:
        #print(f'{guild} has connected the bot')
        #print(guild.members)
        '''if guild.name == GUILD:
            await guild.send(file=discord.File("danish.jpg"))
            message2='Yo guys , i am up! check out >help to know meeee.'

            await message.channel.send('{}'.format(message2))'''
        print("Bonjour")
        break

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    for attachment in message.attachments:
        if any(attachment.filename.lower().endswith(image) for image in image_types):
            await attachment.save("sample.gif")
            #print("its running eveything below")
            #print("ahhh filter running before")
            filter_func("sample.gif")
            #display toonify
            await message.channel.send(file=discord.File("toonify.gif"))
            await message.channel.send(file=discord.File("blackwhite.gif"))
        #display toonify
    if message.content.startswith('>developers info'):
        #message2='Team members :Raghav,Abhijnya and Jaaswin D Kots , And that is us in that order xD'+str(message.author)[:-5]
        #await message.channel.send('{}'.format(message2))
        await message.channel.send(file=discord.File("spiderman.jpg"))
        #await message.channel.send(file=discord.File("abj.jpg"))
        #await message.channel.send(file=discord.File("jas.jpg"))
    if message.content.startswith('>hi potter'):
        message2='Hello There , Welcome to the Future'
        await message.channel.send('{}'.format(message2))
    '''elif message.content.startswith('3'):
        message2='Jaaswin D kots'
        await message.channel.send('{}'.format(message2))
    if message.content.startswith('>hi Potter'):
        message2='Hi there, '+str(message.author)[:-5]
        await message.channel.send('{}'.format(message2))
    if message.content.startswith('>rcb'):
        message2='Nope they dont win ipl, '+str(message.author)[:-5]
        await message.channel.send('{}'.format(message2))'''
    if message.content.startswith('>help'):
        message2='This bot is currently in development, '+str(message.author)[:-5]+'.The commands availabe are >hi potter ,developers info(upcoming) , >click a pic(upcoming) '
        await message.channel.send('{}'.format(message2))
    
    

'''@bot.command()
async def test(ctx, arg):
     ctx.send(arg)
'''

    

client.run(TOKEN)
