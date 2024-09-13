from discord.ext import commands
from control.MonitorPriceControl import MonitorPriceControl

class StopMonitoringBoundary(commands.Cog):
    def __init__(self, bot, browser_entity):
        self.bot = bot
        self.monitor_price_control = MonitorPriceControl(browser_entity)

    @commands.command(name='stop_monitoring')
    async def stop_monitoring(self, ctx):
        """Command to stop monitoring the price."""
        response = self.monitor_price_control.stop_monitoring()
        await ctx.send(response)
