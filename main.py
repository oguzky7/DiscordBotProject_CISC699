import discord
from discord.ext import commands
from entity.BrowserEntity import BrowserEntity
from boundary.HelpBoundary import HelpBoundary
from boundary.AccountBoundary import AccountBoundary
from boundary.StopBoundary import StopBoundary  # Import StopBoundary
from boundary.LaunchBrowserBoundary import LaunchBrowserBoundary  # Import BrowserBoundary for browser launch
from boundary.CloseBrowserBoundary import CloseBrowserBoundary  # Import CloseBrowserBoundary for closing browser
#from boundary.LoginBoundary import LoginBoundary 
from boundary.NavigationBoundary import NavigationBoundary  # Import NavigationBoundary for navigating to a URL
from utils.Config import Config

# Set up the bot's intents
intents = discord.Intents.default()
intents.message_content = True  # Enable reading message content

# Initialize the bot with the correct command prefix and intents
class MyBot(commands.Bot):
    async def setup_hook(self):
        browser_entity = BrowserEntity()
        await self.add_cog(HelpBoundary(self))  # Register HelpBoundary
        await self.add_cog(AccountBoundary(self))  # Register AccountBoundary
        await self.add_cog(StopBoundary(self))  # Register StopBoundary
        await self.add_cog(LaunchBrowserBoundary(self, browser_entity))
        await self.add_cog(NavigationBoundary(self, browser_entity))
        await self.add_cog(CloseBrowserBoundary(self, browser_entity))  # Register CloseBrowserBoundary to close browser
        #await self.add_cog(LoginBoundary(self))

    async def on_ready(self):
        # Greet the user when the bot is online
        print(f"Logged in as {self.user}")
        channel = discord.utils.get(self.get_all_channels(), name="general")  # Adjust the channel name
        if channel:
            await channel.send("Hi, I'm online! Type '!project_help' to see what I can do.")

    async def on_command_error(self, ctx, error):
        """Handle unrecognized commands."""
        if isinstance(error, commands.CommandNotFound):
            await ctx.send("Command not recognized. Type !project_help to see the list of commands.")

# Run the bot
if __name__ == "__main__":
    bot = MyBot(command_prefix="!", intents=intents)
    print("Bot is starting...")
    bot.run(Config.DISCORD_TOKEN)  # Run the bot with your token
