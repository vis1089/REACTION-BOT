import discord
from discord.ext import commands

# Create a bot instance with a command prefix
bot = commands.Bot(command_prefix='/')

# Define a command to start the bot
@bot.command(name='start', help='Start the bot')
async def start(ctx):
    await ctx.send('Hello! I am your reaction bot. Type /react to see a reaction.')

# Define a command to trigger a reaction
@bot.command(name='react', help='React to the command')
async def react(ctx):
    await ctx.send('Reacting to your command! 😄')

# Run the bot with the bot token
bot.run('MTE3ODkwNjY4NTY3MTIzMTU1OA.GPPluy.kP3lqw3-_3jZfE-ehndot3x3g09j7ZhakDgk_E')
