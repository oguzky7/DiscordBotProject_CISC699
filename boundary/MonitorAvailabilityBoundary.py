from discord.ext import commands
from control.MonitorAvailabilityControl import MonitorAvailabilityControl

class MonitorAvailabilityBoundary(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.control = MonitorAvailabilityControl()


    @commands.command(name="monitor_availability")
    async def start_monitoring(self, ctx, url: str, date_str=None, time_slot=None, frequency: int = 15):
        """Command to start monitoring availability at a given frequency (default: 15 seconds)."""
        # Check if frequency is given as the second argument (but no date or time provided)
        if date_str and date_str.isdigit() and not time_slot:
            frequency = int(date_str)
            date_str = None  # Reset date_str because it was actually the frequency

        await ctx.send(f"Starting availability monitoring every {frequency} second(s).")
        await self.control.start_monitoring(ctx, url, date_str, time_slot, frequency)


    @commands.command(name="stop_monitoring_availability")
    async def stop_monitoring(self, ctx):
        """Command to stop monitoring availability."""
        self.control.stop_monitoring()
        await ctx.send("Stopped monitoring availability.")
