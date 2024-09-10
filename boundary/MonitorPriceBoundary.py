from discord.ext import commands
from control.MonitorPriceControl import MonitorPriceControl

class MonitorPriceBoundary(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.monitor_price_control = MonitorPriceControl()

    @commands.command(name="monitor_price")
    async def monitor_price_command(self, ctx, url: str, frequency: int = 1):
        """Command to start monitoring the price of a product."""
        await self.monitor_price_control.start_monitoring(ctx, url, frequency)

    @commands.command(name="stop_monitoring")
    async def stop_monitoring_command(self, ctx):
        """Command to stop monitoring the price."""
        await self.monitor_price_control.stop_monitoring(ctx)
