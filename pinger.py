#Libraries Required
import discord
import re
import datetime
import asyncio

token = "TOKEN"
client = discord.Client()

def getChannelIDs():
    channelList = []
    with open ("channelID.txt", "r") as file:
        for id in file:
            channelList.append(int(id.strip()))
    return channelList

channelList = getChannelIDs()

@client.event
async def on_ready():
    print (f"[{datetime.datetime.now()}] Listening for messages on these channels:")
    for x in range(len(channelList)):
        print(channelList[x])

@client.event
async def on_message(message):
    if message.channel.id in channelList:
        if message.author == client.user:
           return
        if message.content.startswith(''):
           print (message.content)
           await message.channel.send(content = "<@&980628909131448390>")

client.run(token)
