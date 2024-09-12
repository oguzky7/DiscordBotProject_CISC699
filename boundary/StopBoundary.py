from discord.ext import commands
from control.StopControl import StopControl

class StopBoundary(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.control = StopControl()

    @commands.command(name="stop_bot")
    async def stop_bot(self, ctx):
        """Shut down the bot."""
        await ctx.send("Command recognized, taking action: Shutting down the bot.")
        await self.control.stop_bot(ctx, self.bot)  # Call the control's method to stop the bot
