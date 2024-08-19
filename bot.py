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
        await message.channel.send(f"Message recognized: {message.content}")

    if not recognized:
        logger.log_message_not_recognized()
        await message.channel.send("Message not recognized as a command. Type `!commands` to see possible actions.")

@bot.command(name='launch_browser')
async def launch_browser(ctx, *args):
    incognito = "incognito" in args
    response = cmd.launch_browser(ctx, incognito=incognito)
    await ctx.send(response)

@bot.command(name='navigate_to_url')
async def navigate_to_url(ctx, url: str):
    response = cmd.navigate_to_url(ctx, url)
    await ctx.send(response)

@bot.command(name='get_price')
async def get_price(ctx, url: str):
    response = await cmd.get_price(ctx, url)
    # No need to send the response here, since it's handled within get_price

@bot.command(name='monitor_price')
async def monitor_price(ctx, url: str):
    await cmd.monitor_price(ctx, url)  # Ensure this calls the function from commands.py

@bot.command(name='login')
async def login(ctx, url: str):
    response = cmd.login(ctx, url)
    await ctx.send(response)

@bot.command(name='close_browser')
async def close_browser(ctx):
    response = cmd.close_browser(ctx)
    await ctx.send(response)

@bot.command(name='commands')
async def commands_command(ctx):
    await ctx.send(help.get_help_message())

@bot.command(name='stop')
async def stop_command(ctx):
    if ctx.channel.id == Config.CHANNEL_ID:
        await ctx.send("Stopping the bot. Goodbye!")
        sys.exit(0)
    else:
        logger.log_wrong_channel('stop', ctx.author)
        await ctx.send("This command can only be used in the designated channel.")

# Run the bot with the token from config.py
bot.run(Config.DISCORD_TOKEN)
