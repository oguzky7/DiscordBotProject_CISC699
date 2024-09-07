from discord.ext import commands
from control.BotControl import BotControl

class StopBoundary(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.bot_control = BotControl(bot)

    @commands.command(name="stop_bot")
    async def stop_bot(self, ctx):
        """Handles the stop command and gracefully shuts down the bot."""
        await ctx.send("Stopping the bot...")
        await self.bot_control.stop_bot()
