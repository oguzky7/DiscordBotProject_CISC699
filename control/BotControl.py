import asyncio

class BotControl:
    def __init__(self, bot):
        self.bot = bot

    async def send_greeting(self):
        """Sends a greeting when the bot comes online."""
        channel = self.bot.get_channel(self.bot.config.CHANNEL_ID)
        if channel:
            await channel.send("Hi, I'm online! type '!project_help' to see what I can do")

    async def stop_bot(self):
        """Stops the bot gracefully, ensuring all connections are closed."""
        print("Bot is stopping...")

        await self.bot.close()