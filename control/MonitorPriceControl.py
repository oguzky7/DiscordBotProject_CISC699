from entity.PriceEntity import PriceEntity
from utils.css_selectors import Selectors 
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
                if not url:
                    selectors = Selectors.get_selectors_for_url("bestbuy")
                    url = selectors.get('priceUrl')  # Get the price URL
                    if not url:
                        return "No URL provided, and default URL for BestBuy could not be found."
                    print("URL not provided, default URL for BestBuy is: " + url)

                current_price = self.price_entity.get_price_from_page(url)

                # Exit the loop if monitoring has been stopped
                if not self.is_monitoring:
                    break
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
                
                # Short sleep between checks to avoid missing stop command
                await asyncio.sleep(frequency)
                
        except Exception as e:
            return f"Failed to monitor price: {str(e)}"

    def stop_monitoring(self):
        """Stop the price monitoring loop."""
        self.is_monitoring = False
        return "Price monitoring has been stopped."
