from discord.ext import commands
from control.CloseBrowserControl import CloseBrowserControl

class CloseBrowserBoundary(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.close_browser_control = CloseBrowserControl()

    @commands.command(name='close_browser')
    async def close_browser(self, ctx):
        """Command to close the browser."""
        response = self.close_browser_control.close_browser()
        await ctx.send(response)
