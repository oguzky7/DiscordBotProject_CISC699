import asyncio
from control.CheckAvailabilityControl import CheckAvailabilityControl
from entity.AvailabilityEntity import AvailabilityEntity

class MonitorAvailabilityControl:
    def __init__(self, browser_entity):
        self.availability_entity = AvailabilityEntity(browser_entity)  # Reuse check control logic
        self.monitoring_task = None  # Store the running task

    async def start_monitoring_availability(self, ctx, url: str, date_str=None, frequency=15):
        """Start monitoring availability at the given frequency."""
        if self.monitoring_task:
            await ctx.send("Monitoring is already running.")
            return

        async def monitor():
            while True:
                result, html_msg, excel_msg = await self.availability_entity.check_availability(ctx, url, date_str)
                await ctx.send(result)
                if html_msg:
                    await ctx.send(html_msg)
                if excel_msg:
                    await ctx.send(excel_msg)
                await asyncio.sleep(frequency)

        self.monitoring_task = asyncio.create_task(monitor())

    def stop_monitoring(self):
        """Stop the ongoing monitoring task."""
        if self.monitoring_task:
            self.monitoring_task.cancel()
            self.monitoring_task = None
