#!/usr/bin/python3

# For this bot to work, create a text file called 'token.txt', place it in this script's directory, and paste your Discord bot token inside.

import discord
import asyncio
import random
from datetime import datetime
from datetime import datetime,timedelta


client = discord.Client()

# some ugly dicts and lists incoming
# rip dict
rip_dict = {
    0:                  'https://my.mixtape.moe/cmrzfq.png',    # Default
    130543636264779776: 'https://my.mixtape.moe/ljnyza.png',    # Coty
    100018402306822144: 'https://cdn.discordapp.com/attachments/350892741980323850/351169106982207489/NewRespectsCerberus.png',    # Briggs
    99756023912353792:  'https://cdn.discordapp.com/attachments/172456535010705418/351211834046414848/OasisRespects.png',    # Christian
    99750431231578112:  'https://cdn.discordapp.com/attachments/350892741980323850/351158774377218049/Kyle-F-Respects.png'     # Me
}

best_girl_list = [
    'https://static.zerochan.net/Senjougahara.Hitagi.full.101149.jpg', # Bake
    'https://media3.giphy.com/media/SQ6elRGAgBUME/giphy-facebook_s.jpg?t=1', # Hyouka
    'https://my.mixtape.moe/rpqguy.jpg', # Shirobako
    'http://vignette3.wikia.nocookie.net/gekkan-shoujo-nozakikun/images/1/11/Gekkan_shoujo_nozaki_kun_yuzuki_seo_render_by_koukochiisaki-d7vw9td.png/revision/latest?cb=20160228230642', # Nozaki
    'https://my.mixtape.moe/ogcird.png', # Girls und Panzer
    'https://media.giphy.com/media/13n7mrIkjlc11K/giphy.gif', # UFO
    'https://myanimelist.cdn-dena.com/images/characters/10/310969.jpg', # Girlish Number
    'http://www.darkmirage.com/blog/wp-content/uploads/2011/01/21_madoka07.jpg', # Madoka Magica
    'https://my.mixtape.moe/yxnmni.png', # Ping Pong
    'https://vignette4.wikia.nocookie.net/steins-gate/images/8/83/Kurisu_profile.png/revision/latest?cb=20141222010103', # Steins; Gate
    'https://68.media.tumblr.com/21f030f3821890b0186029294f039640/tumblr_ony4cjNgoh1sv5krro1_500.gif', # Maid Dragon
    'http://orig05.deviantart.net/6e1a/f/2011/227/7/0/nano_fan_art_by_crashhgkldj-d46lazd.png', # Nichijou
    'http://www.writeups.org/wp-content/uploads/Milly-Thompson-Trigun.jpg', # Trigun
    'https://i.stack.imgur.com/HZKzN.jpg' # Katanagatari
]

lottery_list = [
    'https://pre04.deviantart.net/cbe2/th/pre/f/2013/312/2/e/hachikuji_by_kalashnikovkgb-d4m2oul.png',
    'https://images7.alphacoders.com/724/thumb-1920-724896.png',
    'http://imgur.com/RbDCJuc',
    'https://myanimelist.cdn-dena.com/images/characters/2/264877.jpg',
    'http://i.imgur.com/K4Nx28S.jpg',
    'https://formeinfullbloom.files.wordpress.com/2016/12/tsubasa8.png',
    'https://vignette1.wikia.nocookie.net/bakemonogatari1645/images/0/0b/Tsubasa_second_season.jpg/revision/latest/scale-to-width-down/350?cb=20130803141212',
    'https://vignette2.wikia.nocookie.net/nicktheultimaswordwielder/images/d/dc/Tsubasa_profile.jpg/revision/latest?cb=20121220063121',
    'http://pa1.narvii.com/6078/3a2e992c6460fbdc35edbc07585f11a3c2efda2d_hq.gif',
    'http://vignette4.wikia.nocookie.net/bakemonogatari1645/images/7/7c/Owari_kanbaru_2.png/revision/latest?cb=20170106045235'
]

story_list = ['No.', 'Negative.', "I'm not fucking doing that.", 'Denied.', 'Noooooooo', "Noooo no no no no no", 'Negevative']

rip_message = None
rip_count = 0

# various text commands
async def help_cmd(message):
    channel = message.channel
    help_message = """Hedgehog isn't very good yet, but it will do its best!
    **Commands:**
    __hedgehog help__ - *I'll display a list of commands!*
    __tell me a story__ - *I probably won't.*
    __ping__ - *Pong!*
    __rip [@User]__ - *Rest in peace :(*
    __f__ - *Pay respects to a RIP'd user*
    __anichart [season]__ - *I'll pull up the anichart animu list for that season.*
    __bestgirl__ - *Have a randomly-selected best girl picture! Some of them aren't actually best girls though...*
    __waifuwar__ - *Let the Monogatari waifu war begin!*
    """
    await client.send_message(channel, help_message)
    

