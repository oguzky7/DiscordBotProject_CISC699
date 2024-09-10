from discord.ext import commands
from control.LoginControl import LoginControl

class LoginBoundary(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.login_control = LoginControl()

    @commands.command(name='login')
    async def login(self, ctx, site: str, *args):
        """Command to log into a website using stored credentials."""
        incognito = "incognito" in args
        retries = next((int(arg) for arg in args if arg.isdigit()), 1)
        response = await self.login_control.login(site, incognito, retries)
        await ctx.send(response)
