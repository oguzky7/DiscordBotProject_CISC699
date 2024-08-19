import discord
from discord.ext import commands
import sys
import commands as cmd  # Import the commands module
import help
import logger
from config import Config

# Define the intents your bot will use
intents = discord.Intents.default()
intents.message_content = True  # This enables the bot to read message content

# Initialize the bot with a command prefix and intents
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return  # Ignore messages from the bot itself

    # Log the received message
    logger.log_message_received(message)

    # Greet the user if they say "Hello", "Hi", or "Hey"
    if message.content.lower() in ["hello", "hi", "hey"]:
        await message.channel.send(f"Hello, {message.author.name}! How can I help you? If you want to see what I can do, type `!commands`.")
        return

    # Check if the message is a recognized command
    recognized = False

    if message.content.startswith('!'):
        recognized = True
        await bot.process_commands(message)
        logger.log_message_recognized()

    if not recognized:
        logger.log_message_not_recognized()
        await message.channel.send("Message not recognized as a command. Type `!commands` to see possible actions.")

@bot.command(name='launch_browser')
async def launch_browser(ctx, *args):
    incognito = "incognito" in args
    await cmd.launch_browser(ctx, incognito=incognito)


@bot.command(name='navigate_to_url')
async def navigate_to_url(ctx, url: str):
    await cmd.navigate_to_url(ctx, url)

@bot.command(name='get_price')
async def get_price(ctx, url: str):
    await cmd.get_price(ctx, url)

@bot.command(name='login')
async def login(ctx, url: str, username: str, password: str):
    await cmd.login(ctx, url, username, password)

@bot.command(name='close_browser')
async def close_browser(ctx):
    await cmd.close_browser(ctx)

@bot.command(name='commands')
async def commands_command(ctx):
    await cmd.send_help_message(ctx.channel)

@bot.command(name='monitor_price')
async def monitor_price(ctx, url: str):
    await ctx.send(f"Started monitoring price for: {url}")
    await cmd.monitor_price(ctx, url)

@bot.command(name='stop')
async def stop_command(ctx):
    if ctx.channel.id == Config.CHANNEL_ID:
        await cmd.send_stop_message(ctx.channel)
        sys.exit(0)
    else:
        logger.log_wrong_channel('stop', ctx.author)
        await ctx.send("This command can only be used in the designated channel.")

# Run the bot with the token from config.py
bot.run(Config.DISCORD_TOKEN)
