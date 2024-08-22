from datetime import datetime
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
from ExcelInterface import ExcelInterface
from BrowserInterface import BrowserInterface

ex = Ex()
pi = PI()

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

@bot.command(name='get_price')
async def get_price(ctx, url: str):
    result, excel_msg, html_msg = await pi.get_price(ctx, url)
    await ctx.send(f"Price for {url}: {result}")
    await ctx.send(excel_msg)
    await ctx.send(html_msg)

@bot.command(name='monitor_price')
async def monitor_price(ctx, url: str, frequency: int = 1):
    excel_msg, html_msg = await pi.monitor_price(ctx, url, frequency)
    await ctx.send(excel_msg)
    await ctx.send(html_msg)

@bot.command(name='launch_browser')
async def launch_browser(ctx, *args):
    incognito = "incognito" in args
    response = browser.launch_browser(incognito=incognito, user=ctx.author)
    excel_msg, html_msg = PI.excel_interface.log_and_save('launch_browser', "N/A", response, browser)
    await ctx.send(response)
    await ctx.send(excel_msg)
    await ctx.send(html_msg)

@bot.command(name='navigate_to_url')
async def navigate_to_url(ctx, url: str):
    response = browser.navigate_to_url(url)

    # Log and save the result
    excel_msg, html_msg = ex.log_and_save('navigate_to_url', url, response, browser)

    await ctx.send(response)
    await ctx.send(excel_msg)
    await ctx.send(html_msg)

@bot.command(name='close_browser')
async def close_browser(ctx):
    response = browser.close_browser()

    # Log and save the result
    excel_msg, html_msg = ex.log_and_save('close_browser', 'N/A', response, browser)

    await ctx.send(response)
    await ctx.send(excel_msg)
    await ctx.send(html_msg)

@bot.command(name='stop')
async def stop_command(ctx):
    await ctx.send("Stopping the bot. Goodbye!")
    await bot.close()  # Gracefully close the bot

@bot.command(name='login')
async def login(ctx, site: str, *args):
    incognito = "incognito" in args
    retries = next((int(arg) for arg in args if arg.isdigit()), 1)
    response = await browser.login(site, incognito=incognito, retries=retries)

    # Log and save the result
    excel_msg, html_msg = ex.log_and_save('login', site, response, browser)

    await ctx.send(response)
    await ctx.send(excel_msg)
    await ctx.send(html_msg)

@bot.command(name="check_availability")
async def check_availability(ctx, url: str, date_str: str = None, time_slot: str = None):
    availability_text = await DI.check_availability(ctx, url, date_str, time_slot)

    # Log and save the result
    excel_msg, html_msg = ex.log_and_save('check_availability', url, availability_text, browser)

    await ctx.send(f"Availability result: {availability_text}")
    await ctx.send(excel_msg)
    await ctx.send(html_msg)

@bot.command(name='stop_monitoring')
async def stop_monitoring(ctx):
        PI.stop_monitoring()
        # Log and save the result
        excel_msg, html_msg = ex.log_and_save('stop_monitoring', 'N/A', 'Monitoring stopped', browser)
        await ctx.send("Monitoring and availability checks have been stopped.")
        await ctx.send(excel_msg)
        await ctx.send(html_msg)

# Run the bot with the token from config.py
bot.run(Config.DISCORD_TOKEN)
