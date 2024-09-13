from discord.ext import commands
from control.HelpControl import HelpControl

class HelpBoundary(commands.Cog):  # Cog to register with the bot
    def __init__(self, bot):
        self.bot = bot
        self.control = HelpControl()  # Initialize control object

    @commands.command(name="project_help")
    async def project_help(self, ctx):
        """Send a message with all the available commands."""
        await ctx.send("Command recognized, taking action.")
        response = self.control.get_help_message()
        await ctx.send(response)
