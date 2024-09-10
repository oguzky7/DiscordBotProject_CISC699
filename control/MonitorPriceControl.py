import asyncio
from entity.PriceEntity import PriceEntity
from utils.Config import Config
import logging

class MonitorPriceControl:
    def __init__(self):
        self.price_entity = PriceEntity()
        self.is_monitoring = False  # Control flag for monitoring state
        self.logger = logging.getLogger("MonitorPriceControl")

    async def start_monitoring(self, ctx, url, frequency=20):
        """Start monitoring the price at a given interval."""
        if ctx.channel.id == Config.CHANNEL_ID:
            if self.is_monitoring:
                await ctx.send("Already monitoring prices.")
                return

            self.is_monitoring = True
            await ctx.send(f"Monitoring price every {frequency} second(s).")
            previous_price = None

            try:
                while self.is_monitoring:
                    current_price = self.price_entity.get_price(url)
                    if current_price:
                        if previous_price is None:
                            await ctx.send(f"Starting price monitoring. Current price is: {current_price}")
                        elif current_price > previous_price:
                            await ctx.send(f"Price went up! Current price: {current_price} (Previous: {previous_price})")
                        elif current_price < previous_price:
                            await ctx.send(f"Price went down! Current price: {current_price} (Previous: {previous_price})")
                        else:
                            await ctx.send(f"Price remains the same: {current_price}")
                        previous_price = current_price
                    else:
                        await ctx.send("Failed to retrieve the price.")
                    await asyncio.sleep(frequency)  # Wait for the next check
            except Exception as e:
                self.logger.error(f"Failed to monitor price for {url}: {e}")
                await ctx.send(f"Failed to monitor price: {e}")
        else:
            await ctx.send("This command can only be used in the designated channel.")

    async def stop_monitoring(self, ctx):
        """Stop the price monitoring loop."""
        if self.is_monitoring:
            self.is_monitoring = False
            await ctx.send("Price monitoring has been stopped.")
        else:
            await ctx.send("No monitoring process is currently running.")
