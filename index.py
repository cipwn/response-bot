#!/usr/bin/env python3
import os
import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('YOUR BOT TOKEN HERE')

client = discord.Client()
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == '!input':
        response = 'output.'
        await message.channel.send(response)

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord')
client.run('YOUR BOT TOKEN HERE')
