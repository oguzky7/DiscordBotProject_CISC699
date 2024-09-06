import discord
from discord.ext import commands
from boundary.BotBoundary import BotBoundary
from boundary.HelpBoundary import HelpBoundary
from boundary.ChatBoundary import ChatBoundary
from boundary.AccountBoundary import AccountBoundary  # Add this

from Config import Config

# Set up the bot's intents
intents = discord.Intents.default()
intents.message_content = True  # Enable reading message content

# Initialize the bot with the correct command prefix and intents
class MyBot(commands.Bot):
    async def setup_hook(self):
        await self.add_cog(BotBoundary(self))  # General bot boundary
        await self.add_cog(HelpBoundary(self))  # Help-related boundary
        await self.add_cog(ChatBoundary(self))  # Chat-related boundary
        await self.add_cog(AccountBoundary(self))  # Account-related boundary

# Run the bot
if __name__ == "__main__":
    bot = MyBot(command_prefix="!", intents=intents)
    print(f"Bot is starting...")
    
    bot.run(Config.DISCORD_TOKEN)   # Run the bot and connect to Discord
