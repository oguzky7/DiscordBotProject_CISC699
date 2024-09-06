from discord.ext import commands
from control.ChatControl import ChatControl

class ChatBoundary(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.chat_control = ChatControl()

    @commands.command(name='chat_with_bot')
    async def chat_with_bot(self, ctx, *, message):
        """Handles basic greetings and chat."""
        response = self.chat_control.respond_to_chat(message)
        await ctx.send(response)
