import discord
from discord.ext import commands
from entity.BrowserEntity import BrowserEntity
from boundary.HelpBoundary import HelpBoundary
from boundary.AccountBoundary import AccountBoundary
from boundary.StopBoundary import StopBoundary  # Import StopBoundary
from boundary.BrowserBoundary import BrowserBoundary  # Import BrowserBoundary for browser launch
from boundary.LoginBoundary import LoginBoundary 
from boundary.NavigationBoundary import NavigationBoundary  # Import NavigationBoundary for navigating to a URL
from boundary.GetPriceBoundary import GetPriceBoundary
from boundary.MonitorPriceBoundary import MonitorPriceBoundary
from boundary.StopMonitoringPriceBoundary import StopMonitoringPriceBoundary
from control.MonitorPriceControl import MonitorPriceControl
from control.MonitorAvailabilityControl import MonitorAvailabilityControl
from boundary.CheckAvailabilityBoundary import CheckAvailabilityBoundary  # Import for check_availability
from boundary.MonitorAvailabilityBoundary import MonitorAvailabilityBoundary 
from utils.Config import Config

# Set up the bot's intents
intents = discord.Intents.default()
intents.message_content = True  # Enable reading message content

# Initialize the bot with the correct command prefix and intents
class MyBot(commands.Bot):
    async def setup_hook(self):
        browser_entity = BrowserEntity()
         # Create a single instance of MonitorPriceControl
        monitor_price_control = MonitorPriceControl(browser_entity)
        monitor_availibility_control = MonitorAvailabilityControl(browser_entity)
        await self.add_cog(HelpBoundary(self))  # Register HelpBoundary
        await self.add_cog(AccountBoundary(self))  # Register AccountBoundary
        await self.add_cog(StopBoundary(self))  # Register StopBoundary
        await self.add_cog(BrowserBoundary(self))
        await self.add_cog(NavigationBoundary(self))
        await self.add_cog(LoginBoundary(self, browser_entity))
        await self.add_cog(GetPriceBoundary(self, browser_entity)) 
        await self.add_cog(MonitorPriceBoundary(self, monitor_price_control))
        await self.add_cog(StopMonitoringPriceBoundary(self, monitor_price_control))
        await self.add_cog(CheckAvailabilityBoundary(self, browser_entity))  # Register CheckAvailabilityBoundary
        await self.add_cog(MonitorAvailabilityBoundary(self, monitor_availibility_control)) 
        
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
