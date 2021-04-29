import asyncio
import discord
from discord.ext import commands
import json
import subprocess
import os
import datetime
import requests
import re
import random
from string import punctuation
import time

client = discord.Client()

with open('config.json') as config_data:
    config_json = json.load(config_data)
    token = config_json['discord_token']
emojis=[]

@client.event
@asyncio.coroutine
def on_message(message):
    if message.author == client.user:
        return
    if message.content.lower() == 'да':
        p=client.get_emoji(837420439553966100)
        i=client.get_emoji(837420438690463805)
        z=client.get_emoji(837420439533256714)
        d=client.get_emoji(837420439215013909)
        a=client.get_emoji(837420439843897410)
        yield from message.add_reaction(p)
        yield from message.add_reaction(i)
        yield from message.add_reaction(z)
        yield from message.add_reaction(d)
        yield from message.add_reaction(a)
    if message.content.lower() == 'пизда':
        d=client.get_emoji(837420439215013909)
        a=client.get_emoji(837420439843897410)
        yield from message.add_reaction(d)
        yield from message.add_reaction(a)

client.run(token)
