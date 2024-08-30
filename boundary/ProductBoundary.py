import discord
from discord.ext import commands
from control.ProductControl import ProductControl

class ProductBoundary(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.product_control = ProductControl()

    @commands.command(name='get_price')
    async def get_price(self, ctx, url: str):
        price = await self.product_control.get_price(url)
        await ctx.send(f"Price: {price}")

    @commands.command(name='monitor_price')
    async def monitor_price(self, ctx, url: str, frequency=1):
        await self.product_control.monitor_price(url, frequency)
        await ctx.send("Started monitoring price.")