async def rip_cmd(message):
    global rip_message
    global rip_count
    
    if message.mentions:                # check to see if there are any mentions
        user = message.mentions[0]      # grab the mentioned user
        rip_count = 0
        if int(user.id) in rip_dict:    # customized rip picture
            rip_message = await client.send_message(message.channel, 'Press F to pay respects to ' + user.mention + '.\n' + rip_dict[int(user.id)] )
        else:                           # default rip picture
            rip_message = await client.send_message(message.channel, 'Press F to pay respects to ' + user.mention + '.\n' + rip_dict[0] )
                        
            
# Notes:
# If someone has been ripped at, pressing f will add a counter to that rip.
# Resets every time the bot restarts

async def f_cmd(message):
    global rip_message
    global rip_count
    
    if rip_message:
        if rip_count == 0:      # no counter
            rip_split = rip_message.content.split('\n')
            final_string = rip_split[0] + '\n1 respect paid.\n' + rip_split[1]
            await client.edit_message(rip_message, final_string)
            rip_count = 1
        else:                   # already a counter at 1 or higher
            rip_count += 1
            rip_split = rip_message.content.split('\n')
            final_string = rip_split[0] + '\n' + str(rip_count) + ' respects paid.\n' + rip_split[1]
            await client.edit_message(rip_message, final_string)
        await client.delete_message(message)



async def anichart_cmd(message):
    str_list = message.content.split()
    for word in str_list:
        if word.lower() == 'spring':
            await client.send_message(message.channel, 'http://image.anichart.net/i/Spring.jpg')
        if word.lower() == 'summer':
            await client.send_message(message.channel, 'http://image.anichart.net/i/Summer.jpg')
        if word.lower() == 'fall':
            await client.send_message(message.channel, 'http://image.anichart.net/i/Fall.jpg')
        if word.lower() == 'autumn':
            await client.send_message(message.channel, 'http://image.anichart.net/i/Fall.jpg')
        if word.lower() == 'winter':
            await client.send_message(message.channel, 'http://image.anichart.net/i/Winter.jpg')

async def story_cmd(message):
    await client.send_message(message.channel, random.choice(story_list), tts=True)
    
async def ping_cmd(message):
    d = datetime.utcnow() - message.timestamp   # timedelta object
    s = d.seconds*1000 + d.microseconds//1000
    await client.send_message(message.channel, "Pong!\n({} ms)".format(s))
    

# used for debugging
async def debug_userinfo(message):
    if message.mentions:
        user = message.mentions[0]
        await client.send_message(message.channel, user.mention)
        await client.send_message(message.channel, user.name)
        await client.send_message(message.channel, user.id)
        await client.send_message(message.channel, user.discriminator)
        await client.send_message(message.channel, user.avatar)

# Ready for the bot to make its appearance!
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print("ID:", client.user.id)
    print('------')
    current_game = discord.Game(name='with a ball of twine')
    await client.change_presence(game=current_game, status=None)

    
# messages!
@client.event
async def on_message(message):
    # ping pong
    if message.content.lower().startswith('ping'):
       #await client.send_message(message.channel, 'Pong!')
       await ping_cmd(message)
       
    # tell me a story
    elif message.content.lower().startswith('tell me a story'.lower()):
        await story_cmd(message)
    
    # stupid joke
    elif message.content.lower().startswith('who is the king of sighs'):
        await client.send_message(message.channel, "Kyle")
        
    # rip
    elif message.content.lower().startswith('rip'):
        await rip_cmd(message)
        
    # people pressing f to pay respects
    elif message.content.lower() == 'f':
        await f_cmd(message)

    # anichart
    elif message.content.lower().startswith('anichart'):
        await anichart_cmd(message)
                
    # userinfo
    elif message.content.lower().startswith('userinfo'):
        await debug_userinfo(message)
            
    # bestgirl
    elif message.content.lower().startswith('bestgirl'):
        await client.send_message(message.channel, random.choice(best_girl_list))
        
    # waifu lottery
    elif message.content.lower().startswith('waifuwar' or 'waifu war'):
        await client.send_message(message.channel, random.choice(lottery_list))
        
    # help
    elif message.content.lower().startswith('hedgehog help'):
        await help_cmd(message)



# open token.txt
with open('token.txt', 'r') as f:
    token = f.readline()
    token = token.strip()

client.run(token)
    






