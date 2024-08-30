import discord
from discord.ext import commands
from BrowserControl import BrowserControl

class LoginBoundary(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.browser_control = BrowserControl()

    @commands.command(name='login')
    async def login(self, ctx, site: str, username: str, password: str, incognito=False):
        result = await self.browser_control.login(site, username, password, incognito)
        await ctx.send(result)
