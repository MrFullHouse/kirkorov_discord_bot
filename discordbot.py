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
phrasesOne=['Добрый вечер <:lambert:887347067742208011>','Добрый вечер <:lambert:887347067742208011>','Умей проигрывать дружок, ты проиграл <:Murlock_Jokir:874544048029978664>','Может еще сюда нажмёшь: \n<https://www.youtube.com/watch?v=dQw4w9WgXcQ> <:murlockCoolStory:878462386749714492>','Ты пойман за руку, дешёвка','<a:orchesterDrums:886604700110159924> <a:orchesterGuitar:886604700714152026> <a:orchesterMex:886604700626079804> <a:orchesterMicro:886604700449898576> <a:orchesterPiano:886604700642844672> <a:orchesterSax:886604700613509191>']
phrasesTwo=['Я почувствовал что ты сделал это специально <a:noNoppersDisagree:842113425924161588> ','Пахнет обманом <:Murlock_Jokir:874544048029978664>','На этот раз без штрафа но будьте осторожны <:Adolfik:877277880697122847>']

@client.event
@asyncio.coroutine
def on_message(message):
    scenario = random.randint(1, 10)
    if message.author == client.user:
        return
    if message.content.lower() == 'да':
        if scenario in (2,3,4):
            phrase=random.choice(phrasesOne)
            p=client.get_emoji(837420439553966100)
            i=client.get_emoji(837420438690463805)
            z=client.get_emoji(837420439533256714)
            d=client.get_emoji(837420439215013909)
            a=client.get_emoji(837420439843897410)
            yield from message.reply(phrase, mention_author=False)
            yield from message.add_reaction(p)
            yield from message.add_reaction(i)
            yield from message.add_reaction(z)
            yield from message.add_reaction(d)
            yield from message.add_reaction(a)
        if scenario in (5,6,7,8,9,10):
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
        if scenario == 1:
            phrase=random.choice(phrasesTwo)
            yield from message.reply(phrase, mention_author=True)
    if message.content.lower() == 'пизда':
          d=client.get_emoji(837420439215013909)
          a=client.get_emoji(837420439843897410)
          yield from message.add_reaction(d)
          yield from message.add_reaction(a)
client.run(token)
