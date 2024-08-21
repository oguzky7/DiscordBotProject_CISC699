import asyncio
from discord.ext import commands
from CISC699 import logger
from CISC699.help import get_help_message  # Assuming get_help_message is a function in your help module

# Function to handle messages
async def handle_message(bot, message):
    if message.author == bot.user:
        return  # Ignore messages from the bot itself

    # Log the received message
    logger.log_message_received(message)
    
    if message.content.startswith('!'):
        try:
            # Process the command
            await message.channel.send("Message recognized as a command. Taking Action")
            await bot.process_commands(message)
            logger.log_message_recognized()
            
        except commands.CommandNotFound:
            await message.channel.send("I didn't understand that. Please type `!project_help` to see what I can do.")
            logger.log_message_not_recognized()
        except Exception as e:
            logger.log_message_not_recognized()
            await message.channel.send(f"Failed to execute command '{message.content}': {e}")
            print(f"Failed to execute command '{message.content}': {e}")

    else:
        # Respond to greetings
        if message.content.lower() in ["hello", "hi", "hey"]:
            await message.channel.send("Hello! How can I assist you today? Type `!project_help` or `!commands` to see what I can do.")
        else:
            await message.channel.send("I didn't understand that. Please type `!project_help` to see what I can do.")