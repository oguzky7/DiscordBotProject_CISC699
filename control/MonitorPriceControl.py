import asyncio
from entity.PriceEntity import PriceEntity
from Config import Config
import logging

class MonitorPriceControl:
    def __init__(self):
        self.price_entity = PriceEntity()
        self.logger = logging.getLogger("MonitorPriceControl")

    async def monitor_price(self, ctx, url, frequency=1):
        """Monitor the price at a given interval."""
        if ctx.channel.id == Config.CHANNEL_ID:
            try:
                await ctx.send(f"Monitoring price every {frequency} minute(s).")
                previous_price = None
                
                while True:
                    current_price = self.price_entity.get_price(url)
                    if current_price:
                        if previous_price is None:
                            await ctx.send(f"Starting price monitoring. Current price is: {current_price}")
                        else:
                            if current_price > previous_price:
                                await ctx.send(f"Price went up! Current price: {current_price} (Previous: {previous_price})")
                            elif current_price < previous_price:
                                await ctx.send(f"Price went down! Current price: {current_price} (Previous: {previous_price})")
                            else:
                                await ctx.send(f"Price remains the same: {current_price}")
                        previous_price = current_price
                    else:
                        await ctx.send("Failed to retrieve the price.")
                    await asyncio.sleep(frequency * 60)  # Wait for the next check
            except Exception as e:
                self.logger.error(f"Failed to monitor price for {url}: {e}")
                await ctx.send(f"Failed to monitor price: {e}")
        else:
            await ctx.send("This command can only be used in the designated channel.")
