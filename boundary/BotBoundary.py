from discord.ext import commands
from control.BotControl import BotControl

class BotBoundary(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.bot_control = BotControl(bot)

    @commands.Cog.listener()
    async def on_ready(self):
        """Event that triggers when the bot is ready."""
        print(f'Logged in as {self.bot.user}')
        await self.bot_control.send_greeting()

    @commands.command(name='project_help')
    async def project_help(self, ctx):
        """Handles the !project_help command."""
        await self.bot_control.send_help(ctx)
