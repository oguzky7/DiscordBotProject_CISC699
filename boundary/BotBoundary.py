from discord.ext import commands
from control.ChatControl import ChatControl
from Config import Config

class BotBoundary(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.chat_control = ChatControl()

    @commands.Cog.listener()
    async def on_ready(self):
        """Bot startup message when ready."""
        print(f'Logged in as {self.bot.user.name}')
        channel = self.bot.get_channel(Config.CHANNEL_ID)
        if channel:
            await channel.send("Hi, I'm online!")

    @commands.Cog.listener()
    async def on_message(self, message):
        """Handle non-prefixed messages and command-prefixed messages."""
        if message.author == self.bot.user:
            return

        # Handle non-prefixed messages (like greetings)
        if not message.content.startswith('!'):
            response = self.chat_control.process_non_prefixed_message(message.content)
            await message.channel.send(response)

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        """Handle unrecognized commands."""
        if isinstance(error, commands.CommandNotFound):
            # Handle unknown command
            response = self.chat_control.handle_unrecognized_command()
            await ctx.send(response)
