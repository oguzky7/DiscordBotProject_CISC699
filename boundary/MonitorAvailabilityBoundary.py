from discord.ext import commands
from control.MonitorAvailabilityControl import MonitorAvailabilityControl

class MonitorAvailabilityBoundary(commands.Cog):
    def __init__(self, bot, monitor_availibility_control):
        self.bot = bot
        self.monitor_availibility_control = monitor_availibility_control  # Initialize control object

    @commands.command(name="monitor_availability")
    async def monitor_availability(self, ctx, url: str, date_str=None, frequency: int = 15):
        """Command to monitor availability at the given frequency."""
        await ctx.send("Command recognized, taking action.")
        await ctx.send(f"Monitoring availability at {url} every {frequency} second(s).")
        response = await self.monitor_availibility_control.start_monitoring_availability(url, date_str, frequency)
        await ctx.send(response)

    @commands.command(name="stop_monitoring_availability")
    async def stop_monitoring(self, ctx):
        """Command to stop monitoring availability."""
        await ctx.send("Command recognized, taking action.")
        self.monitor_availibility_control.stop_monitoring()
        await ctx.send("Stopped monitoring availability.")
