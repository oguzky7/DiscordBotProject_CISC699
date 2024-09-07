from discord.ext import commands
from control.PriceControl import PriceControl

class PriceBoundary(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.price_control = PriceControl()

    @commands.command(name='get_price')
    async def get_price(self, ctx, url: str):
        """Command to get the price from the given URL."""
        response = await self.price_control.get_price(ctx, url)
        await ctx.send(response)
