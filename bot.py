import discord
from discord.ext import commands
from browser_interface import BrowserInterface
from config import Config  # Import the Config class from config.py

# Define the intents your bot will use
intents = discord.Intents.default()
intents.message_content = True  # This enables the bot to read message content

# Initialize the bot with a command prefix and intents
bot = commands.Bot(command_prefix='!', intents=intents)

# Initialize the browser interface
browser = BrowserInterface()

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

@bot.command(name='launch_browser')
async def launch_browser(ctx):
    # Command to launch the browser
    try:
        browser.launch_browser()
        await ctx.send("Chrome browser launched successfully.")
    except Exception as e:
        await ctx.send(f"Failed to launch browser: {e}")

@bot.command(name='navigate_to_url')
async def navigate_to_url(ctx, url: str):
    # Command to navigate to a specific URL, launches browser if not already running
    try:
        browser.navigate_to_url(url)
        await ctx.send(f"Navigated to URL: {url}")
    except Exception as e:
        await ctx.send(f"Failed to navigate: {e}")

@bot.command(name='login')
async def login(ctx, username: str, password: str, username_field_id: str, password_field_id: str, login_button_xpath: str):
    # Command to perform login
    try:
        browser.login(username, password, username_field_id, password_field_id, login_button_xpath)
        await ctx.send(f"Logged in with username: {username}")
    except Exception as e:
        await ctx.send(f"Failed to log in: {e}")

@bot.command(name='close_browser')
async def close_browser(ctx):
    # Command to close the browser
    try:
        browser.close_browser()
        await ctx.send("Browser closed successfully.")
    except Exception as e:
        await ctx.send(f"Failed to close browser: {e}")

# Run the bot with the token from config.py
bot.run(Config.DISCORD_TOKEN)
