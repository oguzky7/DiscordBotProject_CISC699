from discord.ext import commands
from control.MonitorAvailabilityControl import MonitorAvailabilityControl

class MonitorAvailabilityBoundary(commands.Cog):
    def __init__(self, bot, MonitorAvailabilityControl):
        self.bot = bot
        self.MonitorAvailabilityControl = MonitorAvailabilityControl  # Initialize control object

    @commands.command(name="monitor_availability")
    async def monitor_availability(self, ctx, url: str, date_str=None, frequency: int = 15):
        """Command to monitor availability at the given frequency."""
        await ctx.send("Command recognized, taking action.")
        await ctx.send(f"Monitoring availability at {url} every {frequency} second(s).")
        await self.MonitorAvailabilityControl.start_monitoring_availability(url, date_str, frequency)

    @commands.command(name="stop_monitoring_availability")
    async def stop_monitoring(self, ctx):
        """Command to stop monitoring availability."""
        await ctx.send("Command recognized, taking action.")
        self.MonitorAvailabilityControl.stop_monitoring()
        await ctx.send("Stopped monitoring availability.")
