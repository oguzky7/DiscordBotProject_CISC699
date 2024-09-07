import discord
from discord.ext import commands
from boundary.BotBoundary import BotBoundary
from boundary.HelpBoundary import HelpBoundary
from boundary.AccountBoundary import AccountBoundary
from boundary.BrowserBoundary import BrowserBoundary  # Add BrowserBoundary
from boundary.StopBoundary import StopBoundary
from Config import Config

# Set up the bot's intents
intents = discord.Intents.default()
intents.message_content = True  # Enable reading message content

# Initialize the bot with the correct command prefix and intents
class MyBot(commands.Bot):
    async def setup_hook(self):
        await self.add_cog(BotBoundary(self))
        await self.add_cog(HelpBoundary(self))
        await self.add_cog(AccountBoundary(self))
        await self.add_cog(BrowserBoundary(self))  # Add browser-related commands
        await self.add_cog(StopBoundary(self))

# Run the bot
if __name__ == "__main__":
    bot = MyBot(command_prefix="!", intents=intents)
    print(f"Bot is starting...")
    bot.run(Config.DISCORD_TOKEN)
