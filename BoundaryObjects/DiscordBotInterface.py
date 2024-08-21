import asyncio
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from CISC699 import logger
from CISC699.config import Config
from CISC699 import css_selectors
from CISC699 import help
from CISC699.EntityObjects.Commands import handle_message  # Import the message handler
from CISC699.help import get_help_message  # Import the help message function
import discord
from discord.ext import commands
from ProductInfoInterface import ProductInfoInterface as PI
from ProductInfoInterface import browser
from DateInfoInterface import DateInfoInterface as DI
from ExcelInterface import ExcelInterface as Ex

# Define the intents your bot will use
intents = discord.Intents.default()
intents.message_content = True  # This enables the bot to read message content

# Initialize the bot with a command prefix and intents
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_message(message):
    await handle_message(bot, message)  # Delegate message handling to Command.py
    #await bot.process_commands(message)  # Ensure commands are processed

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("I don't have that command in my list. Please type `!project_help` to see what I can do.")
    else:
        # Handle all other errors
        await ctx.send(f"I encountered an error: {error}")
        print(f"Error while processing command '{ctx.message.content}': {error}")

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

@bot.command(name='project_help')
async def help_command(ctx):
    await ctx.send(get_help_message())

@bot.command(name='launch_browser')
async def launch_browser(ctx, *args):
    incognito = "incognito" in args
    response = browser.launch_browser(incognito=incognito, user=ctx.author)
    await ctx.send(response)

@bot.command(name='navigate_to_url')
async def navigate_to_url(ctx, url: str):
    response = browser.navigate_to_url(url)
    await ctx.send(response)

@bot.command(name='get_price')
async def get_price(ctx, url: str):
    response = await PI.get_price(ctx, url)
    # No need to send the response here, since it's handled within get_price

@bot.command(name='monitor_price')
async def monitor_price(ctx, url: str, frequency: int = 1):
    await PI.monitor_price(ctx, url, frequency)  # Pass the frequency to the function

@bot.command(name='close_browser')
async def close_browser(ctx):
    response = browser.close_browser()
    await ctx.send(response)

@bot.command(name='stop')
async def stop_command(ctx):
    if ctx.channel.id == Config.CHANNEL_ID:
        await ctx.send("Stopping the bot. Goodbye!")
        await bot.close()  # Gracefully close the bot
    else:
        logger.log_wrong_channel('stop', ctx.author)
        await ctx.send("This command can only be used in the designated channel.")

@bot.command(name='login')
async def login(ctx, site: str, *args):
    incognito = "incognito" in args
    retries = next((int(arg) for arg in args if arg.isdigit()), 1)
    response = await browser.login(site, incognito=incognito, retries=retries)
    await ctx.send(response)

@bot.command(name="check_availability")
async def check_availability(ctx, url: str, date_str: str = None, time_slot: str = None):
    availability_text = await DI.check_availability(url, date_str, time_slot)
    await ctx.send(f"Availability result: {availability_text}")

@bot.command(name='stop_monitoring')
async def stop_monitoring(ctx):
    if ctx.channel.id == Config.CHANNEL_ID:
        PI.stop_monitoring()
        await ctx.send("Monitoring and availability checks have been stopped.")
    else:
        logger.log_wrong_channel('stop_monitoring', ctx.author)
        await ctx.send("This command can only be used in the designated channel.")

# Run the bot with the token from config.py
bot.run(Config.DISCORD_TOKEN)
