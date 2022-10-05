import asyncio
from mimetypes import common_types
import discord
from discord.ext import commands
from time import sleep
from config import *
import random

intents = discord.Intents.default()
intents.message_content = True

client = commands.Bot(command_prefix=PREFIX,intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('hello') or message.content.startswith('Hello') or message.content.startswith('bonjour') or message.content.startswith('Bonjour') or message.content.startswith('slt') or message.content.startswith('Salut') or message.content.startswith('Salut') or message.content.startswith('salut') :
        r=random.randrange(0,20)
        if r<=10:
            await message.channel.send('bonjour je suis un bot du groupe <@&1021394696754438145>')
        elif r>10:
            await message.channel.send('Bonjour jeune padawan')
        else :
            await message.channel.send('non')
    if message.content.startswith('non') or message.content.startswith('non'):
        await message.channel.send("Si")
    if message.content.startswith("Ta gueule") or message.content.startswith("TG") or message.content.startswith("tg") or message.content.startswith('Tg') or message.content.startswith('tG') or message.content.startswith("TA GUEULE"): 
        await message.channel.send("Les insultes sont interdites ici")
    await client.process_commands(message)

@client.command()
async def clear(ctx, amount=2):
        '''Supprime les messages par defaut 2 pour plus d'info !help clear'''
        if not amount : 
            return await ctx.send("Erreur\nVous n'avez pas donner de valeur.")
        await ctx.channel.send(f'suppression de {amount} messages')
        sleep(0.4)
        await ctx.channel.purge(limit=amount)

# @client.command()
# async def test(ctx):
#     await ctx.send("Hello world !")

@client.command()
async def hello(ctx):
    '''Ceci est une commande de test'''
    await ctx.send('Hello')

@client.command()
async def deprime(ctx):
    '''Tu deprimes ? tape cette commande elle va te faire sourrire'''
    await ctx.send('Il est temps de sourire !!! :)')

@client.command()
async def blowjob(ctx):
    '''une commande nsfw'''
    await ctx.send('non pas ici -_-')

@client.command()
async def  RS(ctx):
        '''Accueil de communauté'''
        await ctx.send('RS est une communauté complete prete a vous accueillir')

@client.command()
async def jmennui (ctx):
    '''Toi aussi tu t'ennui , tape cette commande et une surprise va venir'''
    await ctx.send("ne t'inquietes pas moi aussi")

@client.command()
async def NSFW(ctx):
    '''Commande global pour les NSFW commandes'''
    await ctx.send("Arrive prochainement !!")
    


client.run('NjIyMTI3NzkwMTkxNDExMjEw.G_AA5s.iIXkn7sRI5NVxC_2F2GlWdNjKGQb3whDOJp-Rw')
