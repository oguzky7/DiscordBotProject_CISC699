import asyncio
from control.AvailabilityControl import AvailabilityControl  # Reuse existing control
import logging

class MonitorAvailabilityControl:
    def __init__(self):
        self.availability_control = AvailabilityControl()  # Reuse AvailabilityControl
        self.monitoring_task = None  # To store the running task
        self.logger = logging.getLogger("MonitorAvailabilityControl")

    async def start_monitoring(self, ctx, url, date_str=None, time_slot=None, frequency=20):
        """Start monitoring availability at the given frequency (in seconds)."""
        # If a task is already running, notify the user
        if self.monitoring_task:
            await ctx.send("Monitoring is already running.")
            return

        # Define the monitoring loop
        async def monitor():
            while True:
                try:
                    # Reuse the existing check_availability method from AvailabilityControl
                    result, html_msg, excel_msg = await self.availability_control.handle_availability_check(ctx, url, date_str, time_slot)

                    # Send availability result to the user
                    await ctx.send(result)

                    # Send HTML and Excel results if available
                    if html_msg:
                        await ctx.send(html_msg)
                    if excel_msg:
                        await ctx.send(excel_msg)

                except Exception as e:
                    self.logger.error(f"Failed to check availability for {url}: {e}")
                    await ctx.send(f"Error: {str(e)}")

                await asyncio.sleep(frequency)  # Wait for the next interval (in seconds)

        # Start the task in the background
        self.monitoring_task = asyncio.create_task(monitor())

    def stop_monitoring(self):
        """Stop the ongoing monitoring task."""
        if self.monitoring_task:
            self.monitoring_task.cancel()  # Stop the task
            self.monitoring_task = None
