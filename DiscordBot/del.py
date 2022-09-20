import asyncio
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)
client = commands.Bot(command_prefix='!',intents=intents)

@client.command(name='clear', help='this command will clear msgs')
async def clear(ctx, amount = 1):
    await ctx.channel.purge(limit=amount)

client.run('NjIyMTI3NzkwMTkxNDExMjEw.G_AA5s.iIXkn7sRI5NVxC_2F2GlWdNjKGQb3whDOJp-Rw')