# bot.py
import os
import discord
from random import *
import random
# from dotenv import load_dotenv

# load_dotenv()

# TOKEN = os.getenv('DISCORD_TOKEN')

TOKEN = "NzkxODM5MTYxMTU3NTUwMDkw.X-U_rw.eYn98DIDbFhszEUG1c54JeUasBY"

client = discord.Client()

version = "0.1.1"

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord')

@client.event
async def on_message(message):

    # Debug
    """
    print(discord.__version__)
    print(message.author.id)
    """

    msg = message.content.lower()

    if message.author == client.user:
        return
    if msg == 'no u':
        response = 'no u'
        await message.channel.send(response)
    
   
    if 'bald' in msg:
        await message.add_reaction('🅱️')
    
    
    # if 'children' in msg or 'child' in msg:
    #     await message.channel.send('children? James likes children')
    
    if 'mlp' in msg or 'my little pony' in msg:
        await message.channel.send('<3 mlp')
    
    if 'samara' in msg:
        await message.add_reaction('😠')
    
    if 'what are you doing' in msg:
        await message.channel.send('your mom')

    if 'rip' in msg:
        await message.add_reaction('🇫')
    
    if 'good bot' in msg:
        await message.add_reaction('👍')
    
    if 'bad bot' in msg:
        await message.add_reaction('🥺')

    # if 'zane' in msg:
    #     await message.channel.send('<:zanemoment:750635985192222752>')
    

    
    if 'ftb server' in msg or 'minecraft server' in msg or 'daniel\'s server' in msg:
        await message.channel.send("server trash")
    
    mention = f'<@!{client.user.id}>'
    if mention in msg:
        await message.channel.send("wut")
    
    # print(message.channel)

    if "horny" in str(message.channel):
        if message.attachments:
            await message.add_reaction('👍')
            await message.add_reaction('👎')

        pic_ext = ['.jpg','.png','.jpeg']
        for ext in pic_ext:
            if msg.endswith(ext):
                await message.add_reaction('👍')
                await message.add_reaction('👎')
        
        for mage in msg.split(" "):
            if mage.isdigit():
                if 1000 < int(mage) < 341200:
                    toSend = "https://nhentai.net/g/{}/".format(mage)
                    await message.channel.send(toSend)

        if message.author.id == 540682323549618197:
            toCheck = msg.replace(" ", "")
            hornyWords = ['horny', 'sex', 'gosh', 'feeling', 'sexual', 'soft', 'hard', 'camp', 'buddy', 'fun', 'man', 'jack', 'mood', 'hole', 'dick', 'fuck', 'wanna', "want to", 'play', 'passion']
            found = False
            for word in hornyWords:
                if word in toCheck:
                    found = True
            if found:
                await message.pin()
                await message.unpin()

        if msg == "imhorny":
            number = random.randint(1, 341200)
            toSend = "https://nhentai.net/g/{}/".format(number)
            await message.channel.send(toSend)
        
        if msg == "-version":
            await message.channel.send(version)
            

    # Removed Features

    """
    
    if 'god' in msg:
        await message.channel.send('god isn\'t real')
    
    if 'fortnite' in msg:
        await message.channel.send('fortnite is for children')
    
    if 'daddy' in msg:
        await message.add_reaction('🥺')

    if 'hentai' in msg or 'sex' in msg:
        await message.add_reaction ('😩')
    
    if 'fuck' in msg:
        await message.add_reaction('😏')
    
    if 'among us' in msg:
        await message.add_reaction('😍')

    if 'ass' in msg:
        await message.add_reaction('🍑')
    
    if 'dick' in msg or 'penis' in msg:
        await message.add_reaction('🍆')
    
    if 'brr' in msg:
        await message.add_reaction('🅱️')
        await message.add_reaction('🇷')
        await message.add_reaction('®️')
    
    if 'gay' in msg:
        await message.add_reaction('🇬')
        await message.add_reaction('🇦')
        await message.add_reaction('🇪')
    
    if message.author.id == 599797556888862731:
        if "bedwars" in msg:
            await message.add_reaction('🚫')

    """

        
    
    if msg == "-invite":
        await message.channel.send('https://discord.com/api/oauth2/authorize?client_id=791839161157550090&permissions=1477442800&scope=bot')

    # nhentai integration



# client.run(TOKEN)
client.run(TOKEN)