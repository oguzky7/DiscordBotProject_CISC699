from discord.ext import commands
from control.BrowserControl import BrowserControl

class BrowserBoundary(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.browser_control = BrowserControl()

    @commands.command(name='launch_browser')
    async def launch_browser(self, ctx, *args):
        """Command to launch the browser."""
        await ctx.send("Command recognized, taking action.")  # Acknowledge the command
        incognito = "incognito" in args
        response = self.browser_control.launch_browser(incognito=incognito)
        await ctx.send(response)
