from discord.ext import commands
from control.CheckAvailabilityControl import CheckAvailabilityControl

class CheckAvailabilityBoundary(commands.Cog):
    def __init__(self, bot, browser_entity):
        self.bot = bot
        self.availibility_control = CheckAvailabilityControl(browser_entity)  # Initialize control object

    @commands.command(name="check_availability")
    async def check_availability(self, ctx, url: str, date_str=None):
        """Command to check availability at a given URL."""
        await ctx.send("Command recognized, taking action.")
        # Call the control layer to handle the availability check
        result, html_msg, excel_msg = await self.availibility_control.check_availability(url, date_str)
        
        # Send the result back to the user in Discord
        await ctx.send(result)

        # Send the exported HTML and Excel messages (if generated)
        if html_msg:
            await ctx.send(html_msg)
        if excel_msg:
            await ctx.send(excel_msg)
