import discord
from discord.ext import commands

class StopBoundary(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='stop')
    async def stop(self, ctx):
        await ctx.send("Stopping the bot. Goodbye!")
        await self.bot.close()
