from discord.ext import commands
from control.MonitorPriceControl import MonitorPriceControl

class MonitorPriceBoundary(commands.Cog):
    def __init__(self, bot, browser_entity):
        self.bot = bot
        self.monitor_price_control = MonitorPriceControl(browser_entity)

    @commands.command(name='start_monitoring_price')
    async def start_monitoring_price(self, ctx, url: str = None, frequency: int = 20):        
        await ctx.send(f"Command recognized, starting price monitoring at {url} every {frequency} second(s).")
        response = await self.monitor_price_control.start_monitoring_price(ctx, url, frequency)
        await ctx.send(response)
