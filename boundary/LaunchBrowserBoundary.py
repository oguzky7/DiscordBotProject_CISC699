from discord.ext import commands
from control.LaunchBrowserControl import LaunchBrowserControl

class LaunchBrowserBoundary(commands.Cog):
    def __init__(self, bot, browser_entity):
        self.bot = bot
        self.launch_browser_control = LaunchBrowserControl(browser_entity)  # Pass the browser_entity to the control

    @commands.command(name='launch_browser')
    async def launch_browser(self, ctx):
        await ctx.send("Command recognized, taking action.")
        result = self.launch_browser_control.launch_browser()
        await ctx.send(result)
