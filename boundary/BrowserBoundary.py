from discord.ext import commands
from control.BrowserControl import BrowserControl

class BrowserBoundary(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.browser_control = BrowserControl()

    @commands.command(name='launch_browser')
    async def launch_browser(self, ctx, *args):
        """Command to launch the browser."""
        incognito = "incognito" in args
        response = self.browser_control.launch_browser(ctx.author, incognito)
        await ctx.send(response)

    @commands.command(name='navigate_to_website')
    async def navigate_to_website(self, ctx, url: str):
        """Command to navigate to a specific URL."""
        response = self.browser_control.navigate_to_url(url)
        await ctx.send(response)

    @commands.command(name='login')
    async def login(self, ctx, site: str, *args):
        """Command to log into a website using stored credentials."""
        incognito = "incognito" in args
        retries = next((int(arg) for arg in args if arg.isdigit()), 1)
        response = await self.browser_control.login(site, incognito, retries)
        await ctx.send(response)
