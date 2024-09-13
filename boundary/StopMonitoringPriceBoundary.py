from discord.ext import commands
from control.MonitorPriceControl import MonitorPriceControl

class StopMonitoringPriceBoundary(commands.Cog):
    def __init__(self, bot, monitor_price_control):
        self.bot = bot
        self.monitor_price_control = monitor_price_control  # Use shared instance

    @commands.command(name='stop_monitoring_price')
    async def StopMonitoringPrice(self, ctx):
        """Command to stop monitoring the price."""
        await ctx.send("Command recognized, taking action.")
        response = self.monitor_price_control.stop_monitoring()
        await ctx.send(response)
