import discord
from discord.ext import commands
from Config import Config  # Importing the configuration (Discord token, etc.)
from boundary.BotBoundary import BotBoundary  # Importing the boundary for bot commands

# Initialize the Discord bot with appropriate intents
intents = discord.Intents.default()
intents.message_content = True  # Allow reading message content

bot = commands.Bot(command_prefix='!', intents=intents)  # Set up bot with a command prefix

# Registering boundary objects (cogs)
bot.add_cog(BotBoundary(bot))  # Register the bot boundary for handling commands

# Start the bot using the token from the config file
if __name__ == "__main__":
    bot.run(Config.DISCORD_TOKEN)
