from discord.ext import commands
from control.HelpControl import HelpControl

class HelpBoundary(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.help_control = HelpControl()

    @commands.command(name='project_help')
    async def project_help(self, ctx):
        """Handles the project_help command."""
        help_message = self.help_control.get_help_message()
        await ctx.send(help_message)
