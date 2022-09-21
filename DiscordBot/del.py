import asyncio
from pydoc import cli
import discord
from discord.ext import commands
from time import sleep

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)
client = commands.Bot(command_prefix='!',intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.command(name='clear', help='this command will clear msgs')
async def clear(ctx, amount = 1):
    await ctx.channel.send(f'suppression de {amount} messages')
    print(ctx)
    sleep(0.4)
    x=0
    egal=["="]
    while x<=amount:
            x+=1
            # await ctx.channel.send(' - '*x)
            if x>amount:
                await ctx.channel.send('='*x+'>')
            else:
                egal=egal.append("="*x)
                await ctx.channel.send(egal)
            sleep(0.2)

    await ctx.channel.purge(limit=amount)


# @bot.command()
# async def test(ctx, arg):
#     await ctx.send(arg)
#     print(ctx,arg)

#reponds au mention du bot uniquement
# @client.event
# async def on_message(ctx):
    
#     if ctx.author == client.user:
#         return

#     if ctx.content.startswith('hello'):
#         await ctx.channel.send('bonjour je suis un bot du groupe <@&1021394696754438145>')
#         print(ctx)
#     if ctx.content.startswith('nice to meet'):
#         await ctx.channel.send('nice to meet you too mister woman')

client.run('NjIyMTI3NzkwMTkxNDExMjEw.G_AA5s.iIXkn7sRI5NVxC_2F2GlWdNjKGQb3whDOJp-Rw')