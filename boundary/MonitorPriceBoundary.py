from discord.ext import commands
from control.MonitorPriceControl import MonitorPriceControl

class MonitorPriceBoundary(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.monitor_price_control = MonitorPriceControl()

    @commands.command(name='monitor_price')
    async def monitor_price(self, ctx, url: str, frequency: int = 1):
        """Command to monitor the price at regular intervals."""
        await self.monitor_price_control.monitor_price(ctx, url, frequency)
