from discord.ext import commands
from control.LoginControl import LoginControl

class LoginBoundary(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.login_control = LoginControl()

    @commands.command(name='login')
    async def login(self, ctx, website: str):
        """Command to log into a website using stored credentials."""
        await ctx.send(f"Attempting to log in to {website}...")

        # Delegate the logic to the control layer
        response = await self.login_control.login(website)
        await ctx.send(response)
