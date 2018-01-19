import asyncio
import discord
import discord.ext
import discord.utils
import json

#grab the owner ID from the json
def getOwner():
    with open("data.json") as json_file:
        json_data = json.load(json_file)
        return json_data['Owner']

#grab the token from the json
def getToken():
    with open("data.json") as json_file:
        json_data = json.load(json_file)
        return json_data['Token']

#setting variables...
owner = getOwner()
token = getToken()
client = discord.Client()

#for checking if you're the owner
def is_owner(ctx):
    return ctx.message.author.id == owner

#on connect, it changes presence to "invisible" and then lets you know your client username and user ID
@client.event
async def on_ready():
    await client.change_presence(status= discord.Status.invisible)
    print('Connected!')
    print('Username: ' + client.user.name)
    print('ID: ' + client.user.id)

#if you say "!hello" the bot will respond "Hello" and tag you
@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('!hello'):
        msg = 'Hello {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)

#let's go!
client.run(token)
