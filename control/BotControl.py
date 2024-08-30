import discord
from discord.ext import commands
from Config import Config

class BotControl(commands.Bot):
    def __init__(self):
        # Define the intents
        intents = discord.Intents.default()

        # Initialize the bot with the command prefix and intents
        super().__init__(command_prefix='!', intents=intents)

    async def setup_hook(self):
        # Registering boundary objects (cogs) in the setup hook
        from boundary.HelpBoundary import HelpBoundary
        from boundary.LoginBoundary import LoginBoundary
        from boundary.BrowserBoundary import BrowserBoundary
        from boundary.ProductBoundary import ProductBoundary
        from boundary.CheckAvailabilityBoundary import CheckAvailabilityBoundary
        from boundary.StopMonitoringBoundary import StopMonitoringBoundary
        from boundary.StopBoundary import StopBoundary
        from boundary.DatabaseBoundary import DatabaseBoundary

        await self.add_cog(HelpBoundary(self))
        await self.add_cog(LoginBoundary(self))
        await self.add_cog(BrowserBoundary(self))
        await self.add_cog(ProductBoundary(self))
        await self.add_cog(CheckAvailabilityBoundary(self))
        await self.add_cog(StopMonitoringBoundary(self))
        await self.add_cog(StopBoundary(self))
        await self.add_cog(DatabaseBoundary(self))

    def run(self):
        # Start the bot using the token from the Config class
        super().run(Config.DISCORD_TOKEN)

    async def shutdown(self):
        # Gracefully shutdown the bot
        await self.close()
