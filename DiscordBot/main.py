import asyncio
import discord
from discord.ext import commands
from time import sleep

intents = discord.Intents.default()
intents.message_content = True

client = commands.Bot(command_prefix='!',intents=intents)
# bot=commands.Bot(command_prefix='!',intents=intents)


@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('hello'):
        await message.channel.send('bonjour je suis un bot du groupe <@&1021394696754438145>')
    if message.content.startswith('/clear'):
        await message.channel.send('message en cours de suppression !')
        await message.channel.send('.')
        x=0
        while x<=6:
            x+=1
            await message.channel.purge(limit=)
            await message.channel.send(' . '*x)
            sleep(0.2)
        sleep(0.5)
        await message.channel.purge(limit=3)

#↓ ceci est un test↓ 
# @client.command()
# async def clear(ctx, amount = 1):
#     await ctx.channel.purge(limit=amount)
#↑ ceci est un test↑

client.run('NjIyMTI3NzkwMTkxNDExMjEw.G_AA5s.iIXkn7sRI5NVxC_2F2GlWdNjKGQb3whDOJp-Rw')