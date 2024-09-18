import discord
from discord.ext import commands
from entity.BrowserEntity import BrowserEntity
from boundary.HelpBoundary import HelpBoundary
from boundary.AccountBoundary import AccountBoundary
from boundary.StopBoundary import StopBoundary
from boundary.BrowserBoundary import BrowserBoundary
from boundary.LoginBoundary import LoginBoundary
from boundary.NavigationBoundary import NavigationBoundary
from boundary.GetPriceBoundary import GetPriceBoundary
from boundary.MonitorPriceBoundary import MonitorPriceBoundary
from boundary.StopMonitoringPriceBoundary import StopMonitoringPriceBoundary
from control.MonitorPriceControl import MonitorPriceControl
from control.MonitorAvailabilityControl import MonitorAvailabilityControl
from boundary.CheckAvailabilityBoundary import CheckAvailabilityBoundary
from boundary.MonitorAvailabilityBoundary import MonitorAvailabilityBoundary

class MyBot(commands.Bot):
    async def setup_hook(self):
        browser_entity = BrowserEntity()
        monitor_price_control = MonitorPriceControl(browser_entity)
        monitor_availibility_control = MonitorAvailabilityControl(browser_entity)

        # Register all the boundaries (commands)
        await self.add_cog(HelpBoundary(self))
        await self.add_cog(AccountBoundary(self))
        await self.add_cog(StopBoundary(self))
        await self.add_cog(BrowserBoundary(self))
        await self.add_cog(NavigationBoundary(self))
        await self.add_cog(LoginBoundary(self, browser_entity))
        await self.add_cog(GetPriceBoundary(self, browser_entity))
        await self.add_cog(MonitorPriceBoundary(self, monitor_price_control))
        await self.add_cog(StopMonitoringPriceBoundary(self, monitor_price_control))
        await self.add_cog(CheckAvailabilityBoundary(self, browser_entity))
        await self.add_cog(MonitorAvailabilityBoundary(self, monitor_availibility_control))

    async def on_ready(self):
        print(f"Logged in as {self.user}")
        channel = discord.utils.get(self.get_all_channels(), name="general")  # Adjust the channel name if needed
        if channel:
            await channel.send("Hi, I'm online! Type '!project_help' to see what I can do.")

    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.CommandNotFound):
            await ctx.send("Command not recognized. Type !project_help to see the list of commands.")
