from discord.ext import commands
from control.GetPriceControl import GetPriceControl

class GetPriceBoundary(commands.Cog):
    def __init__(self, bot, browser_entity):
        self.bot = bot
        self.price_control = GetPriceControl(browser_entity)

    @commands.command(name='get_price')
    async def get_price(self, ctx, url: str=None):
        """Command to get the price from the given URL."""
        await ctx.send("Command recognized, taking action.")
        response = await self.price_control.get_price(url)
        await ctx.send(response)
