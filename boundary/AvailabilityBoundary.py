from discord.ext import commands
from control.AvailabilityControl import AvailabilityControl

class AvailabilityBoundary(commands.Cog):  # Make it a Cog to register as a bot command
    def __init__(self, bot):
        self.bot = bot
        self.control = AvailabilityControl()

    @commands.command(name="check_availability")  # Register the command with this decorator
    async def check_availability(self, ctx, url: str, date_str=None, time_slot=None):
        # Call the control and get the results
        result, html_msg, excel_msg = await self.control.handle_availability_check(ctx, url, date_str, time_slot)
        
        # Send the result first
        await ctx.send(result)

        # Send HTML and Excel results if available
        if html_msg:
            await ctx.send(html_msg)
        if excel_msg:
            await ctx.send(excel_msg)
