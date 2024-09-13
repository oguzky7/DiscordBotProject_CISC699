from discord.ext import commands
from control.LoginControl import LoginControl

class LoginBoundary(commands.Cog):
    def __init__(self, bot, browser_entity):
        self.bot = bot
        self.login_control = LoginControl(browser_entity)  # Pass browser_entity to control

    @commands.command(name='login')
    async def login(self, ctx, site: str):
        await ctx.send("Command recognized, taking action.")
        result = await self.login_control.login(site)
        await ctx.send(result)
