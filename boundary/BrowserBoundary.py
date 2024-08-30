import discord
from discord.ext import commands
from BrowserControl import BrowserControl

class BrowserBoundary(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.browser_control = BrowserControl()

    @commands.command(name='launch_browser')
    async def launch_browser(self, ctx, incognito=False):
        result = self.browser_control.launch_browser(incognito)
        await ctx.send(result)

    @commands.command(name='close_browser')
    async def close_browser(self, ctx):
        result = self.browser_control.close_browser()
        await ctx.send(result)

    @commands.command(name='navigate_to_url')
    async def navigate_to_url(self, ctx, url: str):
        result = self.browser_control.navigate_to_url(url)
        await ctx.send(result)
