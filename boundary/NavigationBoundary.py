import discord
from discord.ext import commands
from control.NavigationControl import NavigationControl

class NavigationBoundary(commands.Cog):
    def __init__(self, bot, browser_entity):
        self.bot = bot
        self.navigation_control = NavigationControl(browser_entity)

    @commands.command(name='navigate_to_website')
    async def navigate_to_website(self, ctx, url: str = None):
        await ctx.send("Command recognized, taking action.")
        result = self.navigation_control.navigate_to_website(url)
        await ctx.send(result)
