from discord.ext import commands
from control.NavigationControl import NavigationControl

class NavigationBoundary(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.navigation_control = NavigationControl()

    @commands.command(name='navigate_to_website')
    async def navigate_to_website(self, ctx, url: str):
        """Command to navigate to a specified URL."""
        response = self.navigation_control.navigate_to_url(url)
        await ctx.send(response)
