import discord
from discord.ext import commands
from control.ProductControl import ProductControl

class StopMonitoringBoundary(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.product_control = ProductControl()

    @commands.command(name='stop_monitoring')
    async def stop_monitoring(self, ctx):
        self.product_control.stop_monitoring()
        await ctx.send("Stopped monitoring prices.")
