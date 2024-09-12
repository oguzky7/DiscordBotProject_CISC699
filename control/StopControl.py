import discord

class StopControl:
    async def stop_bot(self, ctx, bot):
        """Stop the bot gracefully."""
        await ctx.send("The bot is shutting down...")
        await bot.close()  # Close the bot
