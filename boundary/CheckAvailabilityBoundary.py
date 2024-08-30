import discord
from discord.ext import commands
from control.DateControl import DateControl

class CheckAvailabilityBoundary(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.date_control = DateControl()

    @commands.command(name='check_availability')
    async def check_availability(self, ctx, url: str, date_str: str = None, time_slot: str = None):
        result = await self.date_control.check_availability(url, date_str, time_slot)
        await ctx.send(f"Availability result: {result}")
