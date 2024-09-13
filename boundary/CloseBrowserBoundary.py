from discord.ext import commands
from control.CloseBrowserControl import CloseBrowserControl
from entity.BrowserEntity import BrowserEntity

class CloseBrowserBoundary(commands.Cog):
    def __init__(self, bot, browser_entity):
        self.bot = bot
        self.close_browser_control = CloseBrowserControl(browser_entity)  # Pass the browser_entity to the control

    @commands.command(name='close_browser')
    async def close_browser(self, ctx):
        await ctx.send("Command recognized, taking action to close the browser.")
        result = self.close_browser_control.close_browser()
        await ctx.send(result)
