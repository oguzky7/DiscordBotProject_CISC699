import discord
from discord.ext import commands
from UserControl import UserControl

class DatabaseBoundary(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.user_control = UserControl()

    @commands.command(name='get_user')
    async def get_user(self, ctx, username: str):
        user_data = self.user_control.get_user(username)
        if user_data:
            await ctx.send(f"Username: {user_data[0]}, Password: {user_data[1]}")
        else:
            await ctx.send("User not found.")
