import asyncio
import discord
from discord.ext import commands
from time import sleep
from config import *

intents = discord.Intents.default()
intents.message_content = True

client = commands.Bot(command_prefix=PREFIX,intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.command()
async def clear(ctx, amount=1):
        if not amount : 
            return await ctx.send("Erreur\nVous n'avez pas donner de valeur.")
        await ctx.channel.send(f'suppression de {amount} messages')
        sleep(0.4)
        await ctx.channel.purge(limit=amount)

@client.command()
async def test(ctx):
    await ctx.send("Hello world !")

client.run('NjIyMTI3NzkwMTkxNDExMjEw.G_AA5s.iIXkn7sRI5NVxC_2F2GlWdNjKGQb3whDOJp-Rw')
