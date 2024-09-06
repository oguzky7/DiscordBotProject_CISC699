from utils.HelpText import HelpText

class BotControl:
    def __init__(self, bot):
        self.bot = bot

    async def send_greeting(self):
        """Sends a greeting when the bot comes online."""
        channel = self.bot.get_channel(self.bot.config.CHANNEL_ID)
        if channel:
            await channel.send("Hi, I'm online! type '!project_help' to see what I can do")

    async def send_help(self, ctx):
        """Sends the list of commands by calling HelpText."""
        help_message = HelpText.get_help()
        await ctx.send(help_message)
