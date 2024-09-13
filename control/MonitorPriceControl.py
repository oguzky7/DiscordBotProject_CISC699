from entity.PriceEntity import PriceEntity
import asyncio

class MonitorPriceControl:
    def __init__(self, browser_entity):
        self.price_entity = PriceEntity(browser_entity)
        self.is_monitoring = False  # Control flag for monitoring state

    async def start_monitoring_price(self, ctx, url: str = None, frequency=20):
        """Start monitoring the price at a given interval."""
        if self.is_monitoring:
            return "Already monitoring prices."
        
        self.is_monitoring = True
        await ctx.send(f"Monitoring price every {frequency} second(s).")
        previous_price = None

        try:
            while self.is_monitoring:
                current_price = self.price_entity.get_price_from_page(url)
                if current_price:
                    if previous_price is None:
                        await ctx.send(f"Starting price monitoring. Current price: {current_price}")
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
            return f"Failed to monitor price: {str(e)}"

    def stop_monitoring(self):
        """Stop the price monitoring loop."""
        self.is_monitoring = False
        return "Price monitoring has been stopped."
