import discord
from discord.ext import commands

class HelpBoundary(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='project_help')
    async def project_help(self, ctx):
        help_message = """
        Available Commands:
        !login <site> <username> <password> - Logs in to a website
        !launch_browser [incognito] - Launches the browser
        !close_browser - Closes the browser
        !navigate_to_url <url> - Navigates to a specific URL
        !monitor_price <url> [frequency] - Monitors the price of a product
        !get_price <url> - Gets the price of a product
        !check_availability <url> <date> <time> - Checks availability for a reservation
        !stop_monitoring - Stops monitoring prices
        !stop - Stops the bot
        !get_user <username> - Retrieves user data from the database
        """
        await ctx.send(help_message)
